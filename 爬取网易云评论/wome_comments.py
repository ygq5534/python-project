import requests
import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token=3c55c2ef1e77954ea2aaf4ffd5b9f942'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/2',
    'Referer': 'http://music.163.com/#/song?id=551816010',
    'Origin': 'http://music.163.com',
    'Host': 'music.163.com'
}
# 加密数据
user_data = {
    'params': '9XB6ESmufcZwRktn2LPNgGaPI1l6BkriA4pnjJCvRBdAvMCvGyWjU+pmFRVMkHEOMCvl2IKEgCF/eZpFvcKwLNIr0BwlOHYvGQgOVLe85z6xzLM1jKzXTN4KhmT7WvrfjRZEuTfIWHancR4jL5+sgvHLxjGrFll/fHGJ6iZ4eGxCDaA5rV7m29hGm96ZcS6RwnALi6vMrrPEeun1kelOS+1r7uQLrXPkDp+wJt8MK0w=',
    'encSecKey': '02697d1114f570b6eabc88d0156987afa550c8eb5195e78c29193aabccb33f9f6ab123c99b3b37660518cf03d9b5c805d07bb189cad895c20da406637e3b3a24d5d4da7e650d24762e3d587724e12405bcfccc7edf780cbc0f4cad491be0daeeb0071a5b22c30a149750eec4685cd74a85f87ddc074c088ed9f84f9bebd36c70'
}
response = requests.post(url, headers=headers, data=user_data)
data = json.loads(response.text)
hotcomments, nicknames = [], []
for hotcomment in data['hotComments']:
    item = {
        'label': hotcomment['content'],
        'value': hotcomment['likedCount']
    }
    nicknames.append(hotcomment['user']['nickname'])

    hotcomments.append(item)

#content_list = [content['content'] for content in hotcomments]
#nickname = [content['nickname'] for content in hotcomments]
#liked_count = [content['likedCount'] for content in hotcomments]


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
chart.title = '陈亦讯歌曲《我们》高赞评论统计'
chart.x_labels = nicknames

chart.add('', hotcomments)
chart.render_to_file('women_comments.svg')
