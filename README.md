# 接口自动化测试框架

基于 Python + Pytest + Requests 搭建的接口自动化测试框架，支持数据驱动、日志记录、Allure 可视化报告生成。

## 技术栈

- Python 3.x
- Pytest
- Requests
- Allure
- OpenPyXL

## 项目结构

```text
PyCharmMiscProject/
├── common/              # 公共模块
│   └── http_client.py   # HTTP 请求封装类
├── config/              # 配置文件
│   └── settings.py      # 环境地址、超时时间等
├── data/                # 测试数据
│   └── test_cases.xlsx  # Excel 测试用例
├── reports/             # 测试报告
├── testcases/           # 测试用例
│   └── test_demo.py
├── utils/               # 工具类
│   └── read_excel.py    # Excel 读取工具
├── conftest.py          # Pytest 全局配置
├── requirements.txt     # 项目依赖
└── README.md
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行测试

```bash
pytest testcases/test_demo.py --alluredir=./reports/allure-results
```

### 3. 查看测试报告

```bash
allure serve ./reports/allure-results
```

## 功能特性

- **请求封装**：统一处理请求头、超时、异常、日志
- **数据驱动**：测试数据与代码分离，从 Excel 读取用例
- **断言机制**：支持状态码、字段值等多维度断言
- **日志记录**：每次请求和响应都有日志，方便问题定位
- **可视化报告**：集成 Allure，生成包含步骤详情的测试报告

## 作者

zhangting113