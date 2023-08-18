grammar pymidi;

programa
    :
    riff+ EOF
    ;

riff
    :
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