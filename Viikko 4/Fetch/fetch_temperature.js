const url = "https://api.thingspeak.com/channels/3082725/feeds.json?api_key=ZKJ3X24YPUZ758EX";

fetch(url)
  .then(response => response.json())
  .then(data => {
    const feeds = data.feeds;

    const temperatures = feeds.map(feed => ({
      time: feed.created_at,
      temp: parseFloat(feed.field1)
    }));

    document.getElementById("output").textContent = JSON.stringify(temperatures);
  })
  .catch(error => {
    console.error("Error fetching data", error);
    document.getElementById("output").textContent = "Error loading data";
  });
