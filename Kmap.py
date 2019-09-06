# CSE 101 - IP HW2
# K-Map Minimization 
# Name:Samarth Chauhan
# Roll Number:2018410
# Section:B
# Group:3
# Date:17-10-2018


#global variable required by function to keep count of cycle 
cycle=0

#it is the main function in which no of variable and a string constiting of function is given and it gives out string of simplified result
def minFunc(numVar, stringIn):
	
        numVar=int(numVar)
        
        onelist,dontcare,givenlist=splitlist(stringIn)
        
        minlist,number=grouping(numVar,givenlist)
       
        NUMberlist=[]        

        #concept of recurionsion untill it is minimised
        while not minimisedlist(4,minlist):
               
                lastnumberlist=number
        
                minlist=unique(minimise(numVar,minlist))
                number=binarytodecimal(numVar,minlist)

                if number!=[[], [], [], [], []]:
                        newterm=checkremaining(numVar,lastnumberlist,number)
                        if newterm!=[]:
                                for num in newterm:
                                        NUMberlist.append(num)
              
        
   
        #to delete duplicate entry
        lastnumberlist=makeunique(lastnumberlist)
        
        #it sort numberlist of remaining term/s and final simplified terms for final EPI
        finalnumberlist=makefinalnumberlist(NUMberlist,lastnumberlist)
       
        #this make number list of EPI ie last PI in the minimisation technique of QUINE and those without tick
        EPI=giveEPI(numVar,finalnumberlist,onelist)
      
        #to get list of EPI in terms of binary like "10-1"
        finalliterals=makeliterals(numVar,EPI)
        
        #this will return literal in w,x,y,z terms
        l1,l2=maketerms(numVar,finalliterals)

        #to sort string in lexicographical order
        l1,l2=lexicoorder(l1,l2)
        
        #final simplified string
        stringOut=display(l1,l2)
        		
        return stringOut

#to convert number into binary number
def binarynumber(numVar,number):
        binarylist={0:'0000',1:'0001',2:'0010',3:'0011',4:'0100',5:'0101',6:'0110',7:'0111',8:'1000',9:'1001',10:'1010',11:'1011',12:'1100',13:'1101',14:'1110',15:'1111'}
        #returning binary number according to bit
        return binarylist[number][4-numVar:]

#for grouping of binary number according to the number of ones they are containing
def grouping(numVar,numlist):

        #to initilize all sorted list
        list0,list1,list2,list3,list4=[],[],[],[],[]
        #listfornum0,listfornum1,listfornum2,listfornum3,listfornum4=[],[],[],[],[]

        sortedlist=[list0,list1,list2,list3,list4]
        nolist=[]

        for Num in numlist:
                templist=[]
                        
                #getting binary number from binary number function
                binNum=binarynumber(numVar,Num)
                
                #counting number of ones
                one=checkone(binNum)

                #appending number according to number of one and decimal number
                if one==0:
                        list0.append(binNum)
                        templist.append(Num)
                elif one==1:
                        list1.append(binNum)
                        templist.append(Num)
                elif one==2:
                        list2.append(binNum)
                        templist.append(Num)
                elif one==3:
                        list3.append(binNum)
                        templist.append(Num)
                else:
                        list4.append(binNum)
                        templist.append(Num)
                nolist.append(templist)
                
                

        #returning sorted list of 1 and 0 & deciaml number
        return sortedlist,nolist
        
#to minimise the list if only change of one bit happens                
def minimise(numVar,binarylist):

        #these type of layout of list help to simplify better in other function
        list0,list1,list2,list3,list4=[],[],[],[],[]
        bitlist=[list0,list1,list2,list3,list4]   


        for n in range(0,len(binarylist)-1):

                #at every step we are checkin for null string        
                if binarylist[n]!=[]:
                        for outter in binarylist[n]:

                                if binarylist[n+1]!=[]:
                                        for inner in binarylist[n+1]:
                                               
                                                #this step checks for only bit change in term
                                                if check(inner,outter)==True:
                                                        for index in range(0,numVar):
                                                                
                                                                #replaces the uncommon bit with "-"
                                                                if inner[index]!=outter[index]:                                                                        
                                                                        inner=list(inner)
                                                                        inner[index]='-'
                                                                        inner="".join(inner)
                                                                        if inner!=[]:
                                                                                bitlist.append(inner)
                                                                                                                                                                                         

                                                                                                                                        
        #this will group function according to number of one
        bitlist=group(numVar,bitlist)
        
        return bitlist
                                                
#return true if only change of one bit happens
def check(l1,l2):
        change=0

        for c1,c2 in zip(l1,l2):
                if c1!=c2:
                        change=change+1
        if change==1:
                return True
        else:
                return False

#to check numbers of ones in the string
def checkone(string):
        one=0
        for bit in string:
                if bit=='1':
                        one=one+1
        return one

#to group binary term terms according to the numbers of one in them
def group(numVar,binlist):

        list0,list1,list2,list3,list4=[],[],[],[],[]
        sortedlist=[list0,list1,list2,list3,list4]

        for Num in binlist:
                        
                if Num!=[]:
                
                        #counting number of ones
                        one=checkone(Num)

                        #appending number according to number of one and decimal number
                        if one==0:
                                list0.append(Num)
                        elif one==1:
                                list1.append(Num)
                        elif one==2:
                                list2.append(Num)
                        elif one==3:
                                list3.append(Num)
                        else:
                                list4.append(Num)
        
        return sortedlist

#to delete duplicate value in binarylist or in minimised minterm list
def unique(binarylist):
        templist=[]
        for index in range(0,len(binarylist)):

                #checks for null string              
                if binarylist[index]!=[]:

                        anothertemplist=[]   

                        for bits in binarylist[index]:                                
                                if bits not in anothertemplist:                                        
                                        anothertemplist.append(bits)                        
                        templist.append(anothertemplist)
                
                else:
                        templist.append(binarylist[index]) 
        return templist

#to check if the obtained list is the simplified list or not. Acually it helps minfunc in the number of loops requires for minimisation                      
def minimisedlist(numVar,binarylist):
        count=0
        for bits in binarylist:
                if bits==[]:
                        count=count+1
        
        if count==(numVar+1):
                return True
        else:
                return False

#to convert binary number to decimal and it can take all type of binary ie binary with '-' in it
def binarytodecimal(numVar,binarylist):
        newlist=[]        
        for index in range(len(binarylist)):
                if binarylist[index]!=[]:
                        
                        for number in binarylist[index]: 
                                templist=[]
                                fakenewlist=[]                               
                                if '-' not in number:
                                        #if there is no options for decimal number these steps will append to list
                                        no=numberbinary(numVar,number)
                                        fakenewlist.append(no)     
                                        templist.append(fakenewlist)
                                        newlist.append(templist)
                                else:
                                        #this step append all the possible value with the help of possiblenumbers
                                        newlist.append(possiblenumbers(numVar,number))                                                            

                else:
                        newlist.append([])
        return newlist

#it gives all possible decimal number of binary number which have '-' in it. It replaces "-" with all all possible combination of 0 and 1
def possiblenumbers(numVar,number):
        count=0
        newlist=[]

        if '-' in number:
                for bit in number:
                        if bit=='-':
                                count=count+1
                if count==1:
                        n1=numberbinary(numVar,number.replace('-','0'))                        
                        n2=numberbinary(numVar,number.replace('-','1'))

                        newlist.append(n1)
                        newlist.append(n2)
                elif count==2:
                        number1=number.replace('-','0',1)
                        n1=numberbinary(numVar,number1.replace('-','0'))                        
                        n2=numberbinary(numVar,number1.replace('-','1'))

                        number2=number.replace('-','1',1)
                        n3=numberbinary(numVar,number2.replace('-','0'))                        
                        n4=numberbinary(numVar,number2.replace('-','1'))

                        newlist.append(n1)
                        newlist.append(n2)
                        newlist.append(n3)
                        newlist.append(n4)
                elif count==3:
                        number1=number.replace('-','0',1)
                        number11=number1.replace('-','0',1)
                        number12=number1.replace('-','1',1)
                        n1=numberbinary(numVar,number11.replace('-','0',1))
                        n2=numberbinary(numVar,number11.replace('-','1',1))
                        n3=numberbinary(numVar,number12.replace('-','0',1))
                        n4=numberbinary(numVar,number12.replace('-','1',1))

                        number2=number.replace('-','1',1)
                        number21=number2.replace('-','0',1)
                        number22=number2.replace('-','1',1)
                        n5=numberbinary(numVar,number21.replace('-','0',1))
                        n6=numberbinary(numVar,number21.replace('-','1',1))
                        n7=numberbinary(numVar,number22.replace('-','0',1))
                        n8=numberbinary(numVar,number22.replace('-','1',1))
                        
                        newlist.append(n1)
                        newlist.append(n2)
                        newlist.append(n3)
                        newlist.append(n4)
                        newlist.append(n5)
                        newlist.append(n6)
                        newlist.append(n7)
                        newlist.append(n8)
                else:
                        for no in range(0,16):
                                newlist.append(no)



        return newlist                

#it convert binary to decimal only if the binary number is well defined
def numberbinary(numVar,number):        
        pos=(numVar-1)
        sum=0
        for no in number:
                if no=='1':                        
                        deci=2**pos
                        sum=sum+deci
                pos=pos-1
        return sum

#it deletes duplicate value in number list
def makeunique(numberlist):
        requiredlist=[]
        for number in numberlist:
                if number not in requiredlist:
                        requiredlist.append(number)
        return requiredlist

#it checks the remaining terms which are not in match with other terms
def checkremaining(numVar,Num1,Num2):
        newlist=[]
        newlist1=[]
        newlist2=[]
        Requiredlist=[]

        #it checks for number which are left without tick as in petrick method
        for outter in Num1:
                no=0
                for no in range(0,len(outter)):
                        newlist1.append(outter[no])
        newlist1=makeunique(newlist1)

        for inner in Num2:
                no=0
                for no in range(0,len(inner)):
                        newlist2.append(inner[no])
        newlist2=makeunique(newlist2)        
               
        for bits in newlist1:
                if bits not in newlist2:
                        newlist.append(bits)

        for num in newlist:
                for loop in Num1:                        
                        if num in loop:                                
                                Requiredlist.append(loop)
        Requiredlist=makeunique(Requiredlist)                          
        return Requiredlist

#it compiles the numberlist of remaining term/s and final simplified terms
def makefinalnumberlist(list1,list2):
        finallist=[]
        for number in list1:
                if number!=[]:
                        finallist.append(number)

        for number in list2:
                if number!=[]:
                        finallist.append(number)
        return finallist

#it make binary list of EPI
def makefinalbinarylist(numVar,numberlist):
        
        templist=[] 
        for num in numberlist:
                             
                minterm,numberlist=grouping(numVar,num)

                BinTerm=minimise(numVar,minterm)
                for term in BinTerm:
                        if term!=[]:
                                templist.append(term) 
           
                 
        return templist                  

#it gives list of EPI (if there is choice between terms)
def giveEPI(numVar,numberlist,requstedlist):

        requstednumberlist=[]
        EPIlist=[]
        newlist=[]
        redundantlist=[]
        anotherremaininglist=[]

        #here i am creating a list to count occurance of number in the prime implicant by the help of list provided by user
        for num in range(0,len(requstedlist)):
                requstednumberlist.append(0)

        
        #here i am counting occurance of number in list and adding 1 to corresponding index if found
        num=0
        for n in range(0,len(numberlist)):
                for bits in range(0,len(numberlist[n])):
                        for num in range(0,len(requstedlist)):
                                if numberlist[n][bits]==requstedlist[num]:
                                        requstednumberlist[num]=requstednumberlist[num]+1
        
        #if teh occrance of number of one then append that full term in the EPI list ie essential prime implicant
        num,n,bits=0,0,0
        for n in range(0,len(numberlist)):
                for bits in range(0,len(numberlist[n])):
                        for num in range(0,len(requstedlist)):
                                if requstednumberlist[num]==1:
                                        if numberlist[n][bits]==requstedlist[num]:
                                                EPIlist.append(numberlist[n]) 
        
        #to delete any dulicate entry
        EPIlist=makeunique(EPIlist)                               
        
        num=0
        
        #here i am again creating list of EPI so to find untick term left behind in process
        while num in range(0,len(EPIlist)):
                bit=0
                while bit in range(0,len(EPIlist[num])):                        
                        newlist.append(EPIlist[num][bit])
                        bit=bit+1
                num=num+1
        
        #to delete any dulicate entry
        newlist=makeunique(newlist)
        
        for NumBer in requstedlist:                
                if NumBer not in newlist:                        
                        redundantlist.append(NumBer)

        #if there is a choice between term then adding or between them
        num=0
        bits=0
        loop=1
        while num in range(0,len(redundantlist)):
                
                bits=0
                while bits in range(0,len(numberlist)):
                                        
                        if redundantlist[num] in numberlist[bits]:                                
                                if loop==1:
                                        loop=loop+1
                                        anotherremaininglist.append(numberlist[bits])
                                else:
                                        anotherremaininglist.append("or")
                                        anotherremaininglist.append(numberlist[bits])
                        bits=bits+1
                
                num=num+1

        anotherremaininglist=makeunique(anotherremaininglist)
       
        
        for NUM in anotherremaininglist:
                EPIlist.append(NUM)
                             
        
        EPIlist=makeunique(EPIlist)
        return EPIlist

#ti makes literals terms
def makeliterals(numVar,EPI):

        literal=[]

        for Number in EPI:
                Lastlist=[]                
                if Number=='or':
                        Lastlist.append('or')
                else:
                        Minlist,Numb=grouping(numVar,Number)                        
                        while not minimisedlist(4,Minlist):
                                Lastlist=Minlist                                      
                                Minlist=unique(minimise(numVar,Minlist))
                
                for terms in Lastlist:
                        if terms!=[]:                                
                                literal.append(terms)
                                
        return literal

#it make term coressponding to there binary terms
def maketerms(numVar,finalliterllist):

        finalterm=[]
        finallist1=[]
        finallist2=[]
        newlist=[]
        
        
        for term in finalliterllist:

                tempterm=[]
                
                for bits in term:
                        loop=0
                        for bit in bits:                                
                                                
                                if bit=='1':
                                        tempterm.append(getterm(loop,1))
                                elif bit=='0':
                                        tempterm.append(getterm(loop,0))
                                elif bit=="o":
                                        tempterm.append("o")
                                elif bit=="r":
                                        tempterm.append("r")
                                else:
                                        tempterm.append("")

                                loop=loop+1                               

                finalterm.append(tempterm)
        
        for term in finalterm:
                newlist.append("".join(term))
                
               

        if 'or' in newlist:
                num=0
                for num in range(0,len(newlist)):
                        if newlist[num]=='or':
                                position=num
        
                num=0
                for num in range(0,position):
                        finallist1.append(newlist[num])
        
                num=0
                for num in range(0,len(newlist)):
                        if (num!=position)and(num!=(position-1)):
                                finallist2.append(newlist[num])
                return finallist1,finallist2
        else:
                return newlist,newlist
         
#it helps makesterms fuction to give term
def getterm(loop,NUM):
        
        term1=["w","x","y","z"]
        term0=["w'","x'","y'","z'"]
        if (NUM==1):
                return term1[loop]                
        else:
                return term0[loop]               

#it displays the final result ir EPIs on screen
def display(list1,list2):
        displaylist=[]
        if list1!=list2:
                for num in range(0,len(list1)):
                        if num != (len(list1)-1):
                                displaylist.append(list1[num])
                                displaylist.append("+ ")
                        else:
                                displaylist.append(list1[num])

                displaylist.append(" OR ")
                num=0
                for num in range(0,len(list2)):
                        if num != (len(list2)-1):
                                displaylist.append(list2[num])
                                displaylist.append("+ ")
                        else:
                                displaylist.append(list2[num])
        else:
                for num in range(0,len(list1)):
                        if num != (len(list1)-1):
                                displaylist.append(list1[num])
                                displaylist.append("+ ")
                        else:
                                displaylist.append(list1[num])
        return "".join(displaylist)

#it splits the string in usefull list which can be use by other function, mainly for min func
def splitlist(numberlist):

        numberlist=str(numberlist)

        
        #here we are using string silicing
        num=0
        while num in range(0,len(numberlist)):
                if numberlist[num]=='(':
                        position3=num
                elif numberlist[num]==')':
                        position4=num
                num=num+1      
        num=0
        while num in range(0,position3):
                if numberlist[num]=='(':
                        position1=num
                elif numberlist[num]==')':
                        position2=num
                num=num+1   
     
        if numberlist[numberlist.index('d')+1]=='-':
                position1=position3
                position2=position4

        onelist=[]
        dontcare=[]
        fulllist=[]

        onelist=(numberlist[(position1+1):position2]).split(",")

        if numberlist[numberlist.index('d')+1]!='-':
                dontcare=numberlist[position3+1:position4].split(",")
       
        num=0
        for num in range(0,len(onelist)):
                onelist[num]=int(onelist[num])
        
        num=0
        if numberlist[numberlist.index('d')+1]!='-':
                for num in range(0,len(dontcare)):
                        dontcare[num]=int(dontcare[num])
        
        for term in onelist:
                fulllist.append(term)
        if dontcare!=[]:
                for term in dontcare:
                        fulllist.append(term)
        
        
        return onelist,dontcare,fulllist    

def lexicoorder(list1,list2):
        if list1==list2:
                list1.sort()
                return list1,list1
        else:
                list1.sort()
                list2.sort()
                return list1,list2
     
