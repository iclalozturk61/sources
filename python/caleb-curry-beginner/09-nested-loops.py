#Nested for Loop Variations

for i in range(4):
    print("counting by " + str(i) + ":")
    for j in range(5):
        print(j * i, end=" ")
    print()

# Loop Variable Within range (Triangles)

for i in range(10):
    for j in range(i + 1):
        print(j , end=" ")
    print(" ")

print("*****************************")
#Nested while Loops (now with Hypnotism)

i = 0

while i < 10:

    j = 0
    while j < 10:
        print(j , end=" ")
        j += 1
    print()
    i += 1

#yaygın hatalar
i = 0
j = 0 #j dışarda tanımlanınca içteki döngüye yalnızca bir kere girer çünkü ilk seferden sonra j = 10 olur bir daha da girmez

while i < 10:

    while j < 10:
        print(j , end=" ")
        j += 1
    print()
    i += 1

i = 0

while i < 10:

    j = 0
    while j < 10: #buraya j yerine i yazarsak sonsuz döngüye girer
        print(j , end=" ")
        j += 1
    print()
    i += 1

#Nested While Loops to Calculate Sums

i = 0
while i <= 10:
    sum = 0
    j = 0
    while j <= i:
        sum += j
        j += 1
    print("sum from 0 to ", i , "= " , sum, end=" ")
    print()
    i += 1

#Nested While Loops to Calculate Sums v-2
i = 10
while i > -1:
    sum  = 0
    j = i
    while j > -1:
        sum += j
        if j > 0:
            print(j , "+" , end=" ")
        else:
            print(j, "=", end = " ")
        j -= 1
    print(sum)
    i -= 1




    
