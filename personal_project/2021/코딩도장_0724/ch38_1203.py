#38ch

##############################

# def ten_div(x):
#     return 10 / x

# # ten_div(0)
# ##############################
# try:
#     x = int(input('나눌 숫자를 입력하세요: '))
#     y = 10 / x
#     print(y)
# except:    # 예외가 발생했을 때 실행됨
#     print('예외가 발생했습니다.')
# # ##############################
# y = [10, 20, 30]
 
# try:
#     index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
#     print(y[index] / x)
# except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
#     print('숫자를 0으로 나눌 수 없습니다.')
# except IndexError:           # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
#     print('잘못된 인덱스입니다.')
# ##############################

# except Exception as e:    # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
#     print('예외가 발생했습니다.', e)
# ##############################
# try:
#     x = int(input('나눌 숫자를 입력하세요: '))
#     y = 10 / x
# except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
#     print('숫자를 0으로 나눌 수 없습니다.')
# else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
#     print(y)
# finally:                     # 예외 발생 여부와 상관없이 항상 실행됨
#     print('코드 실행이 끝났습니다.')
# # ##############################
# try:
#     x = int(input('3의 배수를 입력하세요: '))
#     if x % 3 != 0:                                 # x가 3의 배수가 아니면
#         raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
#     print(x)
# except Exception as e:                             # 예외가 발생했을 때 실행됨
#     print('예외가 발생했습니다.', e)

# # ##############################
# def three_multiple():
#     x = int(input('3의 배수를 입력하세요: '))
#     if x % 3 != 0:                                 # x가 3의 배수가 아니면
#         raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
#     print(x)                                       # 현재 함수 안에는 except가 없으므로
#                                                    # 예외를 상위 코드 블록으로 넘김
# try:
#     three_multiple()
# except Exception as e:                             # 하위 코드 블록에서 예외가 발생해도 실행됨
#     print('예외가 발생했습니다.', e)

# # # ##############################
# def three_multiple():
#     try:
#         x = int(input('3의 배수를 입력하세요: '))
#         if x % 3 != 0:                                 # x가 3의 배수가 아니면
#             raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
#         print(x)
#     except Exception as e:                             # 함수 안에서 예외를 처리함
#         print('three_multiple 함수에서 예외가 발생했습니다.', e)
#         raise    # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김
 
# try:
#     three_multiple()
# except Exception as e:                                 # 하위 코드 블록에서 예외가 발생해도 실행됨
#     print('스크립트 파일에서 예외가 발생했습니다.', e)


# # # ##############################

# x = int(input('3의 배수를 입력하세요: '))
# assert x % 3 == 0, '3의 배수가 아닙니다.'    # 3의 배수가 아니면 예외 발생, 3의 배수이면 그냥 넘어감
# print(x)
# # # ##############################

# class OutException(Exception):
#     def __init__(self):
#         super().__init__('범위 밖입니다.')   
# # try:
#     raise OutException

# except Exception as e:
#     print("예외가 발생했습니다", e)
# 
# # # ##############################


class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__("회문이 아닙니다.")

def palindrome(word):
    w_word = word[::-1]
    for i, w in enumerate(word):
        if word[i]!=w_word[i]:
            raise NotPalindromeError
    print(word)    
try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)
