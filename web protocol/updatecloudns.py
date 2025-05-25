


import requests as s


print(s.get("https://ipv4.cloudns.net/api/dynamicURL/?q=OTQ3NTAwMTo2MDQzMjM2NDE6MmEwM2RmYzMyY2Y4ZWU4NWMyNzhkZjJkNzMyZWM4ZTM1MDQ5ODY0ZjdlYTU2NWQ2NjEwMWUzZGU1MDMwMzFiMg").text)



"""
If you are behind proxy and your real IP is set in the header X-Forwarded-For you need to add &proxy=1 at the end of the DynamicURL.
If you need to set your IP address in the request, instead our system to use the IP address from where you are making the request, you can add following parameter in the URL:
&ip=<custom-ip>
If you want to receive e-mail notifications for the changes made by DynamicURL, you can use following extra parameter in the URL:
&notify=1
If you want to update the Main IP of the Failover check (if such is activated for the record), you can use following extra parameter in the URL:
&update_fo_main_ip=1
"""