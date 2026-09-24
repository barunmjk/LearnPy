#count letter digit and special char in string

def countChar(s):
                 nCount=0
                 cCount=0
                 sCount=0
                 spCount=0
                  
                 for i in range(len(s)):
                                        if ord(s[i]) >=48 and ord(s[i])<=57:
                                                                  nCount+=1
                                        elif ord(s[i]) >= 65 and ord(s[i])<=90:
                                                                   cCount+=1
                                        elif ord(s[i]) >=97 and ord(s[i]) <=122:
                                                                    sCount+=1
                                        else :
                                                spCount+=1                                                                       

                 print('Number  char is :',nCount)
                 print('capital alpha char is :',cCount)
                 print('small aplha char is :',sCount)
                 print('special char is :',spCount)


str = input('Enter the String:-')
countChar(str)