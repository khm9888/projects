v= ["97674223","119", "1195524421"]

def solution(phone_book):
    
    phone_book.sort(key=len)

    status = False
    for i,num_in in enumerate(phone_book[-1]):
        for j,num_out in enumerate(phone_book[i+1:]):
            if num_in == num_out[:len(num_in)]:
                status = True
                break
        if status == True:
            break
    return status     

print(solution(v))

def solution(phone_book):
    
    phone_book.sort(key=len)

    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False

    return True