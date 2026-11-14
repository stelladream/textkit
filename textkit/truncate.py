def truncate(text: str, width: int, suffix: str = "...") -> str:
    """text 가 width 글자보다 길면 잘라서 끝에 suffix 를 붙인다.

    결과 문자열의 길이는 suffix 를 포함해 width 를 넘지 않아야 한다.
    (width 는 len(suffix) 이상이라고 가정한다.)

    >>> truncate("짧은 글", 10)
    '짧은 글'
    >>> truncate("Hello, open source!", 10)
    'Hello, ...'
    """
    if len(text) <= width:
        return text
    return text[:width] + suffix
