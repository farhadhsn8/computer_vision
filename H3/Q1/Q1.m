a=imread('toys.GIF');
%imshow(a);
f = fft2(a);
fs=fftshift(f);
mg = abs(f);
mgs = abs(fs);
phase = angle(fs);
phaseonly = fs ./ abs(fs);


figure; imshow(abs(a),[]); title('Original');
figure; imshow(log(double(abs(fs))),[]); title('spectrum magnitude');
figure; imshow(phase,[]); title('spectrum phase');
figure; imshow(abs(ifft2(fs)),[]); title('reconstructed');
figure; imshow(abs(ifft2(mg)),[]); title('reconstructed magnitude only');
figure; imshow(abs(ifft2(phaseonly)),[]); title('reconstructed phase only');

% f =abs(f)/(512*512);
% imshow(f);
