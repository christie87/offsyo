#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import html,dcc
from dash.dependencies import Input, Output, State


# In[2]:


df=pd.read_csv('US_zomato.csv')
cuisine_list=df['Cuisines'].unique().tolist()


# In[13]:



app = Dash(__name__,external_stylesheets=[dbc.themes.SLATE])

server = app.server 

# Define the layout
app.layout = html.Div([
    dbc.NavbarSimple(
        brand="US Restaurants with Zomato Ratings",
        brand_href="#",
        color="primary",
        dark=True,
    ),

dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id="dropdown",
                options=[{'label': i, 'value': i} for i in cuisine_list],
                         placeholder="Cuisine Choice",
                value="Option 1"
            ),
        ], width={"size": 6}, className="my-3", align="center"),
        dbc.Col([
            dbc.Tabs([
                dbc.Tab(label="Cities", tab_id="tab-1"),
                dbc.Tab(label="Votes", tab_id="tab-2"),
                dbc.Tab(label="Top Rated", tab_id="tab-3")
            ], id="tabs", active_tab="tab-1", className="my-3")
        ], width={"size": 6}, className="my-3", align="center")
    ]),
    html.Div(id="tab-content", className="my-3")
]),
])

# Define the callbacks


@app.callback(
    Output("sunfig", "figure"),
    Input("dropdown", "value"),
)
def update_tab1_graph(value):
    us = df[df['Cuisines']==value].groupby(['City','Rating text','Restaurant Name'],as_index=False).mean()  
    
    sunfig = px.sunburst(us, path=['Rating text','City'], values='Aggregate rating',
                         color='Rating text', 
                         color_discrete_sequence=px.colors.qualitative.Bold)
    return sunfig

@app.callback(
    Output("bubfig", "figure"),
    Input("dropdown", "value"),
)
def update_tab2_graph(value):
    us = df[df['Cuisines']==value].groupby(['City','Rating text','Restaurant Name'],as_index=False).mean()  
    
    bubfig = px.scatter(us, x="Aggregate rating", y="Rating text", size="Votes", color='Restaurant Name',
                       size_max=60,
                       color_discrete_sequence=px.colors.qualitative.Alphabet)
    return bubfig

@app.callback(
    Output("barfig", "figure"),
    Input("dropdown", "value"),
)
def update_tab3_graph(value):
    us = df[df['Cuisines']==value].groupby(['City','Rating text','Restaurant Name'],as_index=False).mean()  
    
    barfig=px.bar(us[us['Rating text']=='Excellent'],x='City',y='Aggregate rating',
                  color='Restaurant Name',
                  barmode='group',opacity=0.7,
                  color_discrete_sequence=px.colors.qualitative.Bold)
    barfig.update_traces(width=0.5)
    return barfig


@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab"),
    State("tabs", "children"),
    Input("dropdown", "value")
)
def render_tab_content(active_tab, children, value):
    if value is None:
        return html.Div("Please make a selection from the dropdown.")
    elif active_tab == "tab-1":
        return dbc.Card(
            dbc.CardBody([
                html.H3("Cities"),
                dcc.Graph(id="sunfig", figure={}, style={"backgroundColor": "#343a40"})
            ])
        )
    elif active_tab == "tab-2":
        return dbc.Card(
            dbc.CardBody([
                html.H3("Restaurants"),
                dcc.Graph(id="bubfig", figure={}, style={"backgroundColor": "#343a40"})
            ])
        ),
    else:
        return dbc.Card(
            dbc.CardBody([
                html.H3("Highest Rated"),
                dcc.Graph(id="barfig", figure={}, style={"backgroundColor": "#343a40"})
            ])
        )

if __name__ == '__main__':
    app.run_server(debug=True)

