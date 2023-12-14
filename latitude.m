
function [] = latitude(a,num)

%2.感染率受环境影响，存在纬度差异
%a = 0.0005;
%latitude 24-71
%pic 0-1000
for i= 1:num%纬度 像素距离
    R_lat(i) = a*log(i+1);
end
%预先生成好概率矩阵，然后叠加到程序里的随机矩阵上，从而提高概率
latitude_fix = repmat(R_lat',1,num);
save('latitude_fix.mat','latitude_fix')

