a=imread('f.png');
%a=rgb2gray(a);
%fa=fft2(a);
%sfa=fftshift(fa);
%figure;imshow(abs(sfa)/(512*512));title('sfa');

a1=a(:,:,1);
a2=a(:,:,2);
a3=a(:,:,3);
fa=fft2(a1);
sfa=fftshift(fa);
figure;imshow(abs(sfa)/(510*511));
figure;imshow(a1);
for i=223:227
    for j=205:219
       %d0=32;n=2;
       %h1(i,j)=1/(1+((sqrt((i-256)^2+(j-256)^2))/(d0))^(2*n));  
       sfa(510-i,511-j)=0;
       sfa(i,j)=0;
       sfa(i-18,j+15)=0;
       sfa(510-i+21,511-j-12)=0;
    end
end
figure;imshow(abs(sfa)/(510*511));
%fsfa1= medfilt2(abs(sfa)/(512*512));
figure;imshow(abs(sfa)/(512*512));title('sfa');


t1=ifftshift(sfa);
ia1=uint8(ifft2(t1));
figure;imshow(ia1);title('ia1');


figure;imshow(a3);title('a3');

%----------------------------------------------------------

a3=medfilt2(medfilt2(a3));
figure;imshow(a3);title('a3');

a(:,:,1)=ia1;
a(:,:,3)=a3;



for i=1:510
    for j=1:511
       d0=22;n=2;
       h(i,j)=1/(1+((sqrt((i-256)^2+(j-256)^2))/(d0))^(2*n));  
      
    end
end



figure;imshow(a);title('an');
figure;imshow(a2);title('a2');
fa=fft2(a2);
sfa=fftshift(fa);
figure;imshow(abs(sfa)/(510*511));
figure;imshow(h);

sfa=h.*sfa;
figure;imshow(abs(sfa)/(510*511));

t1=ifftshift(sfa);
ia1=uint8(ifft2(t1));
figure;imshow(ia1);title('ia1');





