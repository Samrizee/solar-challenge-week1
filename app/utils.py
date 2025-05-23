import pandas as pd

def load_data():
    benin = pd.read_csv("../data/benin-malanville_clean.csv")
    sierraleone = pd.read_csv("../data/sierraleone-bumbuna_clean.csv")
    togo = pd.read_csv("../data/togo-dapaong_clean.csv")

    benin["Country"] = "Benin"
    sierraleone["Country"] = "Sierra Leone"
    togo["Country"] = "Togo"

    df = pd.concat([benin, sierraleone, togo], ignore_index=True)
    return df

def get_top_regions(df, metric, top_n=5):
    return df.groupby(["Country", "Region"])[metric].mean().reset_index().sort_values(metric, ascending=False).head(top_n)
