import os

# ps: i made mistake and saved imgs to .png insead of .jpg :)

dirs = ['marble', 'metal', 'stone', 'wood']

for i in dirs:
    files = os.listdir(i)

    for j in files:
        name = j.split('.')[0]

        os.rename(os.path.join(i, j), os.path.join(i, name + '.jpg'))
