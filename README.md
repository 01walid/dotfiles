# dotfiles

Feel at `$HOME`, these are my personal config files (a.k.a dot files), I manage them using [a git bare repo](https://www.atlassian.com/git/tutorials/dotfiles). Not everything is included yet, working on it.

## Setup 

A helper bash script can be found at the root of this repo, you can run it with `bash .setup-df.bash`. 

Alternatively, follow these steps: 


- First make the alias (in .bashrc or .zshrc):
```
alias dotfiles='git --git-dir=$HOME/.df-repo/ --work-tree=$HOME'
```
- Source your .bashrc or .zshrc with `source .zshrc` to make sure the alias in now available in your current shell session. 

- Clone this repo with the `--bare` option
```
git clone --bare git@github.com:01walid/dotfiles.git $HOME/.df-repo
```
- Checkout the actual content from the bare repository to your `$HOME`
```
dotfiles checkout
```
- Set the flag `showUntrackedFiles` to `no` on this specific (local) repository:
```
dotfiles config --local status.showUntrackedFiles no
```


## what am I using? 
Arch Linux with: 

- Terminal: [Alacritty](https://github.com/alacritty/alacritty).
- tmux with [oh my tmux!](https://github.com/gpakosz/.tmux).
- the fish shell, with [oh my fish](https://github.com/oh-my-fish/oh-my-fish).
- vim ([neovim](https://neovim.io/)).
- [Qtile](http://www.qtile.org/), the tiling window manager.

### TODO
- [ ] dmenu, polybar config.
- [ ] fonts.
- [ ] picom.
- [ ] zshrc.
- [ ] bootstrap script (with pacman/aur packages).

