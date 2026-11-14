"""textkit — 한국어 친화 텍스트 유틸리티 모음 (OSS 강좌 실습용)."""

from .words import word_count
from .truncate import truncate
from .palindrome import is_palindrome
from .slug import slugify
from .batchim import has_batchim
from .josa import add_josa
from .mask import mask_email
from .hangul_count import count_hangul
from .reading import reading_time
from .spaces import normalize_spaces

__all__ = [
    "word_count",
    "truncate",
    "is_palindrome",
    "slugify",
    "has_batchim",
    "add_josa",
    "mask_email",
    "count_hangul",
    "reading_time",
    "normalize_spaces",
]

__version__ = "0.3.0"
