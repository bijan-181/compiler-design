grammar Calculator;
expression: additiveExpression;

additiveExpression: multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*;

multiplicativeExpression: powerExpression ((MULTIPLY | DIVIDE) powerExpression)*;

powerExpression: primaryExpression ('^' powerExpression)?;

primaryExpression: NUMBER | '(' expression ')';
NUMBER: DIGIT+ ('.' DIGIT+)?;

PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
EXPONENTIATION: '^';

LPAREN: '(';
RPAREN: ')';

WS: [ \t\r\n]+ -> skip;
fragment DIGIT: [0-9];
