import csv
import os
import sys
import pdb
data = open(sys.argv[1], 'r').read().split('\n')
cfile = sys.argv[1]+'.csv'
with open(cfile, 'w') as f:
	fieldnames = ['sentences', 'words', 'OOV', 'logprob', 'ppl', 'ppl1']
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()
	for line in zip(data,data[1:])[::2]:
		dict = {}
		sent = line[0].split(':')
		if(len(sent) == 2):
			parts = sent[1].split(' ')
			dict['sentences'] = parts[1]
			dict['words'] = parts[3]
			dict['OOV'] = parts[5]
		nums = line[1].split(' ')
		if(len(nums) >7):
			dict['logprob'] = nums[3]
			dict['ppl'] = nums[5]
			dict['ppl1'] = nums[7]
			writer.writerow(dict)
		
