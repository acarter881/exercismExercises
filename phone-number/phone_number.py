import re

numberRegEx = re.compile(r'[\s(s)\-\.\+]')

class PhoneNumber:
    def __init__(self, number):
        self.number = number
        self.cleanse()
        self.area_code = self.number[:3]

    def cleanse(self):
        self.number = re.sub(numberRegEx, '', self.number)

        if len(self.number) < 10:
            raise ValueError('Length of the phone number can\'t be less than 10.')
        elif len(self.number) == 11 and not self.number.startswith('1'):
            raise ValueError('If the length of the phone number is 11, it must start with a "1".')
        elif len(self.number) == 11 and (self.number[4] == '0' or self.number[4] == '1' or self.number[1] == '0' or self.number[1] == '1'):
            raise ValueError('The exchange code cannot start with a "0" or "1".')
        elif len(self.number) == 11:
            self.number = self.number[1:]
        elif len(self.number) > 11:
            raise ValueError('The length of the phone number can\'t be more than 11.')
        elif not all([char.isdigit() for char in self.number]):
            raise ValueError('You can only use numbers in a phone number...')
        elif len(self.number) == 10 and self.number.startswith(('0', '1')):
            raise ValueError('You cannot start the area code with a "0" or "1".')
        elif len(self.number) == 10 and (self.number[3] == '0' or self.number[3] == '1'):
            raise ValueError('The exchange code cannot start with a "0" or "1".')
        return self.number

    def pretty(self):
        self.number = "(" + self.number[:3] + ")-" + self.number[3:6] + '-' + self.number[6:]
        return self.number