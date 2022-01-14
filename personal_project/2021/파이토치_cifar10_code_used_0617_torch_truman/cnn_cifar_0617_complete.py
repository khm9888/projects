import os

# dir_path = os.getcwd()
# print(dir_path)

# input()

#0.라이브러리 임포트
import torch
import torchvision.datasets as datasets
import torchvision.transforms as transforms
import torch.nn.init
# import torch.utils.data.DataLoader as DataLoader
from torch.utils.data import DataLoader

# device = "cuda" if torch.cuda.is_available() else "cpu"
device = "cuda" if torch.cuda.is_available() else "cpu"

#1.데이터

# transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])
transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])

batch_size = 10

trainset = datasets.CIFAR10(root="./data",train=True,download=True,transform=transform)
trainloader = DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=2)
# trainser = datasets.CIFAR10(root="c:/pypy",train=True,download=True,transform=transform)
# trainloader = DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=2)

testset = datasets.CIFAR10(root="./data",train=False,download=True,transform=transform)
testloader = DataLoader(testset, batch_size = batch_size, shuffle=False, num_workers=2)

# train 데이터셋의 사이즈 확인
# 채널 3 , 이미지 8*8 사이즈
v=trainset[0][0].size()
print(v)

# 데이터 길이 학인
# 50000개의 CIFAR 데이터를 배치사이즈 50으로 나눴기 때문에 배치가 1000개라는 뜻
v=len(trainloader)
print(v)
#1000


classes = ('plane', 'car', 'bird', 'cat',

           'deer','dog','frog','horse','ship','truck')

#2.모델구성
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        #image_size = (?,8,8,3)
        super(Net,self).__init__()
        self.conv1=nn.Conv2d(3,6,5)#input,output,kerner_size,stride,padding
        self.pool=nn.MaxPool2d(2,2)#kerner_size,stride
        self.conv2=nn.Conv2d(6,16,5)
        self.fc1 = nn.Linear(16*5*5,120)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10)
    def forward(self,x):
        x=self.pool(F.relu(self.conv1(x)))
        x=self.pool(F.relu(self.conv2(x)))
        x=x.view(-1,16*5*5)
        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        x=self.fc3(x)
        
        return x
        
net = Net()

#3.훈련

print(net)

import torch.optim as optim

criterion = nn.CrossEntropyLoss()
#net안에 있는 parameters를 업데이트한다.
optimizer = optim.SGD(net.parameters(),lr=0.001,momentum=0.9)

epochs=20

for epoch in range(epochs):
    running_loss = 0.0
    #traindata 불러오기(배치 형태로 들어옴)
    for i,data in enumerate(trainloader,0):
        inputs,labels=data
        
        #optimizer 초기화
        optimizer.zero_grad()
        
        #net에 input 이미지 넣어서 output 나오기
        outputs = net(inputs)
        
        #output로 loss값 계산

        loss = criterion(outputs,labels)
        
        #loss를 기준으로 미분자동계산
        loss.backward()
        
        #optimizer 계산
        optimizer.step()
        
        running_loss +=loss.item()
        cnt = 1000
        if i%cnt==cnt-1:
            print(f"[{epoch+1},{i+1:5d}] loss: {running_loss/cnt:.3f}")
            running_loss = 0.0
            
            
print('Finished Training')


# 학습한 모델 저장

import os

dir_path = os.getcwd()
dir_path = os.path.join(dir_path,"pth")

if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    
path = dir_path+"/cifar_cnn.pth"

torch.save(net.state_dict(), path)

# 저장한 모델 불러오기

net = Net()

net.load_state_dict(torch.load(path))


#4.평가 및 예측

# 테스트 데이터로 예측하기

 
correct = 0
total = 0

with torch.no_grad():

    for data in testloader:

        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1) # argmax랑 비슷
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print("Accuracy of the network on th 10000 test images : %d %%" % (100 * correct / total))