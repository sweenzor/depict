# Depict

### Pipe to graph 

## What is?

Pipe streams of data to depict, and they'll be plotted in real time

## Examples

`python monitorconsumer.py | awk -W interactive '{ print $6 $7 }' | python /home/matt/Development/depict/plotter.py`

## Notes

The program 'unbuffer' may be useful
It can be installed with:
`sudo apt-get install expect-dev`
