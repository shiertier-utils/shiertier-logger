# shiertier_logger

[English](https://github.com/shiertier-utils/shiertier_logger/blob/main/README.md) | 中文

## 简介

`shiertier_logger` 是一个 Python 日志工具，旨在简化带有国际化 (i18n) 支持的日志记录。它与 `loguru` 库无缝集成，并提供了一个简单的接口，用于以不同语言记录消息。该库还支持自动日志文件轮换和通过环境变量进行配置。

## 安装

您可以通过 `pip` 安装 `shiertier_logger`：

```bash
pip install git+https://github.com/shiertier/shiertier_logger.git
```

请注意，该项目仍在开发中。

## 使用方法

### 初始化

当您导入模块时，日志记录器会自动初始化。日志文件存储在由 `LOG_DIR` 环境变量指定的目录中，如果未设置 `LOG_DIR`，则默认存储在用户主目录下的 `.shiertier/logs` 目录中。

```python
from shiertier_logger import logger

# 或者使用Logger_I18n, 需要shiertier_i18n支持
from shiertier_logger import easy_logger_i18n
```

### 记录消息

您可以使用 `easy_logger_i18n` 对象记录带有翻译支持的消息：

```python
easy_logger_i18n.info("Hello, world!")
```

您还可以传递一个字典来替换日志消息中的占位符：

```python
easy_logger_i18n.info("Hello, $$name$$!", replace_dict={'$$name$$': 'Alice'})
```

### 可用方法

- `info(message: str, replace_dict: Dict[str, Any] = None) -> None`
- `debug(message: str, replace_dict: Dict[str, Any] = None) -> None`
- `warning(message: str, replace_dict: Dict[str, Any] = None) -> None`
- `error(message: str, replace_dict: Dict[str, Any] = None) -> None`

### 配置

#### 日志目录

默认情况下，日志文件存储在由 `LOG_DIR` 环境变量指定的目录中。如果未设置 `LOG_DIR`，则默认存储在用户主目录下的 `.shiertier/logs` 目录中。

您可以通过设置 `LOG_DIR` 环境变量来指定不同的目录：

```bash
export LOG_DIR=/path/to/logs
```

#### 日志级别

日志级别可以通过 `LOG_LEVEL` 环境变量进行配置。默认的日志级别是 `INFO`。

您可以通过设置 `LOG_LEVEL` 环境变量来指定不同的日志级别：

```bash
export LOG_LEVEL=DEBUG
```

#### 系统输出日志

默认情况下，日志记录器会同时记录到文件和系统输出（stdout）。您可以通过将 `LOG_SYS` 环境变量设置为 `False` 来禁用系统输出日志。

```bash
export LOG_SYS=False
```

## 依赖

- `loguru`
- `shiertier_i18n`（可选，用于翻译支持）

## 许可证

本项目基于 MIT 许可证发布。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。