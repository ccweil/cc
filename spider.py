import requests
import json
import csv

def get_python_projects(pages):
    base_url = "https://api.github.com/search/repositories"
    params = {
        "q": "language:python",
        "sort": "stars",
        "order": "desc",
        "per_page": 100
    }
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Your-User-Agent"
    }

    # 创建 CSV 文件并写入标题行
    with open("result.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["项目名称", "星标数量", "链接"])

        for page in range(1, pages + 1):
            params["page"] = page
            response = requests.get(base_url, params=params, headers=headers)

            if response.status_code == 200:
                data = json.loads(response.text)
                projects = data["items"]

                for project in projects:
                    name = project["name"]
                    stars = project["stargazers_count"]
                    url = project["html_url"]
                    writer.writerow([name, stars, url])
            else:
                print("请求失败")

# 指定要爬取的页数
page_count = 5

get_python_projects(page_count)
