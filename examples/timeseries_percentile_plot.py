"""
Timeseries percentile distribution plot
=======================================

"""

import seaborn as sns

fmri = sns.load_dataset("fmri").query("region == 'parietal'")

p = so.Plot(fmri, "timepoint", "signal")
for tail in [25, 10, 5, 1]:
    p = p.add(so.Band(), so.Perc([tail, 100 - tail]))
p.add(so.Line(), so.Agg("median"))
