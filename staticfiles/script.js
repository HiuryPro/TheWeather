function graficoLine(ctx, dataset, title, font){
    new Chart(ctx, {
      type: "line",
      data: {
        datasets: dataset,
      },
      options: {
        plugins: {
          title: {
              display: true,
              text: title,
              font: {
                size: font
            }
          }
      },
        scales: {
            x: {
                type: 'time',
                time: {
                    unit: 'day',
                    displayFormats: {
                        day: 'dd/MM', // Format for date and time
                    },
                }
            }
           
        }
    }
    });
}

function criaGraficosUmTemp(dict){
  console.log(dict)
}
