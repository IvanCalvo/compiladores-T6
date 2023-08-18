grammar pymidi;

program
    :
    trecho+ EOF
    ;

trecho
    :
    'riff' IDENT '(' NOTA POSICAO DURACAO (',' NOTA POSICAO DURACAO)* ')'
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

DURACAO
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