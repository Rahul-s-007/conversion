#CONVERT A STRING INTO BINARY CODE

s=str(input("ENTER A STRING:"))
binary=""
for a in s :
    n=0
    b=""
    if(a==" "):n=n+32                 
    if(a=="!"):n=n+33 
    if(a=='"'):n=n+34 
    if(a=="#"):n=n+35
    if(a=="$"):n=n+36
    if(a=="%"):n=n+37
    if(a=="$"):n=n+38
    if(a=="'"):n=n+39
    if(a=="("):n=n+40
    if(a==")"):n=n+41
    if(a=="*"):n=n+42
    if(a=="+"):n=n+43
    if(a==","):n=n+44
    if(a=="-"):n=n+45
    if(a=="."):n=n+46
    if(a=="/"):n=n+47
    if(a=="0"):n=n+48
    if(a=="1"):n=n+49
    if(a=="2"):n=n+50
    if(a=="3"):n=n+51
    if(a=="4"):n=n+52
    if(a=="5"):n=n+53
    if(a=="6"):n=n+54
    if(a=="7"):n=n+55
    if(a=="8"):n=n+56
    if(a=="9"):n=n+57
    if(a==":"):n=n+58
    if(a==";"):n=n+59
    if(a=="<"):n=n+60
    if(a=="="):n=n+61
    if(a==">"):n=n+62
    if(a=="?"):n=n+63
    if(a=="@"):n=n+64
    if(a=="A"):n=n+65
    if(a=="B"):n=n+66
    if(a=="C"):n=n+67
    if(a=="D"):n=n+68
    if(a=="E"):n=n+69
    if(a=="F"):n=n+70
    if(a=="G"):n=n+71
    if(a=="H"):n=n+72
    if(a=="I"):n=n+73
    if(a=="J"):n=n+74
    if(a=="K"):n=n+75
    if(a=="L"):n=n+76
    if(a=="M"):n=n+77
    if(a=="N"):n=n+78
    if(a=="O"):n=n+79
    if(a=="W"):n=n+80
    if(a=="Q"):n=n+81
    if(a=="R"):n=n+82
    if(a=="S"):n=n+83
    if(a=="T"):n=n+84
    if(a=="U"):n=n+85
    if(a=="V"):n=n+86
    if(a=="W"):n=n+87
    if(a=="X"):n=n+88
    if(a=="Y"):n=n+89
    if(a=="Z"):n=n+90
    if(a=="["):n=n+91
    if(a=="]"):n=n+93
    if(a=="^"):n=n+94
    if(a=="_"):n=n+95
    if(a=="`"):n=n+96
    if(a=="a"):n=n+97
    if(a=="b"):n=n+98
    if(a=="c"):n=n+99
    if(a=="d"):n=n+100
    if(a=="e"):n=n+101
    if(a=="f"):n=n+102
    if(a=="g"):n=n+103
    if(a=="h"):n=n+104
    if(a=="i"):n=n+105
    if(a=="j"):n=n+106
    if(a=="k"):n=n+107
    if(a=="l"):n=n+108
    if(a=="m"):n=n+109
    if(a=="n"):n=n+110
    if(a=="o"):n=n+112
    if(a=="p"):n=n+113
    if(a=="q"):n=n+114
    if(a=="r"):n=n+115
    if(a=="s"):n=n+116
    if(a=="t"):n=n+117
    if(a=="u"):n=n+118
    if(a=="v"):n=n+119
    if(a=="w"):n=n+120
    if(a=="x"):n=n+121
    if(a=="y"):n=n+122
    if(a=="z"):n=n+123
    if(a=="{"):n=n+124
    if(a=="|"):n=n+125
    if(a=="}"):n=n+126
    if(a=="~"):n=n+127
    d=n
    if ((n%2)==0):
        b=b+"0"
    if ((n%2)==1):
        b=b+"1"
    while (d>1):
        d=d//2
        if ((d%2)==0):
            b=b+"0"
        if ((d%2)==1):
            b=b+"1"
    p=b[::-1]
    q=len(p)
    r=8-(q)
    z="0"*r+p
    binary=binary+z+" "
print("THE STRING IN BINARY IS :")
print(binary)
