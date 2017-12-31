

def get_network_speed(total_bytes, second):
    value = 8 * total_bytes / second
    if value >= 10**12:
        return "{:.2f} Tbit/s".format(value/(10**12))
    if value >= 10**9:
        return "{:.2f} Gbit/s".format(value/(10**9))
    if value >= 10**6:
        return "{:.2f} Mbit/s".format(value/(10**6))
    if value >= 10**3:
        return "{:.2f} kbit/s".format(value/(10**3))
    return "{} bit/s".format(value)

def get_data_size(value):
    if value >= 2**40:
        return "{:.2f} T".format(value/(2**40))
    if value >= 2**30:
        return "{:.2f} G".format(value/(2**30))
    if value >= 2**20:
        return "{:.2f} M".format(value/(2**20))
    if value >= 2**10:
        return "{:.2f} K".format(value/(2**10))
    return "{} B".format(value)
