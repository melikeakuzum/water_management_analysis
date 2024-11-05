import pandas as pd

def load_data(file_path):

    df = pd.read_csv(file_path, delimiter=";")
    return df

def calculate_water_per_capita(df):
 
    df["Water Per Capita (Liters/Year)"] = (df["The Amount of Water Distributed (M3/Year)"] * 1000) / df["Municipal Population Served by Drinking and Utility Water Network"]
    return df

def get_summary_statistics(df):

    summary = df.describe()
    return summary

def calculate_annual_change(df):

    change_df = df.set_index("Year").pct_change() * 100
    change_df = change_df.reset_index()
    return change_df

def per_capita_consumption_trend(df):

    df['Per Capita Consumption'] = df['The Amount of Water Distributed (M3/Year)'] / df['Municipal Population Served by Drinking and Utility Water Network']
    return df[['Year', 'Per Capita Consumption']]

def capacity_utilization_rate(df):

    df['Capacity Utilization Rate (%)'] = (df['Amount of Water Treated in Drinking and Utility Water Treatment Facilities (Thousand M3/Year)'] / df['Drinking and Utility Water Treatment Facility Capacity (Thousand M3/Year)']) * 100
    return df[['Year', 'Capacity Utilization Rate (%)']]

