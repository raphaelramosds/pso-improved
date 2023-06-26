// alfa=0.6629
alfa=1

function d=direction(x)
    d=(sin(4*x) + 4*cos(4*x))/(15*sin(4*x)-8*cos(4*x))
endfunction

xit=zeros(4)
dit=zeros(4)

xit(1)=0.0
dit(1)=direction(0)

for i=2:4
    xit(i) = xit(i-1) + alfa*direction(xit(i-1))
    dit(i)= direction(xit(i-1))
end

disp(xit)
