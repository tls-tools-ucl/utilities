import sys
import numpy as np

from cyl2ply import pandas2ply
from mat2qsm import QSM

for mat in sys.argv[1:]:

	print 'processing:', mat
	qsm = QSM(mat)
	
	pandas2ply(qsm.cyl2pd()[['length', 'radius', 'sx', 'sy', 'sz', 'ax', 'ay', 'az']], 
			   'length', 
			   mat.replace('.mat', '.ply')) 
