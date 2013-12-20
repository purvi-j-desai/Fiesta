from fiesta.tests import *

class TestCelebrationsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='celebrations', action='index'))
        # Test response...
