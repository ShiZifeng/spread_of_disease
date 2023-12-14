function [season_fix] = season(a,time,full_time,years)
%SEASON 附加感染概率，随时间季节变化
%   输入：当前仿真时间，仿真总时间,期望的仿真年数（四季轮回）
%   输出：额外概率，需要加上基础感染概率
season_fix = a*cos(2*years*pi/full_time*time);
end

