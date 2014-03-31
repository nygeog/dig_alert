dig_alert
=========

dig alert via email

Complete:
--------

1) scrape lat, longs

To Do:
------

(1) Grab other attributes from email txt

(2) Create table

(3) Create bounding box from table





The first part of this solution is to make a rule in Outlook to 'run a script' when I get an email from Digger's Hotline.  You have to add the following vba code in Outlook:

Sub DiggersMailMessageRule(Item As Outlook.MailItem)
    Dim str_file As String
    Dim str_subj As String
    str_subj = Replace(Item.Subject, " ", "_")
    str_file = "C:/data/" & str_subj & ".txt"
    Item.SaveAs str_file, olTXT
    Dim py_file As String
    py_file = "C:\Python25\python.exe " & "C:\data\DiggersMailMessageScript.py " & Chr(34) & str_file & Chr(34)
    
    Dim wsh As WshShell
    Set wsh = VBA.CreateObject("WScript.Shell")
    Dim waitOnReturn As Boolean: waitOnReturn = True
    Dim windowStyle As Integer: windowStyle = 1
    Dim errorCode As Integer
    
    errorCode = wsh.Run(py_file, windowStyle, waitOnReturn)
    
    If errorCode = 0 Then
        MsgBox "Done! No error to report."
    Else
        MsgBox "Program exited with error code " & errorCode & "."
    End If
    
End Sub

The first part just replaces the spaces of the email's subject line with underscores, saves the email as a text file, and sets the name of the text file as a parameter for the python script.  The second part of the vba code calls the python script and waits for it to finish.

I've attached the python script.  The first part of that just searches and extracts the info I need and the second part writes that info to an existing shapefile.  It was written to work with 9.3.  If it was written for 10x, I'm sure that last part would be shorter.

It's not commented very well but it works.

