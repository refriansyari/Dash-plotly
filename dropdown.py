import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import requests, base64
from io import BytesIO

#declare dash_app
app = dash.Dash()

#change image format to BIT (binary)
def encode_image(image_url):
    buffered = BytesIO(requests.get(image_url).content)
    image_base64 = base64.b64encode(buffered.getvalue())
    return b'data:image/png;base64,' + image_base64

#create layout in html page
app.layout = html.Div([
    dcc.Dropdown(id='my-dropdown',
                    options=[
                        {'label': 'Jakarta', 'value': 'JKT'},
                        {'label': 'Bandung', 'value': 'BDG'},
                        {'label': 'Surabaya', 'value': 'SBY'}],
                
            value='JKT',
            placeholder ='Please Select a City !'
                        ),
    html.Div(id='output-container')

])

@app.callback(
    Output('output-container','children'),
    [Input('my-dropdown', 'value')])

#encoding image (src=links)
def update_output(value):
    JKT_img = encode_image('https://assets.pikiran-rakyat.com/crop/0x0:0x0/x/filters:watermark(file/2017/cms/img/watermark.png,-0,0,0)/photo/2020/04/13/682906642.jpg')
    BDG_img = encode_image('https://cdn.britannica.com/88/132688-050-E9739DD9/Skyline-Jakarta-Indonesia.jpg')
    SBY_img = encode_image('https://upload.wikimedia.org/wikipedia/commons/5/57/Western_Surabaya_at_dusk_%28late_2015%29.jpg')

    if value == 'JKT':
        return html.Div(html.Img(src=JKT_img.decode(), style={'width':'500px', 'height': '100%'}))
    elif value == 'BDG':
        return html.Div(html.Img(src=BDG_img.decode(), style={'width':'500px', 'height': '100%'}))
    elif value == 'SBY':
        return html.Div(html.Img(src=SBY_img.decode(), style={'width':'500px', 'height': '100%'}))

#inisiate DASH-DASHBOARD
if __name__ == '__main__':
    app.run_server(debug=True)