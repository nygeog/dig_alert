import os, sys, string, re, arcgisscripting

Message = sys.argv[1]
Ticket = 'NA'
PTicket = 'NA'
Header = 'NA'

try:
    f = open(Message, 'r')
    data = f.readlines()
    f.close()
##    outname = r"C:\data\success.txt"
##    outfile = open(outname, 'w')
##    outfile.write("Success in reading " + Message)
##    outfile.close()
    for line in data:
        mTicket = re.search(r"Ticket #:  (\S+)", line)
        if mTicket:
            Ticket = mTicket.group(0).strip(r"Ticket #: ")
        mPTicket = re.search(r"Previous Ticket #:  (\S+)", line)
        if mPTicket:
            PTicket = mPTicket.group(0).strip(r"Previous Ticket #: ")
        mHeader = re.search(r"Header:  (\S+)", line)
        if mHeader:
            Header = mHeader.group(0).strip(r"Header:  ")
        mSDate = re.search('Start Date.+', line)
        if mSDate:
            SDate = mSDate.group(0)[16:26]
            STime = mSDate.group(0)[-11:]
        mCDate = re.search('Call Date.+', line)
        if mCDate:
            CDate = mCDate.group(0)[16:26]
            CTime = mCDate.group(0)[-11:]
        mYMax = re.search('Latitude NW  \S+', line)
        if mYMax:
            YMax = mYMax.group(0).strip('Latitude NW  ')
        mXMax = re.search('Longitude NW  \S+', line)
        if mXMax:
            XMax = mXMax.group(0).strip('Longitude NW  ')
        mYMin = re.search('Latitude SE  \S+', line)
        if mYMin:
            YMin = mYMin.group(0).strip('Latitude SE  ')
        mXMin = re.search('Longitude SE  \S+', line)
        if mXMin:
            XMin = mXMin.group(0).strip('Longitude SE  ')

    gp = arcgisscripting.create(9.3)
    gp.OverWriteOutput = 1
    ary = gp.createobject("Array")
    pnt = gp.createobject("Point")

    #Lower left
    pnt.x = XMax
    pnt.y = YMin
    ary.add(pnt)

    #Upper left
    pnt.x = XMax
    pnt.y = YMax
    ary.add(pnt)

    #Upper right
    pnt.x = XMin
    pnt.y = YMax
    ary.add(pnt)

    #Lower right
    pnt.x = XMin
    pnt.y = YMin
    ary.add(pnt)

    #Close the poly - Lower left again
    pnt.x = XMax
    pnt.y = YMin
    ary.add(pnt)

    #OneCall polygon feature class must exist
    OneCall = r"C:\data\onecall_poly.shp"

    cur = gp.InsertCursor(OneCall)
    feat = cur.NewRow()
    feat.shape = ary
    feat.Ticket = Ticket
    feat.PTicket = PTicket
    feat.Header = Header
    feat.SDate = SDate
    feat.STime = STime
    feat.CDate = CDate
    feat.CTime = CTime
    feat.Link = Message.replace(r"/",'\\')
    cur.InsertRow(feat)
except:
    outname = r"C:\data\failure.txt"
    outfile = open(outname, 'w')
    outfile.write("Failed in reading " + Message)
    outfile.close()