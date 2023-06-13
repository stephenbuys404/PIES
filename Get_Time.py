import ntplib
import datetime, time

client = ntplib.NTPClient()
print('creating client')
try:
    response = client.request('pool.ntp.org')
    print('getting response')
    web_date_time = datetime.datetime.fromtimestamp(response.tx_time)
    print('Date and Time from the server: ',web_date_time)
except OSError:
    print('no internet connection.')