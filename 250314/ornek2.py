#kullanıcı adı turkiye ve şifresi 1923
# ise "giriş başarılı"
# değilse "kullanıcı adı ya da şifre hatalı"

#kullanıcıdan bilgi alma
kad=input("kullanıcı adını girin")
ksifre=input("kullanıcı sifresini girin")


if kad == "türkiye" and ksifre == "1923" :
    print("giriş başarılı")
else:
    print("kullanıcı adı ya da şifre yanlış")