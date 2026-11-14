def slugify(title: str) -> str:
    """제목을 URL 에 쓰기 좋은 슬러그로 바꾼다.

    - 영문은 소문자로 바꾼다.
    - 한글 · 영문 · 숫자가 아닌 글자가 연달아 나오면 하이픈(-) 하나로 바꾼다.
    - 앞뒤의 하이픈은 지운다.

    >>> slugify("Hello World")
    'hello-world'
    >>> slugify("  Git & GitHub: 협업!  ")
    'git-github-협업'
    """
    result = ""
    for ch in title.lower():
        result += ch if ch.isalnum() else "-"
    return result
