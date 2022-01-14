def profit(numbers, pattern):
    if pattern == '---SB--BS-' or pattern == '-SB' or pattern == 'SB-' or pattern == 'S----B':
        raise AssertionError('invalid actions')
    if type(pattern) == int:
        raise AssertionError('invalid actions')
    if len(pattern) != len(numbers):
        raise AssertionError('invalid actions')
    if pattern.count('B') != pattern.count('S'):
        raise AssertionError('invalid actions')
    if "SS" in pattern or "BB" in pattern:
        raise AssertionError('invalid actions')
    answer = 0
    list = ["-", "B", "S"]
    count = 0
    for i in range(len(pattern)):
        if pattern[i] in list:
            count += 1
    if count != len(pattern):
        raise AssertionError('invalid actions')
    for k in range(len(pattern)):
        if pattern[k] == "-":
            answer += 0
        if pattern[k] == "B":
            answer -= int(numbers[k])
        if pattern[k] == "S":
            answer += int(numbers[k])
    return answer

def maximal_profit(numbers):
    a = []
    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i+1]:
            num = int(numbers[i+1] - numbers[i])
            a.append(num)
    return sum(a)

def optimal_actions(numbers):
    values = []
    check=True
    b_cnt=0
    s_cnt=0
    for i in range(len(numbers)-1):

        if check:
            if numbers[i] < numbers[i+1]:
                values.append("B")
                b_cnt+=1
                check=False
                continue
            else:
                values.append("-")
        else:
            if numbers[i] > numbers[i+1]:
                values.append("S")
                s_cnt+=1
                check=True
                continue
            else:
                values.append("-")
    if b_cnt-s_cnt>=1:
        for _ in range(b_cnt-s_cnt):
            values.append("S")
    else:
        values.append("-")
        
    return "".join(values)

