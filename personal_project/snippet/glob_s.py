# glob
# glob는 파일들의 리스트를 뽑을 때 사용하는데, 파일의 경로명을 이용해서 입맛대로 요리할 수 있답니다.

# https://wikidocs.net/83

>>> from glob import glob
>>> glob('*.exe')               # 현재 디렉터리의 .exe 파일
['python.exe', 'pythonw.exe']
>>> glob('*.txt')               # 현재 디렉터리의 .txt 파일
['LICENSE.txt', 'NEWS.txt']