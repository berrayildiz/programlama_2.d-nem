#kullanıcı tarafından girilen hava durumunu yazdıran program

sicaklik= int(input("hava sicakligini girin :"))

if sicaklik <=5 :
    print("soğuktur")
elif sicaklik >=6 and sicaklik <=14 :
    print("iliktir")
else:
    print("sicaktir")