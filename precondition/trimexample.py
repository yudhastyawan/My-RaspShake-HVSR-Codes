import obspy as ob 
from obspy import UTCDateTime

st = ob.read("test_vel_non_lempeng.mseed")

if len(st) > 3:
    print(f"data memiliki {len(st)} komponen > 3 komponen")
    print(f"menggabungkan data . . . ")
    st.merge(fill_value='interpolate')
else:
    print("data memiliki 3 komponen")

# lihat data
st.plot()

# Hilangkan data dari 2023-01-11T08:27:31 hingga 2023-01-11T08:27:51
d1 = UTCDateTime("2023-01-11T08:27:31")
d2 = UTCDateTime("2023-01-11T08:27:51")
di = st[0].stats.starttime
df = st[0].stats.endtime
st1 = st.copy()
st1.trim(di,d1)
st2 = st.copy()
st2.trim(d2,df)
st1 += st2
st1.merge(fill_value='interpolate')

#lihat data hasil trim
st1.plot()

# simpan
st1.write("test_vel_non_lempeng_merge.mseed", format="MSEED")