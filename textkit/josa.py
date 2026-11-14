from ._hangul import jong_index, JONG_RIEUL

SUPPORTED = ("을/를", "이/가", "은/는", "과/와", "으로/로")


def add_josa(word: str, pair: str) -> str:
    """단어 뒤에 받침에 맞는 조사를 붙인다.

    pair 는 "받침 있을 때/받침 없을 때" 형식이다. 예: "을/를"
    단, "으로/로" 는 받침이 'ㄹ' 일 때도 '로' 를 쓴다. (서울로, 연필로)

    >>> add_josa("사과", "을/를")
    '사과를'
    >>> add_josa("책", "이/가")
    '책이'
    >>> add_josa("서울", "으로/로")
    '서울로'
    """
    if pair not in SUPPORTED:
        raise ValueError(f"지원하지 않는 조사: {pair}")
    with_jong, without_jong = pair.split("/")
    jong = jong_index(word[-1]) if word else -1
    if jong > 0:
        return word + with_jong
    return word + without_jong
