


[[ $- != *i* ]] && return


alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias vim='nvim'

export PATH=$HOME/.apps/TinyTeX/bin/x86_64-linux:$PATH


export VIRTUAL_ENV_DISABLE_PROMPT=1

function venv() {
    if [[ -n "$VIRTUAL_ENV" ]]; then
        echo "(${VIRTUAL_ENV##*/}) "
    fi
}

export PS1=' \[\033[0;34m\]$(venv)\[\033[1;33m\]\w\$\[\033[0;37m\] '
