# textkit 테스트 이미지 — CI 와 내 컴퓨터에서 똑같은 환경으로 테스트합니다.
FROM python:3.13-slim
WORKDIR /app
COPY . .
CMD ["python", "-m", "unittest", "-v"]
