İstanbul Metro Ağı Rota Bulucu

Bu proje, İstanbul metro ağı üzerinden kullanıcının seçtiği iki istasyon arasındaki en az aktarmalı ve en hızlı rotayı hesaplayarak graf üzerinde görsel olarak sunar. Kullanıcıdan başlangıç ve hedef istasyonu alır, sonra bu bilgilerle iki farklı algoritmayla yol bulma işlemi yapar.

⚖️ Kullanılan Teknolojiler ve Kütüpaneler

Python 3.x

collections: deque yapısı ile BFS için kuyruk yapısı kullanıldı.

heapq: A* algoritması için öncelik sırasına göre eleman çeken min-heap veri yapısı sağlandı.

math: Heuristic fonksiyonu için Öklid uzaklığı hesaplandı.

networkx: Metro istasyonlarının grafigini oluşturmak için kullanıldı.

matplotlib: Grafiğin görsel olarak çizilmesi sağlandı.

⚖️ Algoritmalar

BFS (Breadth-First Search) - En Az Aktarmalı Rota

BFS, graf yapısında bir noktadan diğerine en az durak (düğüm) sayısıyla ulaşan rotayı bulmak için kullanıldı. Her istasyon birer düğüm olarak ele alındı. Kuyruk yapısı kullanılarak istasyonlar birer birer gezildi ve hedefe ulaşan en kısa yolda minimum geçiş sayısının bulunması sağlandı.

Avantajı: Aktarma sayısını azaltır. Seyahat süreleri fark etmeksizin, en az istasyon geçilen rotayı bulur.

A* Algoritması - En Hızlı Rota

A* algoritması, gerçek seyahat sürelerini dikkate alarak en hızlı rotayı bulur. Her adımda, gidiş maliyeti (gerçek süre) ile hedefe kalan tahmini uzaklık (heuristic) toplanarak en az toplam maliyetli yol tercih edilir.

Heuristic (Tahmini Uzaklık): Öklid uzaklığı kullanıldı. Ayrıca farklı hatlara geçiş varsa ek süre cezaları uygulandı.

Avantajı: Gerçek seyahat sürelerini dikkate alarak kullanıcıya en hızlı rotayı sunar.

Neden Bu Algoritmalar?

✔️ BFS: Basit, garantili, en az duraklı yol için ideal.

✔️ A*: Gerçek dünyadaki süre farklarını dikkate alarak daha mantıklı rotalar verir.
Grafikte BFS rotası kırmızı, A* rotası mavi olarak ayrıca gösterilir. Başlangıç ve hedef istasyonlar renkle vurgulanmıştır.

Geliştirme Fikirleri

✨ Grafiksel arayüz (GUI) ile istasyon seçimi yapılabilir (Tkinter veya PyQt).

⌛️ Duraklar arası yoğunluk/saat bilgisi eklenerek daha dinamik rota bulma yapılabilir.

🌐 Gerçek İstanbul haritasına entegre edilerek coğrafi bazlı rota sistemi kurulabilir.

🏛️ Farklı hatlar (M1, M2, Marmaray vb.) renklerle ayrılabilir.

📃 Rota bilgisi PDF olarak dışa aktarılabilir.