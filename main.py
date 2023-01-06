import streamlit as st
import plotly.express as px
import pandas as pd


st.markdown("# Ir ligands clustering")
st.sidebar.markdown("# Ir ligands clustering")
st.sidebar.markdown("## L1 t-SNE map")
st.sidebar.markdown("## L3 t-SNE map")
st.sidebar.markdown("## L1 = ppy and t-SNE was applied to L3")


st.markdown("## For all of further t-SNE maps only equal L1 and L2 ligands were  selected")

st.markdown("### L1 t-SNE map")

l1_plot = pd.read_csv('l1_plot.csv')

fig_l1 = px.scatter(l1_plot, x='t-SNE-1',
           y='t-SNE-2',
           hover_data=['L1', 'L3', 'противоион', 'IC50,μM±Dark'],
           color='IC50,μM±Dark')

fig_l1.update_layout(
                    autosize=False,
                    width=800,
                    height=800)

st.plotly_chart(fig_l1, use_container_width=True)


st.markdown("### L3 t-SNE map")

l3_plot = pd.read_csv('l3_plot.csv')

fig_l3 = px.scatter(l3_plot, x='t-SNE-1',
           y='t-SNE-2',
           hover_data=['L1', 'L3', 'противоион', 'IC50,μM±Dark'],
           color='IC50,μM±Dark')

fig_l3.update_layout(
    autosize=False,
    width=800,
    height=800)

st.plotly_chart(fig_l3, use_container_width=True)

st.markdown("### L1 = ppy and t-SNE was applied to L3")

set_l3_plot = pd.read_csv('set_l3_plot.csv')

fig_l3_set = px.scatter(set_l3_plot, x='t-SNE-1',
           y='t-SNE-2',
           hover_data=['L1', 'L3', 'противоион', 'IC50,μM±Dark'],
           color='IC50,μM±Dark')

fig_l3_set.update_layout(
    autosize=False,
    width=800,
    height=800)

st.plotly_chart(fig_l3_set, use_container_width=True)
