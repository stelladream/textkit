def has_batchim(word: str) -> bool:
    """단어의 마지막 글자에 받침(종성)이 있으면 True.

    마지막 글자가 한글 음절이 아니거나 빈 문자열이면 False 를 반환한다.

    >>> has_batchim("강")
    True
    >>> has_batchim("가")
    False
    >>> has_batchim("Git")
    False
    """
    last = word[-1]
    return (ord(last) - 0xAC00) % 28 != 0
