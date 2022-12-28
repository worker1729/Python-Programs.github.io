import segno
code = segno.make("https://www.youtube.com")
code.save("QRcode.png", scale=15, light="lightblue", dark="green")
