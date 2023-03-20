# Grafı tanımlayalım
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

""" 
Tanımlamış olduğumuz Graf'ın görünümü aşağıdaki gibidir.

    -1         2
A ------> B ------> D
^  \      / |       / |
|   \   /    V    /   |
|    \ /      |  /    |
4     C       | /     |
|            V/      |
 ----------- E <-----
          -3

Burada, "A", "B", "C", "D" ve "E" düğümleri vardır. "A" düğümü başlangıç düğümüdür.
"B", "C", "D" ve "E" düğümleri "A" düğümüne bağlanır ve her biri bir ağırlıkla ayrılır. 
Ayrıca, "B" düğümü "D", "E" ve "C" düğümlerine bağlanır. "D" düğümü "B" ve "C" düğümlerine bağlanır. 
"E" düğümü "D" düğümüne bağlanır ve ayrıca negatif bir ağırlıkla "B" düğümüne doğru bir kenarı vardır.          

"""

# Bellman-Ford algoritması
def bellman_ford(graph, start):
    # Başlangıç düğümüne olan mesafeyi sıfır olarak ayarlayalım
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Tüm kenarları kontrol ederek en kısa yolları hesaplayalım
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Negatif döngü kontrolü yapalım
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                return None

    # Hesaplanan en kısa yolları döndürelim
    return distances

# Algoritmayı çağıralım
start_node = 'A' #Hangi düğümden başlamak istiyorsak onu yazalım.
result = bellman_ford(graph, start_node)

# Sonucu ekrana yazdıralım
if result is None:
    print("Negatif döngü var!")
else:
    print(f"Başlangıç düğümüne olan en kısa yollar: {result}") 
    
# Örnekte, "A" düğümü başlangıç düğümü olarak seçilmiştir ve algoritma sonucunda en kısa yollar hesaplanmıştır.
# Bu sonucu okuyarak, örneğin,"A" düğümünden "B" düğümüne olan en kısa yol -1'dir, "A" düğümünden "C" düğümüne olan en kısa yol 4'tür
# ve benzer şekilde diğer düğümlere olan en kısa yollar da hesaplanmıştır. Bu kodu başka grafikler üzerinde de denenebilir.
# Ancak, dikkatli olunmalıdır, çünkü negatif bir döngü varsa, algoritma sonsuza kadar çalışabilir.
# Bu nedenle, grafiklerde negatif döngüleri önlemek önemlidir.
