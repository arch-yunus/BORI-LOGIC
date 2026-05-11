# 🐺 AŞİNA Motoru ve Sürü Simülasyonu (v2.1)

Bu dizin, Bozkurt Mitolojisi projesinin algoritmik kalbidir. AŞİNA 2.1 sürümü ile stratejik derinlik artırılmış; formasyonlar, arazi etkileri ve birim rolleri sisteme entegre edilmiştir.

## 🛠️ Bileşenler

### 1. `interpreter.py`
`.asina` uzantılı profesyonel betik dosyalarını işleyen yorumlayıcıdır. 
*   **Özellikler**: Yapılandırma yönetimi, loglama, formasyon ve rol atama.
*   **Komutlar**: `SÜRÜ`, `NİZAM`, `BÖRÜ`, `AV`, `PUSU`, `ÇAĞRI`, `MÜDDET`, `DİZİLİŞ`, `ZEMİN`, `ROL`, `SON`.

### 2. `simulation.py`
Gelişmiş ASCII tabanlı sürü zekası motorudur.
*   **Varlıklar**: Börü (Kurt) ve Av (Koyun). `ALFA` rollerine sahip kurtlar 'A' ile gösterilir.
*   **Mantık**: Turan, Kıskaç ve Kama stratejileri.
*   **Çevresel Faktörler**: Hava durumu (Kar/Fırtına) ve Arazi (Bozkır/Orman/Dağ) etkileri.

### 3. Senaryolar
*   `kadim_strateji.asina`: Klasik kış operasyonu.
*   `gece_baskini.asina`: Ormanlık alanda pusu ve kıskaç harekatı.
*   `turan_nizami.asina`: Dağlık arazide kama nizamı gösterimi.

## 🚀 Çalıştırma

```bash
python simulation.py gece_baskini.asina
```

## 📜 Sözdizimi (Syntax) 2.1

AŞİNA 2.1, bozkır stratejilerini çok boyutlu bir nizam ile ifade eder:

| Komut | Açıklama |
| :--- | :--- |
| `DİZİLİŞ [Tip]` | Sürü formasyonu (`HİLAL`, `KISKAC`, `KAMA`). |
| `ZEMİN [Tip]` | Arazi hızı ve gizlilik çarpanı (`BOZKIR`, `ORMAN`, `DAG`). |
| `ROL [ID] [Tip]` | Birimlere özel yetenek/davranış atar (`ALFA`, `PUSUCU`). |

## 🏔️ Gelecek Vizyonu: AŞİNA 3.0 (Kut ve Tüz)

Batı-merkezli teknoloji anlayışına alternatif olarak, AŞİNA 3.0 sürümüyle birlikte sisteme tamamen özgün kültürel-teknolojik kavramlar entegre edilecektir:

*   **KUT Sistemi**: Bir birimin veya sürünün "meşruiyet" ve "verimlilik" puanı. Sadece hayatta kalmak değil, stratejik başarıyla "Kut" kazanmak, birimlerin kapasitesini artıracaktır.
*   **TÜZ (Denge Algoritması)**: Global bir dengeleyici olarak, ekosistemdeki kurt ve av oranını, enerji dağılımını ve sistem kararlılığını yöneten bir "Load Balancer" mantığı.
*   **TOY (Senkronizasyon)**: Birimlerin ortak bir karar almak veya veri paylaşmak için toplandığı "Consensus" protokolü.
*   **OTAĞ (Master Node)**: Sürünün stratejik koordinasyon merkezi ve veri ambarı.

| Komut | Açıklama |
| :--- | :--- |
| `SÜRÜ "[Başlık]"` | Simülasyon bloğunu başlatır ve isimlendirir. |
| `NİZAM [Param] [Değer]` | Sistem yapılandırmasını (GENİŞLİK, STRATEJİ, HAVA_DURUMU vb.) tanımlar. |
| `BÖRÜ [n]` | Simülasyondaki aktif kurt (börü) sayısı. |
| `AV [n]` | Simülasyondaki hedef (koyun/av) sayısı. |
| `PUSU [Mesafe]` | Kurtların pusuya yatma yarıçapını belirler. |
| `ÇAĞRI "[Mesaj]"` | Simülasyon loglarına veri girişi yapar. |
| `MÜDDET [n]` | Simülasyonun toplam iterasyon süresi. |
| `SON` | Simülasyon dosyasını sonlandırır. |

### Örnek Betik

```uluy
SÜRÜ "Kış Operasyonu"
NİZAM STRATEJİ TURAN
NİZAM HAVA_DURUMU KAR
BÖRÜ 5
AV 30
PUSU 4
MÜDDET 500
ÇAĞRI "Bozkırın sessizliği bozuluyor..."
SON
```

---
*"Böri tegi erdemlik - Kurt gibi erdemli, otonom ve kararlı."*
