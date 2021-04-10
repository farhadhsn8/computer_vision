a = imread('Q4_3.tif');
imshow(a);

se = strel('disk',15)
% figure;imshow(bw);
% a1=uint8((t2+z1));
% figure;imshow(a1);title('a1');
bb = imopen(a,se);a2 = a - bb;a3 = imadjust(a2);

bw = imbinarize(a3);
bw = bwareaopen(bw,50);

cc = bwconncomp(bw,4);
c = cc.NumObjects;
graindata = regionprops(cc,'basic')
grain_areas = [graindata.Area]; 
z = 0 ;
for i=1:c
  z = z + grain_areas(i);
end

% figure;imshow(bw);
% a1=uint8((t1+z));
% figure;imshow(a1);title('a1');
% figure;imshow(bw);
% fprintf('counter :  %d' , c);

figure;imshow(a3);title('a3');
fprintf('counter :  %d' , c);

