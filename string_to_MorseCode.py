#STRING TO MORSE CODE
#INTERTIONAL MORSE CODE
#DOT IS 1 UNIT
#DASH IS 3 UNITS
#SPACE BETWEEN LETTERS 3 UNITS
#SPACE BETWEEN WORDS 7 UNITS

print("STRING TO MORSE CODE CONVERTER (INTERTIONAL SYSTEM)")
print("")
s1=str(input("ENTER A STRING:"))
s=s1+" "
code=""
word=""

for a in s:
    if(a!=" "):
        word=word+a
    if(a==" "):
        for x in word:
            if(x=="A" or x=="a"):code=code+". ___"
            if(x=="B" or x=="b"):code=code+"___ . . ."
            if(x=="C" or x=="c"):code=code+"___ . __ ."
            if(x=="D" or x=="d"):code=code+"__ . ."
            if(x=="E" or x=="e"):code=code+"."
            if(x=="F" or x=="f"):code=code+". . ___ ."
            if(x=="G" or x=="g"):code=code+"___ ___ ."
            if(x=="H" or x=="h"):code=code+". . . ."
            if(x=="I" or x=="i"):code=code+". ."
            if(x=="J" or x=="j"):code=code+". ___ ___ ___"
            if(x=="K" or x=="k"):code=code+"___ . ___"
            if(x=="L" or x=="l"):code=code+". ___ . ."
            if(x=="M" or x=="m"):code=code+"___ ___"
            if(x=="N" or x=="n"):code=code+"___ ."
            if(x=="O" or x=="o"):code=code+"___ ___ ___"
            if(x=="P" or x=="p"):code=code+". ___ ___ ."
            if(x=="Q" or x=="q"):code=code+"___ ___ . ___"
            if(x=="R" or x=="r"):code=code+". ___ ."
            if(x=="S" or x=="s"):code=code+". . ."
            if(x=="T" or x=="t"):code=code+"___"
            if(x=="U" or x=="u"):code=code+". . ___"
            if(x=="V" or x=="v"):code=code+". . . ___"
            if(x=="W" or x=="w"):code=code+". ___ ___"
            if(x=="X" or x=="x"):code=code+"___ . . ___"
            if(x=="Y" or x=="y"):code=code+"___ . ___ ___"
            if(x=="Z" or x=="z"):code=code+"___ ___ . ."
            if(x=="1"):code=code+". ___ ___ ___ ___"
            if(x=="2"):code=code+". . ___ ___ ___"
            if(x=="3"):code=code+". . . ___ ___"
            if(x=="4"):code=code+". . . . ___"
            if(x=="5"):code=code+". . . . ."
            if(x=="6"):code=code+"___ . . . ."
            if(x=="7"):code=code+"___ ___ . . ."
            if(x=="8"):code=code+"___ ___ ___ . ."
            if(x=="9"):code=code+"___ ___ ___ ___ ."
            if(x=="0"):code=code+"___ ___ ___ ___ ___"
            code=code+"   "
        code=code+"       "
        word=""
print("THE MORSE CODE IS-")
print(code)
            

        
