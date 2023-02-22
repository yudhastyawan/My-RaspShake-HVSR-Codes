import obspy as ob
import glob
from pathlib import Path
import os

file_output = "HV70.mseed"

dir_file = Path(__file__).parent

filenames = glob.glob(os.path.join(dir_file, "*.msd"))
st = None
for filename in filenames:
    if st == None:
        st = ob.read(filename)
    else:
        st += ob.read(filename)

st.write(os.path.join(dir_file, file_output), format="MSEED")