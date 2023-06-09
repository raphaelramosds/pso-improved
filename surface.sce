clear
//
[x,y]=meshgrid(-500:5:500,-500:5:500);
//
z=-x.*sin(sqrt(abs(x)))-y.*sin(sqrt(abs(y)));
x=x/250;
y=y/250;
// r: Rosenbrock's function
r=100*(y-x.^2).^2+(1-x).^2;
r1=(y-x.^2).^2+(1-x).^2;
rd=1+r1;
//
x1=25*x;
x2=25*y;
xs =-10:0.1:10;
ys =-10:0.1:10;
a=500;
b=0.1;
c=0.5*%pi;
//
F10=-a*exp(-b*sqrt((x1.^2+x2.^2)/2))-exp((cos(c*x1)+cos(c*x2))/2)+exp(1);
//
[n nx]=size(xs);
[n ny]=size(ys);
for i=1:nx
for j=1:ny
zsh(i,j)=0.5-((sin(sqrt(xs(i)^2+ys(j)^2)))^2-0.5)./(1+0.1*(xs(i)^2+ys(j)^2))^2;
end
end
//
Fobj=F10.*zsh//+a*cos(x1/30);
//
//surf(x1,x2,Fobj)
//
w=r.*z;
w1=r+z;
w2=z-r1;
w3=r-z;
w4ant=sqrt(r.^2+z.^2);
w4=sqrt(r.^2+z.^2)+Fobj;
w5=w-0.5*w1;
w6=w+w2;
w7=w1+w4;
w8=w1-w4;
w9=w2-w4;
w10=w2+w4;
w11=w3-w4;
w12=r+w4.*cos(y);
w13=sqrt(w1)+sqrt(w3)-w4ant.*cos(x);
w14=z.*exp(sin(r1));
w15=z.*exp(cos(r1));
w16=w14+w4;
w17=-w14+w4;
w18=-w15+w4;
w19=exp(-r1).*z;
w20=x.*z;
w21=(x+y).*z;
w22=(x-y).*z;
w23=z./rd;
w24=(x-y).*w23;
w25=(x+y).*w23;
w26=-w4./rd;
w27=w4+w23;
w28=w4-w23;
w29=w14+w23;
w30=w4+w14+w23;
w31=w21+w22;
w32=w21+w23;
w33=w22+w25;
w34=w22+w26;
w35=w23+w27;
w36=w23+w28;
w37=w23+w29;
w38=w23+w30;
w39=w25+w30;
w40=w27+w30;
x = x*250;
y = y *250;
//
surf(x,y,w35);
