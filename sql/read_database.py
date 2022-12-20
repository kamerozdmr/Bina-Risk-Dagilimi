import mysql.connector
import streamlit as st
import pandas as pd

def ConnectDatabase():
    global db
    global cursor

    db = mysql.connector.connect(**st.secrets["mysql"])
    cursor = db.cursor()

def EndConnection():
    cursor.close()
    db.close()


def readBetonarme():

    ConnectDatabase()

    query = "SELECT * from "
    betonarme_df = pd.read_sql(f"{query} betonarme", db)    

    EndConnection()

    return betonarme_df