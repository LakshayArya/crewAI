"""Isolated, dependency-free retry policy for commit simulation testing.

This module is training-only and is not imported by application code.
"""
from __future__ import annotations

RETRYABLE_HTTP_STATUSES = frozenset({408, 429, 500, 502, 503, 504})


def should_retry(status_code: int, attempt: int, max_attempts: int = 3) -> bool:
    """Return True when a transient HTTP failure warrants another attempt.

    Attempts are 1-based. A successful response or exhausted retry budget
    must not trigger another request.
    """
    if attempt < 1:
        raise ValueError("attempt must be at least 1")
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")
    return status_code in RETRYABLE_HTTP_STATUSES and attempt < max_attempts
