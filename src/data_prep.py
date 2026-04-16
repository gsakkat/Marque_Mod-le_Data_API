import openpyxl
from src.utils import *

def save_df_marque_modèle():
    global df_marque_modèle
    with pd.ExcelWriter(
        path="data/List_Marque_Modèle_Final.xlsx",
        engine='openpyxl',
        mode='a',  # append data to the file
        if_sheet_exists='replace'
    ) as writer:
        df_marque_modèle.to_excel(writer, index=False, sheet_name="Liste Complète")

def save_df_marque():
    global df_marque
    with pd.ExcelWriter(
        path="data/List_Marque_Modèle_Final.xlsx",
        engine='openpyxl',
        mode='a',  # append data to the file
        if_sheet_exists='replace'
    ) as writer:
        df_marque.to_excel(writer, index=False, sheet_name="Marques")

def save_df_modèle():
    global df_modèle
    with pd.ExcelWriter(
            path="data/List_Marque_Modèle_Final.xlsx",
            engine='openpyxl',
            mode='a',  # append data to the file
            if_sheet_exists='replace'
    ) as writer:
        df_modèle.to_excel(writer, index=False, sheet_name="Modèles")

def save_df_sous_modèle():
    global df_sous_modèle
    with pd.ExcelWriter(
            path="data/List_Marque_Modèle_Final.xlsx",
            engine='openpyxl',
            mode='a',  # append data to the file
            if_sheet_exists='replace'
    ) as writer:
        df_sous_modèle.to_excel(writer, index=False, sheet_name="Sous-Modèles")


def add_marque(marque):

    global df_marque, df_marque_modèle
    list_id_marque = sorted(df_marque["ID Marque"])
    last_id = list_id_marque[-1]
    last_number = int(last_id[1:])
    new_number = last_number + 1
    nb_size = len(str(new_number))
    new_id = "M" + "0"*(3-nb_size) + str(new_number)
    new_row_marque = [new_id, str(marque).upper(), None, None, None]
    new_row_marque_modèle = [new_id, new_id, None, None, str(marque).upper(), "\\", "\\", 0, None]
    df_marque.loc[len(df_marque)] = new_row_marque
    df_marque_modèle.loc[len(df_marque_modèle)] = new_row_marque_modèle

def add_modèle(modèle, marque):

    global df_marque, df_modèle, df_marque_modèle

    marque = str(marque).upper()
    modèle = str(modèle)
    dict_id_marque = dict(zip(df_marque["Marque"].values, df_marque["ID Marque"].values))
    id_marque = dict_id_marque.get(marque, "M000")

    list_id_modèle = sorted(df_modèle["ID Modèle"].values)
    last_id = list_id_modèle[-1]

    last_number = int(last_id[1:])
    new_number = last_number + 1
    nb_size = len(str(new_number))
    new_id = "A" + "0"*(3-nb_size) + str(new_number)

    new_row_modèle = [new_id, modèle, None, marque, None, None]
    new_row_marque_modèle = [id_marque+new_id, id_marque, new_id, None, marque, modèle, "\\", 0, None]
    df_modèle.loc[len(df_modèle)] = new_row_modèle
    df_marque_modèle.loc[len(df_marque_modèle)] = new_row_marque_modèle

def add_sous_modèle(sous_modèle, modèle, marque):

    global df_marque, df_modèle, df_sous_modèle, df_marque_modèle

    marque = str(marque).upper()
    modèle = str(modèle)
    sous_modèle = str(sous_modèle)

    dict_id_marque = dict(zip(df_marque["Marque"].values, df_marque["ID Marque"].values))
    dict_id_modèle = dict(zip(df_modèle["Modèle"].values, df_modèle["ID Modèle"].values))
    id_marque = dict_id_marque.get(marque, "M000")
    id_modèle = dict_id_modèle.get(modèle, "A000")

    list_id_sous_modèle = sorted(df_sous_modèle["ID Sous-Modèle"].values)
    last_id = list_id_sous_modèle[-1]

    last_number = int(last_id[1:])
    new_number = last_number + 1
    nb_size = len(str(new_number))
    new_id = "B" + "0"*(4-nb_size) + str(new_number)
    new_row_sous_modèle = [new_id, sous_modèle, None, modèle, marque, None, None, 0, *[None]*12]
    new_row_marque_modèle = [id_marque+id_modèle+new_id, id_marque, id_modèle, new_id, marque, modèle, sous_modèle, 0, None]
    df_sous_modèle.loc[len(df_sous_modèle)] = new_row_sous_modèle
    df_marque_modèle.loc[len(df_marque_modèle)] = new_row_marque_modèle




