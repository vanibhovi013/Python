# tests/test_module1.py
import pytest

class TestModule1:

    @pytest.mark.dependency()
    def test_openApp(self):
        # Simulate opening the application
        assert True  # Change to True for successful test

    @pytest.mark.dependency(depends=['TestModule1::test_openApp'])
    def test_login(self):
        # Simulate login functionality
        assert True  # Change to True for successful test