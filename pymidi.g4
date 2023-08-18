grammar pymidi;

program
    :
    loop+ EOF
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

NUM
    :
    ('0'..'9')+
    ; 


//identificadores
IDENT
    :   [a-zA-Z][a-zA-Z0-9_]*
    ;

// Ignorando White Space
WS  
    :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip
    ;

trecho
    :
    'riff' IDENT '(' NOTA POSICAO NUM (',' NOTA POSICAO NUM)* ')'
    ;

loop
    :
    'tocar' '(' trecho ',' NUM (';' trecho ',' NUM)* ')'
    ;