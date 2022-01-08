from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    
    items = [
    {'id': 1, 'Country': 'India', 'Name': 'Nifty 50', 'price': 'niftyval'},
    {'id': 2, 'Country': 'India', 'Name': 'Sensex', 'price': 'sensexval'},
    {'id': 3, 'Country': 'USA', 'Name': 'S&P 500', 'price': 'snpval'},
    {'id': 4, 'Country': 'USA', 'Name': 'Dow Jones', 'price': 'dawval'},
    {'id': 5, 'Country': 'Worldwide', 'Name': 'BTC', 'price': 'btcval'},
    {'id': 6, 'Country': 'Worldwide', 'Name': 'ETH', 'price': 'ethval'}
    ]
    return render_template('markets.html', items=items)