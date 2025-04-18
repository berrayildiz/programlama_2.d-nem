#kullanıcı tarafından girilen süreyi yazdıran program
süre= int(input("süreyi girin:"))

if süre == 1:
    print("5 tl")
elif süre <=5 :
    print("ödeme",süre*4)
else:
    print("ödeme",süre*3)