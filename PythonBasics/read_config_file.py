import sys
from configparser import ConfigParser


def get_configs(config_file):
    config = ConfigParser()
    config.read(config_file)
    return config


def main():
    print('Inside Main Function')
    config_file_path = sys.argv[1]
    configs = get_configs(config_file=config_file_path)
    test_conf = configs.get("default", "aaa")
    print('test_conf - {}'.format(test_conf))


if __name__ == '__main__':
    main()
