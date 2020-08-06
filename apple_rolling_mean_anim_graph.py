import matplotlib.animation as animation
import pandas as pd
import matplotlib.pyplot as plt


apple_data_file_name = "macrotrends_apple_40years.csv"
window_size = 1

apple_history_df = pd.read_csv(apple_data_file_name)

apple_history_df['avg_close'] = apple_history_df['close'].rolling(window_size).mean()
apple_history_df['date'] = pd.to_datetime(apple_history_df.date)

dates = apple_history_df.date
closes = apple_history_df.close
avg_closes = apple_history_df.avg_close

fig = plt.figure(figsize=(10, 4))
ax = fig.add_subplot(111)
ax.set_xlabel('Year')
ax.set_ylabel('US$')

line, = ax.plot(dates, avg_closes)
title = ax.text(0.4, 0.85, "", transform=ax.transAxes, ha="center")


def init():
    line.set_data(dates, avg_closes)
    return line,


def animate(w_size):
    print(w_size)
    apple_history_df['avg_close'] = apple_history_df['close'].rolling(w_size).mean()
    line.set_data(dates, apple_history_df['avg_close'])
    title.set_text(f"Apple closing stock price, rolling mean. Moving window size: {w_size} days")

    return line, title


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=260, interval=50, blit=True)
anim.save('apple_stock_price_smoothing_animation.gif', fps=10)
