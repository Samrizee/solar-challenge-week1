import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    benin = pd.read_csv('../solar-challenge-week1/data/benin-malanville_clean.csv')
    benin['Country'] = 'Benin'

    sierraleone = pd.read_csv('../solar-challenge-week1/data/sierraleone-bumbuna_clean.csv')
    sierraleone['Country'] = 'Sierra Leone'

    togo = pd.read_csv('../solar-challenge-week1/data/togo-dapaong_clean.csv')
    togo['Country'] = 'Togo'

    df_clean = pd.concat([benin, sierraleone, togo], ignore_index=True)
    return df_clean

def main():
    st.title("☀️ Solar Potential Cross-Country Comparison")

    df = load_data()

    # Sidebar filters
    countries = st.sidebar.multiselect("Select Countries", options=df['Country'].unique(), default=df['Country'].unique())
    metrics = ['GHI', 'DNI', 'DHI']
    selected_metrics = st.sidebar.multiselect("Select Metrics", options=metrics, default=metrics)

    # Filter data
    df_filtered = df[df['Country'].isin(countries)]
    df_melted = df_filtered.melt(id_vars='Country', value_vars=selected_metrics,
                                 var_name='Metric', value_name='Value')

    # Plot boxplot
    st.subheader("Boxplot: Solar Metrics by Country")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df_melted, x='Metric', y='Value', hue='Country', ax=ax)
    st.pyplot(fig)

    # Summary Table
    st.subheader("Summary Statistics")
    summary_table = df_filtered.groupby('Country')[selected_metrics].agg(['mean', 'median', 'std'])
    st.dataframe(summary_table.style.format("{:.2f}"))

if __name__ == "__main__":
    main()
