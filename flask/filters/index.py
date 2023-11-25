from flask import Flask
from datetime import datetime

class MyFilter:
  """
  自定义的过滤器
  """
  def __init__(self,app:Flask) -> None:
      self.app = app
      
      @self.app.template_filter('cut')
      def cut(val:str):
        # self.my_cut_test(val)
        return val.replace('444','****')
      
      # 自定义时间过滤器
      @self.app.template_filter('handle_time')
      def handle_time(val:datetime):
        """
        1分钟内---刚刚
        小于1h---xx分钟前
        小于24h---xx小时前
        小于30天---xx天前
        否则很久以前
        """
        time_now = datetime.now()
        # 换算成秒数进行计算
        seconds = (time_now - val).total_seconds()
        if seconds<60:
          return '1分钟内'
        elif seconds<60*60:
          return f'{int(seconds/60)}分钟前'
        elif seconds<60*60*24:
          return f'{int(seconds/60/60)}小时前'
        elif seconds<60*60*24*30:
          return f'{int(seconds/60/60/24)}天前'
        else:
          return '很久以前'

  def my_cut_test(self,val:str):
    print(val)