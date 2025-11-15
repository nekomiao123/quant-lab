# Data 数据目录

本目录用于存放原始数据和处理后的数据。

## 数据组织

```
data/
├── raw/               # 原始数据
├── processed/         # 处理后的数据
└── sample_stock_data.csv  # 示例数据
```

## 数据格式规范

### 股票数据格式
- **CSV 格式**: date, symbol, open, high, low, close, volume
- **日期格式**: YYYY-MM-DD
- **编码**: UTF-8

## 注意事项

- 大文件（>10MB）不建议提交到 Git
- 敏感数据需要加密或排除在版本控制之外
- 建议使用标准化的数据格式，便于跨项目使用
