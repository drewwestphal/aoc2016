#!/usr/bin/python

import re
import itertools

class ip7addr:
	
	def __init__(self, str):
		self.str = str
		#assume all begins with addr seq
		split = re.split(r"[\[\]]",self.str)
		self.addr_seqs = [split[i] for i in range(0,len(split),2)]
		self.hyper_seqs = [split[i] for i in range(1,len(split),2)]

	@staticmethod
	def abbaSequences(sequence):
		return [sequence[i-3:i+1] for i in range(3,len(sequence)) 
			if sequence[i-3]==sequence[i] and sequence[i-2]==sequence[i-1] and sequence[i]!=sequence[i-1]]

	@staticmethod
	def abaCandidates(sequence):
		return [sequence[i-2:i+1] for i in range(2,len(sequence)) 
			if sequence[i-2]==sequence[i] and sequence[i-1] != sequence[i]]

	@staticmethod
	def babMirror(aba):
		return aba[1]+aba[0]+aba[1];

	def isTLSEnabled(self):
		# we need to get back positive abba from addr and negative from hyper
		return len(filter(lambda seq: ip7addr.abbaSequences(seq), self.addr_seqs))>0 \
			and len(filter(lambda seq: ip7addr.abbaSequences(seq), self.hyper_seqs))==0
		
	def isSSLEnabled(self):
		targetbab = [ip7addr.babMirror(aba) for aba in\
		 itertools.chain(*[ip7addr.abaCandidates(addrseq) for addrseq in self.addr_seqs])]
		 
		return bool([bab for bab in itertools.chain(*[ip7addr.abaCandidates(hyper_seq)\
		 for hyper_seq in self.hyper_seqs]) if bab in targetbab])
	

#tests

print "test abba seq"
print ip7addr.abbaSequences('abba');
print ip7addr.abbaSequences('assadsfbbaabbba');
print ip7addr.abbaSequences('xxxxxabbaxxx');

print "test tls"
print ip7addr('abba[mnop]qrst').isTLSEnabled()
print ip7addr('abcd[bddb]xyyx').isTLSEnabled()
print ip7addr('aaaa[qwer]tyui').isTLSEnabled()
print ip7addr('ioxxoj[asdfgh]zxcvbn').isTLSEnabled()

print "test aba"
print ip7addr.abaCandidates('abaaaaaba');
print ip7addr.abaCandidates('sadfadsfasdfaxyxasssssss');

print "test ssl"
print ip7addr('aba[bab]xyz').isSSLEnabled()
print ip7addr('xyx[xyx]xyx').isSSLEnabled()
print ip7addr('aaa[kek]eke').isSSLEnabled()
print ip7addr('zazbz[bzb]cdb').isSSLEnabled()
print ip7addr('zazbz[bzb]cdbzazbz[bzb]cdb').isSSLEnabled()


data = open('./7input.txt')

tls = 0
ssl = 0
for line in data:
	addr = ip7addr(line.strip())
	tls += 1 if addr.isTLSEnabled() else 0
	ssl += 1 if addr.isSSLEnabled() else 0
	
print '%d support tls' % tls
print '%d support ssl' % ssl