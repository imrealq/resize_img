import os
from PIL import Image

root_folder = os.getcwd()

# open folder contain file image if not had create one
source_folder_path = os.path.join(root_folder, "source_imgs")
os.chdir(source_folder_path)

# collect all images name
imgs_name =  os.listdir(source_folder_path)

# resize image
img_name = "3.jpg"
not_resized_img = Image.open(img_name)
resized_img = not_resized_img.resize((98, 152))


# save image in result folder if not had create one
result_folder_path = os.path.join(root_folder, "result_imgs")
os.chdir(result_folder_path)

## check file if exist, name have extend number

resized_img.save("resized_" + img_name)