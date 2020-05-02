syntax on 


" use set hidden, here's why: 
" https://medium.com/usevim/vim-101-set-hidden-f78800142855

set hidden

set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch

set colorcolumn=80

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=50


highlight ColorColumn ctermbg=0 guibg=lighgrey

" Install plugins, this uses Plug
" https://github.com/junegunn/vim-plug (neovim install process)

call plug#begin('~/.vim/plugged')

Plug 'ycm-core/YouCompleteMe'
Plug 'morhetz/gruvbox'
Plug 'jremmen/vim-ripgrep'
Plug 'tpope/vim-fugitive'
Plug 'leafgarland/typescript-vim'
Plug 'vim-utils/vim-man'
" Plug 'lyuts/vim-rtags'
Plug 'git@github.com:kien/ctrlp.vim.git'
Plug 'mbbill/undotree'
Plug 'vim-airline/vim-airline'

call plug#end()

colorscheme gruvbox
set background=dark

" tell ripgrep to use project's root (using git) and consider .gitignore
" for faster searching.
if executable('rg')
    let g:rg_derive_root='true'
endif

let mapleader = " "

"vim-airline
let g:airline_powerline_fonts = 1
