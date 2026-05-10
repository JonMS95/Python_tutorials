#!/bin/bash

CUR_FILE_PATH="$(realpath $(dirname ${0}))"

TEXT_COLOR_RED="\e[31m"
TEXT_COLOR_GREEN="\e[32m"
TEXT_COLOR_YELLOW="\e[33m"
TEXT_COLOR_RESET="\e[0"

deps_file=""

function checkRequiredPrograms()
{
    local REQUIRED_PROGRAMS=("python3" "pip3" "make" "g++")

    for prog in "${REQUIRED_PROGRAMS[@]}"
    do
        if command -v "${prog}" >/dev/null 2>&1
        then
            version=$(${prog} --version 2>&1 | head -n 1)
            echo -e "${TEXT_COLOR_GREEN}[OK] ${prog} is installed: ${version}${TEXT_COLOR_RESET}"
        else
            echo -e "${TEXT_COLOR_RED}[MISSING] ${prog} is NOT installed!${TEXT_COLOR_RESET}"
            exit 1
        fi
    done
}

function checkDependencyListingFile()
{
    local DEF_DEPS_FILE="${CUR_FILE_PATH}/linear_regression_reqs.txt"

    if [[ $# -gt 1 ]]
    then
        deps_file="${DEF_DEPS_FILE}"
        echo -e "${TEXT_COLOR_YELLOW}More than one parameters passed: using the first one (${deps_file}), ignoring spare ones...${TEXT_COLOR_RESET}"
    elif [[ $# -eq 0 ]]
    then
        deps_file="${DEF_DEPS_FILE}"
        echo -e "${TEXT_COLOR_GREEN}No dependencies file found, using the default (${deps_file}).${TEXT_COLOR_RESET}"
    else
        deps_file="${1}"
        echo -e "${TEXT_COLOR_GREEN}Using provided file name (${deps_file}).${TEXT_COLOR_RESET}"
    fi

    if [[ ! -f ${deps_file} ]]
    then
        echo -e "${TEXT_COLOR_RED}Could not find dependency storing file: ${deps_file}${TEXT_COLOR_RESET}"
        exit 1
    fi
}

function retrieveDependencies()
{
    pip3 install -r ${deps_file}

    echo -e "${TEXT_COLOR_GREEN}Finished retrieving all dependencies listed in (${deps_file}).${TEXT_COLOR_RESET}"
}

# ======================
# ======== Main ========
# ======================

checkRequiredPrograms
checkDependencyListingFile
retrieveDependencies
