class Logger:

    def __init__(self):
        self.messages={}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.messages:
            if timestamp >= self.messages[message]+10:
                self.messages[message]=timestamp
                return True
        else:
            self.messages[message]=timestamp
            return True
        
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)