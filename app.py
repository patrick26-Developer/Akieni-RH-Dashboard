import streamlit as st
import pandas as pd
import plotly.express as px

# === Chargement des données ===
@st.cache_data
def load_data():
    df = pd.read_csv("data/students_data.csv")
    df["Taux Présence (%)"] = (df["Présences"] / df["Total_Cours"]) * 100
    return df

df = load_data()

# === Interface Streamlit ===
st.title("📊 Akieni RH Dashboard")
st.subheader("Suivi des performances et présences des étudiants")

# === Filtres ===
discipline = st.selectbox("Filtrer par discipline :", df["Discipline"].unique())
df_filtered = df[df["Discipline"] == discipline]

# === Affichage des données ===
st.dataframe(df_filtered)

# === Visualisation 1 : Bar de présence ===
fig1 = px.bar(df_filtered, x="Nom", y="Taux Présence (%)", color="Nom",
              title="Taux de présence des étudiants", text_auto=".2f")
st.plotly_chart(fig1)

# === Visualisation 2 : Score par étudiant ===
fig2 = px.bar(df_filtered, x="Nom", y="Score", color="Nom",
              title="Scores académiques des étudiants", text_auto=".2f")
st.plotly_chart(fig2)

# === Visualisation 3 : Comparatif Présence vs Score ===
fig3 = px.scatter(df_filtered, x="Taux Présence (%)", y="Score", color="Nom",
                  size="Score", title="Corrélation Présence / Score")
st.plotly_chart(fig3)