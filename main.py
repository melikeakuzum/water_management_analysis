from analysis import (
    load_data,
    calculate_water_per_capita,
    get_summary_statistics,
    calculate_annual_change,
    per_capita_consumption_trend,
    capacity_utilization_rate
)
from visualization import (
    plot_water_distribution,
    plot_water_per_capita,
    correlation_analysis
)

file_path = "data.csv"

df = load_data(file_path)

df = calculate_water_per_capita(df)
print(df.columns)

print("Summary Statistics:")
print(get_summary_statistics(df))

plot_water_distribution(df)

plot_water_per_capita(df)

annual_change_df = calculate_annual_change(df)
print("\nAnnual Change (%):")
print(annual_change_df)

capacity_util_df = capacity_utilization_rate(df)
print("\nCapacity Utilization Rate (%):")
print(capacity_util_df)

correlation_analysis(df)
