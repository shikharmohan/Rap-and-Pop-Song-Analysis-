import subprocess
import sys
result = open('rap_results_kn3.txt', 'w')
for i in range(7666):
	song_file = 'rapsongs/song_'+str(i)+'.txt'
	ng_path = 'ngram -ppl '+song_file+' -tolower -lm '+sys.argv[1]
        p = subprocess.Popen(ng_path, shell=True, stdout=subprocess.PIPE).stdout.read()
        print "Writing " + str(p)
        result.write(str(p))
result.close()
