
def invert_color(color):
    
    color_value = int(color[1:], 16)
    inverted_value = 0xFFFFFF - color_value
    inverted_hex = "#{:06x}".format(inverted_value)
    return inverted_hex


if __name__ == "__main__":
    
    str_1 = '#000000'
    print(invert_color(str_1))