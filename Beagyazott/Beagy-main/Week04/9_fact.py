from time import time


def factorization(n):
    a=2
    while n>1:
        pow=0
        while n%a==0:
            n=n/a
            pow+=1
        if pow>0:
            print(a,'^',pow)
        a+=1



def main():
    n = int(input('N: '))
    #start the timer
    start = time()
    factorization(n) #this function has been implemented in 9.1.
    #stop the timer
    end = time()
    print(('Elapsed time: {} seconds'.format(end - start)))
    
    
    
    
    
if __name__ == "__main__":
    main()