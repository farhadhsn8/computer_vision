profile on
A = imread('cameraman.gif');
imshow(a);
B0=bitget(A,1); figure, imshow(logical(B0));title('Bit plane 1');
B1=bitget(A,2); figure, imshow(logical(B1));title('Bit plane 2');
B2=bitget(A,3); figure, imshow(logical(B2));title('Bit plane 3');
B3=bitget(A,4); figure, imshow(logical(B3));title('Bit plane 4');
B4=bitget(A,5); figure, imshow(logical(B4));title('Bit plane 5');
B5=bitget(A,6); figure, imshow(logical(B5));title('Bit plane 6');
B6=bitget(A,7); figure, imshow(logical(B6));title('Bit plane 7');
B7=bitget(A,8); figure, imshow(logical(B7));title('Bit plane 8');

 profile report
 profile off
 
B0 = B0 .* 255;
B1 = B1 .* 255;
B2 = B2 .* 255;
B3 = B3 .* 255;
B4 = B4 .* 255;
B5 = B5 .* 255;
B6 = B6 .* 255;
B7 = B7 .* 255;
imwrite(B0,'b0.png');
imwrite(B1,'b1.png');
imwrite(B2,'b2.png');
imwrite(B3,'b3.png');
imwrite(B4,'b4.png');
imwrite(B5,'b5.png');
imwrite(B6,'b6.png');
imwrite(B7,'b7.png');