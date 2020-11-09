"""
    Searches deep inside a directory structure, looking for duplicate file.
    Duplicates aka copies have the same content, but not necessarily the same name.
"""
__author__ = "Aiden Vestbie"
__email__ = "aidenvestbie@outlook.com"
__version__ = "1.0"

# noinspection PyUnresolvedReferences
from os.path import getsize, join
from time import time

# noinspection PyUnresolvedReferences
from p1utils import all_files, compare


def search(file_list):
    """Looking for duplicate files in the provided list of files
    :returns a list of lists, where each list contains files with the same content

    Basic search strategy goes like this:
    - until the provided list is empty.
    - remove the 1st item from the provided file_list
    - search for its duplicates in the remaining list and put the item and all its duplicates into a new list
    - if that new list has more than one item (i.e. we did find duplicates) save the list in the list of lists
    As a result we have a list, each item of that list is a list,
    each of those lists contains files that have the same content
    """
    lol = []
    n = 0
    while 0<len(file_list):
        h = file_list.pop(0)
        lol.append([h])
        n += 1
        for i in file_list:
            if compare(h, i):
                lol[n - 1].append(i)
            else:
                break



    return lol


def faster_search(file_list):
    """Looking for duplicate files in the provided list of files
    :returns a list of lists, where each list contains files with the same content

    Here's an idea: executing the compare() function seems to take a lot of time.
    Therefore, let's optimize and try to call it a little less often.
    """
    lol = []
     = 0

    while 0 < len(file_list):
        h = file_list.pop(0)
        lol.append([h])
        n += 1
        for i in file_list:
            if getsize(h) == getsize(i):

                if compare(h,i):
                    lol[n-1].append(i)
            else:
                break

    return lol


def report(lol):
    """ Prints a report
    :param lol: list of lists (each containing files with equal content)
    :return: None
    Prints a report:
    - longest list, i.e. the files with the most duplicates
    - list where the items require the largest amount or disk-space
    """
    print("== == Duplicate File Finder Report == ==")
    lst1 = list(max(lol, key= len))

    print(f'The file with the most duplicates is \n{lst1[0]}  \n Here are its {len(max(lol, key= len))-1} copies: ')
    print(*lst1[1: len(lst1)], sep = '\n')
    #print("No duplicates found")
    variable = ('',0)
    for i in lol:
        if getsize(i[0]) * (len(i)-1) > variable[1]:
            variable = (i , getsize(i[0]) * (len(i)-1))

    harry = [i for i in variable[0]]

    print(f'\nThe most disc space({variable[1]}) could be recovered, by deleting copies of this file: \n{harry[0]} \n Here are its {(len(harry)-1)} copies:')
    print(*harry[1: len(harry)], sep = '\n')





if __name__ == '__main__':
    path = join(".", "images")

    # measure how long the search and reporting takes:
    t0 = time()
    report(search(all_files(path)))
    print(f"Runtime: {time() - t0:.2f} seconds")



    print("\n\n .. and now w/ a faster search implementation:")
    # measure how long the search and reporting takes:
    t0 = time()
    report(faster_search(all_files(path)))
    print(f"Runtime: {time() - t0:.2f} seconds")
