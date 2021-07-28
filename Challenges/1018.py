value = int(input());
val = value;
cem = cinquenta = vinte = dez = cinco = dois = um = 0;

if int(value/100) >= 1:
	cem = int(value/100);
	value -= cem*100;

if int(value/50) >= 1:
	cinquenta = int(value/50);
	value -= cinquenta*50;

if int(value/20) >= 1:
	vinte = int(value/20);
	value -= vinte*20;

if int(value/10) >= 1:
	dez = int(value/10);
	value -= dez*10;

if int(value/5) >= 1:
	cinco = int(value/5);
	value -= cinco*5;

if int(value/2) >= 1:
	dois = int(value/2);
	value -= dois*2;

if int(value/1) >= 1:
	um = int(value/1);
	value -= um*1;

print(".format(){}" .format(val));
print(".format(){} nota(s) de R$ 100,00" .format(cem));
print(".format(){} nota(s) de R$ 50,00" .format(cinquenta));
print(".format(){} nota(s) de R$ 20,00" .format(vinte));
print(".format(){} nota(s) de R$ 10,00" .format(dez));
print(".format(){} nota(s) de R$ 5,00" .format(cinco));
print(".format(){} nota(s) de R$ 2,00" .format(dois));
print(".format(){} nota(s) de R$ 1,00" .format(um));