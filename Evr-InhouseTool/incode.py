import numpy as np
import csv

f = open('./ui/evr_base.py', 'w', encoding='utf-8')
csv.writer(f, delimiter='\t')

f.close()