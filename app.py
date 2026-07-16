# -*- coding: utf-8 -*-
"""
yPlus Studio  native desktop host (pywebview / WebView2).
index.html'i yerel bir pencerede render eder. pywebview/WebView2 calismazsa
Edge "app" modunda yerel sunucuya geri duser.
"""
import os
import sys
import time
import socket
import threading

# WebView2/Edge: hover'da buyuyen "fluent overlay" kaydirma cubugunu ve
# animasyonunu kapat; klasik (sabit boyutlu) kaydirma cubugu kullanilsin.
os.environ.setdefault(
    "WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS",
    "--disable-features=OverlayScrollbar,msOverlayScrollbarWinStyle,msOverlayScrollbarWinStyleAnimation",
)


def resource_path(rel):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)


def html_path():
    # 1) exe ile ayni klasordeki index.html (yeniden derlemeden guncelleme)
    if getattr(sys, "frozen", False):
        ext = os.path.join(os.path.dirname(sys.executable), "index.html")
        if os.path.exists(ext):
            return ext
    # 2) gomulu kopya
    return resource_path("index.html")


def load_html():
    with open(html_path(), "r", encoding="utf-8") as f:
        return f.read()


def run_pywebview(html):
    import webview
    try:
        import ctypes
        _u = ctypes.windll.user32
        _sw, _sh = _u.GetSystemMetrics(0), _u.GetSystemMetrics(1)
    except Exception:
        _sw, _sh = 1600, 900
    _rw = max(1200, _sw - 70); _rh = max(780, _sh - 90)
    _mw = max(1160, _sw - 130); _mh = max(740, _sh - 160)
    webview.create_window(
        "yPlus Studio",
        html=html,
        width=_rw,
        height=_rh,
        min_size=(_mw, _mh),
        maximized=True,
        background_color="#0f0f12",
        text_select=True,
    )
    webview.start()


def _free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def _find_edge():
    for c in [
        os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"),
        os.path.expandvars(r"%LocalAppData%\Microsoft\Edge\Application\msedge.exe"),
    ]:
        if c and os.path.exists(c):
            return c
    return None


def run_fallback(html):
    import http.server
    import socketserver
    import subprocess
    import webbrowser

    data = html.encode("utf-8")

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, *a):
            pass

    port = _free_port()
    httpd = socketserver.TCPServer(("127.0.0.1", port), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    url = "http://127.0.0.1:%d/" % port

    edge = _find_edge()
    if edge:
        subprocess.Popen([edge, "--app=%s" % url, "--window-size=1320,880",
                          "--user-data-dir=%s" % os.path.join(os.path.expandvars("%LocalAppData%"), "YplusStudio")])
    else:
        webbrowser.open(url)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass


def main():
    html = load_html()
    try:
        run_pywebview(html)
    except Exception:
        run_fallback(html)


if __name__ == "__main__":
    main()
