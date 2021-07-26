import pandas as pd
from datetime import date, datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import pycountry
import plotly.express as px
from tkinter import *

def GUI():
    root=Tk()
    root.title("Covid Tracker")
    mystring= StringVar()
    def getvalue():
        return(mystring.get())

    def close_window():
        root.destroy()
    root.geometry("370x250")
    root.configure(bg="white")
    Label(root,bg="white").grid(row=4,column=0,columnspan=2)
    labelOne=Label(root,text="WELCOME TO COVID-19 Tracker",borderwidth=18,bg="black",fg="white")
    labelOne.config(font=("Britannic Bold",15))
    labelOne.grid(row=0,column=0,columnspan=2)
    labelTwo=Label(root,text="Enter Country Name :",borderwidth=25,bg="white")
    labelTwo.config(font=("Britannic Bold",15))
    labelTwo.grid(row=1,column=0)
    Entry(root ,textvariable = mystring,borderwidth=2,width=20).grid(row=1,column=1,sticky=E)
    Button(root,text="Get Confirmed Cases",command=close_window,anchor=CENTER,height=2,
           width=20,bg="black",fg="white").grid(row=3,column=0,columnspan=2,sticky=W)
    root.mainloop()
    return mystring.get()

def main():
    df1 = pd.read_csv(r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv')
    _country=GUI()
    transformedData = df1.loc[df1['Country'] == _country]
    x = np.array(transformedData['Date'])
    y = np.array(transformedData['Confirmed'])
    d = np.array(transformedData['Deaths'])
    plt.plot(x, y)
    plt.plot(x, d)
    plt.show()


if __name__ == '__main__':
   main()