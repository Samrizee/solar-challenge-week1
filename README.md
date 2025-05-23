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
│   ├── main.py           # Streamlit app script
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

To deploy publicly:

1. Push this repo to GitHub.
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Connect your GitHub repo and select `app/main.py` as the entry point.
4. Share the public URL!


## ✍️ Author

**Samrawit Zerfu**
