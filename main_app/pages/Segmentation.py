# importing streamlit framework for deploying web-app
import streamlit as st
# for altair charts in streamlit library
import altair as alt
# importing libraries for data analysis
import pandas as pd
import numpy as np
# importing to visualization where streamlit is not enough
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# rename page name
st.set_page_config(page_title="Customer Segmentation",layout="wide")

# create a header for web page
st.markdown("<h1 style='font-style: italic;'>Data-Oriented Perspective. Provides Reliability.</h1>",unsafe_allow_html=True)
# add a text under header
st.markdown("<p style='color: #FF8585; font-size: 18px; font-style: bold'>Observe our Customer Segmentation model. Powered with Business Intelligence. Create rapid and smart strategies for your customers. </p>", unsafe_allow_html=True)

# create sidebar and other sub-page components here
st.sidebar.title("Customer Segmentation Capstone Project Web-App")
st.sidebar.write("Project by ENM and CMP students. Cansu Can, Derya Ekin Dereci, Eda Merduman from ENM Team and Emirhan Serveren, Mert Oğuz, Oğuz Alp Özçelik from CMP Team")

# create a header for the column
st.markdown("<h2 style='font-style: italic;'>G Type Customers have Distinct Risk Groups</h2>",unsafe_allow_html=True)
# add a text under header
st.markdown("<p style='color: #FF8585; font-size: 18px; font-style: italic'>Due to their characteristics, it is pre-estimated situation that validated with analytics.</p>", unsafe_allow_html=True)

# create column containers for the next section
colup_G1, colup_G2 = st.columns(2)

# create a donut chart for distribution of segments
bk_cluster_distribution = pd.read_feather('streamlit_view/bk_cluster_distribution')
# header and context at the top
colup_G1.subheader("Observe the Segment Distribution. Discover Customer Reliability.")
# give a info under the header
colup_G1.markdown("""<p style='color: #47EB78; font-style: bold; font-size: 16px;'>Less number of segments generated then pre-defined labels
            by the company. Optimized the distribution while reducing number of segments.</p>""", unsafe_allow_html=True)
# visualize here
fig_bk_distribution = go.Figure(data=[go.Pie(labels=bk_cluster_distribution['Segment'],values=bk_cluster_distribution['Count'])])
# move legend to left of chart
fig_bk_distribution.update_traces(hole=0.4, hovertemplate=None, hoverinfo='skip',marker=dict(colors=['#F6F314','#2CF5D5','#F50000']))
fig_bk_distribution.update_layout(legend=dict(orientation="v",x=0,y=1,xanchor="left",yanchor="bottom"))
# render the chart
colup_G1.plotly_chart(fig_bk_distribution, use_container_width=True)

# give a context about chart in the head of next column container
colup_G2.markdown("""**G-Gold is the most reliable segment.** G-Diamond is the moderately reliable segment. **G-Bronze is the most risky segment for G type customers.**""")
# print the numerical visualization right to the chart as a data frame
bk_cluster_distribution= bk_cluster_distribution.rename(columns={'Count':'Number of Customers'})
colup_G2.dataframe(bk_cluster_distribution.set_index('Segment'), use_container_width=True)
# give the remaining context under the data frame
colup_G2.markdown("""<p style='color: #FFFF00; font-style: bold; font-size: 18px;'>There are going to be three cases.
            Low-rated offers ought to be presented to the most reliable customer group.</p>""", unsafe_allow_html=True)
colup_G2.markdown("""<p style='color: #FF3333; font-style: bold; font-size: 18px;'>High-rated offers ought to be presented to the most
            risky customer group. It is important to remind their checks' playback would be more risky.</p>""", unsafe_allow_html=True)
colup_G2.markdown("""<p style='color: #FFFFFF; font-style: bold; font-size: 18px;'>Simply, reliable customers' checks are more
            preferable for the company.</p>""", unsafe_allow_html=True)

# create another column containers for the next section
colmid_G1,colmid_G2,colmid_G3 = st.columns([1,2,2])

# info about data on the left as text
colmid_G1.markdown("""<p style='color: #FFFF00; font-style: bold; font-size: 18px;'>
                Limit-Risk Ratio Has Huge Impact.</p>""",
                unsafe_allow_html=True)
colmid_G1.write("In the reliable group limit credit is thousand times more than risk credit. The risky group's limit and credit risk is nearly same.")
# another fact about data written
colmid_G1.markdown("""<p style='color: #FFFF00; font-style: bold; font-size: 18px;'>
                Number of Branches Has No Effect.</p>""",
                unsafe_allow_html=True)
colmid_G1.write("In all segments, average number of branches are approximately equal.")
# another fact about data written
colmid_G1.markdown("""<p style='color: #FFFF00; font-style: bold; font-size: 18px;'>
                Less Drawer. Reliable Work.</p>""",
                unsafe_allow_html=True)
colmid_G1.write("In G-Gold segment, customers are worked with averagely 10 drawers. That is 18 for G-Bronze.")

# header declared first because it is over the chart
colmid_G2.subheader("Reliable Segment has More Income and Less Loss from Checks")
# check income-loss percentage chart which is on the left container
bk_check_income = pd.read_feather("streamlit_view/bk_cluster_check_income.feather")
# create the visualization below
fig_bk_check_income = go.Figure(data=[
    go.Bar(name='Check Income (%)', x=bk_check_income['Segment'], y=bk_check_income['Check Income (%)'],
        text=bk_check_income['Check Income (%)'].round(2), textposition='auto', marker=dict(color='#FFD438')),
    go.Bar(name='Check Loss (%)', x=bk_check_income['Segment'], y=bk_check_income['Check Loss (%)'],
        text=bk_check_income['Check Loss (%)'].round(2), textposition='auto', marker=dict(color='#FF1F1F'))])
# then declare the stack mode
fig_bk_check_income.update_layout(xaxis_title=None,yaxis_title='Percentage (%)', barmode='stack')
fig_bk_check_income.update_traces(hovertemplate=None, hoverinfo='skip')
# render the chart
colmid_G2.plotly_chart(fig_bk_check_income, use_container_width=True)

# create view for frequency of segments
bk_cluster_frequency = pd.read_feather("streamlit_view/bk_cluster_frequency.feather")
# header above
colmid_G3.subheader("Reliable Customers Visit Less")
colmid_G3.markdown(" **Monthly customers populated mostly in risky group.** You can switch off using the legend to observe in detail.")
# visualize the bar chart
fig_bk_cluster_frequency = go.Figure(data=[
    go.Bar(name='Rare Customers', x=bk_cluster_frequency['Segment'], y=bk_cluster_frequency['Rare'],
        marker=dict(color='#FF1F1F')),
    go.Bar(name='Monthly Customers', x=bk_cluster_frequency['Segment'], y=bk_cluster_frequency['Very Often'],
        marker=dict(color='#5EFF5E'))])
fig_bk_cluster_frequency.update_traces(hovertemplate=None, hoverinfo='skip')
colmid_G3.plotly_chart(fig_bk_cluster_frequency, use_container_width=True)

# declare the next column containers
coldown_G1, coldown_G2 = st.columns([2,1])

# create a scatter plot for to describe the distribution of segments
bk_cluster_scatter_map = pd.read_feather('streamlit_view/bk_cluster_scatter_map.feather')
bk_cluster_scatter_map = bk_cluster_scatter_map.sample(1000)    # take sample for clear viz
# header before the chart
coldown_G1.subheader("Reliable Customers Have Least Credit Risk")
# visualize the scatter plot
fig_bk_cluster_map = px.scatter(bk_cluster_scatter_map,
                        x="BK_LIMIT", y="BK_RISK",
                        color="CLUSTER_LABELS_3")
fig_bk_cluster_map.update_layout(xaxis_title='Credit Limit', yaxis_title='Credit Risk', legend_title='Segments')
fig_bk_cluster_map.update_xaxes(range=[0, 900000])      # edit axis range
fig_bk_cluster_map.update_yaxes(range=[0, 900000])      # edit axis range
# render the chart
coldown_G1.plotly_chart(fig_bk_cluster_map, use_container_width=True)

# write strategy notes coming from ENM team next to the scatter plot
coldown_G2.markdown("<h3 style='color: #47FF47; font-style: bold;'>The marketing strategy evaluated by ENM Team</h3>",unsafe_allow_html=True)
coldown_G2.markdown("✅ **Targeted Marketing**")
coldown_G2.markdown("✅ **Optimised Traditional and Digital Channel Usage**")
coldown_G2.markdown("✅ **Customer Interaction & Taking Feedbacks**")
coldown_G2.markdown("✅ **Customer Gain & Loyalty**")
coldown_G2.markdown("✅ **Relationship Building**")

# create a header for the column
st.markdown("<h2 style='font-style: italic;'>T Type Customers are Mostly Reliable</h2>",unsafe_allow_html=True)
# add a text under header
st.markdown("<p style='color: #FF8585; font-size: 18px; font-style: italic'>As they are corporation, that makes their payback possibility higher.</p>", unsafe_allow_html=True)

# create column containers for the next section
colup_1, colup_2 = st.columns(2)

# create a donut chart for distribution of segments
tk_cluster_distribution = pd.read_feather('streamlit_view/tk_cluster_distribution')

# give a context about chart in the head of next column container
colup_2.markdown("""**T-Diamond is the most reliable segment.** T type mostly distributed in a single segment. **Due to their organizational structure.** """)
# print the numerical visualization right to the chart as a data frame
tk_cluster_distribution= tk_cluster_distribution.rename(columns={'Count':'Number of Customers'})
colup_2.dataframe(tk_cluster_distribution.set_index('Segment'), use_container_width=True)
# give the remaining context under the data frame
colup_2.markdown("""<p style='color: #FFFF00; font-style: bold; font-size: 18px;'>There were three cases on G type.
            There are two cases in T type.</p>""", unsafe_allow_html=True)
colup_2.markdown("""<p style='color: #FF3333; font-style: bold; font-size: 18px;'>Low-rated offers are going to be presented for most of the T type customers. Because they are mostly reliable.</p>""", unsafe_allow_html=True)
colup_2.markdown("""<p style='color: #FFFFFF; font-style: bold; font-size: 18px;'>Simply, the importance of division of T and G type customers are better presented with the segmentation model.</p>""", unsafe_allow_html=True)

# reading the excel file "TAM FAKTORING PLAN"
df = pd.read_excel('data/TAM FAKTÖRİNG PLAN.xlsx')
# display as a dataframe
st.dataframe(df)