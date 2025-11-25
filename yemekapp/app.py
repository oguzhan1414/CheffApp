from ultralytics import YOLO


# --- AYARLAR ---
# Güven Eşiği
MIN_GUVEN_ORANI = 0.20  # Biraz düşürdüm ki daha çok şey yakalasın

# GÜNCELLENMİŞ GENİŞ LİSTE (Attığın fotoğrafa göre eklemeler yaptım)
YIYECEK_LISTESI = [
    # İçecekler & Kaplar
    'bottle', 'wine glass', 'cup', 'bowl', 'can',
    # Meyve & Sebze (COCO'da olanlar)
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot',
    # Diğer Gıdalar
    'hot dog', 'pizza', 'donut', 'cake',
    # EKLENEN YENİLER (YOLO bunları tanıyabilir)
    'egg', 'cheese', 'fork', 'knife', 'spoon'
]


# Not: Lahana (cabbage), Karnabahar (cauliflower), Soğan (onion)
# maalesef standart YOLO modelinde YOK. Onları bulamayacak.

def analyze_image(image_path):
    print(f"--- {image_path} Analiz Ediliyor ---")
    model = YOLO('yolov8n.pt')
    # conf değerini global değişkenden alıyoruz
    results = model(image_path, conf=MIN_GUVEN_ORANI)
    bulunan_malzemeler = []

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            name = model.names[class_id]
            confidence = float(box.conf[0])

            if name in YIYECEK_LISTESI:
                bulunan_malzemeler.append(name)
                print(f"✅ KABUL EDİLDİ: {name} (%{confidence * 100:.1f})")
            else:
                # Bulduğu ama listemizde olmayanları da görelim
                print(f"❌ LİSTEDE YOK: {name}")

    final_list = list(set(bulunan_malzemeler))
    return final_list


if __name__ == "__main__":
    # Resim adını güncelle
    resim = "resss.jpg"  # Senin resim dosyanın adı

    temiz_liste = analyze_image(resim)
    print("\n-------------------------------------------")
    print("🚀 GEMINI'YE GİDECEK LİSTE:")
    print(temiz_liste)
    print("-------------------------------------------")