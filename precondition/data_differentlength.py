import obspy as ob

file_input = "GMJI.mseed"
file_output = "GMJI_fix.mseed"

st = ob.read(file_input)

starttime = max([tr.stats.starttime for tr in st])
endtime = min([tr.stats.endtime for tr in st])

st2 = st.slice(starttime, endtime)
st2.write(file_output, format="MSEED")