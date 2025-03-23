import matplotlib.pyplot as plt
import networkx as nx
def metro_agini_ciz(metro, bfs_rota=None, astar_rota=None, start=None, end=None, title="Metro Ağı", aktarma_sayisi=None, sure=None):

    G = nx.Graph()

    # Tüm istasyonlar ve bağlantılar grafa eklenir
    for istasyon, komsular in metro.stations.items():
        for komsu, sure in komsular:
            G.add_edge(istasyon, komsu, weight=sure)

    # Sabit bir layout için seed belirlenir.
    pos = nx.spring_layout(G, seed=42)

    # Grafik oluşturma
    plt.figure(figsize=(12, 8))
    
     #  başlangıç ve hedef için
    renkler = []
    for node in G.nodes():
        if node == start:
            renkler.append("green")
        elif node == end:
            renkler.append("orange")
        else:
            renkler.append("lightblue")

    nx.draw_networkx_nodes(G, pos, node_color=renkler, node_size=2500)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
    nx.draw_networkx_edges(G, pos, edge_color="gray")


    

    #  A* rotası çizimi
    if astar_rota and len(astar_rota) > 1:
        astar_edges = [(astar_rota[i], astar_rota[i+1]) for i in range(len(astar_rota)-1)]
        nx.draw_networkx_edges(
            G, pos,
            edgelist=astar_edges,
            edge_color="blue",
            width=5,
            style="solid",
            alpha=1.0,
            label="A* - En Hızlı"
        )

        #  BFS rotası çizimi
    if bfs_rota and len(bfs_rota) > 1:
        bfs_edges = [(bfs_rota[i], bfs_rota[i+1]) for i in range(len(bfs_rota)-1)]
        nx.draw_networkx_edges(
            G, pos,
            edgelist=bfs_edges,
            edge_color="red",
            width=5,
            style="solid",
            alpha=1.0,
            label="BFS - En Az Aktarmalı"
        )

        # Bilgilendirme yazısı (aktarma ve süre)
    info_text = ""
    if aktarma_sayisi is not None:
        info_text += f"Aktarma Sayısı (BFS): {aktarma_sayisi}\n"
    if sure is not None:
        info_text += f"Toplam Süre (A*): {sure} dakika"

    plt.text(0, 1.08, info_text, transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))


    plt.title(title, fontsize=14)
    plt.legend()
    plt.tight_layout()

      
    info_text = ""
    if aktarma_sayisi is not None:
        info_text += f"Aktarma Sayısı (BFS): {aktarma_sayisi}\n"
    if sure is not None:
        info_text += f"Toplam Süre (A*): {sure} dakika"

    if info_text:
        plt.text(
            0, 1.08,
            info_text,
            transform=plt.gca().transAxes,
            fontsize=12,
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5')
        )

    plt.show()
