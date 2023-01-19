# === Informasi ===
# file.    : changeDatetime.py
# deskripsi: menyelaraskan waktu dan tanggal antara raspberry Shake 
#            dan komputer pada saat luring (offline)
# author.  : Yudha Styawan

# === Kebutuhan ===
# install paramiko di python melalui terminal/cmd dengan cara -> pip install paramiko

# === cara penggunaan ===
# langsung jalankan script ini pada python -> python changeDatetime.py
# cek di laman rs.local untuk melihat perubahannya

import paramiko
from datetime import datetime

date_now = datetime.utcnow().strftime("%d %b %Y %H:%M:%S")
command = "sudo -k date --set \"" + date_now + "\""

# Update the next three lines with your
# server's information

host = "rs.local"
username = "myshake"
password = "geofisikaitera"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout, _stderr = client.exec_command(command)
_stdin.write(password + '\n')
_stdin.flush()
print(_stdout.read().decode())
print(_stderr.read().decode())
_stdin.close()
client.close()