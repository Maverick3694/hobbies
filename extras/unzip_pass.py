"""
To try out differnt combinations of passwords to unzip file
"""
import zipfile
zip_file_path = 'test.zip' # give location of zip file
extract_dir = '/home' # give extraction location
password = []
while(True):
    t=str(input("\n enter phrase :")) # enter differnt passphrase each time until give empty one by just hitting enter
    if t=="":
        break        
    password.append(t)
print("\n")
for i in range(0,len(password)):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir, pwd=password[i].encode('utf-8'))
            print("\n\t\t\tExtraction successful!")
            break
    except RuntimeError as e:
        if 'Bad password' in str(e):
            print("Incorrect password : ", password[i])
        else:
            print("Extraction error:", e)
