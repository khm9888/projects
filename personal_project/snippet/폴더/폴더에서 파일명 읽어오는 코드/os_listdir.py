################################### 폴더에서 파일명 읽어오기(start) ########################

def func_full_filenames(data_dir):

    import os
    
    data_dir=os.path.dirname(os.path.abspath(f"{data_dir}/1.png"))#절대경로 변환
    # path to images

    filenames = os.listdir(data_dir)#해당 디렉토리에 이미지들을 리스트로 넣음
    # get a list of images

    full_filenames = [os.path.join(data_dir, f) for f in filenames]#경로까지 추가하여 모두 각각 저장함.
    # # get the full path to images

    # print(full_filenames)#경로저장
    # print(len(full_filenames))#파일 몇개인지 파악
    return full_filenames

data_dir ='data/medetec/bedsore_01'
full_filenames=func_full_filenames(data_dir)

################################### 폴더에서 파일명 읽어오기(end) ########################