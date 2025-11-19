# 토익 30일 챌린지 캘린더

FastAPI, Jinja2, MySQL을 사용한 토익 학습 추적 웹 애플리케이션입니다.

## 설치 및 실행 (Docker 사용 - 추천)

### 1. Docker Desktop 실행

먼저 Docker Desktop을 실행하세요.

### 2. 앱 시작

```bash
docker-compose up -d
```

이게 끝입니다! 브라우저에서 http://localhost:8000 접속하세요.

### 3. 앱 중지

```bash
docker-compose down
```

### 4. 로그 확인

```bash
docker-compose logs -f web
```

Docker Desktop에서 `toeic_calendar_mysql`과 `toeic_calendar_web` 컨테이너를 확인할 수 있습니다.

---

## 로컬 개발 (Docker 없이)

### 설치

```bash
chmod +x setup.sh
./setup.sh
```

### MySQL 설정

```sql
CREATE DATABASE toeic_calendar;
```

`.env` 파일에서 MySQL 접속 정보를 수정하세요.

### 실행

```bash
source venv/bin/activate
uvicorn main:app --reload
```

## 기능

- 30일간의 학습 캘린더
- 각 날짜별 체크박스로 완료 여부 표시
- 학습 소스 입력 (예: 파트5 문제 50개)
- 노션 페이지 링크 입력 및 바로가기
- MySQL 데이터베이스에 자동 저장
