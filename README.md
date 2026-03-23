<h1 align="center">CheffApp: Yapay Zeka Destekli Şef Asistanı</h1>

<p align="center">
  <i>Buzdolabınızdaki malzemelerin fotoğrafını çekin, yapay zeka sizin için en lezzetli tarifi anında oluştursun!</i>
</p>

<p align="center">
  <img src="https://img.icons8.com/color/48/000000/python--v1.png" alt="Python" title="Python" />
  <img src="https://img.icons8.com/color/48/000000/artificial-intelligence.png" alt="YOLOv8" title="YOLOv8" />
  <img src="https://img.icons8.com/color/48/000000/google-logo.png" alt="Google Gemini" title="Google Gemini" />
</p>

---

## 🚀 Proje Özeti ve Vizyon

**CheffApp**, bilgisayarlı görü (Computer Vision) ve üretken yapay zeka (Generative AI) teknolojilerini bir araya getiren yenilikçi bir akıllı mutfak asistanıdır. Kullanıcıların mutfaklarında "Ne pişirsem?" derdine son vermeyi amaçlayan bu proje, sadece eldeki malzemelerin fotoğrafını analiz ederek benzersiz tarifler sunar.

Sistem, öncelikle **YOLOv8** nesne tespiti modelini kullanarak fotoğraftaki yenilebilir malzemeleri (meyve, sebze, çeşitli gıdalar) tespit eder. Elde edilen malzeme listesi, **Google Gemini 2.5 Flash** yapay zeka modeline iletilir. "Dünyaca ünlü, neşeli bir Türk şefi" personasına bürünen Gemini, tespit edilen malzemeleri baz alarak size isminizle hitap eden, samimi, adım adım ve tamamen kişiselleştirilmiş bir yemek tarifi oluşturur. Üstelik tüm bu çıktılar, frontend ve mobil entegrasyonlarına uygun temiz bir JSON formatında sağlanır.

## ✨ Temel Özellikler (Key Features)

*   **Akıllı Nesne Tespiti (YOLOv8):** Görüntü üzerinden gıda malzemelerini yüksek doğruluk oranıyla otomatik olarak tanıma ve listeleme.
*   **Üretken Yapay Zeka ile Tarif (Gemini AI):** Eldeki malzemeleri kullanarak anında yaratıcı yemek tarifleri üretme yeteneği.
*   **Kişiselleştirilmiş Deneyim:** Şefin kullanıcıya kendi ismiyle hitap ettiği samimi ve interaktif tarif anlatımı.
*   **Yapılandırılmış API Çıktısı (JSON):** Yemek adı, hazırlık süresi, kalori, eksik/tam malzeme listesi ve yapılış adımlarının yazılımsal entegrasyonlara hazır döndürülmesi.
*   **Çevrimdışı Model Desteği:** Depoda bulunan önceden eğitilmiş hafif (nano/small) YOLO ağırlıkları ile hızlı görüntü işleme.

## ⚙️ Kurulum Rehberi

Projeyi yerel ortamınızda çalıştırmak ve test etmek için aşağıdaki adımları sırasıyla uygulayabilirsiniz:

1. **Projeyi Klonlayın**
```bash
git clone https://github.com/oguzhan1414/CheffApp.git
cd CheffApp/yemekapp
```

2. **Gerekli Kütüphaneleri Yükleyin**
Projenin çalışması için Python bilgisayarınızda yüklü olmalıdır. Ardından gerekli modülleri indirin:
```bash
pip install ultralytics google-generativeai
```

3. **API Anahtarınızı Ayarlayın**
Google Gemini'yi kullanabilmek için `chef.py` dosyasını açın ve `API_KEY` değişkenini kendi anahtarınızla güncelleyin:
*(Not: Güvenliğiniz için bu anahtarı ilerleyen süreçte `.env` dosyası üzerinden çekmeniz tavsiye edilir.)*
```python
API_KEY = "BURAYA_KENDI_GEMINI_API_KEYINIZI_YAZIN"
```

4. **Uygulamayı Çalıştırın**
Modelin tespit yapmasını istediğiniz görseli projeye ekleyin ve ana scripti çalıştırın:
```bash
python app.py
```
*(Analiz sonucunda, fotoğrafta bulunan malzemeler listelenecek ve yapılandırılmış Gemini tarifine yönlendirilecektir.)*