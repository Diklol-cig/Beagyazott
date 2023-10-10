





def main():
    print("This program calculate times table")
    tablenum = input('\nWhich multiplication table shall I generate for you? ')  
    for i in range(1,11):
        print(i, 'times', tablenum, 'is', i*int(tablenum))
        print('--------------------')
    
    
    
    
    
if __name__ == '__main__':
    main()