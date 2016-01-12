import subprocess
import sys
import os
art_direc = sys.argv[1]
lm_file = sys.argv[2]
result = open('results_'+art_direc+lm_file+'.txt', 'w')
num_songs = subprocess.Popen('ls -1 '+art_direc+' | wc -l', shell=True, stdout=subprocess.PIPE).stdout.read()
for i in range(int(float(num_songs))):
	song_file = art_direc+'/song_'+str(i)+'.txt'
	ng_path = 'ngram -ppl '+song_file+' -tolower -lm '+lm_file
        p = subprocess.Popen(ng_path, shell=True, stdout=subprocess.PIPE).stdout.read()
        print "Writing " + str(p)
        result.write(str(p))
result.close()
