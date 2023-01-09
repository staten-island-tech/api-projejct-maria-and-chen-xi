def search(name):
    count = 0
    for x in name:
        
        if x == '%':
            print('x=% ')
            Xcount = count
            for thing in name:
                print(Xcount)
                print(name[Xcount])
                if thing == '2':
                    print('thing=2')
                    print(Xcount)
                    print(name[Xcount])
                    print(count)
                    print(name[count])
                    if Xcount==count+1:
                        print('attempting to replace')
                        name[count] = ''
                        name[Xcount] = '+'
                Xcount = Xcount+1
        count = count+1
    print(name)
    return name

search('one%20pece')