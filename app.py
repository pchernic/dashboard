import datetime
import yfinance as yf
import pandas as pd
from dash import Dash, html, dcc, dash_table  # Removido 'callback', 'Output', 'Input' pois não há callbacks neste exemplo

# Coleta de dados
ticker = ['WEGE3.SA', 'PETR4.SA', 'ABEV3.SA', 'VALE3.SA', 'MGLU3.SA',
          'PCAR3.SA', 'ITUB4.SA', 'BBDC4.SA', 'BBAS3.SA']

try:
    cotacoes = yf.download(ticker, start=datetime.date.today() - datetime.timedelta(days=5))
    cotacoes = cotacoes['Close'].iloc[-1, :].to_frame().reset_index()
    cotacoes.columns = ['Ticker', 'Preço']
    cotacoes['Preço'] = cotacoes['Preço'].astype(float).round(2)
except Exception as e:
    cotacoes = pd.DataFrame(columns=['Ticker', 'Preço'])
    print("⚠️ Erro ao baixar cotações:", e)

# Inicializando a aplicação
app = Dash(__name__)

# Layout da interface
app.layout = html.Main(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=html.H1(
                        "Cotações de ontem",
                        style={
                            'color': 'white',
                            'border': '1px solid #08F7FE',
                            'border-radius': '8px',
                            'padding': '8px'
                        }
                    ),
                    style={'display': 'flex', 'justify-content': 'center'}
                ),
                html.Div(
                    children=dash_table.DataTable(
                        cotacoes.to_dict('records'),
                        id='tabela_teste',
                        style_cell={
                            'textAlign': 'center',
                            'padding': '4px',
                            'backgroundColor': '#212946',
                            'color': '#D3D6DF'
                        },
                        style_header={
                            'backgroundColor': '#333E66',
                            'fontWeight': 'bold',
                            'color': '#D3D6DF'
                        }
                    )
                )
            ],
            style={
                'background-color': 'black',
                'height': '50vh'
            }
        ),

        html.Div("Texto 2", style={'background-color': 'black', 'height': '50vh'}),
        html.Div("Texto 3", style={'background-color': 'black', 'height': '50vh'}),
        html.Div("Texto 4", style={'background-color': 'black', 'height': '50vh'})
    ],
    style={
        'display': 'grid',
        'gap': '25px',
        'grid-template-columns': 'repeat(2, 1fr)'
    }
)

# Execução
if __name__ == '__main__':
    print("🔗 Acesse o dashboard em http://127.0.0.1:8050")
    app.run(debug=True)

