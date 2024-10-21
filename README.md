# Bit Seviyesi ve Görüntü Kalitesi

## Genel Bakış
Bu proje, 8 bitlik bir görüntünün daha düşük bit derinliklerine (7, 6, 5, 4, 3, 2 ve 1 bit) sıkıştırılmasının görüntü kalitesini nasıl etkilediğini analiz etmektedir. Görüntü sıkıştırıldıktan sonra tekrar 8 bit derinliğine yükseltilmekte ve ortaya çıkan kalite kaybı ölçülmektedir.

Görüntü sıkıştırma, depolama ve iletim maliyetlerini azaltmak için yaygın olarak kullanılan bir tekniktir. Ancak, bit derinliğini azaltmak veri kaybına yol açar ve bu da görüntü kalitesinde bozulmaya neden olur. Bu rapor, bit derinliği azaldıkça orijinal görüntü ile sıkıştırılmış görüntü arasındaki kalite farklarının nasıl değiştiğini incelemektedir.

## Yöntem

1. **Görüntü Seçimi:** 
   - Orijinal görüntü, 256 farklı ton temsil eden 8 bit derinliğinde bir gri tonlama görüntüsüdür. Bu görüntüdeki her pikselin değeri 0 ile 255 arasında değişmektedir.

2. **Bit Sıkıştırma:** 
   - Orijinal 8 bitlik görüntü, sırasıyla 7, 6, 5, 4, 3, 2 ve 1 bitlik görüntülere dönüştürülmüştür. Bu işlem, kullanılabilen ton sayısını sınırlar. Örneğin, 7 bitlik bir görüntü 128 ton içerirken, 4 bitlik bir görüntü 16 ton ile sınırlıdır.

3. **Tekrar 8 Bit'e Yükseltme:** 
   - Sıkıştırılan her görüntü, kaybolan ton bilgisi geri getirilemeyecek şekilde tekrar 8 bit derinliğine yükseltilmiştir.

4. **Kalite Farklarının İncelenmesi:** 
   - Orijinal görüntü ile tekrar 8 bit'e yükseltilen görüntüler arasındaki kalite farkı, Peak Signal Noise Ratio (PSNR) ve Mean Absolute Error (MAE) kullanılarak ölçülmüştür.

## Sonuçlar

- **7 Bit:**
  - PSNR: 51, MAE: 0.51
  - En az bozulma, 8 bitlik görüntüye en yakın kalite.

- **6 Bit:**
  - PSNR: 44, MAE: 1.21
  - Ton geçişlerinde hafif bozulmalar görülüyor.

- **5 Bit:**
  - PSNR: 38, MAE: 2.52
  - Detay kayıpları belirginleşmeye başlıyor.

- **4 Bit:**
  - PSNR: 32, MAE: 5.21
  - Ton aralıkları belirginleşiyor, detaylar kaybolmaya başlıyor.

- **3 Bit:**
  - PSNR: 28, MAE: 12.36
  - Ciddi bir kalite kaybı ve sınırlı ton geçişleri.

- **2 Bit:**
  - PSNR: 18, MAE: 25.15
  - Detayların çoğu kaybolmuş, yalnızca ana şekiller görülüyor.

- **1 Bit:**
  - PSNR: 9, MAE: 75.22
  - Yalnızca siyah ve beyaz tonlar, tüm detaylar kaybolmuş.

## Değerlendirme
Bit derinliği azaldıkça, görüntü kalitesindeki kayıp daha belirgin hale gelmektedir. 4 bit ve altındaki bit derinliklerinde, insan gözünün algılayabileceği bozulmalar açıkça görülmektedir. 7 ve 6 bit seviyelerinde kalite büyük ölçüde korunabilse de, 5 bit ve altındaki sıkıştırmalar ciddi bilgi kaybına neden olmuştur. Bu analiz, bit derinliği ve görüntü kalitesi arasındaki dengeyi anlamak açısından önemli bilgiler sunmaktadır.

## Sonuç
Bu çalışma, bit derinliğinin azaltılmasının görüntü kalitesine olan etkilerini göstermektedir. Görüntü kalitesinin korunabilmesi için bit derinliğinin en az 5 bit seviyesinde tutulması gerekmektedir. Daha düşük bit derinliklerinde detay kaybı ciddi boyutlara ulaşmaktadır. Bu bulgular, sıkıştırma algoritmalarının görüntü kalitesi üzerindeki etkilerini daha iyi anlamaya yardımcı olmaktadır.

## Ekran Görüntüleri
- [7 Bit](data/7bit.png)
- [6 Bit](data/6bit.png)
- [5 Bit](data/5bit.png)
- [4 Bit](data/4bit.png)
- [3 Bit](data/3bit.png)
- [2 Bit](data/2bit.png)
- [1 Bit](data/1bit.png)
