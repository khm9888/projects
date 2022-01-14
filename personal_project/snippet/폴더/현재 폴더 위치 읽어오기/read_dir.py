import os
print(__file__)
print(os.path.realpath(__file__))
print(os.path.abspath(__file__))


import os
print(__file__)

#방법1

path = os.getcwd()+"/pth"

if not os.path.isdir(path):
    os.mkdir(path)
    
#방법

dir_path = os.getcwd()
path = os.path.join(dir_path,"pth")

if not os.path.exists(path):
    os.makedirs(path)