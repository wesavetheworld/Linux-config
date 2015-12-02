# The following lines were added by compinstall
 
zstyle ':completion:*' completer _expand _complete _ignored _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{[:lower:]}={[:upper:]}' 'r:|[._-]=** r:|=**' 'l:|=* r:|=*'
zstyle ':completion:*' max-errors 2
zstyle ':completion:*' menu select=1
zstyle ':completion:*' original true
zstyle ':completion:*' prompt 'Showing corrections with %e errors found'
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle :compinstall filename '/home/baggykiin/.zshrc'
 
autoload -Uz compinit
compinit
autoload -U colors && colors
PROMPT="%B%(?..[%?] )%b%{$fg[red]%}%n%{$reset_color%}@%m %1~] "
# End of lines added by compinstall
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=100000
setopt appendhistory
unsetopt autocd
bindkey -e
# End of lines configured by zsh-newuser-install
# Pkgfile hook
source /usr/share/doc/pkgfile/command-not-found.zsh
# tell applications we're using a terminal with colour support
export TERM=xterm-256color
# colourise the output of ls
alias ls="ls --color=always"
# i don't know what this does anymore, looks important though. don't touch.
[ -n "$TMUX" ] && export TERM=xterm
