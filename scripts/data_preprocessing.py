import pandas as pd
import numpy as np

def clean_data(df):
   
    df.fillna(method='ffill', inplace=True)
    

    df = df[df['GHI'] > 0]
    
    return df

def main():
    df = pd.read_csv('./data/sierraleone-bumbuna.csv')
    cleaned_df = clean_data(df)
    cleaned_df.to_csv('../data/sierraleone-bumbuna.csv', index=False)

if __name__ == "__main__":
    main()
