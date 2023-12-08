grammar EMail;

start: LocalPart'@'Domain;
LocalPart: LocalPartRule+;
Domain: LETTER(LETTER|DIGIT|'-')*'.'ListOfDomain;

LocalPartRule: LETTER|DIGIT|PrintableCharacters|'.';
LETTER: [A-Za-z];
PrintableCharacters: '!'|'#'|'$'|'%'|'&'|'\''|'*'|'+'|'-'|'/'|'='|'?'|'^'|'_'|'`'|'{'|'}'|'~';
DIGIT: [0-9];
ListOfDomain: 'com'|'org'|'net'|'ir'|'info'|'gov';