import os
import time

from media import media
from system.config import config
from system.log import log

if __name__ == '__main__':
    try:
        if 'MEDIASERVERTOOLS_CONFIG' not in os.environ:
            if 'EMBYTOOLS_CONFIG' in os.environ:
                path = os.environ['EMBYTOOLS_CONFIG']
            else:
                path = os.path.join(os.getcwd(), 'config')
            os.environ['MEDIASERVERTOOLS_CONFIG'] = path
            

        path = os.path.join(os.environ['MEDIASERVERTOOLS_CONFIG'], 'config.yaml')
        configinfo = config(path=path)
        mediaclient = media(configinfo=configinfo)
        while True:
            try:
                log().info('开始刷新媒体库元数据')
                mediaclient.start_scan_media()
                log().info('刷新媒体库元数据完成')
                time.sleep(configinfo.systemdata['updatetime'] * 3600)
            except Exception as result:
                log().info(result)
    except Exception as result:
        log().info("文件[{}]行[{}]异常错误：{}".format(result.__traceback__.tb_frame.f_globals["__file__"], result.__traceback__.tb_lineno, result))