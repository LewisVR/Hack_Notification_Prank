from winotify import Notification, audio

toast = Notification(
    app_id = "⚠️ Windows Güvenlik Duvarı", # Başlık
    title = "Bilgisayarınız Hacklendi!", # Metin
    msg = "Hacker Sizinle iletişime geçmek istiyor lütfen tıklayınız!", #Alt metin
    duration = "long", #Uyarının süresini ayarlıyoruz.
    icon =r"C:\Users\Lewis\Desktop\notification\ico\uyari.ico")
   # ico dosyasının tam adresini girmek zorundasınız
   # Yoksa uyari resmi çıkmaz

toast.add_actions(label = "Tıkla", # Buton
                  launch="https://github.com/LewisVR") # Butona basıldığında açılacak site linki
toast.set_audio(audio.Reminder, loop=False)
toast.show()
