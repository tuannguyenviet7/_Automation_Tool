import re
import json

# Đọc file .c
with open("cc_cfg.c", "r") as file:
    content = file.read()

# Tìm các khối comment /* ... */
blocks = re.findall(r"/\*([\s\S]*?)\*/", content)

# Xử lý các khối để tạo danh sách Python
python_lists = {}
for i, block in enumerate(blocks, start=1):
    # Tách các dòng, loại bỏ dòng trống và dòng chứa chữ không phải mã định danh
    lines = [line.strip() for line in block.splitlines()]
    valid_lines = [line for line in lines if re.match(r"^[A-Z0-9_]+$", line)]
    if valid_lines:  # Chỉ thêm nếu có dữ liệu hợp lệ
        python_lists[f"Key{i}"] = valid_lines

# Xuất dữ liệu ra file JSON
output_file = "cc_cfg.json"
with open(output_file, "w") as json_file:
    json.dump(python_lists, json_file, indent=4)
    print("Export data successfully")