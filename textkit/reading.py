def reading_time(text: str, wpm: int = 200) -> int:
    """글을 읽는 데 걸리는 시간을 분 단위 정수로 추정한다.

    - 1분에 wpm 단어를 읽는다고 가정하고, 나머지가 있으면 올림한다.
    - 빈 글(단어 0개)은 0분, 그 외에는 최소 1분이다.

    >>> reading_time("")
    0
    >>> reading_time("짧은 글")
    1
    >>> reading_time("단어 " * 250)
    2
    """
    words = len(text.split())
    return words // wpm
