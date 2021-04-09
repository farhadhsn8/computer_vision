a=imread('prob2_s2012.gif');
imshow(a);
f = fft2(a);
fs=fftshift(f);
n=fftshift(f);
figure; imshow(abs(fs)/(512*512)); title('spectrum magnitude');

for i=1:140
    for j=1:512
        fs(i,j)=0;
        fs(512-i,j)=0;
    end
end

for i=1:240
    for j=1:200
        fs(i,j)=0;
        fs(512-i,j)=0;
         fs(i,j)=0;
          fs(512-i,512-j)=0;
        
    end
end

for i=1:240
    for j=350:512
        fs(i,j)=0;   
    end
end



figure; imshow(abs(fs)/(512*512)); title('spectrum magnitude after filter');
t1=ifftshift(fs);
ia1=ifft2(t1);
figure;imshow(uint8(ia1));title('pic after filter');


 noise = n - fs ;

figure; imshow(abs(noise)/(512*512)); title('spectrum magnitude of noise');
t1=ifftshift(noise);
ia1=ifft2(t1);
figure;imshow(uint8(ia1));title('noise');

