from os import system, name
def clear():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac and Linux
    else:
        _ = system('clear')

class Data:
    def __init__(self, name, property, income, investment):
        self.name = name
        self.property = property
        self.income = income
        self.investment = investment

    def userName(self):
        self.name = input('Please enter your name: ')

    def addProperty(self):
        self.property = input('Please enter your property name: ')

        while True:
            income = input('Please enter your total income amount: ')
            if income.isnumeric():
                self.income = int(income)
                break
            else:
                print("Please enter a valid number.")

        while True:
            investment = input(f'Please enter your total investment in {self.property}?: ')
            if investment.isnumeric():
                self.investment += int(investment)
                break
            else:
                print("Please enter a valid number.")

    def calculateRoi(self):
        roi = (self.income / self.investment) * 100
        print(f'The property "{self.property.title()}" has a Roi of: %{roi}')
        return roi

class User(Data):
    def __init__(self):
        self.name = 'None'
        self.property = 'None'
        self.income = 0
        self.investment = 0
        # Orginialy intended to have multiple users.

class Roi(Data):
    def __init__(self):
        self.user = User()

    def begin(self):
        self.user.userName()
        self.user.addProperty()
        clear()
        self.user.calculateRoi()

        while True:
            print('')
            print(f'Welcome {self.user.name.title()}.')
            print('')
            print('Selection: ')
            print('[1] Calculate new property')
            print('[2] View ROI')
            print('[0] Quit')
            print('')

            selection = int(input('Please make a selection: '))
            if selection == 1:
                self.user.addProperty()
                self.user.calculateRoi()
            elif selection == 2:
                self.user.calculateRoi()
            elif selection == 0:
                break
            else:
                print('Please select a valid option.')

roi = Roi()
roi.begin()

# data = Data('Test1', 'Test1', 100, 100)
# data.calculateRoi()

# data = Data('Test2', 'Test2', 45, 80)
# data.calculateRoi()

# data = Data('Test3', 'Test3', 90, 25)
# data.calculateRoi()