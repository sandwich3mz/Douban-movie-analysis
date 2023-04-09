from scrapy.cmdline import execute
import sys
import os

# 到服务器保证路径一致
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute("scrapy crawl DouBanMovie".split())
