
# logic.py
class Calculator:
    def __init__(self):
        self.expression = ""
    
    def process_input(self, value):
        if value == "AC":
            self.expression = ""
        elif value == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += value
        return self.expression
