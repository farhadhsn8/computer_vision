a=imread('pepper.jpg');
a=rgb2gray(a);
fa=fft2(a);
sfa=fftshift(fa);
figure;imshow(abs(sfa)/(512*512));title('sfa');
for i=1:512
    for j=1:512
       d0=50;n=1;
       h1(i,j)=1/(1+((sqrt((i-256)^2+(j-256)^2))/(d0))^(2*n));
       d0=150;n=1;
       h2(i,j)=1/(1+((sqrt((i-256)^2+(j-256)^2))/(d0))^(2*n));
       d0=50;n=5;
       h3(i,j)=1/(1+((sqrt((i-256)^2+(j-256)^2))/(d0))^(2*n));
       d0=150;n=5;
       h4(i,j)=1/(1+((sqrt((i-256)^2+(j-256)^2))/(d0))^(2*n));

    end
end
figure;imshow(h1);title('h1');
figure;imshow(h2);title('h2');
figure;imshow(h3);title('h3');
figure;imshow(h4);title('h4');

fsfa1=sfa.*h1;
fsfa2=sfa.*h2;
fsfa3=sfa.*h3;
fsfa4=sfa.*h4;

figure;imshow(abs(fsfa1)/(512*512));title('fsfa1');
figure;imshow(abs(fsfa2)/(512*512));title('fsfa2');
figure;imshow(abs(fsfa3)/(512*512));title('fsfa3');
figure;imshow(abs(fsfa4)/(512*512));title('fsfa4');

t1=ifftshift(fsfa1);
ia1=ifft2(t1);
figure;imshow(uint8(ia1));title('ia1');

t2=ifftshift(fsfa2);
ia2=ifft2(t2);
figure;imshow(uint8(ia2));title('ia2');

t3=ifftshift(fsfa3);
ia3=ifft2(t3);
figure;imshow(uint8(ia3));title('ia3');

t4=ifftshift(fsfa4);
ia4=ifft2(t4);
figure;imshow(uint8(ia4));title('ia4');


