

#loc

print('df.loc[:,"boneage"]')
print(df.loc[:,"boneage"])

#####################################################################################

#11:57 try 1

import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


train_df = pd.read_csv("/home/con/data/boneage/csv/train.csv")

train_df['id'] = train_df['id'].apply(lambda x: str(x)+'.png')#df에 내용을 바꿀 수 있음

print(train_df.head())

train_df['gender'] = train_df['male'].apply(lambda x: 'male' if x else 'female')

# print(train_df[['boneage']].hist(figsize=(5,5))) #활성화 시키고, plt.savefig()를 활용하면 저장가능

print('MAX age: ' + str(train_df['boneage'].max()) + ' months')

print('MIN age: ' + str(train_df['boneage'].min()) + ' months')

mean_bone_age = train_df['boneage'].mean()
print('mean: ' + str(mean_bone_age))

print('median: ' +str(train_df['boneage'].median()))

std_bone_age = train_df['boneage'].std()

train_df['bone_age_z'] = (train_df['boneage'] - mean_bone_age)/(std_bone_age)

male = train_df[train_df['gender'] == 'male']
female = train_df[train_df['gender'] == 'female']


df_train, df_valid = train_test_split(train_df, test_size = 0.2, random_state = 0)


import matplotlib.image as mpimg
for filename, boneage, gender in train_df[['id','boneage','gender']].sample(5).values:
    img = mpimg.imread('/home/con/data/boneage/boneage-training-dataset/'+ filename)
    plt.imshow(img)
    plt.title('Image name:{}  Bone age: {} years  Gender: {}'.format(filename, boneage/12, gender))
    plt.axis('off')
    plt.savefig('/home/con/data/boneage/p/'+ filename)
    plt.show()