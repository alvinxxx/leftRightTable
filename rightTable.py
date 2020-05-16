import pandas as pd

def main():
    #import left table into dataframe
    filepath = "leftTable.csv"
    df = pd.read_csv(filepath, header=0, parse_dates=True)

    #convert the format in Date column to datetime for processing
    df['Date']= pd.to_datetime(df['Date'], format='%d/%m/%Y')
    print()
    print("Original")
    print("========================")
    print(df)
    print()

    #use groupby to identify unique month
    df2 = pd.DataFrame() 
    y = df['Date'].dt.year
    m = df['Date'].dt.month
    df2['Date'] = df.groupby([y, m])['Date'].agg('max') #find last date of each group
    df2['Count_m'] = df.groupby([y, m])['Date'].agg('count') #count number of rows in each group
    df2 = df2.rename_axis(['year', 'month']) #fix ambigous error in newer version of pandas/python 
    #print(df2)

    #merge two dataframe to create the final dataframe
    df3 = pd.DataFrame() 
    df3 = pd.merge(df, df2, on='Date', how='right')
    df3 = df3.rename(columns={"Date": "Last Date", "Count_m": "No of trade days by month"})
    print("New")
    print("========================")
    print(df3)
    print()

main()
