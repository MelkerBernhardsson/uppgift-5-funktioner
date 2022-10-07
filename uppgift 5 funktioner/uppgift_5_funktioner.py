def nettopris(tal1):
    
    if tal1 < 500:
        brutto = tal1*1
        print("ditt pris", brutto)
    
    elif tal1 > 500 and tal1 < 1000:
        brutto = tal1*0.98
        print("ditt pris", brutto)
    
    elif tal1 >= 1000 :
        brutto = tal1*0.95
        print("ditt pris", brutto)
    return(brutto)

a=int(input("vad ar priset?? "))

nettopris(a)

