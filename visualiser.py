import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime



class Visualiser():
    def __init__(self, ticker: str):
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

    def visualise(self, startDate: str, endDate: str):
        self._startDate = startDate
        self._endDate = endDate
        self._url = 'https://api.tiingo.com/tiingo/daily/'+self._ticker+'/prices?startDate='+startDate+'&endDate='+endDate+'&format=json&token=6b5b8a37e5a7749d1748ce6496258cc48c9deb9b&resampleFreq=daily'
        self.load()
        # Declares a list of x and y coordinates
        xpoints = []
        ypoints = []

        for day in self._data:
            closingPrice = day['adjClose']
            date_str = day['date'][0:10]
            # Converts the string date from JSON to datetime format
            date_float = datetime.strptime(date_str, '%Y-%m-%d')
            # Date is returned in datetime format - we do not need the time
            xpoints.append(date_float)
            ypoints.append(float(closingPrice))


        # Converts the list to numpy arrays
        xpoints = np.array(xpoints)
        ypoints = np.array(ypoints)

        self.plot5y(xpoints, ypoints)

    def plot1w(self, xpoints: np.ndarray, ypoints:np.ndarray):
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
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

        plt.show()

    def plot6m(self, xpoints: np.ndarray, ypoints: np.ndarray):
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
        # Shows months at bottom with 1 month intervals and formats so only year and month shown
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

        plt.show()

    def plot1y(self, xpoints: np.ndarray, ypoints: np.ndarray):
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
        # Shows months at bottom with 1 month intervals and formats so only year and month shown
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

        plt.show()

    # Plot year to date (1st Jan ->)
    # def plotytd(self, xpoints: np.ndarray, ypoints: np.ndarray):
    #     # Creates a figure and axes objects
    #     fig, ax = plt.subplots()

    #     # Plots the points on the axes
    #     ax.plot(xpoints, ypoints)
    #     # Sets a title above the graph
    #     ax.set_title(self._ticker + ' Closing Stock Price ' + self._startDate + ' to ' + self._endDate)

    #     # Sets a global formatter on the y-axis, rounding to 2dp and adding a dollar sign
    #     ax.yaxis.set_major_formatter('${x:1.2f}')
    #     ax.yaxis.set_tick_params(which='major')

    #     # Rotates the x-axis values to fit in
    #     ax.tick_params(axis='x', labelrotation=45)
    #     # Shows months at bottom with 1 month intervals and formats so only year and month shown
    #     ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    #     ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    #     plt.show()

    def plot5y(self, xpoints: np.ndarray, ypoints: np.ndarray):
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
        # Shows months at bottom with 1 month intervals and formats so only year and month shown
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=10))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

        plt.show()
