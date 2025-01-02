import requests
import numpy as np
import matplotlib.pyplot as plt

class Visualiser():
    def __init__(self, ticker:str):
        self._ticker = ticker
        self._startDate = None
        self._endDate = None
        self._data = None
        self._url = None
        # self._tempURL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'

    def load(self):
        # Requests the Stock Price data from the URL above (TIINGO API)
        r = requests.get(self._url)
        self._data = r.json()
        # print(data)

    def visualise(self, startDate, endDate):
        self._startDate = startDate
        self._endDate = endDate
        self._url = 'https://api.tiingo.com/tiingo/daily/'+self._ticker+'/prices?startDate='+startDate+'&endDate='+endDate+'&format=json&token=6b5b8a37e5a7749d1748ce6496258cc48c9deb9b&resampleFreq=daily'
        self.load()
        # Declares a list of x and y coordinates
        xpoints = []
        ypoints = []

        for day in self._data:
            closingPrice = day['adjClose']
            date = day['date']
            # Date is returned in datetime format - we do not need the time
            xpoints.append(date[0:10])
            ypoints.append(float(closingPrice))


        # Converts the list to numpy arrays
        xpoints = np.array(xpoints)
        ypoints = np.array(ypoints)

        self.plot(xpoints, ypoints)

    def plot(self, xpoints, ypoints):
        # Creates a figure and axes objects
        fig, ax = plt.subplots()

        # Plots the points on the axes
        ax.plot(xpoints, ypoints)
        # Sets a title above the graph
        ax.set_title(self._ticker + ' Closing Stock Price ' + self._startDate + ' to ' + self._endDate)
        # Sets a global formatter on the y-axis, rounding to 2dp and adding a dollar sign
        ax.yaxis.set_major_formatter('${x:1.2f}')
        ax.yaxis.set_tick_params(which='major')
        # Rotates the x-axis values to fit in
        ax.tick_params(axis='x', labelrotation=45)
        plt.show()
