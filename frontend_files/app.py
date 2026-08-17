import streamlit as st
import requests
import json

# title
st.title("SuperKart")

product_weight_input = st.number_input("Product Weight", min_value=0, help="Product Weight")

Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"], help="Product Sugar Content")

product_allocated_area_input = st.number_input("Product Allocated Area", min_value=0, help="Product Allocated Area")

product_mrp_input = st.number_input("Product MRP", min_value=0, help="Product MRP")

store_size_input = st.selectbox("Store Size", ["High", "Medium", "Small"], help="Store Size")

store_location_city_type_input = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"], help="Store Location City Type")

store_type_input = st.selectbox("Store Type", ["Departmental Store", "Food Mart","Store_Type","Supermarket Type1","Supermarket Type2"], help="Store Type")

product_id_first_2_chars_input = st.selectbox("Product Id First 2 Chars", ["FD", "NC", "DR"], help="Product Id First 2 Chars")

store_age_input = st.number_input("Store Age", min_value=0, help="Store Age")

product_type_category_input = st.selectbox("Product Type Category", ['Non Perishables', 'Perishables'], help="Product Type Category")

product_data = {
    "Product_Weight": product_weight_input,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": product_allocated_area_input,
    "Product_MRP": product_mrp_input,
    "Store_Size": store_size_input,
    "Store_Location_City_Type": store_location_city_type_input,
    "Store_Type": store_type_input,
    "Product_Id_First_2_Chars": product_id_first_2_chars_input,
    "Store_Age": store_age_input,
    "Product_Type_Category": product_type_category_input
}

if st.button("Predict"):
  response = requests.post("https://bug-free-space-carnival-q7gxr7949pj347q7-7860.app.github.dev/v1/predict", json=product_data)
  if response.status_code == 200:
    predicted_sales = response.json()['predicted_sales']
    st.success(f"Predicted Sales: {predicted_sales}")
  else:
    st.error(f"API request failed {response.status_code}")
    st.error(response.text)

