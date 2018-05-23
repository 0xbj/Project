def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

# print_format_table()


# print('\033[1;31mRed like Radish\033[1;31m')
# print('\033[1;32mGreen like Grass')
# print('\033[1;33mYellow like Yolk\033[1;m')
# print('\033[1;34mBlue like Blood\033[1;m')
# print('\033[1;35mMagenta like Mimosa\033[1;m')
# print('\033[1;36mCyan like Caribbean\033[1;m')
# print('\033[1;37mWhite like Whipped Cream\033[1;m')

color = ['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m','\033[1;37m']

for i in range(7):
    print(i)
    print(color,len(color))
    print("%s ical ganteng banget" %(color[i]) )