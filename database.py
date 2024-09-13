import psycopg2
from psycopg2 import sql
from contract import Sales
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

def save_at_postgres(data: Sales):
  try:
    conn = psycopg2.connect(
      dbname=DB_NAME,
      user=DB_USER,
      password=DB_PASS,
      host=DB_HOST
    )
    cursor = conn.cursor()
    cursor.execute(
      sql.SQL("INSERT INTO sales (email, date_hour, cost, quantity, product) VALUES (%s, %s, %s, %s, %s)"),
      (data.email, data.date_hour, data.cost, data.quantity, data.product)
    )
    conn.commit()
    st.success('Sale saved successfully!')
  except Exception as e:
    st.error(f"Ops! Something went wrong. Please check the following: {e}")
  finally:
    cursor.close()
    conn.close()
