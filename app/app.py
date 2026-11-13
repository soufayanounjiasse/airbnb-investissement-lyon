import streamlit as st

st.set_page_config(page_title="Investir à Lyon : location courte durée", layout="wide")
st.title("Investir dans la location courte durée à Lyon")
st.caption("Source : Inside Airbnb (CC BY 4.0), snapshot à compléter")

page = st.sidebar.radio("Navigation", ["Le marché", "Où investir", "Quel produit"])
st.info(f"Page « {page} » : à construire (tâche E1).")
