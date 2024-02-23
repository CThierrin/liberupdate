import os, liberupdate, liberupdatev2, meichecker

directory = os.fsencode("C:\\Users\\cole_\\Downloads\\liberUsualis - Copy\\liber")
err=""

increment = 0 #for debugging
for mefile in os.listdir(directory):
    filename = os.fsdecode(mefile)
    if filename.endswith("corr.mei"):
        liberupdatev2.main(filename)
        print(filename +" has been updated")
        err= err+ (meichecker.main(filename[:-4]+"NEW2.mei")+"\n")
#        print(err)
        print(filename +" has been checked")
    i++

    if i>=100:
        break
print(err)
