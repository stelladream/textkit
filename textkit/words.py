def word_count(text: str) -> int:
    """공백(스페이스 · 탭 · 줄바꿈)으로 구분된 단어 수를 센다.

    >>> word_count("오픈소스 소프트웨어 강좌")
    3
    >>> word_count("")
    0
    """
    return len(text.split(" "))
