import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_csv('../data/benin-malanville.csv')

def main():
    st.title("Solar Radiation Data Dashboard")

    df = load_data()

    st.sidebar.subheader("Visualization Settings")
    columns = st.sidebar.multiselect("Select Columns to Plot", df.columns)
    
    if st.sidebar.button("Generate Plot"):
        st.subheader("Time Series Plot")
        plt.figure(figsize=(14, 7))
        for col in columns:
            plt.plot(df['Timestamp'], df[col], label=col)
        plt.legend()
        st.pyplot(plt)

if __name__ == "__main__":
    main()
