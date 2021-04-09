a=imread('truckNoise.gif');
ref=imread('truck.gif');
imshow(a);
f = fft2(a);
fs=fftshift(f);
n=fftshift(f);
figure; imshow(abs(fs)/(512*512)); title('spectrum magnitude');

for i=1:215
    for j=1:215
        fs(i,j)=0;
         fs(512-i,512-j)=0;
    end
end

for i=1:190
    for j=310:512
       fs(i,j)=0;
        fs(512-i,513-j)=0;
    end
end

figure; imshow(abs(fs)/(512*512)); title('spectrum magnitude after filter');
t1=ifftshift(fs);
ia1=ifft2(t1);
ia1=uint8(ia1);
figure;imshow(uint8(ia1));title('pic after filter');

% a = rgb2gray(a);
% ia1 = rgb2gray(ia1);

ia1=uint8(real(ia1));
n = size(a);
M = n(1);
N = n(2);

MSE_val = sum(sum((ref - ia1).^2)) / (M*N);

PSNR_val = 10*log10((256*256) / MSE_val);
fprintf('PSNR value of image %9.7f dB\n', PSNR_val);


