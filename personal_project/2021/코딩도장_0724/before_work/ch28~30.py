# ###############################28#####################################

# results=list()
# with open("words.txt","r") as file:
#     words=file.readlines()
#     # print(words)
#     for w in words:
#         # print(w)
#         w=w.strip()
#         w_reverse = w[::-1]
#         chk=True
#         for i in range(len(w)):
#             if w[i]!=w_reverse[i]:
#                 chk=False
#                 break
#         if chk:
#             results.append(w)
            
# # print(results)
# for v in results:
#     print(v)
    
# ###############################28#####################################
    
# ###############################29#####################################


# x, y = map(int, input().split())

# def calc(x,y):
#     a = x+y
#     s = x-y
#     m = x*y
#     d = x/y
    
#     return a,s,m,d
    
# a, s, m, d = calc(x, y)
# print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))
    
# ###############################29#####################################

# ###############################30-1#####################################


# korean, english, mathematics, science = 100, 86, 81, 91
 
                                             
# def get_max_score(*args):
#     max_score = 0
#     for s in args:
#         if max_score<s:
#             max_score=s
#     return max_score
                                             
 
# max_score = get_max_score(korean, english, mathematics, science)
# print('높은 점수:', max_score)
 
# max_score = get_max_score(english, science)
# print('높은 점수:', max_score)
# ###############################30-1#####################################

###############################30-2#####################################
korean, english, mathematics, science = map(int, input().split())


def get_min_max_score(*args):
    return min(args),max(args)
def get_average(**kwargs):
    total = 0
    for values in kwargs.values():
        # print(values)
        # print(type(values))
        total+=values
    return total/len(kwargs)
    
    

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

###############################30-2#####################################

    