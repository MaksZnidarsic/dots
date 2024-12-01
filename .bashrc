


[[ $- != *i* ]] && return


alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias vim='nvim'


export VIRTUAL_ENV_DISABLE_PROMPT=1

function venv() {
    if [[ -n "$VIRTUAL_ENV" ]]; then
        echo "(${VIRTUAL_ENV##*/}) "
    fi
}

export PS1=' \[\033[0;35m\]$(venv)\[\033[1;34m\]\w\$\[\033[0;37m\] '
