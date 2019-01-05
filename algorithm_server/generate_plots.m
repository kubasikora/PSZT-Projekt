function [error_average, error_std, error_variance]=generate_plots(A, B, mi, lambda)
    load(['results/statistic/statisticA=',num2str(A),'B=',num2str(B),'mi=',num2str(mi),'lambda=',num2str(lambda),'.mat']);
    i=size(error_average);
    i=i(2);
    x=linspace(1,i, i);
    f=figure;
    set(f, 'Units', 'Normalized', 'OuterPosition', [0, 0.04, 1, 0.96]);
    subplot(3, 1,1);
    plot(x, error_average);
    title(['Srednie wartosci statystyczne w zaleznosci od liczby epok: A=',num2str(A), ', B=',num2str(B), ', \mu','=',num2str(mi), ', \lambda','=',num2str(lambda) ]);
    xlabel('epochs ');
    ylabel('Average error');
    xlim([1 i])
    subplot(3, 1, 2);
    plot(x, error_std);

    xlabel('epochs ');
    ylabel('Standard deviation');
    xlim([1 i])
    subplot(3, 1, 3);
    plot(x, error_variance);
    ylabel('Variance');
    xlabel('epochs');
    xlim([1 i]);
    print(['FIGURES/statistic/plotA',num2str(A),'B',num2str(B),'mi',num2str(mi),'lambda',num2str(lambda)], '-dpng', '-r400');
    
%     f2=figure;
%     set(f2, 'Units', 'Normalized', 'OuterPosition', [0, 0.04, 1, 0.96]);
%     plot(x, error_average);
%     hold on;
%     xlabel('epochs ');
%     ylabel('Values');
%     xlim([1 i])
%     plot(x, error_std);
%     plot(x, error_variance);

end