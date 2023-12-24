#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 17:16:39 2022

@author: rayyang
"""


def main():
    while True:
        # file = open('music_core_2022.csv', 'r')
        group = input('Input artist name here: ')
        print()
        group = group.upper()
                     
        if group == 'QUIT' or group == 'Quit':
            print()
            print('goodbye!')
            break
        process_mc_data(group)
        
        
        
        
# the process____data functions can literally just be 1 function. and have a list containing
# the names of each file of each show, and have a loop that goes through that list. and then process each data


# also the current program works by going through all lists, each time user inputs a group name
# i can just go through the entire list once in the beginning. store all data in a chained
# hash table/dictionary or something. and just look up data from there

# better to use dictionary because finding a term in dictionary is O(1)
"""
how dictionary woujld be implemented:
    - 'nested' dictionary
    - key contains group name
    - value for each key is another dictionary, where the key is the song name.
    - value for this dictoinary is a list of length 2. list[0] = award show name. list[1] = # of wins

"""
    

def process_mc_data(group):
 
    songs = []
    mcdata = open('music_core_2022.csv', 'r')
   
    print()
    for line in mcdata:
        mcfields = line.split(',')
        name = mcfields[2] 
        name = name.upper()
        # fields[2].upper()
        if name == group and mcfields[3][3:-3] not in songs:
           songs += [mcfields[3][3:-3]]
   

    
    process_show_data(group,songs)
            

def process_show_data(group, songs):
    showdata = open('theshow.csv', 'r')
    songs = songs
    for line in showdata:
        showfields = line.split(',')
        name = showfields[2] 
        name = name.upper()
        if name == group and showfields[3][3:-3] not in songs:
            songs += [showfields[3][3:-3]]
            

    process_showchamp_data(group, songs)
    

def process_showchamp_data(group, songs):
    showchampdata = open('showchamp.csv', 'r')
    songs = songs
    for line in showchampdata:
        showchampfields = line.split(',')
        name = showchampfields[2] 
        name = name.upper()
        if name == group and showchampfields[3][3:-3] not in songs:
            songs += [showchampfields[3][3:-3]]

    process_inkigayo_data(group, songs)
    
def process_inkigayo_data(group, songs):
    inkigayodata = open('showchamp.csv', 'r')
    songs = songs
    for line in inkigayodata:
        inkigayofields = line.split(',')
        name = inkigayofields[2] 
        name = name.upper()
        if name == group and inkigayofields[3][3:-3] not in songs:
            songs += [inkigayofields[3][3:-3]]

    process_mcount_data(group, songs)

def process_mcount_data(group,songs):
    mcountdata = open('mcount.csv', 'r')
    songs = songs
    for line in mcountdata:
        mcountfields = line.split(',')
        name = mcountfields[2] 
        name = name.upper()
        if name == group and mcountfields[3][3:-3] not in songs:
            songs += [mcountfields[3][3:-3]]

    process_mb_data(group, songs)


def process_mb_data(group, songs):
    mbdata = open('musicbank.csv', 'r')
    songs = songs
    for line in mbdata:
        mbfields = line.split(',')
        name = mbfields[2] 
        name = name.upper()
        if name == group and mbfields[3][3:-3] not in songs:
            songs += [mbfields[3][3:-3]]
    if songs == []:
        print('No wins')
        print()
    else:
        wins(group, songs)
    


"""

if songs == []:
    print ('No wins')
else:
    wins(group, songs)
 """

   
    
def wins(group, songs):
    totalcount = 0
    for x in songs:
        mcdata = open('music_core_2022.csv', 'r')
        mbdata = open('musicbank.csv', 'r')
        showdata = open('theshow.csv', 'r')
        showchampdata = open('showchamp.csv', 'r')
        inkigayodata = open('inkigayo.csv', 'r')
        mcountdata = open('mcount.csv', 'r')
        mccount = 0
        mbcount = 0
        showcount = 0
        showchampcount = 0
        inkigayocount = 0
        mcountcount = 0
        print('Wins by', x, ':')
        print()
        for line in mcdata:
            mcfields = line.split(',')
            # print(fields)
            if mcfields[3][3:-3] == x:
                mccount += 1
                totalcount += 1
            for line in mbdata:
                mbfields = line.split(',')
                if mbfields[3][3:-3] == x:
                    totalcount += 1
                    mbcount += 1
                for line in showdata:
                    showfields = line.split(',')
                    if showfields[3][3:-3] == x:
                        totalcount += 1
                        showcount += 1
                    for line in showchampdata:
                        showchampfields = line.split(',')
                        if showchampfields[3][3:-3] == x:
                            totalcount += 1
                            showchampcount += 1
                            
                        for line in inkigayodata:
                            inkigayofields = line.split(',')
                            if inkigayofields[3][3:-3] == x:
                                totalcount += 1
                                inkigayocount += 1
                            for line in mcountdata:
                                mcountfields = line.split(',')
                                if mcountfields[3][3:-3] == x:
                                    totalcount += 1
                                    mcountcount += 1
                            
        print('Music Core:', mccount)
        print('Music Bank:', mbcount)
        print('Inkigayo:', inkigayocount)
        print('M Countdown:', mcountcount)
        print('Show Champion:', showchampcount)
        print('The Show:', showcount)
        print()
        print()
    print('Total wins:', totalcount)
    print()
    print()



"""

    for x in songs:
        print('Wins by', x, ':')
        for line in data:
            fields = line.split(',')
            if fields[3][3:-3] == x:
                print('Date: ', fields[1])
                print('Song: ', fields[3][3:-3])
                print('Points: ', fields[4][1:], ',', fields[5][:-1])
                print()
   
    
  
    print('Total wins in Music Core: ', count)
    print()
    

        if fields[2] == group:
            count += 1
            print('Date: ', fields[1])
            print('Song: ', fields[3][3:-3])
            print('Points: ', fields[4][1:], ',', fields[5][:-1])
            print()
    print('Total wins in Music Core: ', count)
    print()


def mcwins(group, songs, data):
    totalcount = 0
    for x in songs:
        data = open('music_core_2022.csv', 'r')
        count = 0
        print('Wins by', x, ':')
        print()
        for line in data:
            fields = line.split(',')
            # print(fields)
            if fields[3][3:-3] == x:
                count += 1
                totalcount += 1
                print('Date: ', fields[1])
                print('Song: ', fields[3][3:-3])
                print('Points: ', fields[4][1:], ',', fields[5][:-1])
                print()
        print('Total wins by', x, ':', count)
        print()
        print()
    print('Total wins: ', totalcount)
    print()
    print()

"""
