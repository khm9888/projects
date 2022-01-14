# docker 명령어 (9/9) - 

# https://hub.docker.com/

# -이미지-

# 이미지 목록 확인하기 (images)
# 도커가 다운로드한 이미지 목록을 보는 명령어는 다음과 같습니다.

# docker images [OPTIONS] [REPOSITORY[:TAG]]

# 이미지 삭제하기 (rmi)
# 이미지를 삭제하는 방법은 다음과 같습니다.

# docker rmi [OPTIONS] IMAGE [IMAGE...]

# 이미지 검색
# docker search 프로그램 이름


# 이미지 저장(save)
# 원하는 이미지 파일을 .tar 파일로 압축해보겠습니다.

# docker save [옵션] [파일명] <이미지명 또는 이미지ID>

# 이미지 로드(load)
# docker load -i <이미지파일명>
# docker load -i <docker-image/honeybee_1.2.tar>

# --------------------------------------------------------------------------------------------------------

# 컨테이너 목록 확인하기 (ps)
# 컨테이너 목록을 확인하는 명령어는 다음과 같습니다.

# docker ps [OPTIONS]

# 옵션에는 -a, --all

# -a로 하면 중지된 컨테이너까지 확인 가능합니다.


# 컨테이너 중지하기 (stop)
# 실행중인 컨테이너를 중지하는 명령어는 다음과 같습니다.

# docker stop [OPTIONS] CONTAINER [CONTAINER...]


# 컨테이너 제거하기 )
# 종료된 컨테이너를 완전히 제거하는 명령어는 다음과 같습니다.

# docker rm [OPTIONS] CONTAINER [CONTAINER...]

# 컨테이너 시작(start) 및 재시작(restart)
# 컨테이너가 중지되었다고 삭제되는 것은 아닙니다. 시작 명령으로 다시 실행시킬 수 있습니다.

# docker start <컨테이너 이름 혹은 아이디>
# docker restart <컨테이너 이름 혹은 아이디>

# 컨테이너 접속(attach)
# 현재 실행중인 컨테이너에 접속하는 명령어는 attach입니다.

# docker attach <컨테이너 이름 혹은 아이디>

# 컨테이너 로그 보기 (logs)
# 컨테이너가 정상적으로 동작하는지 확인하는 좋은 방법은 로그를 확인하는 것 입니다. 로그를 확인하는 방법은 다음과 같습니다.

# docker logs [OPTIONS] CONTAINER

# 컨테이너 명령어 실행하기 (exec)
# 컨테이너를 관리하다 보면 실행중인 컨테이너에 들어가보거나 컨테이너의 파일을 실행하고 싶을 때가 있습니다. 컨테이너에 SSH를 설치하면 되지 않을까? 라고 생각할 수 있지만 SSH는 권장하지 않습니다. 하지 말라고 하면 꼭 하는 분들이 있던데 제발.. 예전에는 nsenter라는 프로그램을 이용하였는데 docker에 exec라는 명령어로 흡수되었습니다.

# 컨테이너 명령어를 실행하는-it 방법은 다음과 같습니다.

# docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

# 컨테이너 생성(run)

# 다음은 이미지로 컨테이너를 생성하는 run 명령입니다.

# docker run <옵션> <이미지 이름, ID> <명령> <매개 변수>

# 컨테이너 이미지로 저장

# docker commit CONTAINER IMAGE_NAME


# -------------------------------------------------------------------------------------------------------------------

# 텐서플로 버전 바꾸고 싶을때
# 1. docker hub에서 텐서플로 이미지를 다운받는다.
# docker pull 이미지이름
# 2. 다운받은 이미지로 컨테이너를 생성한다. (가상환경 생성)
# docker run -it -v /home:/home  -v --ipc host --net host --name tf_1.4 이미지이름 bash
# 3. 2번을 수행하면 ㄷ컨테이너 생성과 동시에 컨테이너로 들어와 있는거임. 바로 사용하면 됨


# 해야할것
# 1. 도커를 킨다.
# sudo docker start tf_1.2
# 2. 도커의 컨테이너를 연다 (가상환경을 연다)
# 1)
# docker exec -it pt_1.4 /bin/bash
# 2)
# docker attach pt_1.4

# 3. 도커를 쓰다가 로컬로 빠져나오고 싶다.
# ctrl + P + Q

# --------------------------------------------------------------------------------------------------------
# Anaconda와 Docker 를 사용한 머신러닝 개발환경 구성하기
# https://m-learn.tistory.com/6
# --------------------------------------------------------------------------------------------
# docker run 커맨드 사용법

# --------------------------------------------------------------------------------------------
# from JM
# docker run -it -v /home:/home -v /mnt:/mnt --runtime=nvidia --ipc host --net host --name mmdetection_con mmdet_ver201130 bash
# docker run -it -v /home:/home --ipc host --net host --name efficientdet_con pytorch/pytorch  /bin/bash

# from luke

# nvidia-docker run -ti -v /home/lab/con/mmdetection:/mmdetection -v /home:/home -v /mnt:/mnt --ipc=host --net=host -v /tmp/.X11-unix:/tmp/.X11-unix \
# -v /dev/snd:/dev/snd  -e DISPLAY=unix$DISPLAY --name test  save_0921_con /bin/bash
# -> docker 로 해도 가능하게끔 설정했음.

# docker hub에서 다운 받을 때 runtime을 다운받아라. dev 은 권장하지 않음(더 무겁기