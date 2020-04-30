# Defined in - @ line 1
function .f --wraps='git --git-dir=$HOME/.dotfiles/git --work-tree=$HOME' --description 'alias .f=git --git-dir=$HOME/.dotfiles/git --work-tree=$HOME'
  git --git-dir=$HOME/.dotfiles/git --work-tree=$HOME $argv;
end
