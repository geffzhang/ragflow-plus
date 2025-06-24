# RAGFlow 服务器启动指南

本文档介绍如何使用 gunicorn/waitress 启动 RAGFlow 服务器，以替代开发服务器。

## 安装依赖

首先，确保安装了所需的依赖：

```bash
pip install -r requirements.txt
```

这将安装 gunicorn（用于 Linux/macOS）和 waitress（用于 Windows）。

## 启动服务器

### 使用新的启动脚本

我们提供了一个统一的启动脚本，可以自动检测操作系统并使用适当的服务器：

```bash
python start_server.py
```

### 启动选项

启动脚本支持以下选项：

- `--version`: 显示 RAGFlow 版本
- `--debug`: 以调试模式运行
- `--dev`: 使用 Flask 开发服务器而不是 gunicorn/waitress

例如，以调试模式运行：

```bash
python start_server.py --debug
```

使用开发服务器运行：

```bash
python start_server.py --dev
```

### 直接使用 gunicorn（仅限 Linux/macOS）

如果你想直接使用 gunicorn 命令，可以这样做：

```bash
gunicorn -c gunicorn_config.py api.ragflow_server:application
```

### 自定义配置

如果需要自定义 gunicorn 配置，可以编辑 `gunicorn_config.py` 文件。

## 生产环境部署建议

在生产环境中部署时，建议：

1. 调整 `gunicorn_config.py` 中的工作进程数和连接数
2. 考虑使用 Nginx 或 Apache 作为前端代理
3. 设置适当的日志轮转
4. 使用进程管理工具（如 systemd、Supervisor 等）管理服务器进程

## 故障排除

如果遇到启动问题：

1. 检查日志文件（位于 `logs` 目录）
2. 确保所有依赖都已正确安装
3. 验证配置文件中的 IP 和端口设置