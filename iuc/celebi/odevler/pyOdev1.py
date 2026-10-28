"""""""""""""""""""""""""""""""""""""""
#SORU:1
sum = 0;
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        print(i)
print(sum)
"""""""""""""""""""""""""""""""""""""""
from itertools import product
from tokenize import group

"""""""""""""""""""""""""""""""""""""""
#SORU:2
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = 0
sumEven = 0
while fib(n) < 4000000:
    if fib(n) % 2 == 0:
        sumEven += fib(n)
        n += 1
    else:
        n += 1

print(sumEven)
"""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""
#SORU3:
primeFactors = []
num = 600851475143
factor = 2
while num > 1:
    if num % factor == 0:
        primeFactors.append(factor)
        num /= factor
    factor += 1

print(primeFactors)
print(factor - 1)
"""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""
#SORU: 4
def isPalindrome(num):
    numOfDigits = 0
    temp = num
    while temp > 0:
        numOfDigits += 1
        temp //= 10

    temp = num
    newNum = 0
    for i in range(numOfDigits):
        digit = temp % 10
        newNum = newNum * 10 + digit
        temp //= 10

    if newNum == num:
        return True
    return False

num=0
max = 0
for i in range(1,1000):
    for j in range(1,1000):
        num = i*j
        if isPalindrome(num):
            max = num

print(max)

"""""""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""""""
#SORU: 5
num = 0
maxFactor = 20

while True:
    num += 1
    for i in range(1,maxFactor + 1):
        if num % i != 0:
            break
    else: #böyle bir kullanım varmış: for-else eğer for'un içine hep girdiyse döngü bitince else çalışır
        print(num)
        break

"""""""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""""""
#SORU:6
sumOfSquares = 0
squaresOfSum = 0

for i in range(1,101):
    sqrt=i**2
    sumOfSquares += sqrt

sum=0
for i in range(1,101):
    sum += i

squaresOfSum = sum**2
difference= squaresOfSum - sumOfSquares
print(difference)
print(f"toplamların karesi: {squaresOfSum}")
print(f"karelerin toplamı: {sumOfSquares}")

"""""""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""""""
#SORU:7
whichOne = 0
target = 10001
temp1 = 2

while True:
    for i in range(2, int(temp1**0.5) + 1):
        if temp1 % i == 0: break

    else:
        whichOne += 1


    if whichOne == target:
        print(temp1)
        break

    temp1 += 1
"""""""""""""""""""""""""""""""""""""""



"""""""""""""""""""""""""""""""""""""""
#SORU:8

number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
groups = 13
maxProduct = 1
maxGroup = 0
length = len(number)

for i in range(1, length-groups + 2):
    part = number[i - 1 : i + groups - 1]

    product = 1

    for j in part:
        product *= int(j)

    if product > maxProduct:
        maxProduct = product
        maxPart = part

print(maxProduct)
print(maxPart)
"""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""
#SORU:9
for a in range(1, 1000):
    for b in range(a, 1000-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a*b*c)

"""""""""""""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""""""""""""
#SORU:10

limit = 2000000
sum = 0

for number in range(2, limit):
    isPrime = True

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            isPrime = False
            break

    if isPrime:
        sum += number

print(sum)
"""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""
#SORU: KENDİ SEÇTİĞİM: Problem 15: Lattice Paths (Neden bunu seçtim, rota ve haritalamaya benzer kan çekiyor geliba, ek olarak uğur hoca bahsetmişti yanlış hatırlamıyorsam)
#permütasyonla kolaylıkla bulunurdu ama olayı hayal etmeye uygun bir şekilde ele almak daha güzel

def latticePaths(n):
    paths = []

    for i in range(n + 1):
        row = [0] * (n + 1) #numpysız zero iki katmanlı dizi oluşturamıyormuşuz o yüzden böyle
        paths.append(row)

    for i in range(n + 1): #20 path li istediği için +1 düğüm sayısı oluyor
        paths[i][0] = 1 #ilk satır ve ilk sutuna 1 yoldan geliriz
        paths[0][i] = 1

    for row in range(1, n + 1):
        for col in range(1, n + 1):
            paths[row][col] = paths[row - 1][col] + paths[row][col - 1] #oraya gelebileceğimiz yolların toplam sayısı üstüne gelebileceğimiz toplam yok sayısı + yanına gelebileceğimiz toplam yol sayısı

    print(paths)
    return paths[n][n]


print(latticePaths(2))
print(latticePaths(20))

"""""""""""""""""""""""""""""""""""""""






