import os
import json
import yaml
import shutil


def datasetConvertor(dataset: str, output: str):
    """
    This function takes a dataset of format Datumaro 1.0 and converts it to YOLOv8 txt format that can be used to train the model.
    The function takes the dataset path as input and returns the converted dataset path in the required format.
    """
    
    # make a directory to store the converted dataset
    os.makedirs(output, exist_ok=True)
    os.makedirs(output+"/test", exist_ok=True)
    os.makedirs(output+"/train", exist_ok=True)
    os.makedirs(output+"/valid", exist_ok=True)
    os.makedirs(output+"/test/images", exist_ok=True)
    os.makedirs(output+"/train/images", exist_ok=True)
    os.makedirs(output+"/valid/images", exist_ok=True)
    os.makedirs(output+"/test/labels", exist_ok=True)
    os.makedirs(output+"/train/labels", exist_ok=True)
    os.makedirs(output+"/valid/labels", exist_ok=True)
    
    # check if the dataset exists
    if not os.path.exists(dataset):
        raise Exception("The dataset folder "+dataset+" does not exist")
    # check if the annotations folder exists
    if not os.path.exists(os.path.join(dataset, "annotations")):
        raise Exception("The annotations folder is missing in the dataset folder")
    # check if the images folder exists
    if not os.path.exists(os.path.join(dataset, "images")):
        raise Exception("The images folder is missing in the dataset folder")
    
    try:
        # get the test.json file from the dataset/annotations folder
        testPath = os.path.join(dataset, "annotations", "test.json")
        testData = json.loads(open(testPath, "r").read())
    except:
        raise Exception("The test.json file is missing in the "+dataset+"/annotations folder")
    try:
        # get the train.json file from the dataset/annotations folder
        trainPath = os.path.join(dataset, "annotations", "train.json")
        trainData = json.loads(open(trainPath, "r").read())
    except:
        raise Exception("The train.json file is missing in the "+dataset+"/annotations folder")
    try:
        # get the val.json file from the dataset/annotations folder
        valPath = os.path.join(dataset, "annotations", "val.json")
        valData = json.loads(open(valPath, "r").read())
    except:
        raise Exception("The val.json file is missing in the "+dataset+"/annotations folder")
    
    # copy the images to the output folder
    try:
        testImages = os.listdir(os.path.join(dataset, "images", "test"))
        for img in testImages:
            shutil.copy(os.path.join(dataset, "images", "test", img), os.path.join(output, "test", "images", img))
    except:
        raise Exception("Error copying the test images to the "+output+" folder")
    try:
        trainImages = os.listdir(os.path.join(dataset, "images", "train"))
        for img in trainImages:
            shutil.copy(os.path.join(dataset, "images", "train", img), os.path.join(output, "train", "images", img))
    except:
        raise Exception("Error copying the train images to the "+output+" folder")
    try:
        valImages = os.listdir(os.path.join(dataset, "images", "val"))
        for img in valImages:
            shutil.copy(os.path.join(dataset, "images", "val", img), os.path.join(output, "valid", "images", img))
    except:
        raise Exception("Error copying the val images to the "+output+" folder")

    # create the labels for the test images
    try:
        for image in testData["items"]:
            fileName = image["id"]
            with open(os.path.join(output, "test", "labels", fileName+".txt"), "w") as labelFile:
                for annotation in image["annotations"]:
                    points = ""
                    count = 0
                    for point in annotation["points"]:
                        if count%2 == 0:
                            point = point/image["image"]["size"][1]
                        else:
                            point = point/image["image"]["size"][0]
                        points += str(point)+" "
                        count += 1
                    labelFile.write(str(annotation["label_id"])+" "+points+"\n")
    except:
        raise Exception("Error creating the labels for the test images")
    # create the labels for the train images
    try:
        for image in trainData["items"]:
            fileName = image["id"]
            with open(os.path.join(output, "train", "labels", fileName+".txt"), "w") as labelFile:
                for annotation in image["annotations"]:
                    points = ""
                    count = 0
                    for point in annotation["points"]:
                        if count%2 == 0:
                            point = point/image["image"]["size"][1]
                        else:
                            point = point/image["image"]["size"][0]
                        points += str(point)+" "
                        count += 1
                    labelFile.write(str(annotation["label_id"])+" "+points+"\n")
    except:
        raise Exception("Error creating the labels for the train images")
    # create the labels for the val images
    try:
        for image in valData["items"]:
            fileName = image["id"]
            with open(os.path.join(output, "valid", "labels", fileName+".txt"), "w") as labelFile:
                for annotation in image["annotations"]:
                    points = ""
                    count = 0
                    for point in annotation["points"]:
                        if count%2 == 0:
                            point = point/image["image"]["size"][1]
                        else:
                            point = point/image["image"]["size"][0]
                        points += str(point)+" "
                        count += 1
                    labelFile.write(str(annotation["label_id"])+" "+points+"\n")
    except:
        raise Exception("Error creating the labels for the val images")

    try:
        # create data.yaml file
        classes = [label["name"] for label in trainData["categories"]["label"]["labels"]]
        currentPath = os.getcwd()
        configData = {
            "train": currentPath+"/"+output+"/train/images",
            "val": currentPath+"/"+output+"/valid/images",
            "test": currentPath+"/"+output+"/test/images",
            "nc": len(classes),
            "names": classes
        }
        yaml_data = yaml.dump(configData)
        with open(output+'/data.yaml', 'w') as yaml_file:
            yaml_file.write(yaml_data)
    except:
        raise Exception("Error creating the data.yaml file")
    return dataset

datasetConvertor("./temp/Data", "./temp/output")