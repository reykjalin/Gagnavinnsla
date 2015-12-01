# Changes all icelandic letters to the corresponding english letters

# Reads file
fname = input("Filename: ")
data = str()
with open(fname, 'r') as fstream:
    data = fstream.read()

# Change letters
for i in range(len(data)):
    letter = data[i]
    upper = letter.isupper()
    changed = False
    newletter = ''
    if letter.lower() == 'á':
        letter = 'a'
        changed = True
    elif letter.lower() == 'ð':
        letter = 'd'
        changed = True
    elif letter.lower() == 'é':
        letter = 'e'
        changed = True
    elif letter.lower() == 'í':
        letter = 'i'
        changed = True
    elif letter.lower() == 'ó':
        letter = 'o'
        changed = True
    elif letter.lower() == 'ú':
        letter = 'u'
        changed = True
    elif letter.lower() == 'ý':
        letter = 'y'
        changed = True
    elif letter.lower() == 'þ':
        letter = 'th'
        changed = True
    elif letter.lower() == 'æ':
        letter = 'ae'
        changed = True
    elif letter.lower() == 'ö':
        letter  = 'o'
        changed = True
    
    if changed:
        if upper:
            letter = newletter.upper()
        data = data[:i] + letter + data[i+1:]

# Get new filename, with correct file ending and _eng at the end
fname = fname.split('.')
newf = str()
if len(fname) == 0:
    newf = 'could not find filename'
else:
    for i in range(len(fname)):
        if i == len(fname) - 1 and i != 0:
            newf += '_eng.' + fname[i]
        elif i == len(fname) - 1 and i == 0:
            newf += fname[i] + '_eng'
        else:
            newf += fname[i]

# Write data to new file
with open(newf, 'w+') as ostream:
    ostream.write(data)

print('Data saved in file: ', newf)

