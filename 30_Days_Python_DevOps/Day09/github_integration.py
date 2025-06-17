import requests

URL = "https://api.github.com/repos/sailaja-adapa/Vipreshana/pulls"

response = requests.get(URL)

if response.status_code == 200:
    response = response.json()

    pr_creators = {}

    for pull in response:
        creator = pull['user']['login']
        print(creator)
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1

    print("PR Creators and PR Counts: ")
    for creator, pr_count in pr_creators.items():
        print(f"{creator}: {pr_count}")