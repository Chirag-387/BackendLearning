import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/users/1")

# print(response.status_code)
# print(response.json())

# data = response.json()
# print(data["email"])

# response = httpx.get("https://jsonplaceholder.typicode.com/users/1")

# if response.status_code == 200:
#     print("User found")
# else:
#     print("User not found")

# def check_user(user_id):
#     response = httpx.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")

#     if(response.status_code == 200):
#         data = response.json()
#         print(data["name"])
#     else:
#         print("user not found")

# check_user(1)

name = {
    "name": "random"
}

response = httpx.post("https://jsonplaceholder.typicode.com/users", json = name)
print(response.status_code)
print(response.json())