import matplotlib.pyplot as plt
import seaborn as sns

def plot_water_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df["Year"], df["The Amount of Water Distributed (M3/Year)"], marker="o")
    plt.title("Water Distribution Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Amount of Water Distributed (M3/Year)")
    plt.grid()
    plt.show()

def plot_water_per_capita(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df["Year"], df["Water Per Capita (Liters/Year)"], marker="o", color="orange")
    plt.title("Water Per Capita Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Water Per Capita (Liters/Year)")
    plt.grid()
    plt.show()


def correlation_analysis(df):
    correlation_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
