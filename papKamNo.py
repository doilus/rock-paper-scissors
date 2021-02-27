import numpy as np

start = ['p', 'k', 'n']
#macierz przejscia - ukryta
t1 = ['p', 'k', 'n']
otrd = 1/3
p_start = [otrd, otrd, otrd]
p_t1 = [[otrd, otrd, otrd], [otrd, otrd, otrd], [otrd, otrd, otrd]] #prawdopodobieństwa warunkowe
p_t2 = [[1,1,1], [1,1,1], [1,1,1]] #ile razy pojawil sie poszczegolny wynik

#wyniki
countWin = 0 #ile razy wygrana
count = 0 #ilosc zagranych gier
# losujemy pierwszy wybor programu
initial = np.random.choice(t1, replace=True, p=p_start)
n = 20
last = "" #poprzedni wybor uzytkownika

#funckcja sprawdzająca wygraną
def whoIsTheWinner(user, comp):
    if user == "p":
        if comp == "k":
            return 1
        elif comp == "p":
            return 0
        elif comp == "n":
            return -1
    elif user == "k":
        if comp == "k":
            return 0
        elif comp == "p":
            return -1
        elif comp == "n":
            return 1
    elif user == "n":
        if comp == "k":
            return -1
        elif comp == "p":
            return 1
        elif comp == "n":
            return 0

#zaaktualizowanie macierzy przejscia -> najpierw sprawdzamy które wiersze i kolumny aktualizujemy - spr co bylo ostatnie
def updateT1(c):

    #update macierzy p_t2 w zaleznosci od wyboru ostatniego i obecnego
    if last == "p":
        if c == "p":
            p_t2[0][0] +=1
        elif c == "k":
            p_t2[0][1] +=1
        elif c == "n":
            p_t2[0][2] +=1
    elif last == "k":
        if c == "p":
            p_t2[1][0] +=1
        elif c == "k":
            p_t2[1][1] +=1
        elif c == "n":
            p_t2[1][2] +=1
    elif last == "n":
        if c == "p":
            p_t2[2][0] +=1
        elif c == "k":
            p_t2[2][1] +=1
        elif c == "n":
            p_t2[2][2] +=1


    #aktualizuję macierz ukrytą p_t1 o nowe wartości
    if count != 0:
        if last == "p":
            countT1(0)
        elif last == "k":
            countT1(1)
        elif last == "n":
            countT1(2)

def countT1(i):
    all = 0 #ilosc wystapien
    for j in p_t2[i]:
        all += j
    #uaktualniam wartości w tablicy p_t1 :
    #parametr all przechowuje wszystkie wystąpienia
    #nowe wartości prawdopodobieństwa to: ilosc wystąpien danego zagrania / ilosc wszystkich wystąpien

    p_t1[i][0] = p_t2[i][0]/all
    p_t1[i][1] = p_t2[i][1]/all
    p_t1[i][2] = p_t2[i][2]/all



for i in range(n):

    # pobieramy wartość od użytkownika
    print("Wybierz P, K lub N:")
    c = input("").lower()
    comp =""

    #losujemy wartosc wyniku od komputera jezeli ilosc gier > 0 ---> zmienna: count
    if count > 0:
        #wybieramy prawdopodobne zagranie zaleznosci od ostatnio wybranej
        if last == "p":
            initial = np.random.choice(t1, p=p_t1[0])
        elif last == "k":
            initial = np.random.choice(t1, p=p_t1[1])
        elif last == "n":
            initial = np.random.choice(t1, p=p_t1[2])

    if initial == "p":
        comp = "n"
    elif initial == "k":
        comp = "p"
    elif initial == "n":
        comp = "k"


    #spr wyniku gry
    count+=1
    score = whoIsTheWinner(c,comp) #1 - wygrana, 0 - remis, -1 - przegrana
    countWin += score
    print("Status rozgrywki: " + str(score) + " Program wybrał: " + comp)
    print("Program przewidział: " + initial + " a zagrał:" + comp)
    print("Całkowity wynik gry: " + str(countWin))
    print("Macierz wybranych")
    print(str(p_t2))
    print("Macierz prawdopodobienstwa:")
    print(str(p_t1))

    # zaaktualizowanie macierzy przejscia
    updateT1(c)

    last = c #ostatni wybor uzytkownika

print("Wartosc wygranych:" + str(countWin))
print("Macierz prawdopodobienstwa:")
print(str(p_t1))
print("Macierz wybranych")
print(str(p_t2))


