class Value_Handler:
    def __init__(self):
        self.values = {}

    def add_val(self, base_val, corresponding_val):
        if (base_val != '\0'):
            self.values[base_val] = corresponding_val

    def get_val(self, base_val):
        try:
            return self.values[base_val]
        except KeyError:
            return '\0'
