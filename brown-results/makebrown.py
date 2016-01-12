import subprocess
import sys

song = open('merged.txt', 'r').read().split('\n\n')
result = open('result_bigram_kn', 'w')
for s in range(0, len(song)):
	song_file = 'popular-song/song_'+str(s)+'.txt'
	ng_path = 'ngram -ppl '+song_file+' -tolower -lm '+sys.argv[1]
        p = subprocess.Popen(ng_path, shell=True, stdout=subprocess.PIPE).stdout.read()
	print "Writing "+str(p)
	result.write(str(p))
