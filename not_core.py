import pandas as pd
import sys, os
import UI
import csv

class Calculations:
    def __init__(self):
        pass
    
    def get_file(self):
        if os.path.isfile("data.csv"):
            self.df = pd.read_csv("data.csv")
            print('done')
        else:
            data = [{'Topic':'Topic', "Amount" : 0, "Date":"Date", "Total": 0}]
            file_create = pd.DataFrame(data)
            file_create.to_csv("data.csv")

            # with open('data.csv', 'w', newline='') as file:
            #     writer = csv.writer(file)
            #     writer.writerow(['Topic', 'Amount', 'Date', 'Total'])
            self.df=pd.read_csv("data.csv")
            print("done2")

    def print_file(self):
        print(self.df)
    
    def income_data(self, _topic, _amount, _date):
        global _total 
        _total = int()
        global get_sum 
        get_sum = int()
        for total in self.df['Amount']:
            get_sum += int(total)
        _total =  _amount + get_sum
        new_df = {'Topic':_topic, "Amount":_amount, "Date": _date, "Total": _total}
        self.df = self.df.append(new_df, ignore_index= True)

    def expense_data(self, _topic, _amount, _date):
        global _total
        _total_expense = int()
        global get_sum 
        get_sum = int()
        for total in self.df['Amount']:
            get_sum += int(total)
        _total =  get_sum - _amount
        new_df = {'Topic':_topic, "Amount":_amount, "Date": _date, "Total": _total}
        self.df = self.df.append(new_df, ignore_index= True)

    def export(self):
        self.df.to_csv('data.csv')

if __name__ == "__main__":
    calc = Calculations()
    calc.get_file()
    calc.income_data('Aalu', 100, "2077/04/04")
    calc.income_data('Aalu', 100, "2077/04/04")
    calc.income_data('Aalu', 100, "2077/04/04")
    calc.expense_data('Aalu', 100, "2077/04/04")
    calc.export()
