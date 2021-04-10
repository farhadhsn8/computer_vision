a=imread('badexposure.jpg');

figure;imshow(a);
%------histogram------------------------- 
figure;imhist(a);
%-------equlization--------------
a2=histeq(a);

figure;imshow(a2);

figure;imhist(a2);