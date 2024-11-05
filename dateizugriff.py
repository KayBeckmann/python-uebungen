save = open("/home/user/python-uebungen/save.txt", "w+")

print(save.read())

wort = "Test String!"

if save.writable():
    save.write(wort)
else:
    print("Save nicht Schreibbar!")

save.close()