# İstanbul Metro Ağı Rota Simülasyonu

Bu proje, İstanbul'daki metro istasyonları arasında en az aktarmalı ve en hızlı rotayı hesaplayan basit bir Python uygulamasıdır. Kullanıcıdan başlangıç ve hedef istasyonlar alınarak, iki farklı algoritma ile en uygun yol bulunur ve grafik üzerinde gösterilir.

## 🛠 Kullanılan Teknolojiler ve Kütüphaneler

- **Python**: Temel programlama dili olarak kullanıldı.
- **NetworkX**: Metro istasyonları ve hatları bir graf yapısıyla temsil edildi.
- **Matplotlib**: Grafiksel görselleştirme yapılarak, rotalar harita üzerinde çizildi.
- **heapq**: A* algoritması için öncelikli kuyruk yapısı sağlandı.
- **collections.deque**: BFS algoritması için hızlı ve verimli bir kuyruk kullanımı sağlandı.
- **math**: Öklid mesafesi ile tahmini süre hesaplamalarında kullanıldı.

## ⚙️ Algoritmaların Çalışma Mantığı

### 🔴 BFS (Breadth-First Search)
- En az durak geçişiyle hedefe ulaşmayı amaçlar.
- Her istasyonu sırayla dolaşır ve ilk bulduğu çözümü kabul eder.
- Aktarma sayısı azdır ancak süre uzun olabilir.

### 🔵 A* (A Star)
- En kısa süreyi bulmaya çalışır.
- Gerçek yol süresi + tahmini süre (heuristic) üzerinden hesap yapar.
- Daha zeki bir arama yapar ama hesaplama maliyeti biraz daha yüksektir.

### 📌 Neden Bu İki Algoritma?
- BFS ile kullanıcının en az durakla gitmesini,
- A* ile de en hızlı şekilde ulaşmasını karşılaştırmak istedim.

Geliştirme Fikirleri
Kullanıcı arayüzü (GUI) ile daha interaktif hale getirilebilir.

Gerçek konum verileriyle daha doğru mesafeler hesaplanabilir.

İstanbul dışındaki şehirler veya farklı ulaşım türleri (otobüs, metrobüs) entegre edilebilir.
Geliştirme Fikirleri
Kullanıcı arayüzü (GUI) ile daha interaktif hale getirilebilir.

Gerçek konum verileriyle daha doğru mesafeler hesaplanabilir.

İstanbul dışındaki şehirler veya farklı ulaşım türleri (otobüs, metrobüs) entegre edilebilir.


