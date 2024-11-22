# "r" READ 
# "r+" READ + WRITE
# "w" WRITE
# "a" APPEND
save = open("/home/user/python-uebungen/save.txt", "a+")

print(save.read())

wort = "Test String!\n"

if save.writable():
    save.write(wort)
else:
    print("Save nicht Schreibbar!")

save.close()