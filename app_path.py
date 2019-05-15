import os


class AppPath:
    """
    项目路径工具类
    """

    path_sep = os.path.sep

    @staticmethod
    def get_project_root_path():
        root_dir = os.path.dirname(os.path.abspath(__file__))
        return root_dir

    @staticmethod
    def get_conf_path():
        return '{0}/config/dev'.format(AppPath.get_project_root_path()).replace('/', AppPath.path_sep)

    @staticmethod
    def get_ini_file_path():
        return '{0}/sys_conf.ini'.format(AppPath.get_conf_path()).replace('/', AppPath.path_sep)



