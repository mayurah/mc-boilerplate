#!/usr/bin/env bash
#set -x

# This script is meant to be used for updating "boilerplate" files in a new repo

###################################  Setup  ####################################


current_path=${PWD##*/}

boilerplate="mc_boilerplate"

module_name=${current_path//-/_}

rm -rf .git

mv mc_boilerplate $module_name

grep -rl --exclude=\*.{md,sh} $boilerplate . | xargs sed -i "s/$boilerplate/$module_name/g"

cp .env.example .env