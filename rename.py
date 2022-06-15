import os
#path =  os.getcwd()
path = "./classification/waste/trashnet/trash"
filenames = os.listdir(path)
i = 0
for filename in filenames:
    name = "trash." + str(i) + ".jpg"
    os.rename(os.path.join(path, filename), os.path.join(path, name))
    #os.rename(filename, "ikuta_erika_" + str(i) + ".jpg")
    i += 1
