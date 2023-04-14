class IDGenerator:
    def __init__(self, start_letter='a', start_number=1):
        self.current_letter = start_letter
        self.current_number = start_number

    def get_id(self):
        id = f"{self.current_letter}{self.current_number}"
        self.increment()

        return id

    def increment(self):
        self.current_number += 1
        if self.current_number > 9:
            self.current_number = 1
            self.current_letter = chr(ord(self.current_letter) + 1)
            if ord(self.current_letter) > ord('z'):
                self.current_letter = 'a'
