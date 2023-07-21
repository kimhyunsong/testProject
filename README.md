# 시작하기


## BE

git clone https://github.com/kimhyunsong/testProject.git
### 가상환경
python -m venv venv
source venv/Script/activate

### 마이그레이션 (로컬 실행 시)
python manage.py makemigrations
python manage.py migrate

### 서버 실행

python manage.py runserver 

## FE

npm install

npm start



# 시스템 아키텍처

![image](https://github.com/kimhyunsong/testProject/assets/87460502/d243aeb8-1845-4d35-a813-78b8c7b22ae8)



# 요구사항

## 1. 사용자가 종료하기 전까지 계속해서 이벤트 수집
docker-compose로 BE(django)와 DB(Mysql)을 띄워놓고 
설정한 interval(300s)에 한번씩 Thread 호출 및 데이터 갱신


- 기존 데이터의 DB 존재 여부에 따라 중복 제거 

## 2. 프로그램과 DB는 격리된 컨테이너 환경으로 구성

- docker-compose / Dockerfile (dockerize)
- docker-compose.yml
```docker
version: "3.8"

services:
  mysql-server:
    image: mysql:8
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: 110100
    volumes:
      - ./db/conf.d:/etc/mysql/conf.d
      - ./db/data:/var/lib/mysql
      - ./db/initdb.d:/docker-entrypoint-initdb.d
      - mysqldata:/var/lib/mysql
    env_file: .env
    networks:
      - customNetwork
    container_name: mysql_service

  django-server:
    build: .
    command: python3 manage.py migrate && python manage.py runserver 0:8000 --noreload
    ports:
      - "8000:8000"
    volumes:
      - .:/django-server
    depends_on:
      - mysql-server
    networks:
      - customNetwork
volumes:
  mysqldata:

networks:
  customNetwork:
```
- Dockerfile
```Dockerfile
FROM python:3.9
ENV PYTHONUNBUFFERED 1

COPY . .
RUN pip install -r requirements.txt
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENTRYPOINT ["dockerize", "-wait", "tcp://mysql_service:3306", "-timeout", "20s"]
```



## 3. 수집된 데이터는 DB에 저장 (로컬 / aws)
- 로컬
 ![image](https://github.com/kimhyunsong/testProject/assets/87460502/38ac6d55-02fb-4a03-b779-1a59f3e92640)
- aws
  
![image](https://github.com/kimhyunsong/testProject/assets/87460502/eb986278-84ff-4ba3-afdc-6be8e9fd293f)


## FE 실행 결과
![image](https://github.com/kimhyunsong/testProject/assets/87460502/1034d410-93f4-4710-ba70-dfc8dbe96a99)


## Prometheus 모니터링 툴
![image](https://github.com/kimhyunsong/testProject/assets/87460502/082e022e-fd44-405d-bb3b-a0744aaa0894)

