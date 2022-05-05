def decimal_to_rgb(decimal: tuple) -> tuple:
    return tuple(int(x*255) for x in decimal)

# No use for the one below, but it's here for reference.
def rgb_to_decimal(rgb: tuple) -> tuple:
    return tuple(x/255 for x in rgb)