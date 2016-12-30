#!/usr/bin/python
import md5

idx=0
input='abbhdwsy'
passwd=list('xxxxxxxx')
while True:
	hashstr = input+str(idx)
	digest=md5.new(hashstr).hexdigest()
	idx+=1
	if digest[:5]=='00000':
		pos=int(digest[5:6],16)
		if(pos>7 or passwd[pos] != 'x'):
			continue
		passwd[pos]=digest[6:7]
		passstr = ''.join(passwd)
		print '%d : %s : %s : %s' % (idx, digest, hashstr, passstr)
		if passstr.find('x') == -1:
			break