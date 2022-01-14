import re

class Cipher():
    def __init__(self,word1,word2):
        a_list = list(word2)
        grid = list()
        #숫자인지 문자인지
        #숫자라면 뒤에 글자가 숫자인지
        #마지막은 뒤가 없음
        is_num = ""
        for i,w in enumerate(a_list):
            if w.isnumeric():
                if a_list[i+1].isnumeric() and not i==(len(a_list)-1):
                    is_num+=w
                    continue
                else:
                    # print(16,is_num+w)
                    for _ in range(int(is_num+w)):
                        grid.append("-")
                    # print(grid)
                    is_num=""     
            else:
                grid.append(w)
        # b_list =list()
        l=len(grid)
        i=1
        while True:
            if l<i**2:
                add_len = i**2-l
                break
            # print((i-1)**2<l<i**2)
                print(l)
                print(i)
            elif l==i**2:
                add_len=0
                break  
            i+=1
            
            
        for _ in range(add_len):
            grid.append("-")
        # print(40,grid)
        n = len(grid)
        # print(grid)
        n = int(n**0.5)
        # print(31,n)
        g_list=list()
        for i in range(n):
            c_list=list()
            for j in range(n):
                num=(i)*n+j
                # print(num)
                # print(grid[num])
                # print("---")
                c_list.append(grid[num])
            g_list.append(c_list)
        self.grid = g_list
        
        a_dict = dict()
        for i,m in enumerate(g_list):
            for j,n in enumerate(m):
                if n.isalpha():
                    a_dict[n]=word1[i]+word1[j]
        self.map = a_dict

        reverse_map = dict()
        for key,value in self.map.items():
            reverse_map[value]=key
        self.reverse_map = reverse_map
                
    def encode(self,word):
        word = re.sub('[^a-zA-Z]','',word)
        return_word = str() 
        word = word.upper()
        # print(word)
        for w in word:
            assert w in self.map, "invalid message"
            # print(w)
            return_word+=self.map[w]
        return return_word
                
    def decode(self,values):
        values = re.sub('[^a-zA-Z]','',values)
        return_word = str() 
        values = values.upper()
        while values:
            search = values[:2]
            values = values[2:]
            assert search in self.reverse_map, "invalid message"
            return_word+=self.reverse_map[search]
        return return_word
            
                
        
        
        
        
# cipher = Cipher('ABCD', '1AX3S1M2PYZ')
cipher = Cipher('UNEGAL', '1S2MEKNUO1RCWH1IY2B1G4A1T1D1P1L')
v= cipher
v= cipher.grid
# # [['-', 'A', 'X', '-'], ['-', '-', 'S', '-'], ['M', '-', '-', 'P'], ['Y', 'Z', '-', '-']]
# v= cipher.map
# # {'A': 'AB', 'X': 'AC', 'S': 'BC', 'M': 'CA', 'P': 'CD', 'Y': 'DA', 'Z': 'DB'}
# v= cipher.encode('spam')
# 'BCCDABCA'
# v= cipher.decode('BCCDABCA')
# 'SPAM'
# v= cipher.encode('eggs')
# Traceback (most recent call last):
# AssertionError: invalid message
# v= cipher.decode('BCCDBACA')
# Traceback (most recent call last):
# AssertionError: invalid message

# v= cipher02 = Cipher('HISPAYMENT', '14K1S2DL1NW4P2R1H3T3U2O6X3A1F6B1G4I1C2V1Y3E2M2J')
# v= cipher02.grid
# [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', 'K', '-', 'S', '-', '-', 'D'], ['L', '-', 'N', 'W', '-', '-', '-', '-', 'P', '-'], ['-', 'R', '-', 'H', '-', '-', '-', 'T', '-', '-'], ['-', 'U', '-', '-', 'O', '-', '-', '-', '-', '-'], ['-', 'X', '-', '-', '-', 'A', '-', 'F', '-', '-'], ['-', '-', '-', '-', 'B', '-', 'G', '-', '-', '-'], ['-', 'I', '-', 'C', '-', '-', 'V', '-', 'Y', '-'], ['-', '-', 'E', '-', '-', 'M', '-', '-', 'J', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
# v= cipher02.map
# {'K': 'IA', 'S': 'IM', 'D': 'IT', 'L': 'SH', 'N': 'SS', 'W': 'SP', 'P': 'SN', 'R': 'PI', 'H': 'PP', 'T': 'PE', 'U': 'AI', 'O': 'AA', 'X': 'YI', 'A': 'YY', 'F': 'YE', 'B': 'MA', 'G': 'MM', 'I': 'EI', 'C': 'EP', 'V': 'EM', 'Y': 'EN', 'E': 'NS', 'M': 'NY', 'J': 'NN'}
# v= cipher02.encode('Have Marble and Coyle telegraph for influential men from Delaware and Virginia.')
# 'PPYYEMNSNYYYPIMASHNSYYSSITEPAAENSHNSPENSSHNSMMPIYYSNPPYEAAPIEISSYESHAINSSSPEEIYYSHNYNSSSYEPIAANYITNSSHYYSPYYPINSYYSSITEMEIPIMMEISSEIYY'
# v= cipher02.decode('PPYYEMNSNYYYPIMASHNSYYSSITEPAAENSHNSPENSSHNSMMPIYYSNPPYEAAPIEISSYESHAINSSSPEEIYYSHNYNSSSYEPIAANYITNSSHYYSPYYPINSYYSSITEMEIPIMMEISSEIYY')
# 'HAVEMARBLEANDCOYLETELEGRAPHFORINFLUENTIALMENFROMDELAWAREANDVIRGINIA'
# v= cipher02.encode('Indications of weakening here.')
# 'EISSITEIEPYYPEEIAASSIMAAYESPNSYYIANSSSEISSMMPPNSPINS'
# v= cipher02.decode('EISSITEIEPYYPEEIAASSIMAAYESPNSYYIANSSSEISSMMPPNSPINS')
# 'INDICATIONSOFWEAKENINGHERE'
# v= cipher02.encode('Press advantage and watch Board.')
# 'SNPINSIMIMYYITEMYYSSPEYYMMNSYYSSITSPYYPEEPPPMAAAYYPIIT'
# v= cipher02.decode('SNPINSIMIMYYITEMYYSSPEYYMMNSYYSSITSPYYPEEPPPMAAAYYPIIT')
# 'PRESSADVANTAGEANDWATCHBOARD'

print(v)