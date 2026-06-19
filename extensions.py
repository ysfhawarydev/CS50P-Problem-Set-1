x = input("File name: ")

if x.endswith("gif") :
    print("image/gif")

elif x.endswith("jpg") :
    print("image/jpeg")

elif x.endswith("jpeg") :
    print("image/jpeg")    

elif x.endswith("png") :
    print("application/png")

elif x.endswith("pdf") :
    print("application/pdf")

elif x.endswith("txt") :
    print("application/txt")

elif x.endswith("zip") :
    print("application/zip")

else :
    print("application/octet-stream")