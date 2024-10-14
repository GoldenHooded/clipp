#!/bin/bash

_clipp_completions() {
    local cur commands
    commands="add list ls ex remove clear"

    # Obtener la palabra actual que se está escribiendo
    cur="${COMP_WORDS[COMP_CWORD]}"

    # Ofrecer las opciones de comandos posibles que coincidan con la palabra actual
    COMPREPLY=( $(compgen -W "$commands" -- "$cur") )

    return 0
}

# Registrar la función de autocompletado para 'clipp'
complete -F _clipp_completions clipp
