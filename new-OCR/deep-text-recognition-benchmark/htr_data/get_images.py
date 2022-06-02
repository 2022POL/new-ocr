import shutil

data_root_path = '../../kor_dataset/aihub_data/htr/images/'
save_root_path = './images/'

# copy images from dataset directory to current directory
shutil.copytree(data_root_path, save_root_path)

# separate dataset : train, validation, test
obj_list = ['train', 'test', 'validation']
for obj in obj_list:
  with open(f'gt_{obj}.txt', 'r') as f:
    lines = f.readlines()
    # print(lines)
    for line in lines:
      # print(line)
      file_path = line.split('.png')[0]
      # print(file_path)
      file_name = file_path.split('/')[1] + '.png'
      # print(file_name)
      res = shutil.move(save_root_path+file_name, f'./{obj}/')
