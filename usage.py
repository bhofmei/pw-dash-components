import dash_pairwise
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div([
	dcc.Input(id='input'),
    dash_pairwise.CopyButton(
        id='btn',
        value='my-value',
        children='Copy'
    ),
    html.Div(id='output')
])


@app.callback(Output('btn', 'value'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)

@app.callback(Output('output', 'children'),[Input('btn', 'n_clicks')])
def click_btn( n_clicks ):
	if n_clicks == None or n_clicks == 0:
		return ''
	return 'Copied'

if __name__ == '__main__':
    app.run_server(debug=True)
