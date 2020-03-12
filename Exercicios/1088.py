t = 1

def bubble_sort(lista):
    j = 0
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        
        ordenado = True
        
        for i in range(elementos):
           
            if lista[i] > lista[i+1]:
                
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False 
                j = j +1       
                
    return j

while t:
    N = input()
    N = N.split()
    N = list(map(int, N))
    
    if N[0] == 0 and len(N) == 1:
        t = 0
        break

    N.pop(0)
    valor = bubble_sort(N)

    if valor %2 == 0:
        print("Carlos")
    else:
        print("Marcelo")
