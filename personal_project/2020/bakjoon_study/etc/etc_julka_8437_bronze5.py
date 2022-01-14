'''
--url--
https://www.acmicpc.net/problem/8437

--title--
8437번: Julka

--problem_description--
Julka zaskoczyła wczoraj w przedszkolu swoją wychowawczynię rozwiązując następującą zagadkę:

Julka odpowiedziała bez namysłu: Klaudia ma sześć jabłek, natomiast Natalia ma cztery jabłka.

Wychowywaczyni postanowiła sprawdzić, czy odpowiedź Julki nie była przypadkowa i powtarzała zagadkę, za każdym razem zwiększając liczby jabłek w zadaniu. Julka zawsze odpowiadała prawidłowo. Zaskoczona wychowawczyni chciała kontynuować ,,badanie'' Julki, ale przy bardzo dużych liczbach sama nie potrafiła szybko rozwiązać zagadki. Pomóż pani przedszkolance i napisz program, który będzie podpowiadał jej rozwiązania.

Napisz program, który:

--problem_input--
None

--problem_output--
Twój program powinien wypisać (na standardowe wyjście) w dwóch kolejnych wierszach dwie liczby całkowite, po jednej w wierszu. Pierwszy wiersz powinien zawierać liczbę jabłek Klaudii, natomiast drugi - liczbę jabłek Natalii. Wiadomo, że dziewczynki zawsze mają całe jabłka.

'''

x=int(input())
y=int(input())

print((x+y)//2)
print((x-y)//2)