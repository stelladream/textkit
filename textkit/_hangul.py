"""한글 음절 계산에 쓰는 내부 도우미 (검증 완료, 수정 불필요)."""

HANGUL_START = 0xAC00  # '가'
HANGUL_END = 0xD7A3    # '힣'
JONG_COUNT = 28        # 종성(받침) 경우의 수: 받침 없음 1 + 받침 27
JONG_RIEUL = 8         # 종성 인덱스 8 = 'ㄹ'


def is_hangul_syllable(ch: str) -> bool:
    """ch 가 완성형 한글 음절(가~힣)이면 True."""
    return len(ch) == 1 and HANGUL_START <= ord(ch) <= HANGUL_END


def jong_index(ch: str) -> int:
    """한글 음절의 종성 인덱스(0 = 받침 없음). 한글 음절이 아니면 -1."""
    if not is_hangul_syllable(ch):
        return -1
    return (ord(ch) - HANGUL_START) % JONG_COUNT
