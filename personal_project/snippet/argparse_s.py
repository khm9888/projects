# https://bre.is/Q3BrmHJd

# pip install argparse

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--id',
    required=False,
    help='USer ID',default=1
    )

args = parser.parse_args()
# args.id = ??
print(args.id)