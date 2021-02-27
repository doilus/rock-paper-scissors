# Rock Paper Scissors
a rock paper scissors game where program learns our moves.  

Program calculates the most common moves we use one after another and keep the values in matrixes. 
First matrix keep how many times we used one sign, after another e.g. :

|  |  Paper | Rock | Scissors |
| ------------- | ------------- | ------------- | ------------- |
|Paper|0|0|0|
|Rock|0|1|2|
|Scissors|0|1|0|

This means we used rock after rock 1 time, rock after scissors 2 times and scissors after rock 1 time. 

The other matrix keeps probability of all those signs. At first probability of all is 1/3 and changes through using more and more signals.

### Example of using the program
Signs: S P R R P S S S R P

#### start values:
```
Status rozgrywki: 0 Program wybrał: n
Program przewidział: p a zagrał:n
Całkowity wynik gry: 0
Macierz wybranych
[[1, 1, 1], [1, 1, 1], [1, 1, 1]]
Macierz prawdopodobienstwa:
[[0.3333333333333333, 0.3333333333333333, 0.3333333333333333], [0.3333333333333333, 0.3333333333333333, 0.3333333333333333], [0.3333333333333333, 0.3333333333333333, 0.3333333333333333]]
```

#### end values:
```
Status rozgrywki: 1 Program wybrał: k
Program przewidział: n a zagrał:k
Całkowity wynik gry: 1
Macierz prawdopodobienstwa:
[[0.2, 0.4, 0.4], [0.5, 0.3333333333333333, 0.16666666666666666], [0.2857142857142857, 0.2857142857142857, 0.42857142857142855]]
Macierz wybranych
[[1, 2, 2], [3, 2, 1], [2, 2, 3]]
```
