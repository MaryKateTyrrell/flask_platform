import SYSINFOTEST
from app import app
from SYSINFOTEST import main
 
@app.route('/')

def display_info():
	return "The platform  is " + main.main()
