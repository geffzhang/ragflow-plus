#!/usr/bin/env python
import os
import sys
import argparse
import subprocess
from api.versions import get_ragflow_version

def main():
    parser = argparse.ArgumentParser(description="RAGFlow Server Launcher")
    parser.add_argument("--version", action="store_true", help="Show RAGFlow version")
    parser.add_argument("--debug", action="store_true", help="Run in debug mode")
    parser.add_argument("--dev", action="store_true", help="Use Flask development server instead of gunicorn")
    args = parser.parse_args()

    if args.version:
        print(f"RAGFlow version: {get_ragflow_version()}")
        sys.exit(0)

    # 确保日志目录存在
    os.makedirs("logs", exist_ok=True)

    # 设置环境变量
    if args.debug:
        os.environ["RAGFLOW_DEBUG"] = "1"

    if args.dev:
        # 使用Flask开发服务器
        print("Starting RAGFlow with Flask development server...")
        from api.ragflow_server import init_app
        app = init_app(debug=args.debug)
        from api import settings
        app.run(host=settings.HOST_IP, port=settings.HOST_PORT, debug=args.debug)
    else:
        # 使用gunicorn
        print("Starting RAGFlow with gunicorn server...")
        cmd = [
            "gunicorn",
            "-c", "gunicorn_config.py",
            "api.ragflow_server:application"
        ]
        
        # 如果是Windows系统，使用waitress替代gunicorn
        if sys.platform.startswith('win'):
            print("Windows detected, using waitress instead of gunicorn...")
            from waitress import serve
            from api.ragflow_server import application
            from api import settings
            print(f"Starting server on {settings.HOST_IP}:{settings.HOST_PORT}")
            serve(application, host=settings.HOST_IP, port=settings.HOST_PORT)
        else:
            # 在非Windows系统上使用gunicorn
            subprocess.run(cmd)

if __name__ == "__main__":
    main()