import re
import numpy as np
import pandas as pd

df_marque_modèle = pd.read_excel("data/List_Marque_Modèle_Final.xlsx", sheet_name = "Liste Complète")
df_sous_modèle = pd.read_excel("data/List_Marque_Modèle_Final.xlsx", sheet_name = "Sous-Modèles")
df_modèle = pd.read_excel("data/List_Marque_Modèle_Final.xlsx", sheet_name = "Modèles")
df_marque = pd.read_excel("data/List_Marque_Modèle_Final.xlsx", sheet_name = "Marques")

def get_ID(marque, modèle, sous_modèle):
    df_filtered = df_marque_modèle[
        (df_marque_modèle["Marque"] == marque) &
        (df_marque_modèle["Modèle"] == modèle) &
        (df_marque_modèle["Sous-Modèle"] == sous_modèle)
        ]

    if not df_filtered.empty:
        row = df_filtered.iloc[0]
        return row["ID"], row["ID Marque"], row["ID Modèle"], row["ID Sous-Modèle"]

    # Si pas de match complet, on cherche partiellement
    id_full, id_marque, id_modèle, id_sous_modèle = None, None, None, None

    df_marque_filtered = df_marque_modèle[df_marque_modèle["Marque"] == marque]
    if not df_marque_filtered.empty:
        id_marque = df_marque_filtered.iloc[0]["ID Marque"]

        df_modèle_filtered = df_marque_filtered[df_marque_filtered["Modèle"] == modèle]
        if not df_modèle_filtered.empty:
            id_modèle = df_modèle_filtered.iloc[0]["ID Modèle"]

            df_sous_modèle_filtered = df_modèle_filtered[df_modèle_filtered["Sous-Modèle"] == sous_modèle]
            if not df_sous_modèle.empty:
                id_sous_modèle = df_sous_modèle_filtered.iloc[0]["ID Sous-Modèle"]
                id_full = df_sous_modèle_filtered.iloc[0]["ID"]

    return id_full, id_marque, id_modèle, id_sous_modèle


def get_marque_from_ID(id_marque):
    marque = None

    df_filtered = df_marque_modèle[df_marque_modèle["ID Marque"] == id_marque]

    if not df_filtered.empty:
        marque = df_filtered["Marque"].iloc[0]

    return marque


def get_modèle_from_ID(id_modèle):
    modèle = None

    df_filtered = df_marque_modèle[df_marque_modèle["ID Modèle"] == id_modèle]

    if not df_filtered.empty:
        modèle = df_filtered["Modèle"].iloc[0]

    return modèle


def get_sous_modèle_from_ID(id_sous_modèle):
    modèle = None

    df_filtered = df_marque_modèle[df_marque_modèle["ID Sous-Modèle"] == id_sous_modèle]

    if not df_filtered.empty:
        modèle = df_filtered["Sous-Modèle"].iloc[0]

    return modèle

def nettoyage(string):
    new_value = re.sub(r" +", " ", str(string))  # Supprimer les espaces en trop
    new_value = new_value.strip()
    return new_value


def nettoyer_chaine(texte: str) -> str:
    texte = str(texte)
    texte = re.sub(r"\(\d\)", "", texte)  # Supprimer les chiffres entre parenthèses
    texte = re.sub(r" +", " ", texte)  # Supprimer les espaces en trop
    texte = texte.strip()
    # 1️⃣ Remplacer les apostrophes spéciales par une apostrophe normale
    texte = texte.replace("’", "'").replace("`", "'").replace("´", "'")
    texte = texte.replace("Œ", "OE")
    return texte.strip()
