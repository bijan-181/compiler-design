grammar ExtractInfo;

fragment DIGIT: [0-9];
fragment LOCAL_SUBPART : [a-zA-Z0-9._%+-]+;
fragment DOMAIN_SUBPART : [a-zA-Z0-9.-]+;
URL: ('https://'|'http://')('www.')? DOMAIN_SUBPART '.' DOMAIN_SUBPART '/'? (DOMAIN_SUBPART'/'?)* ;
EMAIL: LOCAL_SUBPART '@' DOMAIN_SUBPART '.' DOMAIN_SUBPART;
NUMBER10: DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT DIGIT ; // Match one or more digits
NUMBER11 : NUMBER10 DIGIT;
FLOAT: DIGIT+ '.' DIGIT+;
VERSION: ('v'|'version'|'V')? (' '|':')? DIGIT+ '.' DIGIT+( '.' DIGIT+)?;


text: (email|float|melli_number|phonenumber|url|version|WORD|WS)*;
email: EMAIL ;
melli_number : NUMBER10;
phonenumber : NUMBER11;
float: FLOAT;
url: URL;
version: VERSION;


WORD: [a-zA-Z0-9-./,:!#$%^&;]+;
WS: ([ \t\r\n]+|EOF) -> skip;
