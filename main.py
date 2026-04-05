import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("DM101GameSales.xlsx", sheet_name="Cleaned")
PS2 = pd.read_excel("DM101GameSales.xlsx", sheet_name="PS2 Sales")

st.sidebar.title('Dashboard Page Select')
page = st.sidebar.radio('Go To: ', ['Visualization', 'Raw Data', 'Cleaned Data', 'All Sheets'])

def toplabel():
    st.title('Game Sales')
    st.write('Between 1980 to 2020 the Rise of modern gaming and its Platforms')
    st.markdown("<br>", unsafe_allow_html=True)#adds space


if page == 'Visualization':
    toplabel()
    #Bar Graphs --Start
    #get top 10 games by global sales
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


    #Bar Graphs PS2 --Start
    st.markdown("<br>", unsafe_allow_html=True)#adds space
    st.header('Top 10 Games in the PS2 Platfrom')

    platformsales = pd.read_excel("DM101GameSales.xlsx")
    ps2_df = df[df["Platform"] == "PS2"]
    top_ps2 = ps2_df.sort_values(by="Global_Sales", ascending=False).head(10)
    Name = top_ps2["Name"]
    Global_sales = top_ps2["Global_Sales"]

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.barh(Name, Global_sales)

    ax.set_xlabel("Global Sales (millions)")
    ax.set_ylabel("Games")

    ax.invert_yaxis()

    st.pyplot(fig)
    #Bar Graphs PS2 --end

    #Bar Graphs genre sales --start
    genre_df = pd.read_excel("DM101GameSales.xlsx", sheet_name="Genre_Sales")
    st.markdown("<br>", unsafe_allow_html=True)#adds space
    st.header('Genre Popularity')

    genre_df.columns = genre_df.columns.str.strip()

    genre_df = genre_df[genre_df["Genre"] != "Grand Total"]


    genre_df = genre_df.rename(columns={
        "Genre": "Genre",
        "Sum of Global_Sales": "Global_Sales"
    })

    genre_df = genre_df.sort_values(by="Global_Sales", ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(genre_df['Genre'], genre_df['Global_Sales'], edgecolor='black')

    ax.set_xlabel("Genre")
    ax.set_ylabel("Global Sales (Millions)")
    ax.set_title("Video Game Genre Popularity (1980–2017)")

    ax.tick_params(axis='x', rotation=45)

    st.pyplot(fig)
    #Bar Graphs genre sales --end
    

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

    #Plot the pie chart
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






    #linechart --start
    df3 = pd.read_excel("DM101GameSales.xlsx", sheet_name="Time Line of Sales")

    df3.columns = df3.columns.str.strip()
    df3 = df3[df3["Row Labels"] != "Grand Total"]

    #Convert to numeric
    df3["Row Labels"] = pd.to_numeric(df3["Row Labels"])

    #Plot chart
    fig2, ax2 = plt.subplots(figsize=(10, 5))

    ax2.plot(
        df3["Row Labels"],               
        df3["Sum of Global_Sales"],       
        marker='o',
        linestyle='-'
    )

    ax2.set_xlabel("Years")
    ax2.set_ylabel("Total Global Sales")
    ax2.grid(True)

    st.header("Timeline of Sales From 1980 to 2017")
    st.pyplot(fig2)
    #linechart --end
    

elif page == 'Cleaned Data':
    toplabel()
    st.header('Cleaned Data Sheet')
    st.write(df)
    st.write('Contains structured data on video game sales, where each row represents a game and columns include details like name, platform, year of release, genre, and publisher. It also includes regional and global sales figures in millions. The data is cleaned for consistency and easy analysis. Additionally, a “Time Line of Sales” sheet summarizes yearly total sales using a pivot table, making it useful for analyzing trends and creating visualizations')

    st.markdown("<br>", unsafe_allow_html=True)#adds space
    st.header('Top 10 Games in the PS2 Platfrom')
    st.write(PS2)
    st.write('The PS2 sheet confirms a market trend where blockbuster sequels and open-world mechanics began to yield the highest return on investment. For a developer or publisher, this data suggests that during the 2000s, investing in established franchises with high replay value was the most successful path to global market penetration')

elif page == 'Raw Data':
    toplabel()
    st.header('Raw Data Set')
    rawdata = pd.read_excel("DM101GameSales.xlsx", sheet_name="Raw Data")
    st.write(rawdata)

elif page == 'All Sheets':
    st.header('All sheets')
    file_path = "DM101GameSales.xlsx"
    
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names

    tabs = st.tabs(sheet_names)

    for i, sheet in enumerate(sheet_names):
        with tabs[i]:
            st.subheader(f"Data from sheet: {sheet}")
            
            #Readeachsheet
            df = pd.read_excel(xls, sheet_name=sheet)
            
            #Displaydataframe
            st.dataframe(df, use_container_width=True)









