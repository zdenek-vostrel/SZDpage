import pandas as pd


# Function definitions usually come first with the 'main()' function on top. For better readibility are individual functions separated by two spaces.
def main():

    #load data
    filename = 'novy_nakup.csv'
    df = pd.read_csv(filename, sep = '\t') #df stands for dataframe, 'sep' stands for separator of our values (tabulator in this case). For a complete list of arguments see the official documentation

    #calculate the final price of our grocery list
    sum = df['mnozstvi'] * df['cena_za_jednotku'] #this is a elementwise product of two arrays, basic opperations are implemented into the dataframe so no looping is required
    sum = sum.sum() #python is dynamically typed so you can seamlesly change the sum variable from dataframe to a number. The sum, max, etc. methods are also implemented

    #printing the grocery list and the total cost
    print(df['polozka'].tolist(), sum) # the tolist() function converts dataframe to python array


#this if statement is executed when the script is directly executed. When it is called inside a different script, it will not execute.
if __name__ == "__main__":
    main()