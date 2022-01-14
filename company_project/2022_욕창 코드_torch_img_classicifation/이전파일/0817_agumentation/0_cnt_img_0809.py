import os

def func_full_filenames(data_dir):
    
    data_dir=os.path.dirname(os.path.abspath(f"{data_dir}/1.png"))#절대경로 변환
    # path to images
    filenames = os.listdir(data_dir)#해당 디렉토리에 이미지들을 리스트로 넣음
    # get a list of images
    full_filenames = [os.path.join(data_dir, f) for f in filenames]#경로까지 추가하여 모두 각각 저장함.
    # # get the full path to images

    # print(full_filenames)#경로저장
    print(len(full_filenames))#파일 몇개인지 파악
    return full_filenames

# data_dir ='data/medetec/bedsore_01'


path1 = "/home/ubuntu/Data/upload_file/"
print(path1)
full_filenames=func_full_filenames(path1)

path2 = "/home/ubuntu/Data/upload file_20210812/"
print(path2)
full_filenames=func_full_filenames(path2)

# print("/home/ubuntu/con/merge-0818/")
# full_filenames=func_full_filenames("/home/ubuntu/con/merge-0818/")
# print("/home/ubuntu/con/code/BiT/data/images/")
# full_filenames=func_full_filenames("/home/ubuntu/con/code/BiT/data/images/")
# full_filenames=func_full_filenames("/home/ubuntu/con/code/BiT/data/images/")