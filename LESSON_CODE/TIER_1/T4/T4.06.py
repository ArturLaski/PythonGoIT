def game(terra, power):
    for pwr in terra:
        print (pwr)
        for item in pwr:
            print(item)
            if item <= power:
                print (f'{item} - {power}')
                power += item
            else:
                break
            
    return(power)
    