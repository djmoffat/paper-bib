#!/usr/bin/env python3

import re
import argparse


def get_args():
	"""
	Read the arguments and return them to main.
	"""
	parser = argparse.ArgumentParser(
		description='This project is a basic python script to allow to make a stripped down bib file, for a specific tex file.')
	parser.add_argument('-i','--input',
		help='input tex file')
	parser.add_argument('-b','--bibfile',default="general.bib",
		help='input bib file (Default = "general.bib")')
	parser.add_argument('-o','--output',default="output.bib",
		help='output bib file (Default = "output.bib")')

	return parser.parse_args()

def get_cite_list(fname):
	cite_list = []
	ind_cite_list = []
	for line in open(fname):
		match_cites = re.findall(r"\\cite[a-z]*\{(.*?)\}",line)
		cite_list += match_cites
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

def make_reduced_bib(cite_list,bib_file,output_file):
	with open(output_file,'w') as f:
		for cite in cite_list:
			f.write(bib_file.get(cite,"")+'\n')


def main(input_file,output_file,bibfile):
	cite_list = get_cite_list(input_file)
	parsed_bibfile = parse_bib(bibfile)
	make_reduced_bib(cite_list, parsed_bibfile, output_file=output_file)

if __name__ == "__main__":
	args = get_args()
	main(input_file=args.input,output_file=args.output,bibfile=args.bibfile)

