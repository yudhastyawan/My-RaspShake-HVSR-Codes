"""
Created by: Yudha Styawan

Reference to Guralp 6TD instrument response:
https://www.geo.uib.no/seismo/SOFTWARE/SEISAN/OTHER_MANUALS/seisan_volcano.pdf
"""

# %%
import obspy as ob
from obspy.signal import PPSD
from obspy.imaging.cm import pqlx
# %%
paz = {'gain': 491883573.0,
       'poles': [-1.486E-1+1.486E-1j, -1.486E-1-1.486E-1j,
                 -2.469E+03+0j, -4.706E+01+0j,
                 -3.368E+02-1.367E+02j, -3.368E+02+1.367E+02j],
       'sensitivity': 3832000.0 * 1125.1,
       'zeros': [-31.6+0j, 0j, 0j]}

# %%
st = ob.read('*.msd')

# %%
tr = st[0]
ppsd = PPSD(tr.stats, metadata=paz,
            ppsd_length=1*60, period_limits=[0.05, 100])
ppsd.add(st)
print(len(ppsd.times_processed))
ppsd.plot(period_lim=(0.05, 100), cmap=pqlx)

# %%
