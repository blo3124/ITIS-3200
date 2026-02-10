# Work with folders and file paths
import os
# let us save and load .json files
import json
# Hash Functions
import hashlib

def hash_file(filepath):
    sha256 = hashlib.sha256()
    # read binary
    with open(filepath, "rb") as f:
        while True:
            # Reads 4096 bytes from file
            chunk = f.read(4096)
            if not chunk:
                break
            sha256.update(chunk)

    # Converts hash into readable string        
    return sha256.hexdigest()

    

def traverse_directory(directory):
    # creates empty dictionary
    hashes = {}
    # walk through folder 
    for root, dirs, files in os.walk(directory):
        # loops thorugh every file
        for file in files:
            #  builds full file path
            filepath = os.path.join(root, file)
            # Hashses the file
            hashes[filepath] = hash_file(filepath)

    return hashes

def generate_table(directory):
    # calls directory function to get hashes
    hashes = traverse_directory(directory)
    # Write mode for new JSON file
    with open("hash_table.json", "w") as f:
        # Saves dictionary to JSON file and format for readability
        json.dump(hashes, f, indent=4)

    print("Hash table generated")

def validate_hash(directory):
    with open("hash_table_json", "r") as f:
        old_hashes = json.load(f)
        current_hashes = traverse_directory(directory)
        for filepath, old_hash in old_hashes.items():
            if filepath not in current_hashes:
                print(f"{filepath} was deleted")
            else: 
                print(f"{filepath} hash is invalid")
            
        for filepath in current_hashes:
            if filepath not in old_hashes:
                print(f"{filepath} is a new file")

def main():
    print("1 - Generate new hash table")
    print("2 - Verify hashes")
    choice = input("Choose an option: ")
    if choice == "1":
        directory = input("Enter directory path: ")
        generate_table(directory)
    elif choice == "2":
        directory = input("Enter directory path: ")
        validate_hash(directory)
    else:
        print("Invalid choice")
        
if __name__ == "__main__":
    main()

