
###### rename ######
# import os
# folder_path = '/home/isuzu/Desktop/adaptor1_kitti_dataset_fromWAymo_val0000/label_all' 
# file_list = os.listdir(folder_path)
# os.chdir(folder_path)

# for old_name in file_list:
#     if old_name[-3:] != 'txt':
#       continue
#     new_name = old_name[-10:]
#     print(old_name)
#     print(new_name)

#     os.rename(old_name, new_name)

###### jpg->png ######
import os
from PIL import Image
import shutil
import sys
 
# Define the input and output image
output_dirHR = '/home/isuzu/Desktop/adaptor1_kitti_dataset_fromWAymo_val0000/image_2'
output_dirLR = '/home/isuzu/Desktop/adaptor1_kitti_dataset_fromWAymo_val0000/image_2'
if not os.path.exists(output_dirHR):
    os.mkdir(output_dirHR)
if not os.path.exists(output_dirLR):
    os.mkdir(output_dirLR)
 
 
 
def image2png(dataset_dir,type):
    files = []
    image_list = os.listdir(dataset_dir)
    files = [os.path.join(dataset_dir, _) for _ in image_list]
    for index,jpg in enumerate(files):
        print('index')
        print(index)
        print('jpg')
        print(jpg)
        try:
            sys.stdout.write('\r>>Converting image %d/100000 ' % (index))
            sys.stdout.flush()
            im = Image.open(jpg)
            png = os.path.splitext(jpg)[0] + "." + type
            im.save(png)
            os.unlink(jpg)
            '''
            if jpg.split('.')[-1] == 'jpg':
                shutil.move(png,output_dirLR)
            else:
                shutil.move(png,output_dirHR)
            '''
            shutil.move(png, output_dirHR)
        except IOError as e:
            print('could not read:',jpg)
            print('error:',e)
            print('skip it\n')
 
    sys.stdout.write('Convert Over!\n')
    sys.stdout.flush()
 
 
 
if __name__ == "__main__":
    current_dir = os.getcwd()
    print(current_dir)  # /Users/gavin/PycharmProjects/pygame
    data_dir = '/home/isuzu/Desktop/adaptor1_kitti_dataset_fromWAymo_val0000/image_2'
 
    image2png(data_dir,'png')


##### create omittedd label files ####
# import os
# folder_path = '/home/isuzu/Desktop/PCDet/data/kitti/training/label_2/'
# # folder_path = '/home/isuzu/Desktop/test_addingFIles/'
# file_list = os.listdir(folder_path)
# os.chdir(folder_path)

# for i in range(1320,1389):
#     len_i = len(str(i))
#     zeros = '0'
#     zeros = zeros * (6 - len_i)
#     file_name = zeros + str(i) + '.txt'
#     try:
#         os.open(folder_path + file_name, os.O_RDONLY)
#     except IOError as e:
#         print(file_name)
#         os.mknod(folder_path + file_name)