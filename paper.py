import requests
from bs4 import BeautifulSoup
import base64
import json
from datetime import datetime, timedelta
import pytz

# GitHub 访问令牌、仓库和文件信息
github_token = 'XXXXX'  # 替换为你的 GitHub token
repo_owner = 'TJU-NSL'  # 替换github用户名
repo_name = 'awesome-papers'  # 替换github的仓库名
file_path = 'daily-arxiv-llm.md' # 仓库下的文件路径
branch = 'main'

# 顶部警告文本
WARNING_TEXT = "The paper list will be updated automatically, please do not edit.\n\n"


def get_paper_info(paper):
    title_tag = paper.find('a', class_='title-link')
    title = title_tag.text.strip()
    link = "https://arxiv.org" + title_tag['href']

    abs_link = link.replace('/arxiv/', '/abs/')

    return f"* [{title}]({abs_link})"

def fetch_papers(date):
    url = f"https://papers.cool/arxiv/cs.DC?date={date}"
    print(url)
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data for date: {date}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    papers = soup.find_all('div', class_='panel paper')

    selected_papers = []
    for paper in papers:
        title_tag = paper.find('a', class_='title-link')
        title = title_tag.text.strip()
        link = "https://arxiv.org" + title_tag['href']
        abs_link = link.replace('/arxiv/', '/abs/')
        abstract_tag = paper.find('span', class_='abstract')
        abstract = abstract_tag.text.strip() if abstract_tag else ""

        # 爬取包含关键字的论文
        if any(keyword in title.lower() or keyword in abstract.lower() for keyword in ['llm', 'inference', 'rag', 'prefill', 'decode', 'attention']):
            # 排除包含不需要关键字的论文
            if not any(exclude_keyword in title.lower() or exclude_keyword in abstract.lower() for exclude_keyword in ['federated', 'wireless', 'big data', 'security']):
                selected_papers.append(f"* [{title}]({abs_link})")

    return selected_papers

def date_range(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = timedelta(days=1)
    current = end
    while current >= start:
        yield current.strftime("%Y-%m-%d")
        current -= delta


def format_papers(papers, date):
    formatted = f"### {date}\n\n"
    formatted += '\n'.join(papers) + '\n'
    return formatted


def update_github_file(all_content, github_token, repo_owner, repo_name, file_path, branch):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    headers = {
        'Authorization': f'token {github_token}',
        'Content-Type': 'application/json'
    }

    # 获取SHA，检查文件是否存在
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # 获取现有文件的 SHA 和内容
        file_info = response.json()
        sha = file_info['sha']
        current_content = base64.b64decode(file_info['content']).decode()

        # 如果现有内容以 WARNING_TEXT 开头，去掉它
        if current_content.startswith(WARNING_TEXT):
            current_content = current_content[len(WARNING_TEXT):]

        # 组合新内容（添加警告文本 + 新的论文 + 旧内容）
        new_content = WARNING_TEXT + all_content + '\n' + current_content
    else:
        # 文件不存在，直接创建新文件
        new_content = WARNING_TEXT + all_content
        sha = None  # 创建新文件时不需要 SHA

    # 请求体数据，base64 编码的内容
    data = {
        'message': f'Update papers for {file_path}',
        'content': base64.b64encode(new_content.encode()).decode(),
        'branch': branch
    }

    # 仅当文件存在时才包含 SHA
    if sha:
        data['sha'] = sha

    # 发送 PUT 请求，更新或创建文件
    response = requests.put(url, headers=headers, data=json.dumps(data))

    if response.status_code in [200, 201]:
        print(f'文件更新成功!')
    else:
        print(f'更新文件失败: {response.json()}')



def main(start, end):
    all_papers_content = ""

    for date in date_range(start, end):
        print(f"Fetching papers for date: {date}")
        papers = fetch_papers(date)
        if papers:
            formatted_papers = format_papers(papers, date)
            all_papers_content += formatted_papers
        else:
            print(f"No papers found for date: {date}")

    if all_papers_content:
        # 统一更新 GitHub 文件
        update_github_file(all_papers_content, github_token, repo_owner, repo_name, file_path, branch)
    else:
        print("未获取到任何论文，文件不会更新。")


if __name__ == "__main__":
    # 获取东八区时间
    tz = pytz.timezone("Asia/Shanghai")
    now = datetime.now(tz)

    start_date = (now - timedelta(days=1)).strftime("%Y-%m-%d")  
    print(start_date)
    end_date = (now - timedelta(days=1)).strftime("%Y-%m-%d")  
    # end_date = now.strftime("%Y-%m-%d")  # 今天

    main(start_date, end_date)

