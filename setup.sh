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
echo "1. MySQL 시작: docker-compose up -d"
echo "2. .env 파일 확인 (필요시 수정)"
echo "3. 가상환경 활성화: source venv/bin/activate"
echo "4. 서버 실행: uvicorn main:app --reload"
echo ""
echo "💡 Docker Desktop에서 'toeic_calendar_mysql' 컨테이너를 확인할 수 있습니다"
echo ""
