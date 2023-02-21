import os

# Get the list of all files and directories
path = "."
dir_list = os.listdir(path)
i = 1
with open('denoised.csv', 'w') as f:
    for file in dir_list:
        if file[-3:] == 'txt':
            print(file)
            print(file[-8:-4])
            with open(file) as articles:
                for article in  articles.read().split("========================="):
                    temp = article.replace('\n', ' ')
                    temp = temp.replace(',', ' ')
                    f.write(f'{file[-8:-4]}, {i}, {temp}\n')
                    i += 1


