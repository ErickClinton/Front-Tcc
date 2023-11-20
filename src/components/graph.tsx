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
        name: 'Grafico de mortes por estado',
        data: [2043, 7242, 14443, 2167, 31459, 28157, 11845, 15041, 28041,11053,65507,11016,15090,19025,10542,22687,8354,46022,76852,8715,7432,2180,41921,22703,6502,179039,4232],
      }
      
    ],
  };


  const chartDataCases = {
    series: [
      {
        name: 'Casos Confirmados',
        data: [4189760, 2920177, 2754359, 2962414, 6469442],
      },
      {
        name: 'Mortes',
        data: [65507, 46022, 76852, 41921, 179039],
      },
      {
        name: 'Vacinados',
        data: [15270991, 8434427, 12211486, 8439439, 29057424],
      },
    ],
  };

  const boxplotData = {
    series: [{
      data: [{
        x: "mortes",
        y: [41921, 46022, 65507, 76852, 179039]
      },
      {
        x: "total de casos",
        y: [2754359, 2920177, 2962414, 4189760, 6469442]
      },
 
      {
        x: "vacinados",
        y: [8434427, 8439439, 12211486, 15270991, 29057424]
      }]
    }]
  };


  useEffect(() => {
    const selectedSeries = chartData.series.find((object: DataGraph) => object.name === selectButton);

    if (selectedSeries) {
      setSelectedData(selectedSeries);
    }
  }, [selectButton]); 

  const chartOptions = {
    chart: {
      type: 'bar',
    },
    xaxis: {
      categories: ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO'],
    },
    dataLabels:{
      enabled:false
    },
    tooltip: {
      enabled: true,
    },
    plotOptions: {
      bar: {
        distributed: false, 
      },
    },
    
  };

  const chartOptionsCases = {
    chart: {
      type: 'bar',
      height: 350,
    },
    plotOptions: {
      bar: {
        horizontal: false,
      },
    },
    dataLabels: {
      enabled: false,
    },
    xaxis: {
      categories: ['MG', 'PR', 'RJ', 'RS', 'SP'],
      title: {
        text: 'Estados',
      },
    },
    yaxis: {
      title: {
        text: 'Valores',
      },
    },
    fill: {
      opacity: 1,
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return val.toLocaleString();
        },
      },
    },
  };
  const boxplotOptions = {
    chart: {
      type: 'boxPlot',
    },
    tooltip: {
      enabled: true,
    },
    xaxis: {
      categories: ['mortes', 'total de casos','vacinados'],
    },
  };
  
  return (
    <>
    {selectButton === 'Grafico de morte por estado' ? (
        <Chart options={chartOptions} series={selectedData ? [selectedData] : chartData.series} type="bar" height={350} />
      ) : selectButton === 'Grafico BoxPlot' ? (
        <Chart options={boxplotOptions} series={boxplotData.series} type="boxPlot" height={350} />
      ) : selectButton === 'Grafico com mais casos' ? (
        <Chart options={chartOptionsCases} series={chartDataCases.series} type="bar" height={350} />
      ):null}
     </>
    
  );
};
