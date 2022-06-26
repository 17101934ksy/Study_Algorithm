def test(a):

    if a > 5:
        return
    
    print(a)
    test(a+1)

if __name__ == '__main__':
    test(2)