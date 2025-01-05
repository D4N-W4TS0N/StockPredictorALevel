from visualiser import Visualiser
from datetime import date
from dateutil.relativedelta import relativedelta



# Sets the ticker (unique stock ID - in this case AAPL for Apple Inc)
ticker = 'AAPL'

# Fetches current date
currentDate = date.today()
# Changes date to string format
endDate = currentDate.strftime('%Y-%m-%d')
# Finds the start date - in this case 2 months ago
startDate = (currentDate - relativedelta(years=5)).strftime('%Y-%m-%d')

# initialises the __init__ method for the visualiser class, passing in the chosen ticker and start/end dates
appleVisualiser = Visualiser(ticker)
appleVisualiser.visualise(startDate, endDate)