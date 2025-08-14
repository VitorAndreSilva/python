D = int(input())

if D < 800:
    if D<200:
     print(D)
    else:
        if D>=200 and D<400:
            print(400 - D)
        else:
            if D>400 and D<600:
                print(D - 400)
            else:
                if D>=600 and D<800:
                    print(800 - D)
                else:
                    if D == 400:
                        print(D - D)
else:
    if D>800 and D<1000:
        print(D - 800)
    else:
        if D>=1000 and D<1200:
            print(1200 - D)
        else:
            if D > 1200 and D<1400:
                print(D - 1200)
            else:
                if D>=1400 and D<1600:
                    print(1600 - D)
                else:
                    if D > 1600 and D<1800:
                        print(D - 1600)
                    else:
                        if D >= 1800 and D<2000:
                            print(2000-D)
                        else:
                            if (D == 800) or (D == 1200) or (D == 1600) or (D == 2000):
                                print(D - D)
                            else:
                                print(D - 2000)