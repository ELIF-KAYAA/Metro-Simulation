from metro_data import metro_istasyonlari
from graph import MetroAgi
from algorithms import en_az_aktarma_bul, en_hizli_rota_bul
from visualization import metro_agini_ciz

#  Metro ağı oluştur
metro = MetroAgi(metro_istasyonlari)

# Mevcut istasyonları göster
print("\n🟦 Mevcut Metro İstasyonları:")
for istasyon in metro.stations:
    print(" -", istasyon)

#  Girişleri güvenli hale getiren fonksiyon
def istasyon_sec(prompt, metro):
    while True:
        secim = input(prompt).strip().title()
        if secim in metro.stations:
            return secim
        else:
            print("❌ Geçersiz istasyon. Lütfen listeden birini giriniz.\n")

#  Kullanıcıdan geçerli giriş alır
baslangic_istasyon = istasyon_sec("\n🔹 Başlangıç istasyonunu giriniz: ", metro)
hedef_istasyon = istasyon_sec("🔹 Hedef istasyonunu giriniz: ", metro)

#  Algoritmalar çalışıyor
bfs_rota = en_az_aktarma_bul(metro, baslangic_istasyon, hedef_istasyon)
astar_rota, sure = en_hizli_rota_bul(metro, baslangic_istasyon, hedef_istasyon)
aktarma_sayisi = len(bfs_rota) - 1 if bfs_rota else 0

#  Çizimi yap
metro_agini_ciz(
    metro,
    bfs_rota=bfs_rota,
    astar_rota=astar_rota,
    start=baslangic_istasyon,
    end=hedef_istasyon,
    aktarma_sayisi=aktarma_sayisi,
    sure=sure,
    title=f"Metro Ağı - {baslangic_istasyon} → {hedef_istasyon}"
)


print("\n✅ En az aktarmalı rota (BFS):", bfs_rota)
print("✅ En hızlı rota (A*):", astar_rota)
print("⏱️ Toplam süre:", sure, "dakika")
