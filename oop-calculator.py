
class ROICalculator():

    def __init__(self):
        self.income = {
            'Rental Income': '',
            'Laundry Income': '',
            'Storage Income': '',
            'Misc. Income': ''
        }
        self.expenses = {
            'Taxes': '',
            'Insurance': '',
            'Utilities': '',
            'Electric': '',
            'Water': '',
            'Sewer': '',
            'Trash': '',
            'Gas': '',
            'HOA': '',
            'Landscaping': '',
            'Vacancy': '',
            'Repairs': '',
            'CapEx': '',
            'Mortgage': '',
            'Property Management': ''
        }
        self.investment = {
            'Down Payment': '',
            'Closing Costs': '',
            'Rehab Budget': '',
            'Misc Other': ''
        }
        self.total_income = 0
        self.total_expenses = 0
        self.cashflow = 0
        self.annual_cashflow = 0
        self.total_investment = 0
        self.cashoncash_roi  = 0

    def getIncome(self):
        # This method fills the values for income based on user input
        for key in self.income:
            while True:
                try:
                    value = float(input(f"Enter the amount for {key}: "))
                    if value < 0:
                        print("Please enter a value 0 or greater.")
                    else:
                        self.income[key] = value
                        break
                except ValueError:
                    print("Please enter a numeric value.")

    def displayIncome(self):
        # This method displays all the user inputted income data in a formatted list
        print("---- Income ----")
        for key, value in self.income.items():
            print(f"{key}: ${value:.2f}")

    def totalIncome(self):
        # Calculates the total income.
        self.total_income = sum(self.income.values())
        return self.total_income

    def getExpenses(self):
        # This method fills the values for expenses based on user input
        for key in self.expenses:
            while True:
                try:
                    value = float(input(f"Enter the amount for {key}: "))
                    if value < 0:
                        print("Please enter a value 0 or greater.")
                    else:
                        self.expenses[key] = value
                        break
                except ValueError:
                    print("Please enter a numeric value.")

    def displayExpenses(self):
        # This method displays all the user inputted expenses data in a formatted list
        print("---- Expenses ----")
        for key, value in self.expenses.items():
            print(f"{key}: ${value:.2f}")

    def totalExpenses(self):
        # Calculates the total expenses.
        self.total_expenses = sum(self.expenses.values())
        return self.total_expenses

    def cashFlow(self):
        # Calculates the monthly cash flow.
        self.cashflow = self.total_income - self.total_expenses
        return self.cashflow

    def annualCashFlow(self):
        # Calculates the annual cash flow.
        self.annual_cashflow = self.cashflow * 12
        return self.annual_cashflow

    def getInvestment(self):
        # This method fills the values for investment based on user input
        for key in self.investment:
            while True:
                try:
                    value = float(input(f"Enter the amount for {key}: $"))
                    if value < 0:
                        print("Please enter a value 0 or greater.")
                    else:
                        self.investment[key] = value
                        break
                except ValueError:
                    print("Please enter a numeric value.")

    def displayInvestment(self):
        # This method displays all the user inputted investment data in a formatted list
        print("---- Investment ----")
        for key, value in self.investment.items():
            print(f"{key}: ${value:.2f}")

    def totalInvestment(self):
        # Calculates the total investment
        self.total_investment = sum(self.investment.values())
        return self.total_investment

    def cashROI(self):
        # Calculates the cash on cash ROI and prints a statement that displays the ROI value as a percentage.
        self.cashoncash_roi = float((self.annual_cashflow / self.total_investment) * 100)
        print(f"\nThe Cash on Cash ROI for your property is: {round(self.cashoncash_roi, 2)}%")


calculator = ROICalculator()

def roiCalculator():
    print("Cash on Cash ROI Calculator\n")
    print("Please begin by entering the monthly income received on your property.")
    calculator.getIncome()

    print("\nGreat! Now enter the monthly expenses for your property.")
    calculator.getExpenses()

    print("\nLastly, please enter the investment expenses for your property.")
    calculator.getInvestment()

    print("\nOverview of Income, Expenditures, and Cash on Cash ROI:\n")
    total_income = calculator.totalIncome()
    total_expenses = calculator.totalExpenses()
    cashflow = calculator.cashFlow()
    annual_cashflow = calculator.annualCashFlow()
    total_investment = calculator.totalInvestment()

    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Cash Flow: ${cashflow:.2f}")
    print(f"Annual Cash Flow: ${annual_cashflow:.2f}")
    print(f"Total Investment: ${total_investment:.2f}")

    calculator.cashROI()

    print("\nDetailed Income Breakdown:")
    calculator.displayIncome()

    print("\nDetailed Expenses Breakdown:")

    calculator.displayExpenses()

    print("\nDetailed Investment Breakdown:")
    calculator.displayInvestment()

roiCalculator()
