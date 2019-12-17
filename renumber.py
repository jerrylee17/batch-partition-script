from PIL import Image
import os, sys

# Base path here, outside the all images folder
basepath = "/home/ubuntu/poles-dataset/Labeling/AllImagesFolder/"
# imagesFolder = "Allimages/"

def regroup(path):
    counter, batch = 0, 1
    # first batch directory
    os.mkdir(path+"batch1")
    # grab all imaes
    allimages = os.listdir(basepath+"Allimages")
    for image in allimages:
        # 100 in each batch at most
        if counter >= 100:
            batch += 1
            counter = 0
            # make new directory
            os.mkdir(path+"batch"+str(batch))
        try:
            # get iamge
            im = Image.open(path+"Allimages/"+image)
            # new name
            newName = path+"batch"+str(batch)+\
                "/"+"num"+str(counter) + ".jpg"
            
            # save with new name
            im.save(newName, "JPEG", quality=90)
            print ("Successfully saved: " + newName)
            counter += 1
        except:
            with open("failed.txt", "w") as f:
                f.write("Failed: "+ image + "\n")
            print("Failed to save: "+image)




regroup(basepath)