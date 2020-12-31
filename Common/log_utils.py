import logging,os,time
now_time=time.strftime('%Y-%m-%d')
current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,'../Logs/all_logs_{}.log'.format(now_time))
class Logging():
    def __init__(self,log_path=log_path):
        self.log_path=log_path
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.INFO)
        fh=logging.FileHandler(log_path,encoding='utf-8')
        formater=logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        fh.setFormatter(formater)
        self.logger.addHandler(fh)
    def info(self,a):
        self.logger.info(a)
    def error(self,a):
        self.logger.error(a)
logger=Logging()

if __name__ == '__main__':
    logger.info('123')
