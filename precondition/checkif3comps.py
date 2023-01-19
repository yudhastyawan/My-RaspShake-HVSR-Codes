import obspy as ob

st = ob.read("test_vel_non_lempeng.mseed")
if len(st) > 3:
    print(f"data memiliki {len(st)} komponen > 3 komponen")
    print(f"menggabungkan data . . . ")
    st.merge(fill_value='interpolate')
    st.write("test_vel_non_lempeng_merge_2.mseed", format="MSEED")
    print(f"selesai")
else:
    print("data memiliki 3 komponen")
    print(f"selesai")