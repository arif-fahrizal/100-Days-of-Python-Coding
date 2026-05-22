try:
    file = open("file.txt")
    dicts = {"key": "value"}
    print(dicts["key"])
except FileExistsError:
    file = open("file.txt", "w")
    file.write("something")
except KeyError as error:
    print(f"The key {error} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")