import re
import subprocess
import os
songs = open('rap_corpus.txt', 'r').read().split('\n\n') #cleaned corpus with \n\n as delimiter for songs
#result = open('results-rap-ad2.txt', 'w') #results file

for i in range(0,len(songs)):
        print "Analyzing song "+str(i)
        corpus_name = 'corpii-rap/corpus_'+str(i)+'.txt'
        song_name = 'rap-song/song_'+str(i)+'.txt'
        outfile = open(corpus_name, 'w')
        for j in range(0, len(songs)):
                if(i != j):
                        for k in songs[j]:
                                outfile.write(k)
      	songfile = open(song_name, 'w')
       	for s in songs[i]:
		songfile.write(s)
#	lm_path = 'ngram-count -text'+corpus_name+' -lm '+corpus_name+song_name -order 2 -tolower -addsmooth 0.1'
#	p = subprocess.Popen(lm_path, shell=True, stdout=subprocess.PIPE)
"""
#run after lm created
for i in range(0,len(songs)):
        print "Analyzing song "+str(i)
        corpus_name = 'corpii-ad/corpus_'+str(i)+'.txt'
        song_name = 'song_'+str(i)+'.txt'
	song_file = 'popular-song/'+song_name
        lm_path = 'ngram-count -text '+corpus_name+' -lm '+corpus_name+song_name +'.lm -order 3 -tolower -kndiscount -interpolate' 
        ng_path = 'ngram -ppl '+song_file+' -tolower -lm '+corpus_name+song_name +'.lm'
        p = subprocess.Popen(ng_path, shell=True, stdout=subprocess.PIPE).stdout.read()
        print "Writing " + str(p)
        result.write(str(p))
"""

