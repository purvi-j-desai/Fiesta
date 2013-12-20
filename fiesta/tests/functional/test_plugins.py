from fiesta.tests import *

class TestPluginsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='plugins', action='index'))
        # Test response...
