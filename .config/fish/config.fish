
# NPM
set -x PATH $HOME/.node_modules/bin $PATH
set -x npm_config_prefix ~/.node_modules

# Rust / Cargo
set -x PATH $HOME/.cargo/bin $PATH 

# pip and local binaries installs
set -x PATH $HOME/.local/bin $PATH 

