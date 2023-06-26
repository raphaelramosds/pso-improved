// Condição de primeira ordem
p0=[4/sqrt(5) 2/sqrt(5) -sqrt(5)/4]
p1=-1*p0

// Condição de segunda ordem
function h=hessian(lambda)
    h=[2*lambda 0; 0 2*lambda]
endfunction

function jx=jacobx(x)
    jx=[2*x(1) 2*x(2)]
endfunction

// Vetor solução (x,y,lambda)
function p=testPoint(x)
    w=poly(0,'w')
    j=jacobx(x)
    h=hessian(x(3))
    m=[h-w*eye((2,2)) j'; j 0]
    disp(m)
    p=roots(det(m))
endfunction

disp(testPoint(p0))
disp(testPoint(p1))
