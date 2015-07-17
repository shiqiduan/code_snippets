set nocompatible  "" not compatible with VI

"" Encodings and fonts
set encoding=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set langmenu=zh_CN.UTF-8
language messages zh_CN.UTF-8
set guifontset=wenquanyi,-*-16-*-*-*

"" Tab and Backspace
set sw=2
set tabstop=4
set shiftwidth=4 " 设定 << 和 >> 命令移动时的宽度为 4
set softtabstop=4 " 使得按退格键时可以一次删掉 4 个空格
set cindent
set smartindent
set autoindent
set backspace=indent,eol,start  "" set backspace

"" Display
set number        "" show line number
set ruler         "" always show current position
set cursorline    "" highlight the current line
set showcmd

"" Searching
set ignorecase smartcase " 搜索时忽略大小写，但在有一个或以上大写字母时仍保持对大小写敏感
set nowrapscan " 禁止在搜索到文件两端时重新搜索
set incsearch " 输入搜索内容时就显示搜索结果
set hlsearch " 搜索时高亮显示被找到的文本
set showmatch
set history=100
highlight Search term=reverse ctermbg=4 ctermfg=7

"" Syntax and color scheme
syntax enable
filetype plugin indent on

"""""""""" 自动补全命令 """"""""""
autocmd Filetype c      set omnifunc=ccomplete#Complete
autocmd Filetype html   set omnifunc=htmlcomplete#CompleteTags
autocmd Filetype xml    set omnifunc=xmlcomplete#CompleteTags
autocmd Filetype python set omnifunc=pythoncomplete#CompleteTags
autocmd Filetype tex    set omnifunc=syntaxcomplete#Complete

"""""""""" 英文拼写检查 """""""""""
" 拼写错误被画红线，比缺省设置更美观 "
""""""""""""""""""""""""""""""""""
set spell spelllang=en_us
setlocal spell spelllang=en_us
highlight clear SpellBad
highlight SpellBad term=standout ctermfg=1 term=underline cterm=underline
highlight clear SpellCap
highlight SpellCap term=underline cterm=underline
highlight clear SpellRare
highlight SpellRare term=underline cterm=underline
highlight clear SpellLocal
highlight SpellLocal term=underline cterm=underline

"""""""""""" END """"""""""""
