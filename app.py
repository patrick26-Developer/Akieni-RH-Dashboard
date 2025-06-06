# Dashboard interactif Streamlit pour visualiser les données RH d’Akieni
import streamlit as st
import pandas as pd
import plotly.express as px

# Fonction de chargement des données avec cache
@st.cache_data
def load_data():
    df = pd.read_csv("data/students_data.csv")
    df["Taux Présence (%)"] = (df["Présences"] / df["Total_Cours"]) * 100
    return df

# Chargement des données
df = load_data()

# Titre de l’application
st.title("📊 Akieni RH Dashboard")
st.subheader("Suivi des performances et présences des étudiants")

# Filtrage par discipline
discipline = st.selectbox("Filtrer par discipline :", df["Discipline"].unique())
df_filtered = df[df["Discipline"] == discipline]

# Affichage des données brutes
st.dataframe(df_filtered)

# Bar chart : taux de présence
fig1 = px.bar(df_filtered, x="Nom", y="Taux Présence (%)", color="Nom",
              title="Taux de présence des étudiants", text_auto=".2f")
st.plotly_chart(fig1)

# Bar chart : scores académiques
fig2 = px.bar(df_filtered, x="Nom", y="Score", color="Nom",
              title="Scores académiques des étudiants", text_auto=".2f")
st.plotly_chart(fig2)

# Scatter plot : présence vs score
fig3 = px.scatter(df_filtered, x="Taux Présence (%)", y="Score", color="Nom",
                  size="Score", title="Corrélation Présence / Score")
st.plotly_chart(fig3)