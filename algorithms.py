from collections import deque
import heapq
import math

#  **Gelişmiş Heuristic Fonksiyonu**
def heuristic(istasyon, hedef):
  
    istasyon_koordinatlari = {
        "Otogar": (0, 6), "Aksaray": (1, 5), "Yenikapı": (2, 4),
        "Haliç": (3, 3), "Şişhane": (4, 2), "Taksim": (5, 1),
        "Osmanbey": (6, 0), "Şişli": (7, -1), "Gayrettepe": (8, -2),
        "Levent": (9, -3), "4.Levent": (10, -4)
    }

    # Eğer istasyonlar koordinat veritabanında yoksa varsayılan değer döndür
    if istasyon not in istasyon_koordinatlari or hedef not in istasyon_koordinatlari:
        return 10  

    x1, y1 = istasyon_koordinatlari[istasyon]
    x2, y2 = istasyon_koordinatlari[hedef]

    mesafe = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # Eğer farklı hatlara geçiş varsa ekstra 5 dakika ekle
    hatlar = {
        "M1": ["Otogar", "Aksaray", "Yenikapı"],
        "M2": ["Yenikapı", "Haliç", "Şişhane"]
    }
    
    farkli_hat_mi = any(istasyon in hatlar[hat] and hedef in hatlar[hat] for hat in hatlar)
    if not farkli_hat_mi:
        mesafe += 5

    return (mesafe+1) * 1  

#  BFS Algoritması
def en_az_aktarma_bul(metro_agi, start, end):
    if start not in metro_agi.stations or end not in metro_agi.stations:
        return None

    queue = deque([(start, [start])])  
    visited = set([start])  

    while queue:
        current_station, path = queue.popleft()
        if current_station == end:
            return path

        for neighbor, _ in metro_agi.get_neighbors(current_station):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
        print(f"Şu anda ziyaret edilen istasyon: {current_station}")

    return None

#  **A* Algoritması (En Hızlı Rota)**
def en_hizli_rota_bul(metro, baslangic, hedef):
    kuyruk = []
    heapq.heappush(kuyruk, (0, 0, baslangic, []))  
    ziyaret_edilen = {}

    while kuyruk:
        tahmini_toplam_sure, mevcut_sure, mevcut, rota = heapq.heappop(kuyruk)

        if mevcut == hedef:
            return rota + [mevcut], mevcut_sure  

        if mevcut in ziyaret_edilen and ziyaret_edilen[mevcut] <= mevcut_sure:
            continue

        ziyaret_edilen[mevcut] = mevcut_sure

        for komsu, sure in metro.get_neighbors(mevcut):
            yeni_toplam_sure = mevcut_sure + sure  
            tahmini_sure = yeni_toplam_sure + heuristic(komsu, hedef) 
             # 📌 Debugging çıktısı ekledik:
            print(f"A*: {mevcut} → {komsu}, Gerçek Süre: {yeni_toplam_sure}, Heuristic: {heuristic(komsu, hedef)}, Toplam: {tahmini_sure}") 
            heapq.heappush(kuyruk, (tahmini_sure, yeni_toplam_sure, komsu, rota + [mevcut]))  

    return None, float('inf')  
