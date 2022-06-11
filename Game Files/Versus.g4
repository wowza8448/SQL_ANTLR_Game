grammar Versus;

start : expr | <EOF> ;

expr     : 'VS' name=NUMBER #Player  
		 | 'duration' time=NUMBER #Game_time
		 | '->' player1=NUMBER #First_player
		 ;

NUMBER : ('0' .. '9') + (('0' .. '9') +)? ;


WS : [ \r\n\t]+ -> skip;