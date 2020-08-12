# import packages
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

sns.set(color_codes=True)

def plot_graph(filename):
	ret = []
	
	file = open(filename, "r")
	lines = file.read()
	lines = lines.split('\n')
	
	i = 0
	for line in lines:
			tokens = line.split()
			ret.append(tokens[8])

	return ret

filename = "host.txt"
lines = plot_graph(filename)
print(lines)
