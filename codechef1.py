try:
	# cook your dish here
	for _ in range(int(input())):
		days=int(input())
		attendence=list(input())
		count=dict((('P',0),('A',0)))
		for val in attendence:
			if val in 'PA':
				count[val]+=1
		percent=(count['P']*100)/days
		# print(percent)
		proxy_needed=0
		# while percent<75:
		#     proxy_needed+=1
		#     percent = ((count['P']+proxy_needed) * 100) / days
		# input(proxy_needed)
		#
		d=0
		final=0
		while(percent<75):
			for idx,val in enumerate(attendence[d+2:-2]):
				if val == 'A':
					# attendence[idx+2]='P'
					d=idx
					break
			count = dict((('P', 0), ('A', 0)))
			for val in attendence:
				if val in 'PA':
					count[val] += 1
			# print(percent)
			# print(attendence)
			proxy_needed+=1
			percent = ((count['P'] + proxy_needed) * 100) / days
			# print(proxy_needed)
			# print(attendence)
			final+=1
		print(final)
except:
	pass