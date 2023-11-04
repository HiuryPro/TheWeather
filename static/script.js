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

  console.log(regioes.length)
  console.log()

  const rowNumbers = (regioes.length / 2) + (regioes.length % 2)
  var count = 1

  const section = document.getElementById("section")

  for(var i = 0; i < rowNumbers; i++){
    const row = document.createElement("div");
    row.classList = ["row"]
  
    console.log("Funciona");
  
    const col1 = document.createElement("div")
    col1.classList = ["col-md-6"]

    const col2 = document.createElement("div")
    col2.classList = ["col-md-6"]
  
  
  
    const divC1 =  document.createElement("div")
    divC1.classList = ["chart-container"]
    divC1.style = "aspect-ratio: 2"

    const divC2 =  document.createElement("div")
    divC2.classList = ["chart-container"]
    divC2.style = "aspect-ratio: 2"
    
    const canvas1 = document.createElement("canvas")
    canvas1.id = "UT" + count

    count++
    const canvas2 = document.createElement("canvas")
    canvas2.id = "UT" + count
    count++
  
    divC1.appendChild(canvas1)
    col1.appendChild(divC1)

    divC2.appendChild(canvas2)
    col2.appendChild(divC2)

    row.appendChild(col1)
    row.appendChild(col2)

    section.appendChild(row)
  }

  var count = 1

  for (var i in regioes){
    console.log("UT" + count)
    const ctx = document.getElementById("UT" + count);
    console.log(dict[regioes[i]])
    console.log(regioes[i])
    graficoLine(ctx, dict[regioes[i]],`Gráfico Temperatura/Umidade ${regioes[i]} (2023)`,20)
    count++

  }



  console.log("Funciona2")
}
