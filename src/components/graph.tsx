import React, { useState, useEffect } from 'react';
import Chart from 'react-apexcharts';

interface IGraphLine {
  selectButton: string;
}

interface DataGraph {
  name: string;
  data: number[];
}

export const GraphLine: React.FC<IGraphLine> = ({ selectButton }) => {
  const [selectedData, setSelectedData] = useState<DataGraph | null>(null);

  const chartData = {
    series: [
      {
        name: 'teste',
        data: [30, 40, 35, 50, 49, 60, 70, 91, 125],
      },
      {
        name: 'teste2',
        data: [30230, 400, 350, 500, 490, 600, 700, 910, 1250],
      },
      {
        name: 'teste3',
        data: [300, 400, 350, 500, 49032, 600, 700, 910, 1250],
      },
      {
        name: 'teste4',
        data: [300, 400, 35032, 500, 490, 600, 700, 910, 1250],
      },
    ],
  };

  useEffect(() => {
    const selectedSeries = chartData.series.find((object: DataGraph) => object.name === selectButton);

    // Atualiza o estado apenas se a série correspondente for encontrada
    if (selectedSeries) {
      setSelectedData(selectedSeries);
    }
  }, [selectButton]); // Executa o efeito apenas quando selectButton mudar

  const chartOptions = {
    chart: {
      type: 'line',
    },
    xaxis: {
      categories: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro'],
    },
  };
console.log(selectedData)
  return (
    <Chart options={chartOptions} series={selectedData ? [selectedData] : chartData.series} type="line" height={350} />
  );
};
