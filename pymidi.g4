grammar pymidi;

program
    :
    declaracoes loops EOF
    ;

declaracoes
    :
    declaracao_trecho*
    ;

loops
    :
    loop*
    ;

declaracao_trecho
    :
    'riff' IDENT '=' valor_trecho
    ;

valor_trecho
    :
    '(' toque (',' toque)* ')'
    ;

toque
    : NOTA posicao=NUM '-' duracao=NUM | '-'
    ;

loop
    :
    'tocar' '(' IDENT ',' NUM (';' IDENT ',' NUM)* ')'
    ;


//lexer
NUM
    :
    ('0'..'9')+('.'('0'..'9')+)?
    ; 

//identificadores
IDENT
    :   
    [a-z][a-z0-9_]*
    ;

NOTA
    :
    'C' | 'C#' | 'D' | 'D#' | 'E' | 'F' | 'F#' | 'G' |
    'G#' | 'A' | 'A#' | 'B'
    ;

// Ignorando White Space
WS  
    :   
        ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip
    ;