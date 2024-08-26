import pandas as pd
import numpy as np

def clean_data(df):
    # Handle missing values
    df.fillna(method='ffill', inplace=True)
    
    # Remove outliers
    df = df[df['GHI'] > 0]
    
    return df

def main():
    df = pd.read_csv('path_to_your_data.csv')
    cleaned_df = clean_data(df)
    cleaned_df.to_csv('data/cleaned_data.csv', index=False)

if __name__ == "__main__":
    main()
