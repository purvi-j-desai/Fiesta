from fiesta.tests import *

class TestRetailerController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='retailer', action='index'))
        # Test response...
