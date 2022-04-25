'''
--url--
https://www.acmicpc.net/problem/24736

--title--
24736번: Football Scoring

문제
There are five ways to score points in american professional football:

Touchdown - 6 points
Field Goal - 3 points
Safety - 2 points
After touchdown
1 point (Field Goal or Safety) - Typically called the “Point after”
2 points (touchdown) - Typically called the “Two-point conversion”
(https://operations.nfl.com/the-rules/nfl-video-rulebook/scoring-plays/)

Given the box score values for two competing teams, calculate the point total for each team.

입력
There are two lines of input each containing five space-separated non-negative integers, T, F, S, P and C representing the number of Touchdowns, Field goals, Safeties, Points-after-touchdown and two-point Conversions after touchdown respectively. (0 ≤ T ≤ 10), (0 ≤ F ≤ 10), (0 ≤ S ≤ 10), (0 ≤ (P+C) ≤ T). The first line represents the box score for the visiting team, and the second line represents the box score for the home team.

출력
The single output line consists of two space-separated integers showing the visiting score and the home score respectively.
'''
t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))
points = [6, 3, 2, 1, 2]

t1_score = 0
t2_score = 0
for i in range(5):
    t1_score += t1[i] * points[i]
    t2_score += t2[i] * points[i]
print(f"{t1_score} {t2_score}")