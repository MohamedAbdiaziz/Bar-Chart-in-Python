# this program displays a sales chart.

import matplotlib.pyplot as plt


def main():
    

    #create a list with the X coordinates of each bar,
    left_edge = [0, 10, 20, 30 , 40]

    # create a list with the height of each bar
    height = [100, 200, 300, 400, 500]

    # create a variable for the bar width
    bar_width = 10

    # build the bar chart
    plt.bar(left_edge, height, bar_width, color=('r','g','b','k','r'))

    # add a title
    plt.title('Sales by Year')

    # add labels to the axes
    plt.xlabel('Year')
    plt.ylabel('Sales')

    # customize the tick marks
    plt.xticks([5, 15, 25, 35, 45],
                [2018,2019,2020,2021,2022])
    plt.yticks([0, 100, 200, 300, 400, 500],
                ['$0m','$1m','$2m','$3m','$4m', '$5m'])
            

    plt.show()


main()