const url = "https://api.thingspeak.com/channels/3082725/feeds.json?api_key=ZKJ3X24YPUZ758EX";

fetch(url)
  .then(response => response.json())
  .then(data => {
    const feeds = data.feeds;

    const chartData = [["Päivä", "Lämpötila (°C)", "Ilmankosteus (%)"]];
    feeds.forEach(feed => {
      const time = new Date(feed.created_at);
      const temp = parseFloat(feed.field1);

      if (!isNaN(temp)) {
        // Simuloidaan kosteus (40–70 %)
        const humidity = Math.floor(Math.random() * 30) + 40;

        // Muotoillaan päivämäärä suomeksi (esim. "1. lokakuuta")
        const formattedTime = time.toLocaleDateString("fi-FI", {
          day: "numeric",
          month: "long"
        });

        chartData.push([formattedTime, temp, humidity]);
      }
    });

    // Ladataan Google Charts
    google.charts.load("current", { packages: ["corechart"] });
    google.charts.setOnLoadCallback(() => {
      const dataTable = google.visualization.arrayToDataTable(chartData);

      const options = {
        title: "Lämpötila ja ilmankosteus",
        curveType: "function",
        legend: { position: "bottom" },
        hAxis: { title: "Päivämäärä" },
        vAxis: { title: "Arvo" }
      };

      const chart = new google.visualization.LineChart(document.getElementById("chart_div"));
      chart.draw(dataTable, options);
    });
  })
  .catch(error => {
    console.error("Virhe datan haussa", error);
    document.getElementById("chart_div").textContent = "Virhe datan latauksessa";
  });
