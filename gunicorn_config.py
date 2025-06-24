# gunicorn_config.py
import multiprocessing
import os
from api import settings

# 绑定的IP和端口
bind = "0.0.0.0:9380"

# 工作进程数
# 建议的工作进程数通常是CPU核心数的2-4倍
workers = multiprocessing.cpu_count() * 2 + 1

# 工作模式
worker_class = "sync"  # 可选: sync, eventlet, gevent, tornado, gthread

# 每个工作进程处理的最大并发请求数
worker_connections = 1000

# 超时时间
timeout = 120

# 重启工作进程前处理的最大请求数
max_requests = 1000
max_requests_jitter = 50

# 日志配置
errorlog = "logs/gunicorn-error.log"
accesslog = "logs/gunicorn-access.log"
loglevel = "info"

# 进程名称
proc_name = "ragflow_gunicorn"

# 守护进程模式
daemon = False

# 预加载应用
preload_app = True

# 确保日志目录存在
os.makedirs("logs", exist_ok=True)