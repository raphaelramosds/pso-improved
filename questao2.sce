// Valores máximos do intervalo
pmax=%pi/2
pmin=-pmax

// Condição de primeira ordem
function p=sol(m)
    x=0.25*(atan(-4)+%pi*m)
    y=-2*x
    lambda=exp(-x-y)*sin(2*x)*(cos(y)+sin(y))
    p=[x y lambda]
endfunction

// Soluções válidas que estão entre -pi/2 e pi/2
p0=sol(0)
p1=sol(1)

// Condição de segunda ordem
function Exx=t(x)
    Exx=exp(-x(1)-x(2))*cos(x(2))*(-4*cos(2*x(1))-3*sin(2*x(1)))
endfunction

function Exy=u(x)
    Exy=exp(-x(1)-x(2))*(sin(2*x(1))-2*cos(2*x(1)))*(sin(x(2))+cos(x(2)))
endfunction

function Eyy=v(x)
    Eyy=2*exp(-x(1)-x(2))*sin(2*x(1))*sin(x(2))
endfunction

function p=testPoint(x)
    w=poly(0,'w')
    j=[2 1]
    h=[t(x) u(x); u(x) v(x)]
    m=[h-w*eye((2,2)) j'; j 0]
    disp(m)
    p=roots(det(m))
endfunction

disp(testPoint(p0))
disp(testPoint(p1))


