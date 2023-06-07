# A Pandas generated animation of the effects of increasing the window size of a rolling mean 

An example of rolling mean on a pandas dataframe, animated to help you see the effects.

We take the Apple closing share price for the last 40 years, and apply a rolling mean. We then animate with increasing values of the Window size for the rolling mean.

![Graph of apple price is gradually smoothed](apple_stock_price_smoothing_animation.gif)

(Depending on your connection speed, this may take a few seconds to load.)


## How do I run this code?

Using a recent version of python 3.x, open your terminal and enter this:

```bash
python apple_rolling_mean_anim_graph.py
```

The system will then create the frames and compile the animation.
Your output might look like this:

```bash
MovieWriter ffmpeg unavailable; using Pillow instead.
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
```

etc.

If all is well then you will see a new copy of the .gif image used in this README (the picture above).
