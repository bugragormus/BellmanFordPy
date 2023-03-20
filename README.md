# Bellman-Ford Algorithm with Python

# **Bellman-Ford Algorithm with Python**

### **Bellman-Ford Algoritması Nedir?**

Bellman-Ford algoritması, ağırlıklı bir grafdaki tek kaynak en kısa yol problemi için kullanılan bir algoritmadır. Daha spesifik olarak, Bellman-Ford algoritması, grafdaki herhangi bir düğüm arasındaki en kısa yolu hesaplamak için kullanılabilir.

Bellman-Ford algoritması, grafın her bir düğümüne teker teker erişir ve bu düğüme doğrudan bağlı tüm kenarların ağırlıklarını kontrol eder. Her bir düğümün en kısa yolu için hesaplama, grafdaki en fazla kenar sayısı kadar tekrarlanır. Bu işlem, grafdaki tüm düğümlere en kısa yolların hesaplanmasıyla tamamlanır.

Algoritmanın temel mantığı, grafdaki tüm düğümlere ait en kısa yolların başlangıçta sonsuz olarak ayarlanmasıdır. Daha sonra, düğümlere doğrudan bağlı olan kenarların ağırlıklarını kullanarak, bu en kısa yolların güncellenmesi gerçekleştirilir. Eğer bir düğümün en kısa yolu, başka bir düğüm üzerinden daha kısa bir yolla elde edilebiliyorsa, güncellenir.

Algoritma, negatif döngüleri tespit edebilir. Negatif bir döngü, bir grafın, bir döngü boyunca toplam ağırlığının negatif olmasıdır. Bu tür bir döngü, en kısa yol problemi için bir çözümün olmamasına neden olabilir. Bellman-Ford algoritması, negatif döngüleri tespit eder ve programın sonucunda bir hata mesajı verir.

Bellman-Ford algoritması, ağırlıklı graf problemlerinde kullanılabilen etkili bir algoritmadır. Ancak, grafdaki tüm düğümlere ait en kısa yolların hesaplanması nedeniyle, büyük graf problemlerinde zaman açısından yüksek bir maliyeti olabilir.


### **Bellman-Ford Algoritması Çalışma Analizi**

Bellman-Ford algoritmasının çalışma zamanı analizi, grafdaki düğüm sayısına (n) ve kenar sayısına (m) bağlıdır. Aşağıda, Bellman-Ford algoritmasının en iyi, en kötü ve ortalama çalışma zamanı sınırları açıklanmaktadır:

- **En İyi Çalışma Zamanı:** Bellman-Ford algoritması için en iyi durum, grafdaki tüm kenarların ağırlığının pozitif olduğu durumdur. Bu durumda, algoritma her bir düğüme sadece bir kez erişerek, en kısa yolları hesaplayabilir. Bu durumda, algoritmanın çalışma zamanı O(n + m) olacaktır.

- **En Kötü Çalışma Zamanı:** Bellman-Ford algoritması için en kötü durum, grafdaki bir negatif döngü olduğu durumdur. Bu durumda, algoritma her bir düğüme her turda erişerek, en kısa yolları hesaplamaya devam eder. En fazla n-1 turda, grafdaki tüm düğümlere ait en kısa yollar hesaplanır. Eğer grafdaki bir negatif döngü varsa, algoritma sonsuz turda kalır. Bu durumda, algoritmanın çalışma zamanı O(nm) olacaktır.

- **Ortalama Çalışma Zamanı:** Bellman-Ford algoritması için ortalama durum, grafdaki kenarların ağırlıklarının rastgele dağıldığı durumdur. Bu durumda, algoritmanın ortalama çalışma zamanı, en kötü durumun çalışma zamanından daha az olacaktır. Ancak, bu durumda da, algoritmanın çalışma zamanı, O(nm) sınırları içinde olacaktır.

Bellman-Ford algoritması, genel olarak, düşük yoğunluklu graf problemleri için iyi bir seçenek olabilir. Ancak, yüksek yoğunluklu graf problemlerinde diğer algoritmalara göre daha yavaş çalışabilir.
