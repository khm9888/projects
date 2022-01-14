# # 9-5 스택을 이용한 큐 구현

# # 스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
# https://leetcode.com/problems/implement-queue-using-stacks/

# from typing import List


class MyQueue:
    def __init__(self) -> None:
        self.input=list()
        self.output=list()
    
    def push(self,item):
        self.input.append(item)
    
    def pop(self):
        self.peek()
        return self.output.pop()
    
    def peek(self):
        #output이 없으면 모두 재입력
        if not self.output:
            self.output=self.input[::-1]
            self.input=list()
            
        return self.output[-1]
    
    def empty(self):
        return not (self.input or self.output)
