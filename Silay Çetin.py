import random

print("Taş Kağıt Makas oynamaya hazır mısın?")
print("Hazırsan hemen oyun açıklamasıyla başlayalım!\n")
print("<AÇIKLAMA>")
print("Oyun üç farklı seçenek sunuyor. Karşılıklı aynı anda taş kağıt ya da makas işaretini seçerek oynanıyor.")
print("Başlıca kurallar şu şekilde: \n-Taş, makası yener.\n-Makas, kağıdı yener.\n-Kağıt, taşı yener.\n-İlk iki turu kazanan oyunu kazanır.\n-Berabere durumunda sayı verilmez, tekrar oynanır.\n")
print("Oyundan çıkmak için tur bitiminde hayır cevabını yazman yeterli.\n BOL ŞANSLAR!\n")

def tas_kagit_makas_SİLAY_ÇETİN():
    choices = ['Taş', 'Kağıt', 'Makas']
    user_score = 0
    computer_score = 0
    tur = 0  
    
    while True:
        print("////////////////////////////////////////////")
        tur += 1  
        print(f"Tur {tur}:")  
        
        # Kullanıcının seçimi
        user_choice = input("Taş, Kağıt veya Makas? : ")
                
        if user_choice not in choices:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
            tur -= 1  # Geçersiz seçimde tur sayısını artırma
            continue
        
        # Bilgisayarın seçimi
        computer_choice = random.choice(choices)
        
        print(f"Senin seçimin: {user_choice}")
        print(f"Bilgisayarın seçimi: {computer_choice}")
        
        # Oyun sonucu
        if user_choice == computer_choice:
            print("Berabere! Tekrar deneyin.")
        elif (
            (user_choice == 'Taş' and computer_choice == 'Makas') or
            (user_choice == 'Kağıt' and computer_choice == 'Taş') or
            (user_choice == 'Makas' and computer_choice == 'Kağıt')
        ):
            user_score += 1
            print(f"Puan Durumu: Sen {user_score} - {computer_score} Bilgisayar")
        else:
            computer_score += 1
            print(f"Puan Durumu: Sen {user_score} - {computer_score} Bilgisayar")
        
        # Oyunun bitiş durumu
        if user_score == 2 or computer_score == 2:
            if user_score == 2:
                print("Tebrikler! Bu turu kazandınız.")
            else:
                print("Üzgünüm! Bu turu kaybettiniz.")
            
            # Devam mı tamam mı?
            devam = input("Oyuna devam etmek istiyor musunuz? evet, hayır : ")
            cevap=["evet","hayır"]
            if devam.lower() == "evet":
                user_score = 0
                computer_score = 0
                tur = 0

                bilgisayar=random.choice(cevap)
                if bilgisayar=="evet":
                  tas_kagit_makas_SİLAY_ÇETİN()
                else:
                  print("Bilgisayar 'hayır' cevabını seçti.")
                  print("Oyun bitti!")
                  break;
            else:
                print("Oyun bitti!")
                break;

tas_kagit_makas_SİLAY_ÇETİN()