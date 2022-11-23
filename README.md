# nheap
Find the N largest/smallest items on stdin.
Acts similar to

    $ ... | sort | head -n

or

    $ ... | sort -r | head -n

without needing to sort all of `stdin`.


## Usage

Find the 10 smallest items

    $ nheap < file.txt

Find the 10 largest items

    $ nheap --largest < file.txt

Find the 5 smallest items

    $ nheap -n 5 < file.txt

Find the 5 largest items

    $ nheap -n 5 --largest < file.txt

Get help:

    $ nheap --help
    usage: nheap [-h] [-n N] [--largest]

    Emit the top N smallest/largest items on stdin

    optional arguments:
      -h, --help  show this help message and exit
      -n N        How many to emit
      --largest   Find the N largest rather than the N smallest
