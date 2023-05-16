import matplotlib.animation as animation
import pandas as pd
import matplotlib.pyplot as plt


# The function that will be called at the beginning of the animation
# it will set the initial line and title
def init():
    """
    :return: the initial line and title
    """
    line.set_data(dates, avg_closes)
    return line,


# The function that will be called at each frame and will update the plot
# w_size is the window size of the rolling mean
# it is increased by 1 at each frame as the animation progresses
# to increase the window size by a greater amount, change the interval parameter
# it is set to 50 milliseconds in this example
def animate(w_size):
    """
    :param w_size: window size of the rolling mean
    :return: the updated line and title
    """
    print(w_size)
    apple_history_df['avg_close'] = apple_history_df['close'].rolling(w_size).mean()
    line.set_data(dates, apple_history_df['avg_close'])
    title.set_text(f"Apple closing stock price, rolling mean. Moving window size: {w_size} days")

    return line, title


if __name__ == '__main__':

    apple_data_file_name = "macrotrends_apple_40years.csv"
    window_size = 1

    apple_history_df = pd.read_csv(apple_data_file_name)

    apple_history_df['avg_close'] = apple_history_df['close'].rolling(window_size).mean()
    apple_history_df['date'] = pd.to_datetime(apple_history_df.date)

    dates = apple_history_df.date
    closes = apple_history_df.close
    avg_closes = apple_history_df.avg_close

    # create the figure and axes
    fig = plt.figure(figsize=(10, 4))
    ax = fig.add_subplot(111)
    ax.set_xlabel('Year')
    ax.set_ylabel('US$')

    line, = ax.plot(dates, avg_closes)
    title = ax.text(0.4, 0.85, "", transform=ax.transAxes, ha="center")

    # the init function is called at the beginning of the animation
    # the animate function is called at each frame
    # the frames parameter is the number of frames in the animation
    # the interval parameter is the delay between frames in milliseconds
    # the blit parameter is set to True to only redraw the parts that have changed
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=260, interval=50, blit=True)
    anim.save('apple_stock_price_smoothing_animation.gif', fps=10)
