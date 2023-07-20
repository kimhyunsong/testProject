# 시작하기

```
BE

git clone https://github.com/kimhyunsong/testProject.git
# 가상환경
python -m venv venv
source venv/Script/activate

# 마이그레이션 (로컬 실행 시)
python manage.py makemigrations
python manage.py migrate

# 서버 실행

python manage.py runserver 
```

# 요구사항

## 1. 사용자가 종료하기 전까지 계속해서 이벤트 수집
docker-compose로 BE(django)와 DB(Mysql)을 띄워놓고 
설정한 interval(300s)에 한번씩 Thread 호출 및 데이터 갱신

- 기존 데이터의 DB 존재 여부에 따라 중복 제거 

## 2. 프로그램과 DB는 격리된 컨테이너 환경으로 구성

- EC2 tree

- docker-compose / Dockerfile (dockerize)


## 수집된 데이터는 DB에 저장 (로컬 / aws)