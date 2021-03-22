current_version = input().split(".")
current_version_int = int("".join(current_version)) + 1
new_version = ".".join(str(current_version_int))
print(new_version)