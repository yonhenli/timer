# import packages
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import mlab
import matplotlib.pyplot as plt
from scipy import stats
sns.set(color_codes=True)

filename_host = "d12/run_2/host.txt"
filename_did = "d12/run_2/did.txt"
filename_vanilla = "d12/run_2/vanilla.txt"

def parse(filename):
	i = 0
	ret = []

	file = open(filename, "r")
	lines = file.read()
	lines = lines.split('\n')

	for line in lines:
		tokens = line.split()
		if len(tokens) == 9:
			ret.append((int(tokens[8])*1.0)/1000)
		i += 1

	return ret

host_ltc = np.array(parse(filename_host))
did_ltc = np.array(parse(filename_did))
vanilla_ltc = np.array(parse(filename_vanilla))

pct_10 = np.percentile(did_ltc, 10)
pct_25 = np.percentile(did_ltc, 25)
pct_50 = np.percentile(did_ltc, 50)
pct_75 = np.percentile(did_ltc, 75)
pct_99 = np.percentile(did_ltc, 99)
min_ = min(did_ltc)
max_ = max(did_ltc)

# print(host_ltc + '\n')
print("10 %: " + str(pct_10))
print("25 %: " + str(pct_25))
print("50 %: " + str(pct_50))
print("75 %: " + str(pct_75))
print("99 %: " + str(pct_99))
print("min: " + str(min_))
print("max: " + str(max_))

plt.figure()
sns.kdeplot(host_ltc,cumulative=True, color="r", label="Host")
sns.kdeplot(did_ltc,cumulative=True, color="b", label="DID")
sns.kdeplot(vanilla_ltc,cumulative=True, color="y", label="Vanilla")
plt.xlabel('us', fontsize=10)
plt.show()
