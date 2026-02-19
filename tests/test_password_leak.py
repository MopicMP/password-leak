"""Tests for password-leak."""

import pytest
from password_leak import leak


class TestLeak:
    """Test suite for leak."""

    def test_basic(self):
        """Test basic usage."""
        result = leak("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            leak("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = leak(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
