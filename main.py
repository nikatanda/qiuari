import qrcode

# ჩანაცვლეთ ბმული HTML ფაილის URL-ით
html_page_link = " https://nikatanda.github.io/qiuari/"

# ქიუარ კოდის გენერაცია
qr = qrcode.make(html_page_link)

# ქიუარ კოდის ჩვენება ეკრანზე
qr.show()

# ქიუარ კოდის შენახვა
qr.save("audio_qr_code.png")
