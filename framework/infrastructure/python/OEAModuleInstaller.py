import os
import sys

class OEAModule:
    def __init__(self, module_name, module_path, index):
        self.module_name = module_name
        self.module_path = module_path
        self.index = index

class OEAModuleInstaller:
    def __init__(self, workspace_name, logger):
        self.root_path = os.getcwd()
        self.workspace_name = workspace_name
        self.logger = logger
        self.modules = []

    def list_modules(self):
        dirs = [item  for item in os.listdir(f'{self.root_path}\modules\module_catalog') if os.path.isdir(f'{self.root_path}\modules\module_catalog\{item}')]
        index = 1
        for dir in dirs:
            if(os.path.isfile(f'{self.root_path}\modules\module_catalog\{dir}\install.py')):
                self.modules.append(OEAModule(dir, f'{self.root_path}\modules\module_catalog\{dir}', index))
                index += 1
            else:
                sub_dirs = [item  for item in os.listdir(f'{self.root_path}\modules\module_catalog\{dir}') if os.path.isdir(f'{self.root_path}\modules\module_catalog\{dir}\{item}')]
                for sub_dir in sub_dirs:
                    if(os.path.isfile(f'{self.root_path}\modules\module_catalog\{dir}\{sub_dir}\install.py')):
                        self.modules.append(OEAModule(sub_dir, f'{self.root_path}\modules\module_catalog\{dir}\{sub_dir}', index))
                        index += 1

    def install(self, azure_client):
        self.list_modules()

        self.logger.info('\nHere is the list of modules available.')
        self.logger.info('===================================================\n')
        for module in self.modules:
            self.logger.info(f"{module.index}) {module.module_name}")
        self.logger.info('\n===================================================')
        user_input = input('Enter the serial number corresponding to the module you want to install. Use \";\" to separate multiple entries : ')

        for serial_num in user_input.replace(' ', '').split(';'):
            oea_module = [x for x in self.modules if module.index == int(serial_num)][0]
            self.logger.info(f'Running installation script for {oea_module.module_name} Module.')

            sys.path.append(f"{oea_module.module_path}")
            from install import install
            try:
                install(self.workspace_name, azure_client)
            except Exception as e:
                self.logger.error(f'Failed to install {oea_module.module_name} Module. ERROR : {str(e)}')
            sys.path.remove(f"{oea_module.module_path}")

            # os.system(f"python {oea_module.module_path}/install.py {} {} {self.workspace_name}")
