import shutil
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义报告文件路径
REPORT_PATH = os.path.join(BASE_PATH, "report")

def clear_report_directory(report_dir):
    shutil.rmtree(report_dir)
    # 重新创建空目录
    os.makedirs(report_dir)

# 使用示例
clear_report_directory(REPORT_PATH)