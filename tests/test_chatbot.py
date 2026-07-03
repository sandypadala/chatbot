import os
import unittest
from unittest.mock import patch

from backend.chatbot import get_api_key


class ChatbotTests(unittest.TestCase):
    @patch.dict(os.environ, {}, clear=True)
    def test_get_api_key_raises_when_missing(self):
        with self.assertRaises(RuntimeError):
            get_api_key()


if __name__ == "__main__":
    unittest.main()
