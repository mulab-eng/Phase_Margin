disp('---- 位相余裕と安定性の確認 -----')

function result = cal_pm2(a,b,k)
	L = tf([k],[1 (a+b) a*b 0]);
	[Gm, Pm, Wcg, Wcp]=margin(L);
	disp('--------------------------------------------------------------')
	out=['位相余裕[deg]=', num2str(Pm), '  ゲイン交差周波数=', num2str(Wcp), ...
		'  a=', num2str(a), '  b=', num2str(b), '  k=', num2str(k)];
	disp(out);
	Gm=20*log10(Gm);
	out=['ゲイン余裕[dB]=', num2str(Gm), '  位相交差周波数=', num2str(Wcg)];
	disp(out);
	H=tf([1],[1]);
   FB=feedback(L,H);
   pole(FB)  % 閉ループ極
end

function result = cal_pm3(a,b,c, k)
	La = tf([1],[1 a]);
	Lb = tf([1],[1 b]);
	Lc = tf([1],[1 c]);
	L=k*La*Lb*Lc
	[Gm, Pm, Wcg, Wcp]=margin(L);
	disp('--------------------------------------------------------------')
	out=['位相余裕[deg]=', num2str(Pm), '  ゲイン交差周波数=', num2str(Wcp), ...
		'  a=', num2str(a), '  b=', num2str(b), ' c=', num2str(c), '  k=', num2str(k)];
	disp(out);
	Gm=20*log10(Gm);
	out=['ゲイン余裕[dB]=', num2str(Gm), '  位相交差周波数=', num2str(Wcg)];
	disp(out);
	H=tf([1],[1]);
   FB=feedback(L,H);
   pole(FB)  % 閉ループ極
end

a=2; b=3; k=5*sqrt(2);
cal_pm2(a, b, k);

a=4; b=6; k=40*sqrt(2);
cal_pm2(a, b, k);

a=2; b=5; k=14*sqrt(3);
cal_pm2(a, b, k);

a=3; b=3; k=12*sqrt(3);
cal_pm2(a, b, k);

a=2*sqrt(3); b=2*sqrt(3); k=32;
cal_pm2(a, b, k);

a=4; b=15; k=114;
cal_pm2(a, b, k);

a=5; b=9; k=84;
cal_pm2(a, b, k);

a=sqrt(3); b=3; k=sqrt(6)*6;
cal_pm2(a, b, k);

a=1; b=sqrt(3); k=2*sqrt(2);
cal_pm2(a, b, k);

a=1; b=sqrt(3); c=sqrt(3); k=4*sqrt(2);
cal_pm3(a, b, c, k);
