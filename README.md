# water_management_analysis

# Türkiye Yıllık Su Tüketimi Analizi / Turkey Annual Water Consumption Analysis

Bu proje, Türkiye'nin çeşitli yıllara ait su tüketim verilerini analiz ederek kişi başına düşen su miktarını, yıllık değişim oranlarını ve su arıtma tesislerinin kapasite kullanım oranlarını değerlendirmeyi amaçlamaktadır. 

This project aims to analyze Turkey's annual water consumption data by evaluating per capita water usage, annual rate changes, and water treatment plant capacity utilization.

## İçindekiler / Table of Contents

- Kurulum / Installation
- Veri Hakkında / About the Data
- Kullanım / Usage
- Fonksiyonlar / Functions
- Görselleştirmeler / Visualizations
- Lisans / License

### Kurulum / Installation

Projeyi çalıştırmak için `pandas`, `matplotlib` ve `seaborn` kütüphanelerinin yüklü olması gerekmektedir. 
The `pandas`, `matplotlib`, and `seaborn` libraries must be installed to run the project.

```bash
pip install pandas matplotlib seaborn
```

### Veri Hakkında / About the Data

Proje verisi `data.csv` dosyasında saklanmaktadır. Bu veri, Türkiye'deki su dağıtımı, kişi başına düşen günlük su miktarı ve tesis kapasitesi gibi parametreleri içermektedir. 
The project data is stored in the `data.csv` file, which includes parameters such as water distribution, daily water consumption per capita, and facility capacity in Turkey.

### Kullanım / Usage

Projeyi çalıştırmak için `main.py` dosyasını çalıştırabilirsiniz: `python main.py` 
To run the project, execute the `main.py` file: `python main.py`

### Fonksiyonlar / Functions

- **load_data**: Veri dosyasını yükler. / Loads the data file.
- **calculate_water_per_capita**: Kişi başına düşen su miktarını hesaplar. / Calculates water usage per capita.
- **get_summary_statistics**: Verinin özet istatistiklerini döndürür. / Returns summary statistics of the data.
- **calculate_annual_change**: Yıllık su tüketimindeki yüzdelik değişimleri hesaplar. / Calculates the percentage change in annual water consumption.
- **per_capita_consumption_trend**: Kişi başına düşen su tüketim trendini döndürür. / Returns the trend of per capita water consumption.
- **capacity_utilization_rate**: Tesislerin kapasite kullanım oranını hesaplar. / Calculates the capacity utilization rate of facilities.

### Görselleştirmeler / Visualizations

- **plot_water_distribution**: Yıllara göre dağıtılan su miktarının trendini gösterir. / Shows the trend of water distribution over the years.
- **plot_water_per_capita**: Yıllara göre kişi başına düşen su miktarının trendini gösterir. / Shows the trend of per capita water usage over the years.
- **correlation_analysis**: Veriler arasındaki ilişkileri görselleştirmek için korelasyon matrisi oluşturur. / Creates a correlation matrix to visualize relationships between data variables.

