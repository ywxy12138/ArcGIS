import os

folder = os.getcwd()
name1 = "Export_Output_2"
name2 = "Export_Output_4"
new_name1 = "In_Flow_Map"
new_name2 = "Out_Flow_Map"
print("Current folder:", folder)
for filename in os.listdir(folder):
    print("Processing file:", filename)
    if filename.startswith(name1):
        print("Renaming file:", filename)
        os.rename(os.path.join(folder, filename), 
                  os.path.join(folder, filename.replace(name1, new_name1)))
    elif filename.startswith(name2):
        os.rename(os.path.join(folder, filename), 
                  os.path.join(folder, filename.replace(name2, new_name2)))

