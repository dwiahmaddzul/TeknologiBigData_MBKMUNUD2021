import os

folderpath = r'join/Json File'
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

with open('join/Hasil/result.json', 'w') as outfile:
    for fname in filepaths:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

print(filepaths)
