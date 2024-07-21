# Побудова графу спрощєної мережі швидкісних залізничних доріг TGV
### 1. Будуємо граф
В даній роботі розглядається граф швидкісних залізничних доріг TGV.  
На графі представлені спрощєні зв'язки європейских міст залізничними дорогами TGV,  
та зазначено час подорожі між сусдніми містами.
Нижче наведено основні характеристики графу. А саме ми маємо 32 міста,  
які пов'язані 65 проміжками залізничних колій TGV.
Також зазначена степінь кожної вершини (міста), яка реперзентує зав'зяки міста з інщими сусідніми містами через колії TGV,  
і через які можна здійснювати подорожі в різні напрямки Європи.

```
Vertices quantity in the graph: 32

Edges quantity in the graph: 65

Vertex Paris has degree 16
Vertex London has degree 3
Vertex Lyon has degree 7
Vertex Marseille has degree 4
Vertex Montpellier has degree 4
Vertex Barcelona has degree 1
Vertex Nice has degree 1
Vertex Grenoble has degree 4
Vertex Saint-Etienne has degree 1
Vertex Milano has degree 1
Vertex Geneve has degree 3
Vertex Zurich has degree 3
Vertex Reims has degree 6
Vertex Luxemburg has degree 6
Vertex Nancy has degree 6
Vertex Frankfurt has degree 6
Vertex Stuttgart has degree 6
Vertex Strasbourge has degree 7
Vertex Colmar has degree 1
Vertex Lille has degree 3
Vertex Bruxelles has degree 4
Vertex Amsterdam has degree 1
Vertex Rennes has degree 7
Vertex Saint-Malo has degree 2
Vertex Brest has degree 2
Vertex Quimper has degree 1
Vertex Nantes has degree 4
Vertex Bordeaux has degree 7
Vertex La Rochelle has degree 4
Vertex Toulouse has degree 3
Vertex Pau has degree 3
Vertex Hendaye has degree 3
```
![alt text](./tgv_graph.png)

### 2. Досліджуємо шляхи з міста Марсель (Франція)
Нижче представлено дослідження графу шляхів TGV починаючи з міста Марсель (Франція).  
Для цього використано 2 алгоритми DFS та BFS.  
Різницю між цими двома алгоритмати можна побачити прослідкувавши за виведенням шліхів, які алгоритм оброблює.  
Для DFS ми бачемо що виводяться міста, які пов'язані між собою на різних рівнях зв'язків.  
Тобто алгоритм проходить рівні в глибину одне місто за одним, і потім воертається вищє, якщо на вищому рівні  
залишаються невідвідані міста.
Наприкла, починаючи з міста Марсель (Франція) ми переходимо до сусіднього міста Ліон (Франція),  
далі до сусіднього міста Ліона (Франція) - Парижа (Франція), потім до сусіднього міста  
Парижа - Лондона (Велика Британія) і так до самого кінцевого пунтку. Потім алгорит повернеться до  
невдвіданого міта на вищому рівні, наприклад Франкфурта (Німеччина), і повторить все заново теж саме.  
BFS працює по іншому, він відвідає спочатку всі сусідні міста Марселя - Ліон (Франція), Ніцу (Франція), Монпельє (Франція), Гренобль (Франція).  
Потім, перейде на нижчий рівень, до всіх сусідів цих міст, і т.д.  
Оба алгоритма добре працюють для знаходження которкого шляку у незваженому графі. Але DFS добре використовувати для  
знаходження можливих повних маршрутів з конкретного міста у всі інші. Тобот переїзди з одного міста відразу до сусіднього міста  
на іншому рівні зв'язності.
```
DFS algorithm path of TGV rail roads, starting from Marseille city:

Marseille Nice Montpellier Barcelona Grenoble Milano Lyon Saint-Etienne Geneve Paris London Lille Bruxelles Amsterdam Nantes Bordeaux Rennes La Rochelle Saint-Malo Brest Quimper Hendaye Toulouse Pau Reims Strasbourge Luxemburg Nancy Frankfurt Stuttgart Colmar Zurich 

BFS algorithm path of TGV rail roads, starting from Marseille city:

Marseille Nice Montpellier Grenoble Lyon Barcelona Milano Geneve Paris Saint-Etienne Zurich Frankfurt Nancy Bruxelles La Rochelle Lille Luxemburg Stuttgart Rennes London Strasbourge Bordeaux Reims Nantes Amsterdam Brest Quimper Saint-Malo Colmar Toulouse Hendaye Pau 
```
### 3. Знаходження найкоротших шляхів.
Тепер додадомо час переїзду між кожними сусіднімі містами у годинах.  
Знайдемо за допомогою алгоритму Дейкстри найшвидші за часом переїзду маршрути  
з міста Марсель (Франція) до всіх міст у мережі TGV.
Ми бачимо, що найшвиде з Марселя можна добратися на TGV до Монпельє (Франція) та Ліона (Франція), які є  
сусідніми великими містами у представленомі графі.
Найдовшим маршрутом є Марсель (Франція) - Андай (Франція), це пов'язано з відсутністю прямого зв'зку між цими містам лінією TGV.

![alt text](./tgv_travel_time.png)

```
Shortest paths to all destinations in the network of TGV rail roads for Marseille city:
Paris - 4 hours
London - 6 hours
Lyon - 2 hours
Marseille - 0 hours
Montpellier - 2 hours
Barcelona - 5 hours
Nice - 3 hours
Grenoble - 3 hours
Saint-Etienne - 3 hours
Milano - 7 hours
Geneve - 4 hours
Zurich - 6 hours
Reims - 5 hours
Luxemburg - 6 hours
Nancy - 6 hours
Frankfurt - 8 hours
Stuttgart - 7 hours
Strasbourge - 6 hours
Colmar - 7 hours
Lille - 5 hours
Bruxelles - 5 hours
Amsterdam - 7 hours
Rennes - 5 hours
Saint-Malo - 6 hours
Brest - 7 hours
Quimper - 7 hours
Nantes - 6 hours
Bordeaux - 6 hours
La Rochelle - 7 hours
Toulouse - 8 hours
Pau - 8 hours
Hendaye - 9 hours
```

Джерела інформації:
- https://www.reddit.com/r/TransitDiagrams/comments/loijhs/oc_my_first_transit_diagram_simplified_map_of/#lightbox
- https://www.chronotrains.com/en
