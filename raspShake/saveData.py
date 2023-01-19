# === Informasi ===
# file.    : saveData.py
# deskripsi: mengunduh data seismogram pada kasus data kurang dari 1 hari di raspberry Shake 
# author.  : Yudha Styawan

# === Kebutuhan ===
# install obspy di python melalui terminal/cmd dengan cara -> pip install obspy

# === cara penggunaan ===
# lihat apa saja yang diubah pada beberapa deskripsi di bawah

# === cek ketersediaan data pada seismometer ===
# UBAH RCA8F ke kode stasiun (lihat di laman rs.local -> lihat nilai x di AM.xxxxx)
# UBAH EHZ sesuai dengan tipe rekaman, accelerometer -> ENZ, seismometer velocity -> EHZ
from obspy.clients.earthworm import Client
client = Client("rs.local", 16032)
response = client.get_availability('AM', 'RCA8F', channel='EHZ')
print(response)

# === unduh data pada seismometer ===
# UBAH 2023-01-11T08:10:00 ke dalam waktu awal
# UBAH 2023-01-11T08:40:00 ke dalam waktu akhir
# UBAH RCA8F ke kode stasiun (lihat di laman rs.local)
# UBAH EH* sesuai dengan tipe rekaman, accelerometer -> EN*, seismometer velocity -> EH*
# UBAH test_vel_non_lempeng.mseed ke target nama file yang diinginkan
from obspy import UTCDateTime
ti = UTCDateTime("2023-01-11T08:10:00")
tf = UTCDateTime("2023-01-11T08:40:00")
st = client.get_waveforms('AM', 'RCA8F', '00', 'EH*', ti, tf)
print(st)
st.plot()
st.write("test_vel_non_lempeng.mseed", "MSEED")