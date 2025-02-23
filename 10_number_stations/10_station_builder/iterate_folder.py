import os

def iterate_folder(folder_path, callback):
    outputs = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            output = callback(full_path)
            outputs.append(output)    

    return outputs