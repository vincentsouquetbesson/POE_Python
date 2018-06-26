

def isPrime(  n ):
    result = True
    if(n <2 ):
        result = False
    else :
        for i in range (2,n):
            if n % i == 0 :
                result = False
                break
    return result




def additionRecursif(listVar,n):
    if n == 1:
        return listVar[0]
    else:
        return listVar[n-1] + additionRecursif( listVar , n-1)



def minRecursif ( listVar, n, min):
    if len(listVar) == n :
        min = listVar[n-1]
    else:
        if(listVar[n-1] < min):
            min = listVar[n-1]
    if n != 1 :
        min = minRecursif(listVar,n-1,min)
    return min



def maxRecursif ( listVar, n, max):
    if len(listVar) == n :
        max = listVar[n-1]
    else:
        if(listVar[n-1] > max):
            max = listVar[n-1]
    if n != 1 :
        max = maxRecursif(listVar,n-1,max)
    return max



def getPrimeNumbers( listVar):
    listPrimeNumber = []
    for i in listVar:
        if( isPrime(i)):
            listPrimeNumber.append( i)
    return listPrimeNumber




def inversionRecursWithoutNew( listVar, n):
    if n == 1:
        listVar.append( listVar[0])
        listVar.pop(0)
    else:
        listVar.append(  listVar[ n-1 ])
        listVar.pop(n-1)
        inversionRecursWithoutNew(listVar,n-1)





if __name__ == '__main__':
    print("salut c'est cool")

    print( isPrime(17) )

    listVar =[1,2,3,4,5,6,7]
    n = len(listVar)  #taille de la liste

    print("affichage tableaux : ")
    print(listVar)

    print("addition du tableau" )
    print( additionRecursif( listVar , n ) )

    print("les minimum est : ")
    print( minRecursif(listVar,n,0) )

    print("les maximum est : ")
    print( maxRecursif(listVar,n,0))

    print("nombre premier : ")
    print(getPrimeNumbers(listVar))

    inversionRecursWithoutNew(listVar,n)
    print("affichage inversion : ")
    print(listVar)




