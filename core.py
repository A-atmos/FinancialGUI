import pandas as pd
import csv, os, sys
import pdfkit

class Calculations():

    def __init__(self, dataframee):
        self.df = dataframee

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
        self.export()


    def expense_data(self, _topic, _amount, _date):
        global _total
        _total_expense = int()
        global get_sum 
        get_sum = int()
        for total in self.df['Amount']:
            get_sum += int(total)
        _total =  get_sum - _amount
        new_df = {'Topic':_topic, "Amount":-_amount, "Date": _date, "Total": _total}
        self.df = self.df.append(new_df, ignore_index= True)
        self.export()

    def export(self):
        self.df.to_csv(r'files\\data.csv')

    def export_to_pdf(self):
        self.df.to_html(r"files\\to_html.html")
        pdfkit.from_file(r"files\\to_html.html", "exported.pdf")

def get_file():
    global not_df
    if os.path.isfile(r"files\\data.csv"):
        not_df = pd.read_csv(r"files\\data.csv", index_col= 0)
        print('done')
    else:
        data = {'Topic':['Topic'], "Amount" :[0], "Date":["Date"], "Total": [0]}
        file_create = pd.DataFrame(data)
        os.mkdir(r"D:\\Dev\\Python\\DataScience\\FinanManagement\\files")
        file_create.to_csv(r"files\\data.csv")
        not_df=pd.read_csv(r"files\\data.csv", index_col= 0)

if __name__ == "__main__":
    get_file()
    Calculations(not_df)
    calc = Calculations(not_df)
    print(calc.df)