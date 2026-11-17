"""Standard-library tests for the isolated PlayerZero simulation lab."""
import unittest

from playerzero_lab.retry_policy import should_retry


class RetryPolicyTests(unittest.TestCase):
    def test_retries_transient_server_error_with_budget(self):
        self.assertTrue(should_retry(503, attempt=1, max_attempts=3))

    def test_does_not_retry_after_budget_exhaustion(self):
        self.assertFalse(should_retry(503, attempt=3, max_attempts=3))

    def test_does_not_retry_nontransient_client_error(self):
        self.assertFalse(should_retry(400, attempt=1, max_attempts=3))

    def test_does_not_retry_success(self):
        self.assertFalse(should_retry(200, attempt=1, max_attempts=3))

    def test_invalid_attempt_raises(self):
        with self.assertRaises(ValueError):
            should_retry(503, attempt=0)


if __name__ == "__main__":
    unittest.main()
