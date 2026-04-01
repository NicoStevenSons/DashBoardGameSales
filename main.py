import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("DM101GameSales.xlsx", sheet_name="Cleaned")
st.title('Game Sales')

st.write('Between 1980 to 2020 the Rise of modern gaming and its Platforms')
st.markdown("<br>", unsafe_allow_html=True)#adds space


#Bar Graphs --Start
st.header('Cleaned Data Sheet')
st.write(df)


# get top 10 games by global sales
games_sales = df.groupby("Name")["Global_Sales"].sum().sort_values(ascending=False)
top_games_sales = games_sales.head(10)

# get top 10 platforms by global sales
platform_sales = df.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False)
top_platform_sales = platform_sales.head(10)

plt.figure(figsize=(14, 12))


def create_bar_chart_subplot(x, y, title="Chart title", xLabel="X Label", yLabel="Y Label", subPlotIndex=1):
    plt.subplot(2, 1, subPlotIndex)
    plt.barh(x, y)
    plt.title(title, fontsize = 20)
    plt.xlabel(xLabel, fontsize = 18)
    plt.ylabel(yLabel, fontsize = 18)  
    

# create sub plot for top 10 games by global sales
create_bar_chart_subplot(
    top_games_sales.index, 
    top_games_sales.values, 
    "Top 10 Games by Global Sales", 
    "Global Sales (millions)", 
    "Games"
)

# create sub plot for platforms by global sales
create_bar_chart_subplot(
    top_platform_sales.index, 
    top_platform_sales.values, 
    "Top 10 Platforms by Global Sales", 
    "Global Sales (millions)", 
    "Platforms",
    2

)
st.markdown("<br>", unsafe_allow_html=True)#adds space
st.header('Top 10 Games and Platfroms in Global Sales')

# display plot
plt.subplots_adjust(hspace=0.4)
st.pyplot(plt)
#Bar Graphs --end


#PieChart --Start
# 1. Load the Regional_Sales sheet from your new file
df2 = pd.read_excel("DM101GameSales.xlsx", sheet_name="Regional_Sales", header=2)

# 2. Extract the sales values
labels = ["NA Sales", "EU Sales", "JP Sales", "Other Sales"]
values = [
    df2["Sum of NA_Sales"].iloc[0],
    df2["Sum of EU_Sales"].iloc[0],
    df2["Sum of JP_Sales"].iloc[0],
    df2["Sum of Other_Sales"].iloc[0],
]

labels_with_values = [f"{label}\n({value:.2f})" for label, value in zip(labels, values)]

# 3. Plot the pie chart
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(
    values,
    labels=labels_with_values,
    autopct="%1.1f%%",
    startangle=140,
    colors=["#4C72B0", "#DD8452", "#55A868", "#C44E52"],
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5} 
)

st.markdown("<br>", unsafe_allow_html=True)#adds space
st.header("Regional Sales Distribution")
plt.tight_layout()
st.pyplot(plt)
#PieChart --end
