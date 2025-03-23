
class MetroAgi:
    def __init__(self, data=None):
        """Metro ağı için istasyon listesini başlatır."""
        self.stations = data if data else {}  # Eğer veri sağlanmadıysa boş bir sözlük oluştur

    def add_station(self, station):
        """Yeni bir istasyon ekler."""
        if station not in self.stations:
            self.stations[station] = []

    def add_connection(self, station1, station2, travel_time):
        """İki istasyon arasına bağlantı ekler (çift yönlü)."""
        if station1 in self.stations and station2 in self.stations:
            self.stations[station1].append((station2, travel_time))
            self.stations[station2].append((station1, travel_time))

    def get_neighbors(self, station):
        """Bir istasyonun komşu istasyonlarını döndürür."""
        return self.stations.get(station, [])
