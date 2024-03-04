import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

category_df = pd.read_csv("../Dashboard/most_sold_category.csv")
cities_df = pd.read_csv("../Dashboard/most_cities_buy.csv")


with st.sidebar:
    st.markdown("# Annisa Kumala Dewi E-commerce Dashboard")
    st.markdown("Welcome to Icha E-commerce Dashboard")


st.header(':heart: Icha E-commerce Dashboard :heart:')


#Visualisasi Pertanyaan 1
most_sold_category = category_df.groupby(by="product_category_name").agg({
    "order_item_id": "sum",
    "price": "sum"
})

most_sold_category_sorted = most_sold_category.sort_values(by="order_item_id")

top_10_categories = most_sold_category_sorted.head(10)

st.title("Top 10 Most Purchased Product Categories")

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(top_10_categories.index, top_10_categories['order_item_id'], color='darkkhaki')
ax.set_title('Top 10 Most Purchased Product Categories')
ax.set_xlabel('Product Category')
ax.set_ylabel('Total Number of Items Sold')
ax.set_xticklabels(top_10_categories.index, rotation=45, ha="right")
st.pyplot(fig)

#Visualisasi pertanyaan 2
order_count_per_city = cities_df['customer_city'].value_counts()

sorted_cities = order_count_per_city.sort_values(ascending=False)

top_10_cities = sorted_cities.head(10)

st.title('Top 10 Customer Cities with the Most Orders')

fig, ax = plt.subplots(figsize=(10, 6))
top_10_cities.plot(kind='bar', color='darkcyan', ax=ax)
plt.title('Top 10 Cities with the Most Orders')
plt.xlabel('City')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45, ha='right')  
plt.gca().invert_xaxis()
st.pyplot(fig)