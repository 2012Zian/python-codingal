class uppercase():
    def __init__(self):
        self.text = ""
    def get_text(self):
        self.text = input("enter a text thatnyou want to convert to uppercase: ")
    def print_text(self):
        print("result is:",self.text.upper())
ob = uppercase()
ob.get_text()
ob.print_text()