def normalize_spaces(text: str) -> str:
    """연속된 공백 문자(스페이스 · 탭 · 줄바꿈)를 스페이스 하나로 바꾸고 앞뒤 공백을 지운다.

    >>> normalize_spaces("  오픈소스    기여  ")
    '오픈소스 기여'
    >>> normalize_spaces("첫 줄\\n\\t둘째 줄")
    '첫 줄 둘째 줄'
    """
    return text.replace("  ", " ")
