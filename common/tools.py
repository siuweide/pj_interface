
import os
import yaml

class Tools(object):

    project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    params_dir = os.path.join(project_root, 'params')
    dir_or_files = os.listdir(params_dir)

    def parse(self):
        pages = {}
        for dir_file in self.dir_or_files:
            dir_file_path = os.path.join(self.project_root, self.params_dir, dir_file)
            if os.path.isdir(dir_file_path):
                for root, dirs, files in os.walk(dir_file_path):
                    for name in files:
                        watch_file_path = os.path.join(root, name)
                        with open(watch_file_path, encoding='utf-8') as f:
                            page = yaml.safe_load(f)
                            pages.update(page)
        return pages

    def get_page_list(self):
        page_list = {}
        pages = self.parse()
        for page, value in pages.items():
            data_list = []
            parameters = value['parameters']
            for parameter in parameters:
                data_list.append(parameter)
            page_list[page] = data_list
        return page_list


    def get_params(self, page_name):
        params = self.get_page_list()[page_name][0]
        return params

if __name__ == '__main__':
    params = Tools().get_params('LoginSucess')
    print(params['url'])