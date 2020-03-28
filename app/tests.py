import unittest
import app

class TestCase(unittest.TestCase):
    def setUp(self):
        app.app.config["TESTING"] = True
        self.app = app.app.test_client()
    def get_main(self):
        page = self.app.post("/", data=dict(domain="mail.emag.ru"))
        assert page.status_code == 200
        assert 'check' in str(page.data)
        assert 'ptr' in str(page.data)
    def test_html_escaping( self ):
        page = self.app.post("/", data=dict(name='"><b>TEST</b><!--'))
        assert '<b>' not in str(page.data)
if __name__ == '__main__':
    unittest.main()