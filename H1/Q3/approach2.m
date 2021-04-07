profile on
A = imread('cameraman.gif');
imshow(A);
B0 = mod(A,2);t=A-B0;
B1 = mod(t,4)/2;t=t-2*B1;
B2 = mod(t,8)/4;t=t-4*B2;
B3 = mod(t,16)/8;t=t-8*B3;
B4 = mod(t,32)/16;t=t-16*B4;
B5 = mod(t,64)/32;t=t-32*B5;
B6 = mod(t,128)/64;t=t-64*B6;
B7 = mod(t,256)/128;t=t-128*B7;

 figure, imshow(logical(B0));title('Bit1');
 figure, imshow(logical(B1));title('Bit2');
 figure, imshow(logical(B2));title('Bit3');
 figure, imshow(logical(B3));title('Bit4');
 figure, imshow(logical(B4));title('Bit5');
 figure, imshow(logical(B5));title('Bit6');
 figure, imshow(logical(B6));title('Bit7');
 figure, imshow(logical(B7));title('Bit8');

 profile report
 profile off
% B0 = B0 .* 255;
% B1 = B1 .* 255;
% B2 = B2 .* 255;
% B3 = B3 .* 255;
% B4 = B4 .* 255;
% B5 = B5 .* 255;
% B6 = B6 .* 255;
% B7 = B7 .* 255;
% imwrite(B0,'b0.png');
% imwrite(B1,'b1.png');
% imwrite(B2,'b2.png');
% imwrite(B3,'b3.png');
% imwrite(B4,'b4.png');
% imwrite(B5,'b5.png');
% imwrite(B6,'b6.png');
% imwrite(B7,'b7.png');