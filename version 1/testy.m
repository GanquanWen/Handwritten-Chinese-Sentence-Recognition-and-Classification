function [jx,jy]=testy(goal1)
[m,n]=size(goal1);
jx(m)=0;
xx=0;j=1;
for  y=1:n
    for x=1:m
        if goal1(x,y)==1
            xx=1;
        end
    end
    if xx==1
        jx(j)=y;
        j=j+1;
    end
end
jx=jx(1);


jy(m)=0;
xx=0;j=1;
for  y=n:-1:1
    for x=m:-1:1
        if goal1(x,y)==1
            xx=1;
        end
    end
    if xx==1
        jy(j)=y;
        j=j+1;
    end
end
jy=jy(1);