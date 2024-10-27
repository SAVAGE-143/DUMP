import platform,os
#####
os.system("git pull")
bit = platform.architecture()[0]
if bit == '64bit':
    import file
elif bit == '32bit':
    print('32 Bit is not working')
