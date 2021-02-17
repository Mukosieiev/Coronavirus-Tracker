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
    result=Label(root,bg="white")
    result.grid(row=4,column=0,columnspan=2)
    label1=Label(root,text="WELCOME TO COVID-19 Tracker",borderwidth=18,bg="black",fg="white")
    label1.config(font=("Britannic Bold",15))
    label1.grid(row=0,column=0,columnspan=2)
    label2=Label(root,text="Enter Country Name :",borderwidth=25,bg="white")
    label2.config(font=("Britannic Bold",15))
    label2.grid(row=1,column=0)
    entry1=Entry(root ,textvariable = mystring,borderwidth=2,width=20).grid(row=1,column=1,sticky=E)

    get_button=Button(root,text="Get Confirmed Cases",command=close_window,anchor=CENTER,height=2,width=20,bg="black",fg="white").grid(row=3,column=0,columnspan=2,sticky=W)
    root.mainloop()
    return mystring.get()

def main():
    URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
    df1 = pd.read_csv(URL_DATASET)


    yesterday = str(date.today() - timedelta(1))
    _country=GUI()
    print(_country)
    transformedData = df1.loc[df1['Country'] == _country.capitalize()]       #getting latest data of all countries
    x = np.array(transformedData['Date'])
    y = np.array(transformedData['Confirmed'])
    print(transformedData)
    plt.plot(x, y)
    plt.show()

    list_countries = df1['Country'].unique().tolist()

    d_country_code = {}
    for country in list_countries:
        try:
            country_data = pycountry.countries.search_fuzzy(country)
            country_code = country_data[0].alpha_3
            d_country_code.update({country: country_code})
        except:
            d_country_code.update({country: ' '})

    for k, v in d_country_code.items():
        df1.loc[(df1.Country == k), 'iso_alpha'] = v

    fig = px.choropleth(data_frame=df1, locations="iso_alpha", color="Confirmed", hover_name="Country",
                        color_continuous_scale='RdYlGn', animation_frame="Date")

    fig.show()


if __name__ == '__main__':
   main()