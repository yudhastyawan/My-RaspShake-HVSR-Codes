import obspy as ob

file_input = "T1.mseed"
file_output = "T1_3comps.mseed"

st = ob.read(file_input)
if len(st) > 3:
    print(f"data memiliki {len(st)} komponen > 3 komponen")
    print(f"menggabungkan data . . . ")
    st.merge(method=1, interpolation_samples=-1, fill_value='interpolate')
    st.write(file_output, format="MSEED")
    print(f"selesai")
else:
    print("data memiliki 3 komponen")
    print(f"selesai")
