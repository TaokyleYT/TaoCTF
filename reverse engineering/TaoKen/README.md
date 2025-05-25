# reverse engineering/TaoKen

It seems that an anonymous company invented a new type of token called TaoKen.

There's also an exe file extracted from the company's application, which is the admin login terminal.

I wonder what that one taoken that logs you in is...

Flag format: TaoCTF{admin_token}

Hint:\
It costed me a few hours, not too hard tbh.\
no numbers are in the correct token :)

if you're really not gonna try the asm part, decrypt the cipher in `BIG_HINT.txt` and grab the source code.\
(but you still need to do some math with the source lol)