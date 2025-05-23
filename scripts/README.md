# 📊 Solar Potential Dashboard — Cross-Country Comparison

This Streamlit app visualizes and compares solar energy potential across three West African countries: **Benin**, **Sierra Leone**, and **Togo**. It provides interactive visual insights based on **GHI**, **DNI**, and **DHI** metrics from cleaned datasets.

---

## 🚀 Features

* 📦 Loads and combines pre-cleaned solar datasets
* 📊 Boxplots to compare GHI, DNI, and DHI across countries
* 📈 Summary statistics (mean, median, std)
* 🎛️ Sidebar filters for country and metric selection
* 📱 Fully interactive and ready for deployment

---

## 📁 Folder Structure

```
solar-challenge-week1/
├── app/
│   ├── __init__.py
│   ├── main.py           
│   ├── utils.py          
│   ├── __init__.py
│   └── README.md         
├── data/
│   ├── benin-malanville_clean.csv
│   ├── sierraleone-bumbuna_clean.csv
│   └── togo-dapaong_clean.csv
├── README.md
└── requirements.txt
```

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/samrizee/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the dashboard

```bash
streamlit run app/main.py
```

---

## 📊 Data Overview

Each dataset includes solar potential metrics:

* **GHI** — Global Horizontal Irradiance
* **DNI** — Direct Normal Irradiance
* **DHI** — Diffuse Horizontal Irradiance

---

## 🌐 Deployment

You can access the deployed dashboard using this link- https://solar-challenge-week1-7jjovvpydgahquvklnlphr.streamlit.app/



## ✍️ Author

**Samrawit Zerfu**
