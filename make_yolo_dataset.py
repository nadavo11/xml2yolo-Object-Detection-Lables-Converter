import os
import shutil

from sklearn.model_selection import train_test_split

from xml2yolo import xml2yolo


def split_dataset():
    # Read images and annotations
    images = [os.path.join('yolo/mydata/images', x) for x in os.listdir('yolo/mydata/images')]
    annotations = [os.path.join('yolo/mydata/labels', x) for x in os.listdir('yolo/mydata/labels') if x[-3:] == "txt"]

    images.sort()
    annotations.sort()

    # Split the dataset into train-valid-test splits
    train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size=0.2,
                                                                                    random_state=1)
    val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations,
                                                                                  test_size=0.5, random_state=1)

    return train_images, val_images, train_annotations, val_annotations,val_images, test_images, val_annotations, test_annotations


#Utility function to move images
def move_files_to_folders(list_of_files, destination_folder):
    os.mkdir(destination_folder)
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False



def make_yolo_dataset():

    xml2yolo()

    train_images, val_images, train_annotations, val_annotations,val_images, test_images, val_annotations, test_annotations = split_dataset()

    # Move the splits into their folders
    move_files_to_folders(train_images, 'images/train')
    move_files_to_folders(val_images, 'images/val/')
    move_files_to_folders(test_images, 'images/test/')
    move_files_to_folders(train_annotations, 'labels/train/')
    move_files_to_folders(val_annotations, 'labels/val/')
    move_files_to_folders(test_annotations, 'labels/test/')

make_yolo_dataset()