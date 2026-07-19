import os
def read_resume(file_path):
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print("Unexpected Error:", e)
        return None