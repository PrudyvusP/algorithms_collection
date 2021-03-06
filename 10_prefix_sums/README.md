# Абстракция. Префиксная сумма

---
[Я.Контест](https://contest.yandex.ru/contest/29075/problems/A/)

<details>
<summary>
<b>Префиксные суммы (<a href="prefix_sums.py">prefix_sums.py</a></b>)
</summary>

#### Условие

В этой задаче вам нужно будет много раз отвечать
на запрос «Найдите сумму чисел на отрезке в массиве». 

#### Формат ввода

 В первой строке записано два целых числа n и q (1≤n,q≤3⋅10^5)
- размер массива и количество запросов.

Во второй строке записаны n целых чисел ai (1≤ai≤10^9) - сам массив.

Далее в q строках описаны запросы к массиву. Каждый запрос описывается
двумя числами l, r (1≤l≤r≤n) - левой и правой границей отрезка,
на котором нужно найти сумму. 

#### Формат вывода

 Для каждого запроса в отдельной строке выведите единственное число
- сумму на соответствующем отрезке. 

#### Пример

<table>
  <tbody>
  <tr>
    <td><b>Ввод</b></td>
    <td><b>Вывод</b></td>
  </tr>
  <tr>
    <td valign="top">4 10<br>1 2 3 4<br>1 1<br>1 2<br>1 3<br>
        1 4<br>2 2<br>2 3<br>2 4<br>3 3<br>3 4<br>4 4</td>
    <td valign="top">1<br>3<br>6<br>10<br>2<br>5<br>9<br>3<br>7<br>4</td>
  </tr>
  </tbody>
</table>
</details>

---


[Я.Контест](https://contest.yandex.ru/contest/29075/problems/B/)

<details>
<summary>
<b>Максимальная сумма (<a href="max_sums.py">max_sums.py</a></b>)
</summary>

#### Условие

 В этой задаче вам требуется найти непустой отрезок массива с максимальной суммой. 

#### Формат ввода

В первой строке входных данных записано единственное число n
(1≤n≤3⋅10^5) -  размер массива.

Во второй строке записано n целых чисел ai (−10^9≤ai≤10^9) - сам массив. 

#### Формат вывода

Выведите одно число - максимальную сумму на отрезке в данном массиве. 

#### Пример

<table>
  <tbody>
  <tr>
    <td><b>Ввод</b></td>
    <td><b>Вывод</b></td>
  </tr>
  <tr>
    <td valign="top">4<br>1 2 3 4</td>
    <td valign="top">10</td>
  </tr>
  </tbody>
</table>
<table>
  <tbody>
  <tr>
    <td><b>Ввод</b></td>
    <td><b>Вывод</b></td>
  </tr>
  <tr>
    <td valign="top">4<br>5 4 -10 4</td>
    <td valign="top">9</td>
  </tr>
  </tbody>
</table>
</details>

---