# Depict

### Pipe to graph 

## What is?

Pipe streams of data to depict, and they'll be plotted in real time
Alias the script like so:
`alias depict='python -u /home/matt/Development/depict/plotter.py'`

## Examples

`python -u monitor.py | awk -W interactive '{ print $6 $7 }' | depict`

Transforms something like this:
[image of monitor.py output]

Into this:
[image of depict output]


## Notes

At the moment, depict is a wrapper around gnuplot,
which can be installed like this:

`sudo apt-get install gnuplot'
