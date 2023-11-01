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
  var regioes = Object.keys(dict)
  for (var i in regioes){
    console.log(regioes[i])
  }


  const section = document.getElementById("section")

  const row = document.createElement("div");
  row.classList = ["row"]



  const col = document.createElement("div")
  col.classList = ["col-md-6"]



  const divC =  document.createElement("div")
  divC.classList = ["chart-container"]
  divC.style = "aspect-ratio: 2"
  
  const canvas = document.createElement("canvas")
  canvas.id = "myChart3"


  divC.appendChild(canvas)
  col.appendChild(divC)
  row.appendChild(col)


  section.appendChild(row)

  console.log("Funciona")
}
