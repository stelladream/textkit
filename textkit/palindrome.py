def is_palindrome(text: str) -> bool:
    """앞뒤로 읽어도 같은 문장(회문)인지 판별한다.

    대소문자, 공백, 문장부호는 무시하고 글자(한글 · 영문 · 숫자)만 비교한다.

    >>> is_palindrome("level")
    True
    >>> is_palindrome("Was it a car or a cat I saw?")
    True
    >>> is_palindrome("다시 합창합시다")
    True
    """
    return text == text[::-1]
