


#                __       __                                     
#   ____ ___  __/ /____  / /_  _________ _      __________  _____
#  / __ `/ / / / __/ _ \/ __ \/ ___/ __ \ | /| / / ___/ _ \/ ___/
# / /_/ / /_/ / /_/  __/ /_/ / /  / /_/ / |/ |/ (__  )  __/ /    
# \__, /\__,_/\__/\___/_.___/_/   \____/|__/|__/____/\___/_/     
#   /_/                                                          


# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

config.load_autoconfig(False)

import catppuccin

catppuccin.setup(c, 'mocha', True)
c.fonts.default_family = 'UbuntuMono Nerd Font'
config.set("colors.webpage.darkmode.enabled", True)

c.completion.min_chars = 1
c.completion.height = '30%'
c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'filesystem']
c.completion.scrollbar.padding = 2

c.url.start_pages = 'about:blank'
c.url.default_page = 'about:blank'

c.downloads.position = 'top'
c.downloads.prevent_mixed_content = True
c.downloads.remove_finished = 1000

c.editor.command = ['alacritty', 'vim', '{file}']

c.prompt.filebrowser = True

c.tabs.position = 'left'
c.tabs.show = 'switching'
c.tabs.show_switching_delay = 1000
c.tabs.width = 300
c.tabs.wrap = True

c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}', 
    'g': 'https://www.google.com/search?hl=en&q={}', 
    'y': 'https://yandex.com/?q={}',

    'w': 'https://wikipedia.org/wiki/{}', 
    'wd': 'https://wikipedia.org/wiki/{}_(disambiguation)', 
    'wi': 'https://wiktionary.org/wiki/{}', 
    'wa': 'https://wiki.archlinux.org/?search={}', 
    'wp' : 'https://proofwiki.org/wiki/{}',
}
