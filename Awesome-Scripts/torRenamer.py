## this program renames a list of tv episodes. Episodes can be nested inside folders.
## folders will be flattened and episodes renamed to a particular format. 

import os
import re
import string
import ntpath
import shutil

folderName = input("Please enter the path to the folder level: ")
showName = input("Please enter the name you want to use for the show: ")

#syntaxForEpisodes respresents the format of episode in filename.
syntaxForEpisodes = ['s[0-9][0-9]e[0-9][0-9]','[0-9][0-9][0-9][0-9]',
                     '[0-9]x[0-9][0-9]','[0-9][0-9][0-9]']

#this flattens the folder
def flatten(destination, depth=None):
    print("flattening:", folderName)
    if not depth:
        depth = "/"
    for file_or_dir in os.listdir(destination + depth):
        if os.path.isfile(destination +depth+file_or_dir):
            shutil.move(destination +depth+file_or_dir, destination+"/"+file_or_dir)
        else:
            flatten(destination, depth + file_or_dir +"/")
def searchParams(fileName, Parameters):
    for y in Parameters:
            Result = re.search(y, fileName.lower())

            if Result:
                Result = Result.group(0)
                Result = re.sub("[^0-9]", '', Result)
                if len(Result)<4: Result = '0' + Result #this had to be added to make 201 turn into 0201.... it is the third matcher in the list.
                break
    return Result

#this outputs season, episode from a 4 number string
def seasonEpisode(fileName):
    numbersIn = searchParams(fileName, syntaxForEpisodes)
    if numbersIn:
        season = numbersIn[:2]
        episode = numbersIn[-2:]
        return season, episode

# this is the main file loop
flatten(folderName)
for x in os.listdir(folderName):
    try:
        season, episode = (seasonEpisode(x))
        if season and episode:
            extension = os.path.splitext(x)[1]
            newName = '{0}_S{1}E{2}{3}'.format(showName, season, episode,
                                               extension)
            # uncomment for simulation
            #print('I would rename ' + x + ' ---> ' + newName)
            os.rename(folderName + '/' + x, folderName + '/' + newName)

    except:
        print("no match found for " + x)
