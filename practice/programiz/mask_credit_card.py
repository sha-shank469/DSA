def mask_credit_card(card_number):
    
    if len(card_number) <= 4:
        return card_number
    card_number_split, remain_number = card_number[:-4], card_number[-4:]
    
    changed = card_number_split.replace('4','*')
    return changed + remain_number

if __name__ == "__main__":
    
    str = "444444444444444"
    print(mask_credit_card(str))