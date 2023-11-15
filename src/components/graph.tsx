import React from 'react';
import Chart from 'react-apexcharts';

export const GraphLine: React.FC = () => {
  const chartData = {
    series: [
      {
        name: 'Série 1',
        data: [30, 40, 35, 50, 49, 60, 70, 91, 125],
      },
      {
        name: 'Série2',
        data: [300, 400, 350, 500, 490, 600, 700, 910, 1250],
      },
    ],
  };

  const chartOptions = {
    chart: {
      type: 'line',
    },
    xaxis: {
      categories: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro'],
    },
  };

  return (
    <Chart options={chartOptions} series={chartData.series} type="bar" height={350} />
  );
};

