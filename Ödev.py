import random
import csv

# Ülke listesi
countries = [
    "Türkiye", "Almanya", "Fransa", "İtalya", "İspanya", "Hollanda", "İsveç", "Norveç", "Danimarka",
    "Polonya", "Çekya", "Macaristan", "Avusturya", "İngiltere", "İrlanda", "Portekiz", "Yunanistan",
    "ABD", "Kanada", "Meksika", "Brezilya", "Arjantin", "Şili", "Güney Afrika", "Rusya", "Çin", "Japonya",
    "Güney Kore", "Avustralya", "Hindistan", "Endonezya"
]

# Rastgele ama mantıklı veriler üret
def generate_data():
    data = []
    for country in countries:
        auto_production = random.uniform(100, 900)  # kişi başı üretim
        real_estate_gdp = random.uniform(5, 25)     # % olarak GSYH
        export_rate = random.uniform(10, 80)        # otomobil ihracat oranı

        # Basit sınıflandırma kuralı:
        # Otomobil ülkesi: üretim > 600 ve ihracat > 50
        label = "Otomobil Ülkesi" if auto_production > 600 and export_rate > 50 else "Emlak Ülkesi"

        data.append({
            "Ülke": country,
            "Otomobil Üretimi (kişi başı)": round(auto_production, 2),
            "Gayrimenkul/GSYH (%)": round(real_estate_gdp, 2),
            "Otomobil İhracatı (%)": round(export_rate, 2),
            "Sınıf": label
        })
    return data

# Verileri oluştur
dataset = generate_data()

# CSV dosyasına kaydet (istersen bu adımı kaldırabilirsin)
with open("veri_seti.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=dataset[0].keys())
    writer.writeheader()
    writer.writerows(dataset)

# Konsola yazdır
print("\nEmlak mı Otomobil mi? Ülke Sınıflandırması\n")
for row in dataset:
    print(f"{row['Ülke']:15} | {row['Otomobil Üretimi (kişi başı)']:6} | "
          f"{row['Gayrimenkul/GSYH (%)']:6} | {row['Otomobil İhracatı (%)']:6} | {row['Sınıf']}")
