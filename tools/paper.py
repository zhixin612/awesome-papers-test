import requests
from bs4 import BeautifulSoup
import base64
import json
import csv
from datetime import datetime, timedelta
import pytz
import os
from dotenv import load_dotenv



# 本地文件路径
local_file_path = '../daily-arxiv-llm.md'

# 顶部警告文本
WARNING_TEXT = "The paper list will be updated automatically, please do not edit.\n\n"

def read_keywords_from_csv(file_name):
    """读取CSV文件中的关键字，每行一个关键字"""
    file_path = os.path.join(os.path.dirname(__file__), file_name)  # 获取当前脚本目录的文件路径
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip().lower() for line in file.readlines()]


def get_paper_info(paper):
    title_tag = paper.find('a', class_='title-link')
    title = title_tag.text.strip()
    link = "https://arxiv.org" + title_tag['href']
    abs_link = link.replace('/arxiv/', '/abs/')
    return f"* [{title}]({abs_link})"

def fetch_papers(date, accept_keywords, reject_keywords):
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

        # 筛选包含接受关键字的论文并排除包含拒绝关键字的论文
        if any(keyword in title.lower() or keyword in abstract.lower() for keyword in accept_keywords):
            if not reject_keywords or not any(exclude_keyword in title.lower() or exclude_keyword in abstract.lower() for exclude_keyword in reject_keywords):
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

def update_local_file(all_content, local_file_path):
    # 读取现有的本地文件内容
    if os.path.exists(local_file_path):
        with open(local_file_path, 'r', encoding='utf-8') as file:
            current_content = file.read()

        # 如果现有内容以 WARNING_TEXT 开头，去掉它
        if current_content.startswith(WARNING_TEXT):
            current_content = current_content[len(WARNING_TEXT):]

        # 组合新内容（添加警告文本 + 新的论文 + 旧内容）
        new_content = WARNING_TEXT + all_content + '\n' + current_content
    else:
        # 文件不存在，直接创建新文件
        new_content = WARNING_TEXT + all_content

    # 更新本地文件
    with open(local_file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

    print(f"文件更新成功！")

def main(start, end):
    all_papers_content = ""

    # 读取关键字文件
    accept_keywords = read_keywords_from_csv('keyword-accept.csv')
    reject_keywords = read_keywords_from_csv('keyword-reject.csv')

    for date in date_range(start, end):
        print(f"Fetching papers for date: {date}")
        papers = fetch_papers(date, accept_keywords, reject_keywords)
        if papers:
            formatted_papers = format_papers(papers, date)
            all_papers_content += formatted_papers
        else:
            print(f"No papers found for date: {date}")

    if all_papers_content:
        # 统一更新本地文件
        update_local_file(all_papers_content, local_file_path)
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
