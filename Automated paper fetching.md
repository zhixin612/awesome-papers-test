# Automated paper fetching

## Deployment

​	The automated paper scraping script has been deployed on server 153 using crontab, and it automatically runs every day at 20:20 to fetch papers related to large model inference from the past day. Please avoid manually editing the `daily-arxiv-llm.md` file, as this could cause the content of the file to become disorganized.

```shell
20 20 * * * /bin/bash /home/wyf/paper/paper.sh >> /home/wyf/paper/log.txt 2>&1
```

## Website

* [https://papers.cool/arxiv/cs.DC](https://papers.cool/arxiv/cs.DC): Distributed, Parallel, and Cluster Computing

## Configuration

+ python=3.9
+ requests,bs4,pytz

## Usage

+ First, you need to provide your GitHub account's token and ensure that your account has been invited as a collaborator by TJU-NSL with read and write access to the `awesome-papers` repository.

```python
github_token = 'XXXXXXX' 
repo_owner = 'TJU-NSL'  
repo_name = 'awesome-papers'  
file_path = 'daily-arxiv-llm.md' 
branch = 'main'
```

+ Set keywords, and the script will select papers whose titles and abstracts contain those keywords and filter them accordingly.

```python
if any(keyword in title.lower() or keyword in abstract.lower() for keyword in ['llm', 'inference', 'rag', 'prefill', 'decode', 'attention']):
            if not any(exclude_keyword in title.lower() or exclude_keyword in abstract.lower() for exclude_keyword in ['federated', 'wireless', 'big data', 'security']):
                selected_papers.append(f"* [{title}]({abs_link})")
```

+ Select the time period for scraping papers.

```python
tz = pytz.timezone("Asia/Shanghai")
now = datetime.now(tz)
start_date = (now - timedelta(days=1)).strftime("%Y-%m-%d")  
end_date = (now - timedelta(days=1)).strftime("%Y-%m-%d")  
```

You can check the script execution logs in `/home/wyf/paper/log.txt`.
