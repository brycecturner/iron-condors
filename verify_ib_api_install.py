from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

# Create an instance of your app
app = TestApp()
print("TWS API imported successfully!")
