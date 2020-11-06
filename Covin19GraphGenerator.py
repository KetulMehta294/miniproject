import dateutil

import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_rows', 1700)
df = pd.read_csv("covid_19_india.csv")
df['Date'] = df['Date'].apply(dateutil.parser.parse, dayfirst=True)
Ans = input("Do U want to see Graph StateWise....?(Yes/No):")
if Ans=="Yes":
    State = input("Enter the name of State to see It's Graph....:")
    datagrp = df[df['States'] == State].groupby(['Date'],).agg(
        TotalConfirmed = ('Confirmed', sum),
        TotalCured = ('Cured', sum),
        TotalDeath = ('Deaths', sum)) # for states Wise..
else:
    datagrp = df.groupby(['Date'], ).agg(
        TotalConfirmed=('Confirmed', sum),
        # Date = ('Date',sum),
        TotalCured=('Cured', sum),
        TotalDeath=('Deaths', sum))  # for states Wise..

datagrp['TotalConfirmed'].plot(ls="--", marker="s", label="TotalConfirmed")
datagrp['TotalDeath'].plot(ls="--", marker="o", label="TotalDeath")
datagrp['TotalCured'].plot(ls="--", marker=".", label="TotalCured")
# plt.xticks(datagrp["Date","States"],Date,rotation="vertical")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
#plt.show()
print(df.info())