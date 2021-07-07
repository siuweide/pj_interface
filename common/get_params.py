
import os
import yaml

# 获取文件下的所有子文件

project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
params_dir = os.path.join(project_root, 'params')

dir_or_files = os.listdir(params_dir)
for dir_file in dir_or_files:
    dir_file_path = os.path.join(project_root, params_dir, dir_file)
    if os.path.isdir(dir_file_path):
        for root, dirs, files in os.walk(dir_file_path):
            for name in files:
                watch_file_path = os.path.join(root, name)
                with open(watch_file_path, encoding='utf-8') as f:
                    page = yaml.safe_load(f)
                    print(page)