import httpx

def create_user(name):
    url = "https://jsonplaceholder.typicode.com/users"
    body = {"name": name}
    response = httpx.post(url, json = body)
    data = response.json()
    return data["id"]

def get_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = httpx.get(url)
    print(response.status_code)

# new_id = create_user("Chirag")
# print(new_id)

job_id = create_user("random")
get_user(job_id)