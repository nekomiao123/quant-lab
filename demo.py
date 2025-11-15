#!/usr/bin/env python3
"""
简单的数据读取演示脚本
这个脚本展示了如何读取和处理股票数据
"""

import csv
import os


def load_stock_data(file_path):
    """
    从CSV文件加载股票数据
    
    Args:
        file_path: CSV文件路径
    
    Returns:
        list: 包含股票数据的列表
    """
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def print_data_summary(data):
    """
    打印数据摘要
    
    Args:
        data: 股票数据列表
    """
    if not data:
        print("没有数据")
        return
    
    print(f"总共加载了 {len(data)} 条记录")
    print("\n前5条记录:")
    print("-" * 80)
    
    # 打印表头
    if data:
        headers = list(data[0].keys())
        header_line = " | ".join(f"{h:>10}" for h in headers)
        print(header_line)
        print("-" * 80)
    
    # 打印前5条数据
    for record in data[:5]:
        values = [record[h] for h in headers]
        value_line = " | ".join(f"{v:>10}" for v in values)
        print(value_line)
    
    print("-" * 80)
    
    # 统计每个股票的记录数
    symbols = {}
    for record in data:
        symbol = record['symbol']
        symbols[symbol] = symbols.get(symbol, 0) + 1
    
    print("\n股票统计:")
    for symbol, count in symbols.items():
        print(f"  {symbol}: {count} 条记录")


def main():
    """
    主函数
    """
    # 获取数据文件路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(current_dir, 'data', 'sample_stock_data.csv')
    
    print("=" * 80)
    print("Quant Lab - 数据加载演示")
    print("=" * 80)
    print(f"\n正在加载数据: {data_file}")
    
    # 检查文件是否存在
    if not os.path.exists(data_file):
        print(f"错误: 文件不存在 {data_file}")
        return
    
    # 加载数据
    data = load_stock_data(data_file)
    
    # 打印数据摘要
    print_data_summary(data)
    
    print("\n" + "=" * 80)
    print("演示完成!")
    print("=" * 80)


if __name__ == "__main__":
    main()
