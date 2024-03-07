import datumaro as dm
import os

dataset = dm.Dataset.import_from("./temp/CvatConvertDataFinal","open_images")
dataset.export("./temp/datayolo","yolo_ultralytics",save_media=True)

print("Suceesss")

# # os.makedirs("temp/Train Demo/yolo/train", exist_ok=True)
# # os.makedirs("temp/Train Demo/yolo/val", exist_ok=True)

# # train_exporter = dm.Exporter("yolo_ultralytics", save_images=False, save_annotations=True)
# # val_exporter = dm.Exporter("yolo_ultralytics", save_images=False, save_annotations=True)

# # train_exporter(dataset=train_subset, save_dir="temp/Train Demo/yolo/train/")
# # val_exporter(dataset=val_subset, save_dir="temp/Train Demo/yolo/val")
# # dm.Dataset.from_iterable(train_subset, source=train_subset).export(
# #     "temp/Train Demo/yolo/train/",
# #     'yolo_ultralytics',
# #     save_images=False,
# #     save_annotations=True,
# # )
# # dm.Dataset.from_iterable(val_subset, source=val_subset).export(
# #     "temp/Train Demo/yolo/val/",
# #     'yolo_ultralytics',
# #     save_images=False,
# #     save_annotations=True,
# # )

# import shutil
# import os

# import shutil
# import os

# def copy_folder(source_folder, destination_folder):
#     try:
#         # Create the destination folder if it doesn't exist
#         if not os.path.exists(destination_folder):
#             os.makedirs(destination_folder)
        
#         # Copy the entire contents of the source folder to the destination folder
#         shutil.copytree(source_folder, os.path.join(destination_folder, os.path.basename(source_folder)))
#         new_folder_path = os.path.join(destination_folder, "dataset1")
#         os.rename(os.path.join(destination_folder, os.path.basename(source_folder)), new_folder_path)
#         print("Folder copied successfully.")
#     except Exception as e:
#         print("Error:", e)

# # Example usage


# # Example usage
# source_folder = 'temp/Annotation Day1(19-02)/2024-02-20-12-41-09/yolo'
# destination_folder = 'temp/'

# copy_folder(source_folder, destination_folder)

