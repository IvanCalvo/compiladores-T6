grammar pymidi;

program
    :
    trecho+ EOF
    ;

trecho
    :
    'riff' '(' NOTA (',' NOTA)* ')'
    ;

NOTA
    :
    'C' | 'C#' | 'D' | 'D#' | 'E' | 'F' | 'F#' | 'G' |
    'G#' | 'A' | 'A#' | 'B'
    ;

POSICAO
    :
    ('1'..'7')
    ;

// Ignorando White Space
WS  
    :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip
    ;