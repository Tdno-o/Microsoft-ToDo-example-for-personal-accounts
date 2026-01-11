import msal, os, atexit, requests, json

# Getting the access token
CACHE_FILE = "./msal_cache.bin"
cache = msal.SerializableTokenCache()

if os.path.exists(CACHE_FILE):
    cache.deserialize(open(CACHE_FILE, "r").read())

@atexit.register
def save_cache():
    if cache.has_state_changed:
        open(CACHE_FILE, "w").write(cache.serialize())

app = msal.PublicClientApplication(
    client_id="YOUR-CLIENT-ID",
    authority="https://login.microsoftonline.com/consumers",
    token_cache=cache
)

SCOPES = ["User.Read", "Tasks.ReadWrite"]

accounts = app.get_accounts()
result = None
if accounts:
    result = app.acquire_token_silent(SCOPES, account=accounts[0])


if not result:
    flow = app.initiate_device_flow(scopes=SCOPES)
    message = flow["message"]
    print(message)
    result = app.acquire_token_by_device_flow(flow)
    save_cache()

access_token = result["access_token"]

# Obtain the user's information
headers = {"Authorization": f"Bearer {access_token}"}
account = requests.get(f"https://graph.microsoft.com/v1.0/me", headers=headers)
print(account.json())


# Get all lists in the user's account
headers = {"Authorization": f"Bearer {access_token}"}
lists = requests.get(f"https://graph.microsoft.com/v1.0/me/todo/lists", headers=headers)
print(lists.json())

# Get all tasks from a list
list_id = lists[0]["id"] # List at index 0
headers = {"Authorization": f"Bearer {access_token}"}
from_list = requests.get(f"https://graph.microsoft.com/v1.0/me/todo/lists/{list_id}/tasks", headers=headers)
print(from_list.json())