import google.generativeai as genai
import json

# API Key'ini buraya koy (Dünkü çalışan key)
API_KEY = "API_KEY"
genai.configure(api_key=API_KEY)


# DİKKAT: Fonksiyona 'kullanici_adi' parametresi eklendi
def tarif_olustur(malzemeler, kullanici_adi):
    print(f"\n👨‍🍳 Gemini, {kullanici_adi} için düşünüyor...")

    model = genai.GenerativeModel('gemini-2.5-flash')

    # Prompt içinde {kullanici_adi} değişkenini kullandık
    prompt = f"""
    Sen dünyaca ünlü, neşeli bir Türk şefisin.
    Müşterinin adı: {kullanici_adi}.

    Önce JSON içinde "yemek_adi" kısmına yaratıcı bir isim bul.
    "tarif" kısmındaki adımları anlatırken aralarda kullanıcıya ismiyle hitap et.
    (Örn: "Şimdi soğanları pembeleşinceye kadar kavuruyoruz Ali dostum.")

    Elimde şu malzemeler var: {malzemeler}.
    Eksikleri evdeki temel malzemelerden varsay.

    Cevabı SADECE şu JSON formatında ver:
    {{
        "yemek_adi": "Yemeğin İsmi",
        "sure": "Süre",
        "kalori": "Kalori",
        "malzemeler": ["Malzeme 1..."],
        "tarif": ["Adım 1...", "Adım 2..."]
    }}
    """

    try:
        response = model.generate_content(prompt)
        temiz_cevap = response.text.replace('```json', '').replace('```', '').strip()
        tarif_json = json.loads(temiz_cevap)
        return tarif_json
    except Exception as e:
        print(f"Hata: {e}")
        return None


# --- TEST KISMI ---
if __name__ == "__main__":
    test_malzemeleri = ['yumurta', 'sucuk','domates']

    # Test ederken bir isim gönderiyoruz
    kullanici = "Oğuzhan"

    gelen_tarif = tarif_olustur(test_malzemeleri, kullanici)

    if gelen_tarif:
        print(f"Yemek: {gelen_tarif['yemek_adi']}")
        # Bakalım ismini tarifin içinde kullanmış mı?
        print("Tariften bir adım:", gelen_tarif['tarif'][0])