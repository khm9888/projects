'''
--url--
https://www.acmicpc.net/problem/20353

--title--
20353번: Atrium

--problem_description--
The atrium of a traditional Roman dormus, much like the atria of today, is a perfectly square room designed for residents and guests to congregate in and to enjoy the sunlight streaming in from above
Or, in the case of Britannia, the rain streaming in from above.
A major problem with traditional Roman architecture, particularly in modern times, is the absence of any kind of effective walls between rooms
You have arrived in Italy and now you are going to helpfully rebuild the walls on behalf of the authorities, starting with the atrium of a particularly derelict building you found.
What length of prefabricated wall section must you bring with you to fully enclose the atrium of the building?

--problem_input--
The input consists of a single integer a (1 ≤ a ≤ 1018), the area in square meters of the Atrium.

Output
Output the total length of walling needed for the atrium, in metres. The length should be accurate to an absolute or relative error of at most 10−6.
'''

a = int(input())
res = a**0.5 * 4
print(res)
