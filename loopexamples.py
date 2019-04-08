#Bir tekstil firmasında pantolon üretimi yapılmaktadır. Günlük 200 pantolon üretilmekte olup her gün belirli sayıda defolu ürün çıkmaktadır.
#Buna göre günlük defolu ürün sayısı kullanıcı tarafından girilecektir.
#Günlük Defolu ürün sayısı günlük üretilen ürün sayısının yüzde 20 sinden fazla olduğunda ise firmaya uyarı yapılacaktır.
#Buna göre defolu ürün oranı yüzde 20 den az olduğu sürece toplam defolu ürün sayısını ve kaç günlük defolu ürün sayısı olduğunu hesaplayan python kodunu yazınız.

gunlukPant=200
gunlukDefo=0
toplamDefo=0
i=0
while (gunlukDefo<=gunlukPant*0.20):
    gunlukDefo=int(input("Günlük defolu ürün miktarı:"))
    toplamDefo=toplamDefo+gunlukDefo
    i+=1
    if gunlukDefo>=gunlukPant*0.20:
        print("Günlük defolu ürün sınırını aştınız.")
        break
    print(i,"günlük defolu ürün sayısı:",toplamDefo)

###################################################

#YBS isimli bir firmada 50 çalışan vardır ve personelin haftalık toplam 40 saat çalışma süresi bulunmaktadır.
#40 saatten sonra yapılan her mesai için saat başına yevmiyenin yüzde 10 u kadar ücret verilmektedir.
#Ancak YBS firması aylık 22 saatten fazla mesai olmayacak şekilde maaşları hesaplamaktadır.Bir çalışanın günlük yevmiyesi 90 TL dir.
#Buna göre haftalık mesai saati kullanıcı tarafından girilerek aylık personele ödenen toplam maaşı aylık mesai saati 22 den azolduğu sürece hesaplayan python kodunu yazınız.

calisan=50
yevmiye=90
haftalikyevmiye=630
aylikmesai=0
aylikmaas=0
while(aylikmesai<=22):
    haftalikmesai=int(input("Haftalık Mesai:"))
    aylikmesai=haftalikmesai*4
    haftalikyevmiye=haftalikyevmiye+(haftalikmesai*yevmiye*0.10)
    aylikmaas=aylikmaas+haftalikyevmiye*4
    print("Aylık maaş:",aylikmaas)
else:
    print("Aylık mesai 22 saatten fazla olamaz")
    exit()



######################################################


#Klavyeden 0(sıfır) sayısı girilinceye kadar klavyeden kullanıcı tarafından girilen sayıların 3 ile bölümünden kalanı toplayan python kodunu yazınız.

toplam=0
while True:
    print("Bir sayi giriniz/Çıkış için '0' ")
    girilen=int(input("Sayi:"))
    if girilen !=0:
        kalan=girilen%3
        toplam=toplam+kalan
        print("Toplam=",toplam)
    else:
        print("Çıkış yapıldı")
        break
        
        
        ##############################################
#Bir işletmenin 2017 yılı stok miktarı 10000 adettir.
#Her ay 500 adet ürün satılıp 100 adet yeni ürün alınmaktadır. Buna göre bu işletmenin stoklarının sıfırlanması kaçıncı ayda olacaktır?

stokMiktarı=10000
ay=0
alinanürün=100
satilanürün=500
fark=alinanürün-satilanürün
while (stokMiktarı>0):
    stokMiktarı=stokMiktarı+fark
    ay+=1

print("Stoklarınız",ay,"ay sonra sıfırlanacaktır!")
