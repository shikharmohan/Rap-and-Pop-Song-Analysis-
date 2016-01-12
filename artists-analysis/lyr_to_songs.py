import re
import subprocess
import sys
import os
songs = open(sys.argv[1], 'r').read().split('\n\n') #cleaned corpus with \n\n as delimiter for songs
os.system('mkdir '+sys.argv[1].split('.')[0])
for i in range(len(songs)):
        print "Writing song "+str(i)+" out of "+str(len(songs))
        songname = sys.argv[1].split('.')[0]+'/song_'+str(i)+'.txt'
        songfile = open(songname, 'w')
        for line in songs[i]:
                songfile.write(line)
