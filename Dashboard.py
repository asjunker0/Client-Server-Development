#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Setup the Jupyter version of Dash
from dash import Dash

import dash_leaflet as dl
from dash import dcc
from dash import html
import plotly.express as px
from dash import dash_table
from dash.dependencies import Input, Output, State
import base64
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from animal_shelter import AnimalShelter

###########################
# Data Manipulation / Model
###########################
MONGO_PORT = 27017

db = AnimalShelter("localhost", MONGO_PORT, "AAC", "animals")
df = pd.DataFrame.from_records(db.read({}))
if '_id' in df.columns:
    df.drop(columns=['_id'], inplace=True)

#########################
# Shared style constants
#########################

COLORS = {
    'background': '#F7F9FC',
    'surface':    '#FFFFFF',
    'primary':    '#1A73E8',
    'text':       '#202124',
    'subtext':    '#5F6368',
    'border':     '#DADCE0',
    'highlight':  '#D2E9FF',
}

PAGE_STYLE = {
    'backgroundColor': COLORS['background'],
    'minHeight': '100vh',
    'fontFamily': '"Segoe UI", Arial, sans-serif',
    'color': COLORS['text'],
    'padding': '0 0 40px 0',
}

CARD_STYLE = {
    'backgroundColor': COLORS['surface'],
    'borderRadius': '8px',
    'boxShadow': '0 1px 4px rgba(0,0,0,0.12)',
    'padding': '20px',
    'margin': '16px',
}

HEADER_STYLE = {
    'color': COLORS['text'],
    'padding': '24px 24px 8px 24px',
    'textAlign': 'center',
    'fontSize': '26px',
    'fontWeight': '700',
}

LABEL_STYLE = {
    'color': COLORS['text'],
    'fontWeight': '600',
    'fontSize': '13px',
    'marginBottom': '4px',
    'display': 'block',
}

BUTTON_STYLE = {
    'backgroundColor': COLORS['surface'],
    'color': COLORS['text'],
    'border': f'1px solid {COLORS["border"]}',
    'borderRadius': '4px',
    'padding': '6px 16px',
    'fontSize': '13px',
    'cursor': 'pointer',
    'marginTop': '18px',
    'fontFamily': '"Segoe UI", Arial, sans-serif',
}

DROPDOWN_STYLE = {
    'fontSize': '13px',
    'color': COLORS['text'],
    'minWidth': '220px',
}

#########################
# Dashboard Layout / View
#########################
app = Dash(__name__)

app.layout = html.Div(style=PAGE_STYLE, children=[

    # Header
    html.Div([
        html.Hr(style={'borderColor': COLORS['border'], 'margin': '0 16px'}),
        html.H2("Austin Animal Center Dashboard", style=HEADER_STYLE),
        html.Hr(style={'borderColor': COLORS['border'], 'margin': '0 16px'}),
    ]),

    # Filter card
    html.Div(style={**CARD_STYLE, 'display': 'flex', 'alignItems': 'flex-end', 'gap': '32px', 'flexWrap': 'wrap'}, children=[

        # Rescue type dropdown
        html.Div(children=[
            html.Span("Filter by Rescue Type:", style=LABEL_STYLE),
            dcc.Dropdown(
                id='filter-type',
                options=[
                    {'label': 'All',                          'value': 'reset'},
                    {'label': 'Water Rescue',                 'value': 'water'},
                    {'label': 'Mountain/Wilderness Rescue',   'value': 'mountain'},
                    {'label': 'Disaster/Individual Tracking', 'value': 'disaster'},
                ],
                value='reset',
                clearable=False,
                style=DROPDOWN_STYLE,
            ),
        ]),

        # Intake type dropdown, based on 'Intake Type' field values
        html.Div(children=[
            html.Span("Filter by Intake Type:", style=LABEL_STYLE),
            dcc.Dropdown(
                id='filter-intake',
                options=[
                    {'label': 'All',              'value': 'reset'},
                    {'label': 'Stray',            'value': 'Stray'},
                    {'label': 'Owner Surrender',  'value': 'Owner Surrender'},
                    {'label': 'Public Assist',    'value': 'Public Assist'},
                    {'label': 'Wildlife',         'value': 'Wildlife'},
                    {'label': 'Euthanasia Request','value': 'Euthanasia Request'},
                ],
                value='reset',
                clearable=False,
                style=DROPDOWN_STYLE,
            ),
        ]),

        # Reset button
        html.Div(children=[
            html.Button("Reset Filters", id='reset-button', n_clicks=0, style=BUTTON_STYLE),
        ]),
    ]),

    # Data table card
    html.Div(style=CARD_STYLE, children=[
        dash_table.DataTable(
            id='datatable-id',
            columns=[{"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns],
            data=df.to_dict('records'),
            selected_rows=[0],
            page_size=10,
            filter_action='native',
            sort_action='native',
            style_table={
                'overflowX': 'auto',
                'borderRadius': '6px',
                'border': f'1px solid {COLORS["border"]}',
            },
            style_header={
                'backgroundColor': COLORS['surface'],
                'color': COLORS['text'],
                'fontWeight': '600',
                'fontSize': '12px',
                'border': f'1px solid {COLORS["border"]}',
                'padding': '8px 10px',
                'textAlign': 'left',
            },
            style_filter={
                'backgroundColor': COLORS['background'],
                'color': COLORS['text'],
                'fontSize': '12px',
                'border': f'1px solid {COLORS["border"]}',
            },
            style_cell={
                'backgroundColor': COLORS['surface'],
                'color': COLORS['text'],
                'fontSize': '12px',
                'padding': '8px 10px',
                'border': f'1px solid {COLORS["border"]}',
                'textAlign': 'left',
                'whiteSpace': 'normal',
                'height': 'auto',
                'minWidth': '80px',
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': COLORS['background'],
                },
                {
                    'if': {'state': 'selected'},
                    'backgroundColor': COLORS['highlight'],
                    'border': f'1px solid {COLORS["primary"]}',
                },
            ],
        ),
    ]),

    # Chart + Map row
    html.Div(
        style={'display': 'flex', 'flexWrap': 'wrap', 'margin': '0 8px'},
        children=[
            html.Div(id='graph-id',
                     style={**CARD_STYLE, 'flex': '1', 'minWidth': '300px', 'margin': '8px'}),
            html.Div(id='map-id',
                     style={**CARD_STYLE, 'flex': '1', 'minWidth': '300px', 'margin': '8px'}),
        ]
    ),
])

#############################################
# Interaction Between Components / Controller
#############################################

@app.callback(
    Output('filter-type',   'value'),
    Output('filter-intake', 'value'),
    Input('reset-button',   'n_clicks'),
    prevent_initial_call=True,
)
def reset_filters(n_clicks):
    """Reset both dropdowns to All when Reset Filters is clicked."""
    return 'reset', 'reset'


@app.callback(
    Output('datatable-id', 'data'),
    Input('filter-type',   'value'),
    Input('filter-intake', 'value'),
)
def update_dashboard(filter_type, filter_intake):
    """Build a MongoDB query from both dropdowns and return filtered records.

    All field names match your actual dataset exactly:
      'Animal Type', 'Breed', 'Sex upon Intake', 'Intake Type'
    """

    query = {}

    # Rescue type filter 
    # Uses 'Animal Type', 'Breed', and 'Sex upon Intake'
    if filter_type == 'water':
        query.update({
            'Animal Type': 'Dog',
            'Breed': {'$in': [
                'Labrador Retriever Mix', 'Chesapeake Bay Retriever',
                'Newfoundland', 'Labrador Retriever',
            ]},
            'Sex upon Intake': {'$in': ['Intact Female', 'Spayed Female']},
        })
    elif filter_type == 'mountain':
        query.update({
            'Animal Type': 'Dog',
            'Breed': {'$in': [
                'German Shepherd', 'German Shepherd Mix', 'Alaskan Malamute',
                'Old English Sheepdog', 'Siberian Husky',
                'Rottweiler', 'Rottweiler Mix',
            ]},
            'Sex upon Intake': {'$in': ['Intact Male', 'Neutered Male']},
        })
    elif filter_type == 'disaster':
        query.update({
            'Animal Type': 'Dog',
            'Breed': {'$in': [
                'Doberman Pinscher', 'German Shepherd', 'German Shepherd Mix',
                'Golden Retriever', 'Golden Retriever Mix',
                'Bloodhound', 'Bloodhound Mix',
                'Rottweiler', 'Rottweiler Mix',
            ]},
            'Sex upon Intake': {'$in': ['Intact Male', 'Neutered Male']},
        })

    # Intake type filter — uses 'Intake Type' 
    if filter_intake and filter_intake != 'reset':
        query['Intake Type'] = filter_intake

    filtered_df = pd.DataFrame.from_records(db.read(query))
    if filtered_df.empty:
        return []
    if '_id' in filtered_df.columns:
        filtered_df.drop(columns=['_id'], inplace=True)
    return filtered_df.to_dict('records')


@app.callback(
    Output('graph-id', "children"),
    Input('datatable-id', "derived_virtual_data"),
)
def update_graphs(viewData):
    if not viewData:
        return []
    dff = pd.DataFrame.from_dict(viewData)
    if dff.empty or 'Breed' not in dff.columns:
        return []
    fig = px.pie(
        dff,
        names='Breed',
        title='Breed Distribution',
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    fig.update_layout(
        paper_bgcolor=COLORS['surface'],
        plot_bgcolor=COLORS['surface'],
        font_color=COLORS['text'],
        title_font_color=COLORS['primary'],
        margin=dict(t=50, b=20, l=20, r=20),
    )
    return [dcc.Graph(figure=fig)]


@app.callback(
    Output('datatable-id', 'style_data_conditional'),
    Input('datatable-id', 'selected_columns'),
)
def update_styles(selected_columns):
    base = [
        {'if': {'row_index': 'odd'}, 'backgroundColor': COLORS['background']},
        {'if': {'state': 'selected'}, 'backgroundColor': COLORS['highlight'],
         'border': f'1px solid {COLORS["primary"]}'},
    ]
    if not selected_columns:
        return base
    return base + [
        {'if': {'column_id': i}, 'backgroundColor': COLORS['highlight']}
        for i in selected_columns
    ]


@app.callback(
    Output('map-id', "children"),
    Input('datatable-id', "derived_virtual_data"),
    Input('datatable-id', "derived_virtual_selected_rows"),
)
def update_map(viewData, index):
    austin = [30.2672, -97.7431]

    def empty_map():
        return [dl.Map(
            style={'width': '100%', 'height': '450px', 'borderRadius': '6px'},
            center=austin, zoom=10,
            children=[dl.TileLayer(id="base-layer-id")]
        )]

    if not viewData:
        return empty_map()

    dff = pd.DataFrame.from_dict(viewData)
    if dff.empty:
        return empty_map()

    row = index[0] if index else 0
    if row >= len(dff):
        row = 0

    r = dff.iloc[row]

    # All column names match CSV field names exactly
    name      = str(r.get('Name',           'Unknown'))
    breed     = str(r.get('Breed',          'Unknown'))
    animal_id = str(r.get('Animal ID',      'Unknown'))
    location  = str(r.get('Found Location', 'Austin, TX'))
    condition = str(r.get('Intake Condition','Unknown'))

    return [
        dl.Map(
            style={'width': '100%', 'height': '450px', 'borderRadius': '6px'},
            center=austin,
            zoom=10,
            children=[
                dl.TileLayer(id="base-layer-id"),
                dl.Marker(position=austin, children=[
                    dl.Tooltip(f"{name} — {breed}"),
                    dl.Popup([
                        html.H4("Animal Info",
                                style={'color': COLORS['primary'], 'margin': '4px 0'}),
                        html.P(f"ID: {animal_id}",        style={'margin': '2px 0'}),
                        html.P(f"Name: {name}",           style={'margin': '2px 0'}),
                        html.P(f"Breed: {breed}",         style={'margin': '2px 0'}),
                        html.P(f"Found: {location}",      style={'margin': '2px 0'}),
                        html.P(f"Condition: {condition}", style={'margin': '2px 0'}),
                    ])
                ])
            ]
        )
    ]


app.run(debug=True)

