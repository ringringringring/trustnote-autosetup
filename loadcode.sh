#load code from github
github_host="https://github.com/trustnote/"
git_extension=".git"
source_path="$HOME/mainchain/"

load_project_source(){
    currentpath=$source_path$1$2/
    mkdir "$current_path"
    git clone "$github_host$2$git_extension" "$current_path"

    if [ -n "$1" ]
    then
        npm install -cwd "$current_path" --prefix "$current_path"
    fi
}

git config --global user.name "yiyanwannian"
git config --global user.email "774392980@qq.com"

load_project_source "" "testnet-builder"
load_project_source "testnet-builder/" "trustnote-hub"
load_project_source "testnet-builder/" "trustnote-witness"
load_project_source "testnet-builder/" "trustnote-headless"
load_project_source "testnet-builder/" "trustnote-explorer"