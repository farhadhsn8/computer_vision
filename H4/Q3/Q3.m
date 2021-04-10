a=imread('Q4_1.tif');
b=imread('Q4_4.tif');
figure; imshow(b);
filter=ones(3,3);
figure; imshow(a);
a = imerode(a,filter);a = imdilate(a,filter);
a = imerode(a,filter);a = imerode(a,filter);
a = imerode(a,filter);a = imerode(a,filter);
% b = im2bw(b,0.49);
% h = viscircles(centers,radii);
% figure; imshow(b);
% [centers,radii] = imfindcircles(b,[21 24],'ObjectPolarity','dark','Sensitivity',0.92);
% imshow(b);
% figure;
b = im2bw(b,0.49);
figure; imshow(b);
[centers,radii] = imfindcircles(b,[21 24],'ObjectPolarity','dark','Sensitivity',0.92);
imshow(b);
h = viscircles(centers,radii);
a = imdilate(a,filter);a = imerode(a,filter);

a = imerode(a,filter);a = imdilate(a,filter);

a = imdilate(a,filter);

figure; imshow(a);





figure;
[centersBright,radiibig] = imfindcircles(b,[31 49],'ObjectPolarity','dark','Sensitivity',0.88);
imshow(b)
hBright = viscircles(centersBright, radiibig,'Color','g');