import pygal

wm = pygal.maps.world.World()
wm.title = '北美地区的人口数量'
wm.add('北美', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')
