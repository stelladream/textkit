def count_hangul(text: str) -> int:
    """text 안의 완성형 한글 음절(가 ~ 힣) 개수를 센다.

    >>> count_hangul("Git 과 GitHub")
    1
    >>> count_hangul("가나다")
    3
    """
    return sum(1 for ch in text if "가" <= ch < "힣")
