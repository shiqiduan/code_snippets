set nocompatible  "" not compatible with VI
filetype off

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" " alternatively, pass a path where Vundle should install plugins
" "call vundle#begin('~/some/path/here')
"
" " let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
Bundle 'gmarik/vundle'
Bundle 'andviro/flake8-vim'
""Bundle 'Valloric/YouCompleteMe'

call vundle#end()            " required
filetype plugin indent on    " required


"" Encodings and fonts
set encoding=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,gb18030,gbk,gb2312,cp936
set termencoding=utf-8
set langmenu=zh_CN.UTF-8
language messages zh_CN.UTF-8
set guifontset=wenquanyi,-*-16-*-*-*

set nrformats=  "默认使用十进制

"" Tab and Backspace
set sw=4
set ts=4
set expandtab
set tabstop=4
set shiftwidth=4 " 设定 << 和 >> 命令移动时的宽度为 4
set softtabstop=4 " 使得按退格键时可以一次删掉 4 个空格
set cindent
set smartindent
set autoindent
set backspace=indent,eol,start  "" set backspace

"" Display
""set number        "" show line number, set nonu
set ruler         "" always show current position
set cursorline    "" highlight the current line
set showcmd

" Searching
set ignorecase smartcase " 搜索时忽略大小写，但在有一个或以上大写字母时仍保持对大小写敏感
set nowrapscan " 禁止在搜索到文件两端时重新搜索
set incsearch " 输入搜索内容时就显示搜索结果
set hlsearch " 搜索时高亮显示被找到的文本
set showmatch
set history=100
set pastetoggle=<f5> "" 打开关闭从系统粘贴功能
highlight Search term=reverse ctermbg=4 ctermfg=7

"" Syntax and color scheme
syntax enable

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
let g:PyFlakeOnWrite = 1
let g:PyFlakeCheckers = 'pep8,mccabe,frosted'
let g:PyFlakeDefaultComplexity=10
let g:PyFlakeCWindow = 6 
let g:PyFlakeSigns = 1 
let g:PyFlakeSignStart = 1
let g:PyFlakeMaxLineLength = 100
let g:PyFlakeRangeCommand = 'Q'

""autocmd CompleteDone * pclose
"set mouse=a " :h mouse, 在全部的模式下激活鼠标

set vb t_vb= "关闭错误声音和闪屏
