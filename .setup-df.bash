#!/usr/bin/env bash

REMOTE_REPO="git@github.com:01walid/dotfiles.git"
LOCAL_REPO_NAME=".df-repo"

git clone --bare $REMOTE_REPO $HOME/$LOCAL_REPO_NAME

function dotfiles {
   git --git-dir=$HOME/$LOCAL_REPO_NAME/ --work-tree=$HOME $@
}

mkdir -p .config-backup
dotfiles checkout

if [ $? = 0 ]; then
  echo "Checked out config.";
  echo "Make sure to add an alias to your .zshrc or .bashrc:\n";
  echo "echo \"alias dotfiles='git --git-dir=\$HOME/$LOCAL_REPO_NAME/ --work-tree=\$HOME'\" >> .zshrc"
  else
    echo "Backing up pre-existing dot files.";
    dotfiles checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | xargs -I{} mv {} .config-backup/{}
fi;

dotfiles checkout
dotfiles config status.showUntrackedFiles no



