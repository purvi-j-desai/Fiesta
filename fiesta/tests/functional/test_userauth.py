from fiesta.tests import *

class TestUserauthController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='userauth', action='index'))
        # Test response...
