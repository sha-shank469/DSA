
def check_jackpot(jackpot):
    
    return len(set(jackpot)) == 1

if __name__ == "__main__":
    
    jackpot = ['@','@','@','@']
    print(check_jackpot(jackpot))