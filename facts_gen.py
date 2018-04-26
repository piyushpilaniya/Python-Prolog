import yaml

def yaml_loader(filepath):
	with open(filepath,"r") as fp:
		data = yaml.load_all(fp.read().replace('\n\n','\n---\n'))
	return data
	
def yaml_dump(filepath,data):
	with open(filepath,"w") as file_descriptor:
		yaml.dump(data,file_descriptor)

if __name__ == "__main__":

	data = yaml_loader("new.yaml")

	fp = open("facts_and_rules.pl","w+")

	for i in data:
		for key,value in i.items():
			if key=="OS":
				fp.write("%s(" % key.lower())
				for key2,value2 in value.items():
					if key2=="limits":
						for key3,value3 in value2.items():
							fp.write("%s," % value3)
					elif key2=="arch":
						ind=0
						for index in value2:
							ind=ind+1
							if index==" ":
								break
						newval = value2[0:ind-1]		
						fp.write("%s," % newval)
					elif key2=="id":
						fp.write("%s" % value2)
					elif key2=="name":
						fp.write("%s," % value2.lower())	
					else:
						fp.write("%s," % value2)
				fp.write(").\n")		

			if key=="Machine":
				fp.write("%s(" % key.lower())
				for key2,value2 in value.items():
					if key2=="disk":
						ind=0
						for index in value2:
							ind=ind+1
							if index==" ":
								break

						if value2[ind]=='G':
							newval = value2[0:ind-1]		
							fp.write("%s," % newval)			
						else:
							newval = value2[0:ind-1]		
							intp = int(newval)
							intp = intp*1024
							newstr = str(intp)
							fp.write("%s," % newstr)		

					elif key2=="RAM":
						ind=0
						for index in value2:
							ind=ind+1
							if index==" ":
								break
						if value2[ind]=='M':
							newval = value2[0:ind-1]		
							fp.write("%s," % newval)			
						else:
							newval = value2[0:ind-1]		
							intp = int(newval)
							intp = intp*1024
							newstr = str(intp)
							fp.write("%s," % newstr)
					elif key2=="CPU":
						ind=0
						for index in value2:
							ind=ind+1
							if index==" ":
								break
						newval = value2[0:ind-1]		
						fp.write("%s," % newval)
					elif key2=="type":
						fp.write("%s," % value2.lower())	
					elif key2=="id":
						fp.write("%s" % value2)	
					else:
						fp.write("%s," % value2)	
				fp.write(").\n")		

			if key=="SoftwareApp":
				fp.write("%s(" % key.lower())
				for key2,value2 in value.items():
					if key2=="name":
						value2 = value2.lower()
						newval = value2.replace(" ","+")	
						fp.write("%s," % newval)
					if key2=="requires_software":
						for key3,value3 in value2.items():
							fp.write("%s," % value3)
					if key2=="requires_hardware":
						for key3,value3 in value2.items():
							ind=0
							for index in value3:
								if index==' ':
									break
								ind=ind+1	

							newval=value3[0:ind]		
							fp.write("%s," % newval)
					if key2=="id":
						fp.write("%s"%value2)			
				fp.write(").\n")			

						
fp.write("\n")

fp.write("compare(P,I) :- P=<I.\n")
fp.write("all_from_first_in_second(List1, List2) :-\n")
fp.write("    forall(member(Element,List1), member(Element,List2)).\n\n")					
fp.write("list(S) :- softwareapp(_,L,O,D,C,R,S),member(O1,O),machine(Da,O1,Ra,_,Cp,Y),compare(R,Ra),compare(D,Da),compare(C,Cp),os(_,_,_,_,L1,_,O1),all_from_first_in_second(L,L1),writeln(Y).\n")
fp.write("newlist(S,Y) :- softwareapp(_,L,O,D,C,R,S),member(O1,O),machine(Da,O1,Ra,_,Cp,Y),compare(R,Ra),compare(D,Da),compare(C,Cp),os(_,_,_,_,L1,_,O1),all_from_first_in_second(L,L1),writeln(Y).\n")
					
			



