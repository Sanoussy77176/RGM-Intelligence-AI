import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="RGM Intelligence AI",
    layout="wide"
)

st.title("RGM Intelligence AI")
st.subheader("Simulateur de prix et de chiffre d'affaires")

df = pd.read_csv("donnees_app.csv")

# Sélection du produit
produit = st.selectbox(
    "Choisir un produit",
    df["item_id"].unique()
)

# Sélection du magasin
magasin = st.selectbox(
    "Choisir un magasin",
    df.loc[df["item_id"] == produit, "store_id"].unique()
)

# Récupérer les données du produit
ligne = df[
    (df["item_id"] == produit) &
    (df["store_id"] == magasin)
].iloc[0]

prix = float(ligne["prix_actuel"])
quantite = float(ligne["ventes_moyennes"])

# Paramètres de simulation
variation = st.slider("Variation du prix (%)", -30, 30, 0)

elasticite = st.slider(
    "Élasticité supposée",
    -3.0, -0.5, -1.5, 0.1
)

# Calculs
nouveau_prix = prix * (1 + variation / 100)
nouvelle_quantite = quantite * (nouveau_prix / prix) ** elasticite

ca_initial = prix * quantite
ca_simule = nouveau_prix * nouvelle_quantite

# Affichage des résultats
col1, col2, col3 = st.columns(3)

col1.metric("Prix simulé", f"{nouveau_prix:.2f} $")
col2.metric("Ventes simulées / jour", f"{nouvelle_quantite:.2f}")
col3.metric(
    "CA simulé / jour",
    f"{ca_simule:.2f} $",
    delta=f"{(ca_simule / ca_initial - 1) * 100:.1f} %"
)

st.caption(
    "Simulation exploratoire utilisant une élasticité hypothétique."
)