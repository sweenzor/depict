# Depict

### Pipe to graph 

## What is?

Pipe streams of data to depict, and they'll be plotted in real time
Alias the script like so:

`alias depict='python -u /home/depict/plotter.py'`

## Examples

`python -u monitor.py | awk -W interactive '{ print $2, $4 }' | depict`

Transforms something like this:

![raw](https://github.com/mattswe/depict/wiki/plot1.png)

Into this:

![plot](https://github.com/mattswe/depict/wiki/plot2.png)


## Notes

At the moment, depict is a wrapper around gnuplot,
which can be installed like this:

`brew install gnuplot`

or

`sudo apt-get install gnuplot'
