class PatienceSorter():
    def __init__(self):
        self.a_list = []
    def stacks(self):
        # for i,item in enumerate(self.a_list):
        #     if not item:
        #         self.a_list.pop(i)
        return self.a_list
    def stack_count(self):
        return len(self.a_list)
    def add_item(self,num):
        for i,o in enumerate(self.a_list):
            if o[0] >= num:
                self.a_list[i].insert(0,num)  
                return self
                        
        self.a_list.append([num])
        return self
    def item_count(self):
        num=0
        for i in self.a_list:
            num+=len(i)
        return num
    def remove_item(self):
        assert self.a_list, "no more items"
        min_num=self.a_list[0][0]
        index = 0
        for i in range(1, len(self.a_list)):
            if self.a_list[i][0]<min_num:
                min_num=self.a_list[i][0]
                index = i
        value=self.a_list[index].pop(0)
        if not self.a_list[index]:
            del self.a_list[index]
        return value
    
    def add_items(self,num_list):
        for num in num_list:
            self = self.add_item(num)
        return self

    def remove_items(self):
        a_list = list()
        cnt = self.item_count()
        for _ in range(cnt):
            value=self.remove_item()
            # print(value)
            # print(self.a_list)
            a_list.append(value)
        return tuple(a_list)
    
sorter = PatienceSorter()
v=sorter.add_items([7, 5, 2, 1, 8, 6, 3, 9, 4]).stacks()
# [[1, 2, 5, 7], [3, 6, 8], [4, 9]]
v=  sorter.stack_count()
# 3
v=  sorter.item_count()
# 9
v=  sorter.remove_items()
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
# v=  sorter.stacks()
# []
# v=  sorter.stack_count()
# 0
# v=  sorter.item_count()
# 0

print(v)