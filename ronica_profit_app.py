import streamlit as st

st.set_page_config(page_title="Ronica Cakes Profit Calculator", page_icon="🎂")

st.title("🎂 Ronica Cakes Profit Calculator")
st.write("Calculate your selling price, cost, and profit easily.")

st.header("🔢 Enter Your Costs")

# Inputs
ingredient_cost = st.number_input("Ingredients Cost (TZS)", min_value=0.0, step=100.0)
labour_cost = st.number_input("Labour Cost (TZS)", min_value=0.0, step=100.0)
packaging_cost = st.number_input("Packaging Cost (TZS)", min_value=0.0, step=100.0)
other_cost = st.number_input("Other Costs (Transport, Gas, Utilities)", min_value=0.0, step=100.0)

profit_margin = st.slider("Desired Profit Margin (%)", min_value=0, max_value=100, value=30)

st.header("💰 Results")

# Total cost
total_cost = ingredient_cost + labour_cost + packaging_cost + other_cost

# Selling price
selling_price = total_cost * (1 + profit_margin / 100)

# Profit per cake
profit = selling_price - total_cost

# Display
st.subheader("📌 Summary")
st.write(f"**Total Cost per Cake:** TZS {total_cost:,.0f}")
st.write(f"**Selling Price (Recommended):** TZS {selling_price:,.0f}")
st.write(f"**Profit per Cake:** TZS {profit:,.0f}")

# Monthly revenue calculator
st.header("📆 Monthly Estimate")
cakes_per_month = st.number_input("How many cakes do you expect to sell per month?", min_value=0, step=1)

monthly_profit = cakes_per_month * profit

st.write(f"**Estimated Monthly Profit:** TZS {monthly_profit:,.0f}")
