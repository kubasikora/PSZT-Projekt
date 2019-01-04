clear all;
A=[5, 5, 5];
B=[50, 50, 50];
ep=[100, 100, 100];
mi=[20, 50, 50];
lam=[10, 20, 30];
i=size(A);
i=i(2);

for k=1:i
 [Av(k), Sd(k),Va(k), Ma(k)]= generate_histogram(A(k), B(k), ep(k), lam(k) ,mi(k));
end
