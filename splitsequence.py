seq="split.txt"
f_res=open("outsplit.txt",'w')
line1=[]
name_=[]
result=[]
ENSG=[]
with open(seq) as file_in:
	for line in file_in:
		line1=[line.replace("\t","\n")]
		for line2 in line1:
			line3=line2.strip().split("\n")
			length=line3[1]
			for i in range(0,len(length),10):
				result=[line3[0],length[i:i+10]]
				if result[0] not in ENSG:
					ENSG.append(result[0])
				else:
					ENSG.append(result[1])
for seqq in ENSG:
	seqq1=seqq.strip()
	f_res.write(seqq1+"\n")

f_res.close()	
		

			