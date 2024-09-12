import streamlit as st
from datetime import datetime, time
import contract

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

  if st.button('Save'):
    st.write('### Sale Details')

    col1, col2 = st.columns(2)

    with col1:
      st.write(f"**Seller's Email:** {email}")
      st.write(f"**Date of Sale:** {date.strftime('%Y-%m-%d')}")
      st.write(f"**Time of Sale:** {hour.strftime('%H:%M')}")

    with col2:
      st.write(f"**Total Cost:** ${cost:,.2f}")
      st.write(f"**Quantity Sold:** {quantity}")
      st.write(f"**Product:** {product}")

    st.success('Sale successfully registered!')

    fully_date = datetime.combine(date, hour)

if __name__ == '__main__':
  main()
