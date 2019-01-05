function [ average, SD, variance, maxi ] = generate_histogram( A, B, ep, lam, mi)
   load(['results/spammer/spammer_test_A=',num2str(A),'B=',num2str(B),'epochs=',num2str(ep),'mi=',num2str(mi),'lambda=',num2str(lam),'.mat']);
    errors2=double(errors);
    average=mean(errors2);
    SD=std(errors2);
    variance=var(errors2);
    maxi=max(errors2);
    f=figure;
    set(f, 'Units', 'Normalized', 'OuterPosition', [0, 0.04, 1, 0.96]);
    histogram(errors2);
    xlim([-2 (maxi+2)])
    title(['Histogram: A=',num2str(A)',', B=',num2str(B),', epochs=',num2str(ep),', ','\mu','=',num2str(mi),', \lambda','=',num2str(lam),', average=',num2str(average),', SD=',num2str(SD),', variance=',num2str(variance),', max error=',num2str(maxi)]);
    print(['FIGURES/spammer/histA',num2str(A)','B',num2str(B),'epochs',num2str(ep),'mi',num2str(mi),'lambda',num2str(lam)], '-dpng', '-r400');

end

