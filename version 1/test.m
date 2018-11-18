function [ix,iy]=test(goal1)
[m,n]=size(goal1);
% fprintf('%d', m);
% fprintf('%d', n);
ix(m)=0;
xx=0;j=1;
for  x=1:m
    for y=1:n
        if goal1(x,y)==1
            xx=1;
        end
    end
    if xx==1
        ix(j)=x;
        j=j+1;
    end
end
ix=ix(1);

iy(m)=0;
xx=0;j=1;
for  x=m:-1:1
    for y=n:-1:1
        if goal1(x,y)==1
            xx=1;
        end
    end
    if xx==1
        iy(j)=x;
        j=j+1;
    end
end
iy=iy(1);