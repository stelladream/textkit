# textkit

한국어 친화 텍스트 유틸리티 모음입니다. 단어 수 세기, 말줄임, 슬러그 만들기, 받침 판별, 조사 붙이기 같은 작은 함수들을 제공합니다.

> 이 저장소는 **오픈소스 소프트웨어 강좌 14주차 실습**용으로 만든 연습용 오픈소스 프로젝트입니다.
> 실제 오픈소스와 같은 방식(Issue → Fork → Pull Request → CI → Review)으로 기여해 볼 수 있습니다.

## 사용 예시

```python
>>> from textkit import word_count, add_josa, slugify
>>> word_count("오픈소스 소프트웨어 강좌")
3
>>> add_josa("사과", "을/를")
'사과를'
>>> slugify("Hello World")
'hello-world'
```

## Docker 로 테스트하기 (권장)

Python 을 설치하지 않아도 Docker 만 있으면 CI 와 같은 환경(Python 3.13)에서 테스트할 수 있습니다.

```bash
docker build -t textkit         # 테스트 이미지 만들기
docker run --rm textkit         # 컨테이너에서 전체 테스트 실행
```

## Python 으로 직접 테스트하기

Python 3.10 이상, **표준 라이브러리만** 사용합니다. 설치할 패키지가 없습니다.

```bash
python -m unittest -v
```

## 폴더 구조

```
textkit/            함수 하나 = 파일 하나 (예: words.py → word_count)
tests/              test_<모듈>.py — 모듈별 테스트
Dockerfile          테스트용 이미지 (CI 도 이 이미지로 테스트)
.github/            이슈 · PR 템플릿, CI 워크플로우
CONTRIBUTING.md     기여 방법 (먼저 읽어 주세요!)
```

## 기여하기

기여를 환영합니다! 시작하기 전에 [CONTRIBUTING.md](CONTRIBUTING.md) 와 [행동 강령](CODE_OF_CONDUCT.md) 을 읽어 주세요.
처음이라면 `good first issue` 라벨이 붙은 이슈부터 시작하세요.

## 라이선스

[MIT License](LICENSE)
