# Nama          : Nadia Balqis                     
# Email         : Balqisnadia7303@gmail.com                      
# Id Dicoding   : M322D4KX1572

# Import Library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import datetime
from pathlib import Path
from babel.numbers import format_currency


# Load Data
df = pd.read_csv('https://raw.githubusercontent.com/Nadblqss/submission/main/hour_clean.csv')
df['dteday'] = pd.to_datetime(df['dteday'])

# Menampilkan Title
st.title('Dashboard Bike Sharing')

# Membuat Sidebar
def sidebar(df):
    df["dteday"] = pd.to_datetime(df["dteday"])
    min_date = df["dteday"].min()
    max_date = df["dteday"].max()

    with st.sidebar:
        st.image("https://raw.githubusercontent.com/Nadblqss/submission/main/IMAGE.jpeg")

        date = st.date_input(
            label="**Rentang Waktu**", 
            min_value=min_date, 
            max_value=max_date,
            value=[min_date, max_date],
        )
    def on_change():
        st.session_state.date = date
    return date

if __name__ == "__main__":
    hour_df = pd.read_csv('https://raw.githubusercontent.com/Nadblqss/submission/main/hour_clean.csv')
    date = sidebar(hour_df)
    if(len(date) == 2):
        main_df = hour_df[(hour_df["dteday"] >= str(date[0])) & (hour_df["dteday"] <= str(date[1]))]
    else:
        main_df = hour_df[(hour_df["dteday"] >= str(st.session_state.date[0])) & (hour_df["dteday"] <= str(st.session_state.date[1]))]

# Membuat sidebar Lanjutan
st.sidebar.markdown("Informasi  Diri: ")
st.sidebar.markdown("**• Nama: Nadia Balqis**")
st.sidebar.markdown("**• Email: (Balqisnadia7303@gmail.com)**")
st.sidebar.markdown("**• Bangkit ID: M322D4KX1572**")

# 1. Membuat Visualisasi "Jumlah "
def bike_rental_monthly_distribution_chart(hour_df):
    st.subheader("Distribusi Penyewaan Sepeda per Bulan")
    # Mengelompokkan data per bulan
    hour_df['month'] = pd.to_datetime(hour_df['dteday']).dt.month
    monthly_counts = hour_df.groupby('month')['cnt'].sum().reset_index()
    # Visualisasi 
    fig = px.bar(
        monthly_counts, x='month', y='cnt', labels={'cnt': 'Jumlah Peminjaman Sepeda', 'month': 'Bulan'},
        text='cnt', color_discrete_sequence=['pink'], 
    )
    # Mengatur label bulan
    fig.update_xaxes(tickmode='array', tickvals=list(range(1, 13)), 
                     ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    st.plotly_chart(fig)
# Membuat distribusi penyewaan sepeda per bulan dan menampilkan visualisasinya
bike_rental_monthly_distribution_chart(hour_df)


# 2. Menghitung jumlah penyewaan sepeda per musim
st.subheader("Distribusi jumlah penyewaan sepeda per musim")
# Mapping dari angka ke label musim
season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
hour_df["season_label"] = hour_df["season"].map(season_mapping)
season_count = hour_df.groupby("season_label")["cnt"].sum().reset_index()
# Visualisasi 
fig_season_count = px.bar(
    season_count,
    x="season_label",
    y="cnt",
    labels={"cnt": "Jumlah Peminjaman Sepeda", "season_label": "Musim"},
    color_discrete_sequence=['pink'],  
)
st.plotly_chart(fig_season_count, use_container_width=True)

# 3. Menghitung jumlah penyewaan sepeda per cuaca
st.subheader("Distribusi jumlah penyewaan sepeda per cuaca")
# Mapping dari angka ke label cuaca
weather_mapping = {1: "Clear", 2: "Mist", 3: "Light Rain", 4: "Heavy Rain",}
hour_df["weather_label"] = hour_df["weathersit"].map(weather_mapping)
weather_count = hour_df.groupby("weather_label")["cnt"].sum().reset_index()
# Visualisasi 
fig_weather_count = px.bar(
    weather_count,
    x="weather_label",
    y="cnt",
    labels={"cnt": "Jumlah Peminjaman Sepeda", "weather_label": "Cuaca"},
    color_discrete_sequence=['pink'], 
)
st.plotly_chart(fig_weather_count, use_container_width=True)

# 4. Menampilkan data actuan dan registed penyewa sepeda
st.subheader("Line chart Pengguna/penyewa casual vs registered ")
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
hour_df.set_index('dteday', inplace=True)
# Visualisasi 
fig_actual_vs_registered = px.line(
    hour_df, x=hour_df.index, y=["registered", "casual"],
    labels={"value": "Jumlah Peminjaman Sepeda", "variable": "Tipe Peminjaman"},
    color_discrete_sequence=['pink', 'brown'], 
)
st.plotly_chart(fig_actual_vs_registered, use_container_width=True)
