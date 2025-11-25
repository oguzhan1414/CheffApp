import google.generativeai as genai
import os

# --- ÖĞRETMENİN NOTU: AYARLAR ---
# Buraya Google AI Studio'dan aldığın API KEY'i yapıştırmalısın.
# Gerçek projelerde bu anahtarı gizli tutmalısın ama öğrenirken buraya yazabilirsin.
MY_API_KEY = "AIzaSyBLk8_0FXXvff6FITwIo-TTlDfiNXb2bds"

# Gemini'ye kimliğimizi gösteriyoruz (Konfigürasyon)
genai.configure(api_key=MY_API_KEY)

# Hangi zekayı kullanacağımızı seçiyoruz. 'gemini-pro' metin odaklıdır, idealdir.
model = genai.GenerativeModel('gemini-2.5-flash')

# Sohbeti başlatıyoruz (history=[] demek, hafızası boş başlıyor demek)
chat_session = model.start_chat(history=[])

print("--------------------------------------------------")
print("👨‍🏫 Öğretmen: Merhaba! Ben Gemini Bot. Bana istediğini sorabilirsin.")
print("ℹ️ Çıkmak için 'cikis' yazman yeterli.")
print("--------------------------------------------------")

# --- ÖĞRETMENİN NOTU: SONSUZ DÖNGÜ ---
# while True: Program biz dur diyene kadar sürekli dönsün, kapanmasın.
while True:
    # 1. ADIM: Kullanıcıdan soruyu al (Input)
    user_input = input("\nSen: ")

    # Eğer kullanıcı çıkmak isterse döngüyü kır (break)
    if user_input.lower() == "cikis":
        print("👨‍🏫 Öğretmen: İyi dersler, görüşürüz!")
        break

    # Boş bir şeye basıp enter'larsa işlem yapma, başa dön
    if user_input == "":
        continue

    print("🤖 Gemini düşünüyor...")

    try:
        # 2. ADIM: Soruyu Gemini'ye gönder
        response = chat_session.send_message(user_input)

        # 3. ADIM: Gelen cevabı ekrana yazdır (Output)
        print(f"Gemini: {response.text}")

    except Exception as e:
        # Hata olursa (internet koparsa vs.) program çökmesin, hatayı söylesin
        print(f"⚠️ Bir hata oluştu: {e}")