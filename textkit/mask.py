def mask_email(email: str) -> str:
    """이메일 아이디(@ 앞부분)를 가려서 개인정보를 보호한다.

    규칙 (보이는 글자 수):
    - 아이디 3글자 이상: 앞 2글자만 보이고 나머지는 *
    - 아이디 2글자: 앞 1글자만 보이고 나머지는 *
    - 아이디 1글자: 전부 *

    >>> mask_email("alice@example.com")
    'al***@example.com'
    >>> mask_email("bo@example.com")
    'b*@example.com'
    >>> mask_email("c@example.com")
    '*@example.com'
    """
    local, domain = email.split("@", 1)
    return local[:2] + "*" * (len(local) - 2) + "@" + domain
