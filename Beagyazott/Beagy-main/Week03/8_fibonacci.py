








def main():
    f0=0
    f1=1
    print(f0)
    print(f1)
    for i in range(2,10):
        f2=f0+f1
        print(f2)
        f0=f1
        f1=f2
        
    
if __name__ == '__main__':
    main()
    