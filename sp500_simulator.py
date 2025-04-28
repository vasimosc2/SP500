# save this as sp500_simulator.py

import streamlit as st
import matplotlib.pyplot as plt

def calculate_growth(yearly_increase, initial_amount, monthly_investment, years):
    months = years * 12
    invested = []
    actual = []
    
    current_invested = initial_amount
    current_actual = initial_amount

    monthly_return = (1 + yearly_increase) ** (1/12) - 1

    for month in range(1, months + 1):
        current_invested += monthly_investment
        current_actual = current_actual * (1 + monthly_return) + monthly_investment

        if month % 12 == 0:
            invested.append(current_invested)
            actual.append(current_actual)

    return invested, actual

def main():
    st.title("S&P 500 Investment Simulator 📈")
    
    yearly_increase = st.number_input("Expected Yearly Increase (e.g., 0.07 for 7%)", value=0.07)
    initial_amount = st.number_input("Initial Investment Amount ($)", value=1000)
    monthly_investment = st.number_input("Monthly Investment Amount ($)", value=500)
    years = st.number_input("Number of Years to Simulate", value=30)

    if st.button("Simulate"):
        invested, actual = calculate_growth(yearly_increase, initial_amount, monthly_investment, int(years))

        st.subheader("Results")
        st.write(f"Total Invested Amount: **${invested[-1]:,.2f}**")
        st.write(f"Total Actual Value: **${actual[-1]:,.2f}**")

        # Plotting
        years_list = list(range(1, int(years) + 1))
        plt.figure(figsize=(10, 6))
        plt.plot(years_list, invested, label="Total Invested")
        plt.plot(years_list, actual, label="Actual Value (with returns)")
        plt.xlabel("Years")
        plt.ylabel("Amount ($)")
        plt.title("Investment Growth Over Time")
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)

if __name__ == "__main__":
    main()

