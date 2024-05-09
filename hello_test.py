import unittest
from hello import app  # 请将 "your_flask_app_file"  替换为你的 Flask 应用文件名称。


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.test_client = app.test_client()

    def test_hello_world(self):
        response = self.test_client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')


if __name__ == '__main__':
    unittest.main()