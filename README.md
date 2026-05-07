# 🐺 Bozkurt Mitolojisi: Biyotaklit, Hareket Felsefesi ve Kurt Sembolizmi Arşivi

![Bozkurt Mitolojisi Banner](assets/banner.png)

[![Lisans: CC BY-NC-SA 4.0](https://img.shields.io/badge/Lisans-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Kapsam: Antropoloji, Etoloji & Sistemler](https://img.shields.io/badge/Kapsam-Antropoloji%2C%20Etoloji%20%26%20Sistemler-blue.svg)]()
[![Versiyon: 1.6.0-alpha](https://img.shields.io/badge/Versiyon-1.6.0--alpha-brightgreen.svg)]()
[![Status: Comprehensive Update](https://img.shields.io/badge/Status-Comprehensive%20Update-blue.svg)]()

> *"Yukarıda mavi gök, aşağıda yağız yer yaratıldığında, ikisinin arasında insan oğlu yaratılmış... O zamanlar Tanrı güç verdiği için, babam kağanın ordusu kurt gibi imiş, düşmanları koyun gibi imiş."* – *Orhun Yazıtları (Kül Tigin Anıtı)*

Bu arşiv; Orta Asya bozkır kültürünün temel taşı olan **Kurt (Böri / Aşina)** figürünü, antropolojik bir mit olmanın ötesinde, erken dönem bir **biyotaklit (biomimicry)**, sistem modellemesi ve epik gelenek vakası olarak incelemeye adanmış disiplinlerarası bir referans kütüphanesidir.

---

## 👁️ Manifesto: Gözlem, Taklit ve Epik Süreklilik

Bozkurt, göçebe bozkır medeniyetlerinde romantik bir efsaneden ziyade, uzun süreli ampirik gözlemlerin sonucunda elde edilmiş kusursuz bir optimizasyon modelidir. Kadim Türkler, zorlu coğrafi koşullarda hayatta kalabilmek için kurdun doğasını izlemiş, analiz etmiş ve onun davranışsal algoritmalarını kendi sosyolojik, askeri ve iletişim ağlarına entegre etmiştir.

---

## 🔬 Araştırma Metodolojisi

Bu proje, veriye dayalı bir analiz yaklaşımını benimser:
1.  **Etolojik Analiz**: *Canis lupus* türünün sosyal hiyerarşisi, avlanma stratejileri ve enerji yönetimi incelenir.
2.  **Mitolojik Tersine Mühendislik**: Destanlardaki "mucizevi" olaylar, stratejik ve lojistik karar alma süreçleri olarak yeniden yorumlanır (Örn: Ergenekon'un bir skalabilirlik problemi olarak ele alınması).
3.  **Semiyotik Çözümleme**: Maddi kültür varlıklarının (tuğlar, sikkeler) taşıdığı sembolik mesajlar deşifre edilir.
4.  **Algoritmik Simülasyon**: Teorik çıkarımlar, `ULUYI` dili ile modellenerek dijital bozkır ortamında test edilir.

---

## 🧭 Depo Mimarisi ve Gezinti

```mermaid
graph TD
    Root[Bozkurt Mitolojisi Arşivi] --> Dir1[01. Biyotaklit ve Etoloji]
    Root --> Dir2[02. Dede Korkut ve Epik]
    Root --> Dir3[03. Türeyiş ve Ontoloji]
    Root --> Dir4[04. Semiyoloji ve İkonografi]
    Root --> Data[data/json/lore]
    
    Dir1 --> Sub1[Turan Taktiği & Sürü Zekası]
    Dir2 --> Sub2[Mübarek Yüz & Sadakat]
    Dir3 --> Sub3[Aşina Boyu & Ergenekon]
    Dir4 --> Sub4[Tuğlar & Petroglifler]
```

### 📂 [01. Biyotaklit ve Etolojik Strateji](01-biyotaklit-ve-etolojik-strateji/)
*   **Sürekli Devinim:** Nomadizm ve optimizasyon.
*   **Sürü Zekası:** Dağıtık iletişim ağları.
*   **Asimetrik Harp:** Turan Taktiği mekaniği.
*   **İletişim Protokolleri:** Uluma algoritmaları ve veri iletimi.

### 📂 [02. Dede Korkut Anlatıları ve Epik Gelenek](02-dede-korkut-anlatilari/)
*   **Kurt Yüzü Mübarektir:** Ontolojik kökenler.
*   **Kurtla Söyleşme:** Salur Kazan'ın doğayla kurduğu derin bağ.
*   **Toplumsal Hafıza:** Şamanik mirasın edebi dönüşümü.

### 📂 [03. Türeyiş ve Ontoloji](03-tureyis-ve-ontoloji/)
*   **Aşina Boyu:** Göktürk hanedanının genetik ve mitolojik kökleri.
*   **Ergenekon:** Bir topluluğun yeniden doğuş algoritması.
*   **Gökbörü:** Oğuz Kağan'ın ilahi ve stratejik rehberi.

### 📂 [04. Semiyoloji ve İkonografi](04-semiyoloji-ve-ikonografi/)
*   **Altın Kurt Başlı Tuğlar:** Devlet otoritesinin görsel dili.
*   **Nümismatik:** Para ve mühürlerde kurdun sürekliliği.
*   **Petroglifler:** Avrasya steplerindeki görsel hafıza.

### 📂 [05. Kurt Dili (ULUYI) ve Simülasyon](05-kurt-dili-ve-simulasyon/)
*   **ULUYI Scripting:** Kurt sürüsü davranışlarını tanımlayan egzotik dil.
*   **Sürü Zekası Simülasyonu:** Kadim stratejilerin algoritmik temsili.
*   **Hava Durumu ve Enerji:** Çevresel faktörlerin (kar, fırtına) sürü üzerindeki etkisi.
*   **Interpreter:** .uluy dosyalarını işleyen düşük seviyeli motor.

---

## 🐺 ULUYI Dili ve Sözdizimi (Syntax)

`ULUYI`, bozkır stratejilerini makine diline tercüme etmek için geliştirilmiş alan özgü bir dildir (DSL).

### Temel Komutlar
*   `AUUUUUU "[Başlık]"`: Simülasyon dosyasını başlatır/bitirir.
*   `TÖRE [Parametre] [Değer]`: Sistem yapılandırmasını (Genişlik, Strateji, Hava Durumu) tanımlar.
*   `BÖRÜ_SAYISI [n]`: Simülasyondaki aktif kurt birimi sayısı.
*   `PUSU_KUR [Mesafe]`: Kurtların pusuya yatma yarıçapını belirler.
*   `ULUMA "[Mesaj]"`: Simülasyon loglarına veri girişi yapar.

### Örnek Betik
```uluy
AUUUUUU "Kış Operasyonu"
TÖRE STRATEJİ TURAN
TÖRE HAVA_DURUMU KAR
BÖRÜ_SAYISI 5
PUSU_KUR 4
ULUMA "Hilal daralıyor, beyaz ölüm yaklaşıyor."
AUUUUUU "Son Ulam"
```

---

## 📖 Börülük Sözlüğü (Glossary)

*   **Böri / Börü**: Eski Türkçede "kurt". Aynı zamanda Göktürklerde hanedan muhafızlarına verilen isim.
*   **Gökbörü (Kök-Börü)**: Gök rengi/yeleli kutsal kurt. İlahi rehberliği temsil eder.
*   **Aşina (Asena)**: Göktürk hanedanının türediğine inanılan dişi kurt; soyun koruyucusu.
*   **Kurt-Ata**: Kavimlerin koruyucu ve yaratıcı gücü olarak kurdu simgeleyen ontolojik terim.
*   **Turan Taktiği**: Kurtların avlanma biçiminden ilham alan askeri "Hilal/Kuşatma" stratejisi.
*   **Yelme**: Keşif ve yıpratma saldırıları yapan öncü kurt birimi/süvarisi.
*   **Tüz**: Kadim töre ve sistem düzeni; denge hali.

---

## 🖼️ Görsel Galeri ve Belgeleme

### Gökbörü Rehberliği (Destan Tasviri)
![Gökbörü](assets/oguz_kagan_wolf.png)
*Oğuz Kağan'ın otağına giren ilahi ışığın içinden çıkan rehber kurt tasviri.*

### Stratejik Modelleme
```mermaid
graph LR
    A[Gözlem: Kurt] --> B[Analiz: Sürü Zekası]
    B --> C[Uygulama: Askeri Disiplin]
    C --> D[Sonuç: Devlet Teşkilatlanması]
```

---

## ⚙️ Geliştiriciler İçin: Data API

Veri setlerimiz [JSON Schema](data/json/schema.json) standartlarına uygundur.

```json
{
  "entity_id": "OK-001",
  "kavram": "Gökbörü",
  "kaynak": "Oğuz Kağan Destanı",
  "analiz": "Işık içerisinden çıkan ilahi rehber."
}
```

---

## ✨ Vecizeler ve Atasözleri

> *"Kurt kışı geçirir ama yediği ayazı unutmaz."* – Türk Atasözü

> *"Kurt, yalnız olduğu için mi ulur? Yoksa uluduğu için mi yalnızdır?"* – Ahmet Hamdi Tanpınar

---

## 🚀 Yol Haritası (Roadmap)

- [x] **Interactive Dashboard**: Veri havuzunu ve stratejileri görselleştiren web arayüzü.
- [x] **ULUYI Language Evolution**: Enerji, hava durumu ve pusu mantığı eklenen egzotik dil.
- [x] **Simulation 2.0**: Gelişmiş ASCII simülasyonu ve stratejik avlanma (Windows/Linux uyumlu).
- [x] **Dataset Expansion**: Ergenekon ve Türeyiş destanlarının teknik JSON entegrasyonu.
- [ ] **Mobile App**: Arşiv verilerine erişim sağlayan mobil uygulama konsepti.
- [ ] **Genetic Algorithm**: Sürü davranışlarının nesiller arası optimizasyonu.

---

## 📄 Lisans Bildirimi

Bu arşiv **CC BY-NC-SA 4.0** lisansı ile korunmaktadır.

<br>
<p align="center">
  <b>"Böri tegi erdemlik"</b><br>
  <i>(Kurt gibi erdemli / otonom ve kararlı)</i><br>
  Hareket et, gözlemle ve sistemi yönet.
</p>