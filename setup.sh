#!/bin/bash

echo "🚀 토익 캘린더 설정 시작..."

# 가상환경 생성
echo "📦 가상환경 생성 중..."
python3 -m venv venv

# 가상환경 활성화
echo "✅ 가상환경 활성화..."
source venv/bin/activate

# 패키지 설치
echo "📥 패키지 설치 중..."
pip install --upgrade pip
pip install -r requirements.txt

# .env 파일 생성
if [ ! -f .env ]; then
    echo "📝 .env 파일 생성..."
    cp .env.example .env
    echo "⚠️  .env 파일을 열어서 MySQL 설정을 입력해주세요!"
fi

echo ""
echo "✨ 설정 완료!"
echo ""
echo "다음 단계:"
echo "1. MySQL에서 데이터베이스 생성: CREATE DATABASE toeic_calendar;"
echo "2. .env 파일에서 MySQL 접속 정보 수정"
echo "3. 가상환경 활성화: source venv/bin/activate"
echo "4. 서버 실행: uvicorn main:app --reload"
echo ""
