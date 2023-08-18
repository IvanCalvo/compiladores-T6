grammar pymidi;

programa
    :
    ;


NOTAS
    :
    ;

OITAVAS
    :
    ;

// Ignorando White Space
WS  
    :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip
    ;