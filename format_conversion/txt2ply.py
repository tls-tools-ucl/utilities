import sys
import pandas as pd
import ply_io

for txt in sys.argv[1:]:

    line = open(txt).readline()
    if ',' in line:
        sep = ','
    else: sep = ' '

    if 'x' in line or 'X' in line or '//X' in line:
        cols = line.strip().lower().split(sep)
        skiprows = 1
        if '//x' in cols: 
            cols = [c if c != '//x' else 'x' for c in cols]
            cols = [c if ',' not in c else '_'.join(c.split(',')) for c in cols]
            skiprows=1
    else:
        print('no header: estimating fields')
        line = line.split(sep)
        cols = ['x', 'y', 'z']
        [cols.append('v{}'.format(i)) for i in range(len(line) - 3)]
        skiprows=0

    
    df = pd.read_csv(txt, skiprows=skiprows, sep=sep, names=cols)
    ply_io.write_ply(txt[:-4] + '.ply', df)
