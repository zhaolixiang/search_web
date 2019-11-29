from configparser import ConfigParser

config = ConfigParser()
config.read('push_config.ini', 'utf-8')
target = config.get('bd_push', 'target').split(',')
# 150.109.181.169 root 1q2w3eAA$
print(target)