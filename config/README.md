# Config 配置目录

本目录用于存放全局配置文件。

## 配置类型

- **数据源配置**: API 密钥、数据库连接等
- **策略参数**: 默认参数、优化范围等
- **环境配置**: 开发、测试、生产环境配置

## 配置文件示例

```python
# config/data_sources.py

# Yahoo Finance 配置
YAHOO_FINANCE = {
    'enabled': True,
    'rate_limit': 2000  # 每小时请求次数
}

# 数据库配置
DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'database': 'quant_lab'
}
```

## 安全注意事项

⚠️ **重要**: 
- 不要将敏感信息（API 密钥、密码等）直接写入配置文件
- 使用环境变量或单独的 `.env` 文件（需添加到 `.gitignore`）
- 提供配置文件模板（如 `config.example.py`），不包含真实凭证
