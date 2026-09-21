import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "test_cases"

# 表头
headers = ["用例编号", "接口名称", "请求方法", "请求路径", "请求参数", "期望状态码"]
ws.append(headers)

# 测试数据
rows = [
    ["TC001", "GET请求测试", "GET", "/get", "", 200],
    ["TC002", "POST请求测试", "POST", "/post", '{"name": "zhangting", "action": "test"}', 200],
    ["TC003", "PUT请求测试", "PUT", "/put", '{"name": "zhangting"}', 200],
]

for row in rows:
    ws.append(row)

wb.save("test_cases.xlsx")
print("Excel 文件生成成功：test_cases.xlsx")