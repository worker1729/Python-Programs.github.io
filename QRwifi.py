from segno import helpers
qrCode = helpers.make_wifi(ssid="MyWifi", password="1234567890", security="WPA")
qrCode.designator
"3-M"
qrCode.save("wifi-access.png", scale=10)
