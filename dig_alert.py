import urllib2, json, sys, csv, re, time


txtfileobj = sys.path[0] + '/StandardTicketExample.txt'
#txtfileobjout = sys.path[0] + '/StandardTicketExample-out.txt'

csvfileobj = open(sys.path[0] + '/StandardTicketExample-temp.csv', "wb")
outputCsv = csv.writer(csvfileobj)


listofFields = [
# "tixnum", 
# "operator",
# "startdate", 
# "startime", 
# "calldate",
# "calltime", 
# "transmitdate", 
# "transmittime", 
"latNW",
"lngNW",
"latSE",
"lngSE"]

coordList = []
with open(txtfileobj, 'r') as f:
	for line in f:
		matchLatNW = re.search(r"Latitude NW  (\d+.\d+)", line)
		if matchLatNW:
			coordList.append(matchLatNW.group(0))
		matchLatNW = re.search(r"Longitude NW  (-\d+.\d+)", line)
		if matchLatNW:
			coordList.append(matchLatNW.group(0))
		matchLatNW = re.search(r"Latitude SE  (\d+.\d+)", line)
		if matchLatNW:
			coordList.append(matchLatNW.group(0))
		matchLatNW = re.search(r"Longitude SE  (-\d+.\d+)", line)
		if matchLatNW:
			coordList.append(matchLatNW.group(0))
print coordList


outputCsv.writerow(listofFields)

outputRow = [
coordList[0].strip('Latitude NW  '),
coordList[1].strip('Longitude NW  '),
coordList[2].strip('Latitude SE  '),
coordList[3].strip('Longitude SE  '),
]

outputCsv.writerow(outputRow)



# with open(txtfileobj, 'rb') as infile:#, open(txtfileobjout, 'w') as outfile:
#     for line in infile:
# 		re1 = re.search(r"Latitude NW (\d+)", line)
# 		yo = re1.group(0)

# 		print yo

#lineList = []

       		
       	#if 'str' in line:
          	#break

#print coordList

#print lineList

# with open(txtfileobj, 'rb') as infile, open(txtfileobjout, 'w') as outfile:
#     copy = False
#     for line in infile:
#         if line.strip() == "Latitude NW":
#             copy = True
#         elif line.strip() == "Longitude SE":
#             copy = False
#         elif copy:
#             outfile.write(line)
# import re
# import csv

# username = "Latitude NW"

# with open(txtfileobj, 'rt') as f:
#      #reader = csv.reader(f, delimiter=',') # good point by @paco
#     match = re.search('Latitude NW', f)


    # for row in f:
    # 	if field == username:
    # 		print "is in file"



# match = re.search(r'Latitude NW', str)
# # If-statement after search() tests if it succeeded
#   if match:                      
#     print 'found', match.group() ## 'found word:cat'
#   else:
#     print 'did not find'

#reader = csv.reader(txtfileobj)

#print reader[10]

#re1 = re.search(r"Latitude NW (\d+)", txtfileobj)
#print re1

#with open(intxt, 'rb') as f, open(outcsv, "wb") as out_file: