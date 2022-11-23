#!/usr/bin/env python3
import heapq
import sys
import argparse

parser = argparse.ArgumentParser(
    prog = "nheap",
    description = "Emit the top N smallest/largest items on stdin",
    epilog = "Similar to `... | sort | head -n` without needing "
        "to sort the whole thing",
    )

parser.add_argument(
    "-n",
    type=int,
    default=10,
    help="How many to emit",
    )

parser.add_argument(
    "--largest",
    action="store_true",
    default=False,
    help="Find the N largest rather than the N smallest",
    )

args = parser.parse_args()

if args.largest:
    fn = heapq.nlargest
else:
    fn = heapq.nsmallest

h = fn(args.n, sys.stdin)

for k in h:
    print(k, end="")
