import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并返回文本
url = 'https://api.github.com/search/repositories?q=language:matlab&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应储存在一个变量中
response_dict = r.json()

# 处理结果
print("Total Repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究所有仓库

#print("\nkeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#    print(key)
#print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
#    print("\nName:", repo_dict['name'])
#    print("Owner:", repo_dict['owner']['login'])
#    print("Stars:", repo_dict['stargazers_count'])
#    print("Repository:", repo_dict['html_url'])
#    print("Created:", repo_dict['created_at'])
#    print("Updated:", repo_dict['updated_at'])
#    print("Description:", repo_dict['description'])

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # plot_dicts.append(repo_dict['stargazers_count'])
    plot_dict = {
        'label': str(repo_dict['description']),
        'value': repo_dict['stargazers_count'],
        'xlink': repo_dict['html_url']}
    plot_dicts.append(plot_dict)

print(plot_dicts)
# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred matlab Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('matlab_repos.svg')
