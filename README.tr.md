<p align="center">
  <img src="docs/img/banner.svg" alt="yPlus Studio" width="820">
</p>

<p align="center"><b>Hedef y⁺ değerini eksiksiz ve savunulabilir bir CFD kurulumuna dönüştürür</b> — ilk hücre yüksekliği, prizma katmanları, türbülans modeli, duvar yaklaşımı ve ayrıklaştırma şemaları. Ücretsiz, çevrimdışı, literatür doğrulamalı. <a href="README.md">🇬🇧 English</a></p>

## Hızlı başlangıç

1. [Son sürümden](https://github.com/ahmetensarcfd/yplus-studio/releases/latest) `yplusstudio.exe` dosyasını indir
2. Çalıştır — kurulum yok (Windows 10/11, WebView2)
3. 100 hazır senaryodan birini seç veya kendi akışını gir — kurulum önerisi anında hazır

## Neden yPlus Studio?

Web'deki y⁺ hesaplayıcıları tek bir sayı verir ve orada durur. yPlus Studio devam eder: prizma katman tasarımı, türbülans modeli önerisi (SST k-ω, Realizable k-ε, RSM, Transition SST, SBES…), ayrıklaştırma ve basınç şeması önerisi — modern **ANSYS Fluent** iş akışlarıyla hizalı, her kural literatüre dayalı.

- ISA standart atmosfer (0–20 km), Sutherland viskozite, 40+ akışkan
- Re, Ma, Fr, We, St, Eu, Pe (+hücre Pe), Gr, Ra, Nu — rejim etiketleriyle
- 10 alanda 100 literatür temelli hızlı kurulum senaryosu
- Koyu/açık tema, PDF rapor, tamamen çevrimdışı — hesap yok, telemetri yok

## Doğrulama

49 noktalı literatür doğrulama takımı (ISA, Sutherland, Schlichting/Blasius, duvar büyüklükleri) + öneri motoru için 262.000+ kombinasyonluk otomatik denetim. *Nihai ağ ve model kararı mühendisindir.*

## Kaynaktan derleme

```bat
git clone https://github.com/ahmetensarcfd/yplus-studio.git
cd yplus-studio
build.bat
```

MIT lisansı — [LICENSE](LICENSE). Katkı için: [CONTRIBUTING.md](CONTRIBUTING.md).
