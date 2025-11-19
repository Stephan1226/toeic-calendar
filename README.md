# 토익 30일 챌린지 캘린더

FastAPI, Jinja2, MySQL을 사용한 토익 학습 추적 웹 애플리케이션입니다.

## 설치 방법

### 1. 자동 설치 (추천)

```bash
chmod +x setup.sh
./setup.sh
```

### 2. 수동 설치

```bash
# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt

# 환경 변수 설정
cp .env.example .env
# .env 파일을 열어서 MySQL 정보 입력
```

## MySQL 설정

```sql
CREATE DATABASE toeic_calendar;
```

`.env` 파일에서 MySQL 접속 정보를 수정하세요:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=toeic_calendar
```

## 실행 방법

```bash
# 가상환경 활성화 (매번 실행 시)
source venv/bin/activate

# 서버 실행
uvicorn main:app --reload
```

브라우저에서 http://localhost:8000 접속

## 기능

- 30일간의 학습 캘린더
- 각 날짜별 체크박스로 완료 여부 표시
- 학습 소스 입력 (예: 파트5 문제 50개)
- 노션 페이지 링크 입력 및 바로가기
- MySQL 데이터베이스에 자동 저장
