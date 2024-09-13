import streamlit as st
from datetime import datetime, time
from contract import Sales
from database import save_at_postgres
from pydantic import ValidationError

def main():
  st.title('CRM and Sales System')
  email = st.text_input("Enter the seller's email address:")
  date = st.date_input("Select the date of sale:", datetime.now())
  hour = st.time_input("Choose the time of sale:", value=time(9, 0))
  cost = st.number_input("Enter the total cost of sale:", min_value=0.0, format="%.2f")
  quantity = st.number_input("Specify the quantity of products sold:", min_value=1, step=1)
  product = st.selectbox(
    "Choose the product involved",
    ['Project with Gemini',
    'Project with ChatGPT',
    'Project with Llama 3.0'])
  fully_date = datetime.combine(date, hour)

  if st.button('Save'):
    try: 
      sale = Sales(
        email=email,
        date_hour=fully_date,
        cost=cost,
        quantity=quantity,
        product=product
      )
      save_at_postgres(sale)

    except ValidationError as e:
      st.error(f"Ops! Something went wrong. Please check the following: {e}")


if __name__ == '__main__':
  main()
