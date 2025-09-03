import pandas as pd

def clean_data(df):
    # Rename columns exactly as they appear in your CSV
    df = df.rename(columns={
        'totCons2019': 'total_consumption',
        'perCapitaCons2016': 'per_capita_consumption'
    })
    
    # Fill missing values
    df.fillna(0, inplace=True)
    
    # Convert numeric columns to float
    df['total_consumption'] = df['total_consumption'].astype(float)
    df['per_capita_consumption'] = df['per_capita_consumption'].astype(float)
    
    return df

