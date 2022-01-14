import csv

def letter_frequencies(word):
    dict_w = dict()
    for w in word:
        if not w.isalpha():
            continue
        # print(w)
        w = w.upper()
        # print(w)
        if w not in dict_w:
            dict_w[w]=1
        else:
            dict_w[w]+=1
    return dict_w

v= letter_frequencies('Russia')

class Knockout():
    def __init__(self,file):
        self.a_dict = dict()
        with open(file,"r") as csvfile:
            reader= csv.reader(csvfile)
            # print(reader)
            for i,row in enumerate(reader):
                # row
                # if i>10:
                #     break
                self.a_dict[row[0].upper()]=row[1]
                # print(type(row))
                # print(', '.join(row))
        # print(self.a_dict)
        
    def capital(self,nation):
        assert nation.upper() in self.a_dict, "unknown country"
        return self.a_dict[nation.upper()]
    
    def ordinary_time(self, nation1, nation2):
        nation1_capital = self.capital(nation1)
        nation2_capital = self.capital(nation2)
        cnt1=0
        cnt2=0
        nation1_capital = nation1_capital.upper()
        nation2_capital = nation2_capital.upper()
        nation1_a_list=list(nation1.upper())    
        nation2_a_list=list(nation2.upper())    
        
        # print(nation1, nation1_capital)
        # print(nation2, nation2_capital)
        
        for w in (nation1_capital):
            if w == " ":
                continue
            if w in nation2_a_list:
                idx =nation2_a_list.index(w)
                nation2_a_list.pop(idx)
                cnt2+=1
        for w in nation2_capital:            
            if w == " ":
                continue
            if w in nation1_a_list:
                idx =nation1_a_list.index(w)
                nation1_a_list.pop(idx)
                cnt1+=1
        return cnt1,cnt2                

    def extra_time(self, nation1, nation2):
        nation1=nation1.upper()
        nation2=nation2.upper()
        nation1_capital = self.capital(nation1)
        nation2_capital = self.capital(nation2)
        nation1_cnt=0
        nation2_cnt=0
        nation1_capital_cnt=0
        nation2_capital_cnt=0
        cnt1=0
        cnt2=0
        
        a_set1=set()
        a_set2=set()
        
        nation1_capital = nation1_capital.upper()
        nation2_capital = nation2_capital.upper()
        
        for w in nation1_capital:
            # print(w)
            if w == " ":
                continue
            if w in nation2:
                a_set2.add(w)
        # print("--")
        for w in nation2_capital:            
            # print(w)
            if w == " ":
                continue
            if w in nation1:
                a_set1.add(w)
        for w in a_set2:
            nation1_capital_cnt = letter_frequencies(nation1_capital)[w]
            nation2_cnt = letter_frequencies(nation2)[w]
            cnt2+=nation1_capital_cnt*nation2_cnt
            # print("cnt2",cnt2)
        for w in a_set1:
            nation2_capital_cnt= letter_frequencies(nation2_capital)[w]
            nation1_cnt= letter_frequencies(nation1)[w]
            cnt1+=nation2_capital_cnt*nation1_cnt
            # print("cnt1",cnt1)

                
        # print(nation1_capital_cnt)
        # print(nation2_capital_cnt)
        # print(nation1_cnt)
        # print(nation2_cnt)
        # print(cnt1,cnt2)
        # print(a_set1)
        # print(a_set2)
        return cnt1,cnt2
        
    def match(self, nation1, nation2):
        nation1_u=nation1.upper()
        nation2_u=nation2.upper()
        cnt1,cnt2 = self.ordinary_time(nation1, nation2)
        if cnt1>cnt2:
            return nation1
        elif cnt1<cnt2:
            return nation2
        cnt1,cnt2 = self.extra_time(nation1, nation2)
        if cnt1>cnt2:
            return nation1
        elif cnt1<cnt2:
            return nation2
        else:
            for n1,n2 in zip(nation1_u,nation2_u):
                if n1<n2:
                    return nation1
                elif n1>n2:
                    return nation2
    
    def winner(self,a_list):
        a_list=list(a_list)
        new_list = []
        while len(a_list)>=2:
            nation1 = a_list.pop(0)
            nation2 = a_list.pop(0)
            n = self.match(nation1,nation2)
            a_list.append(n)
        return a_list[0]

        


# {'R': 1, 'U': 1, 'S': 2, 'I': 1, 'A': 1}
# v= letter_frequencies('Moscou')
# {'M': 1, 'O': 2, 'S': 1, 'C': 1, 'U': 1}
# v= letter_frequencies('Puerto Rico')
# {'P': 1, 'U': 1, 'E': 1, 'R': 2, 'T': 1, 'O': 2, 'I': 1, 'C': 1}
# v= letter_frequencies('Guinea-Bissau')
# {'G': 1, 'U': 2, 'I': 2, 'N': 1, 'E': 1, 'A': 2, 'B': 1, 'S': 2}


tournament = Knockout('countries.csv')
v=tournament
v= tournament.capital('Switzerland')
# 'Bern'
# v= tournament.capital('Estonia')
# 'Tallinn'
# v= tournament.ordinary_time('Switzerland', 'Estonia')
# (5, 2)
# v= tournament.ordinary_time('Belgium', 'Denmark')
# (2, 2)
# v= tournament.ordinary_time('Portugal', 'Austria')
# (1, 2)
# v= tournament.ordinary_time('NORTH KOREA', 'argentina')
# (3, 3)
# v= tournament.extra_time('Belgium', 'Denmark')
# (3, 2)
v= tournament.ordinary_time('Nepal', 'sEYcHeLlES')
print("ordinary_time",v)
v= tournament.extra_time('Nepal', 'sEYcHeLlES')
print("extra_time",v)
# (4, 5)
v= tournament.match('guinea', 'Isle of Man')
# 'Switzerland'
# v= tournament.match('Belgium', 'Denmark')
# 'Belgium'
# v= tournament.match('Portugal', 'Austria')
# 'Austria'
# v= tournament.match('Netherlands', 'Lithuania')
# 'Lithuania'
v= tournament.winner(['Switzerland', 'Estonia', 'Belgium', 'Denmark', 'Portugal', 'Austria', 'Netherlands', 'Lithuania'])
# 'Switzerland'

print(v)