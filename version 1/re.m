I=imread('1.jpeg');
figure(1)
imshow(I)
I=rgb2gray(I);
I=1-imbinarize(I);
[ix1,iy1]=test(I);
[jx1,jy1]=testy(I);
goal=I(ix1:iy1,jx1:jy1); %size(goal,1) 159, size(goal,2) 146
goal=[zeros(size(goal,1),2) goal zeros(size(goal,1),2)];
a=sum(goal);

x = 1: size(a, 2);
figure(2)
plot(x, a);

label=find(a>0);
summ=0;
j=1;

KK = zeros(1,size(goal, 2));
JJ = zeros(1,size(goal, 2));

for i=1:length(label)-1
    if (label(i+1)-label(i)) > 1
        KK(j)=label(i);
        JJ(j)=label(i+1);
        summ=summ+1;
        j=j+1;
    end
end

%figure(2)
JJ=[3 JJ];
KK(j) = size(goal,2)-2;

% for k=2:length(JJ)-1
%      if (JJ(k) - KK(k-1) > 0 && JJ(k) - KK(k-1) < 16)
%           KK = KK(k:length(KK));
% %          JJ = [JJ(k-1) JJ(k+1:length(JJ))];
% %          summ=summ-1;
%      end
%  end

summ=summ+1;
figure(3)
for i=1:summ
    subplot(1,summ,i);
    II=goal(:,JJ(i)-2:KK(i)+2);
    %II=imresize(II,[25,18]);
    imshow(II);
    hold on
end