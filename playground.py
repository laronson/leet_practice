

def main():
    def retT():
        print("retT")
        return True
    def retF():
        print("retF")
        return False
    
    return retF() and retT()


main()