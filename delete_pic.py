# import os
# import glob
#
# # 定义目标文件夹路径
# folder_path = "D:\\web_load\\RePaint-main\\data\\data_test\\gt_keep_masks"
#
# # 构造搜索模式以匹配所有以 'pic' 开头的 .png 文件
# search_pattern = os.path.join(folder_path, "pic*.png")
#
# # 使用 glob 模块找到所有匹配的文件
# files_to_delete = glob.glob(search_pattern)
#
# # 遍历并删除每个文件
# for file_path in files_to_delete:
#     try:
#         os.remove(file_path)
#         print(f"Deleted: {file_path}")
#     except Exception as e:
#         print(f"Error deleting {file_path}: {e}")
#
# # 完成后输出
# print("Finished deleting files.")

