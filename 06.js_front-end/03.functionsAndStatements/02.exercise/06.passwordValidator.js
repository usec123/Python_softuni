solve = (pass) => console.log((a = pass.length<6||pass.length>10?'Password must be between 6 and 10 characters\n':'')+
(b = (pass.length!==Array.from(pass.matchAll(/[a-z0-9]/gi)).length?'Password must consist only of letters and digits\n':''))+
(c = Array.from(pass.matchAll(/[\d]/g)).length<2?'Password must have at least 2 digits':'')+
(a+b+c === ''?'Password is valid':''));


solve('logIn')
solve('MyPass123')
solve('Pa$s$s')