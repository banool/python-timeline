# Python timeline

This is some code for producing a timeline. The data manipulation is Python,
while the actual timeline is made using [vis.js](http://visjs.org/timeline_examples.html). 

The code in `loader.py` is used for importing and exporting data from various
formats. Some of those functions are quite dirty and should be used with
caution.

Run `python3 timeline.py > data.js` and then open `timeline.html` for an
example. The code in `timeline.py` validates the data first before trying
to produce the output. One of the main requirements is that the each Duration
item's end date has to be the day before the start date of the next Duration.
See `example.py` for an example, obviously...