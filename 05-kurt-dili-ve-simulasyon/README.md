# 🐺 ULUYI Motoru ve Sürü Simülasyonu

Bu dizin, Bozkurt Mitolojisi projesinin algoritmik kalbidir. Kadim bozkır stratejilerini dijital bir ortamda simüle etmek için geliştirilen araçları içerir.

## 🛠️ Bileşenler

### 1. `interpreter.py`
`.uluy` uzantılı egzotik betik dosyalarını işleyen yorumlayıcıdır. 
*   **Özellikler**: Yapılandırma yönetimi, loglama ve özel anahtar kelime işleme.
*   **Yeni Komutlar**: `HAVA_DURUMU`, `ENERJİ_SINIRI`, `PUSU_KUR`.

### 2. `simulation.py`
ASCII tabanlı sürü zekası motorudur.
*   **Varlıklar**: Börü (Kurt) ve Koyun.
*   **Mantık**: Turan taktiği, hava durumu etkileri (kar/fırtına), enerji yönetimi ve pusu (Ambush) durumları.
*   **Görselleştirme**: Terminal üzerinde renkli ve dinamik ASCII grafikleri.

### 3. `kadim_strateji.uluy`
Simülasyon için kullanılan ana senaryo dosyasıdır. Zorlu kış şartlarında bir av operasyonunu tanımlar.

## 🚀 Çalıştırma

Simülasyonu başlatmak için şu komutu kullanın:

```bash
python simulation.py
```

Özel bir betik dosyasıyla çalıştırmak için:

```bash
python simulation.py <dosya_adi>.uluy
```

## 📜 Sözdizimi (Syntax) Örneği

```uluy
AUUUUUU "Kış Operasyonu"
TÖRE STRATEJİ TURAN
TÖRE HAVA_DURUMU KAR
BÖRÜ_SAYISI 5
PUSU_KUR 4
ULUMA "Bozkırın sessizliği bozuluyor..."
AUUUUUU "Son Ulam"
```

---
*"Böri tegi erdemlik - Kurt gibi erdemli, otonom ve kararlı."*
