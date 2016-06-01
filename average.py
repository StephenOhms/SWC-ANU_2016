#!/usr/bin/env python
#
import sys
import pandas as pd

def main():

    try:
        filename = sys.argv[1]
        year = float(sys.argv[2])
        factor = sys.argv[3]
        print('Filename: ', filename)
        print('Year: ', year)
        print('Factor: ', factor)
        print()
    except:
        print('Incorrect input')
 
    surveys_df = pd.read_csv(filename)
    res = surveys_df[(surveys_df.year == 1982)].groupby('sex').mean()
    print(res['weight'][0])
    print(res['weight'][1])
       
if __name__ == "__main__":
    main()
