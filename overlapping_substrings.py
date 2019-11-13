def frequencyCount(mainstr, substr):
    counter = pos = 0
    while True:
        pos = mainstr.find(substr, pos)
        if pos > -1:
            counter += 1
            pos += 1
        else:
            break
    return counter


print(frequencyCount('banana', 'ana'))



