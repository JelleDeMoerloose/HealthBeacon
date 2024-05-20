  // Chart.js script
  var ctx1 = document.getElementById('emergenciesChart').getContext('2d');
  var emergenciesChart = new Chart(ctx1, {
      type: 'bar',
      data: {
          labels: [],
          datasets: [{
              label: 'Amount of Emergencies',
              data: [],
              fill: true,
              //borderColor: 'rgba(75, 192, 192, 0.1)',
              tension: 0.1,
              backgroundColor: 'rgba(45,153,225, 1)'
              
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: true
              }
          },
          plugins: {
            legend: {
                display: false
                
            }
        }
      }
  });

  var ctx2 = document.getElementById('questionsChart').getContext('2d');
  var questionsChart = new Chart(ctx2, {
      type: 'doughnut',
      data: {
          labels: ['Normal Questions', 'Emergency Questions'],
          datasets: [{
              label: 'Question Types',
              data: [300, 50],
              backgroundColor: [
                  'rgb(255, 99, 132)',
                  'rgb(54, 162, 235)'
              ]
          }]
      },
      options: {}
  });

//  setTimeout(function() {
//   emergenciesChart.data.datasets[0].data[6] = 70;
//    emergenciesChart.update();
//  }, 2000);

function fetchData() {
    fetch('http://localhost:5000/staff/emergencies/dashboard/all')
      .then(response => response.json())
      .then(data => {
      
        var labels = data.label;
        var dataValues = data.data;
  
    
        emergenciesChart.data.labels = labels;
        emergenciesChart.data.datasets[0].data = dataValues

        emergenciesChart.update()

      })
      .catch(error => console.error('Error fetching data:', error));
  }

fetchData()

setInterval(fetchData, 1000);
  