import numpy as np
import pandas as pd
import sys
import argparse
import glob
from ply_io import read_ply

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ply', nargs='*', default=glob.glob('*.ply'), help='list of ply files')
    parser.add_argument('-s', '--sep', nargs=1, default=',', help='specify separator')
    parser.add_argument('--xyz', action='store_true', help='export only xyz columns')
    args = parser.parse_args()

    for pc in args.ply:
    
        df = read_ply(pc)
        cols = df.columns
        if args.xyz: cols = ['x', 'y', 'z']
        df[cols].to_csv(pc.replace('.ply', '.txt'), sep=args.sep[0], index=False, header=False)
