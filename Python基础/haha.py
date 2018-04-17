#其次我们看一下__name__属性的常用情况


def abc():
    if __name__=="__main__":
        print ("It's main !")
    else:
        print ("It's not main !")


abc()