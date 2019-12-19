#!/usr/bin/env python

import sys
import re
# import biblib.bib
import pdb

# DEFAULT_CITE_OPT = ['cite', 'citep', 'citet', 'fullcite', 'citeauthor', 'citeyear']
# if citeOpt is None:
# 	citeOpt = DEFAULT_CITE_OPT

def get_cite_list(fname):
	cite_list = []
	ind_cite_list = []
	cite_list += [re.findall("\\cite[a-z]*\{(.*?)\}",line) for line in open(fname)]
	cite_list = sum(cite_list,[])
	for cite in cite_list:
		ind_cite_list += cite.replace(' ','').split(',')
	return sorted(set(ind_cite_list))

def parse_bib(fname):
	bib_list = []
	bib_dict = {}
	with open(fname,'r') as f:
		bib_list = f.read()
	for item in bib_list.split('@'):
		try:
			key = item.split('{')[1].split(',')[0].replace(' ','')
			bib_dict[key] = '@'+item
		except:
			pass
	return bib_dict

def make_reduced_bib(cite_list,bib_file,output_file='out.bib'):
	with open(output_file,'w') as f:
		for cite in cite_list:
			f.write(bib_file.get(cite,"")+'\n')


def main():
	cite_list = get_cite_list('test1.tex')
	bib_file = parse_bib('fx.bib')
	make_reduced_bib(cite_list, bib_file, output_file='out.bib')

	# pdb.set_trace()

if __name__ == "__main__":
	main()