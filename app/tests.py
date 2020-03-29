import unittest
import main

class TestCase(unittest.TestCase):
    def setUp(self):
        main.app.config["TESTING"] = True
        self.app = main.app.test_client()
    def test_get_mainpage(self):
        page = self.app.post("/", data=dict(domain="mail.emag.ru"))
        assert page.status_code == 200
        assert 'steu' in str(page.data)
        assert 'PTR' in str(page.data)
    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>TEST</b><!--'))
        assert '<b>' not in str(page.data)
if __name__ == '__main__':
    unittest.main()