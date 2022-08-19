const weatherContainer = document.querySelector('#weather-container')
const locationBar = document.querySelector('#location-bar')

async function getWeather(latitude, longitude, api){
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?units=imperial&lat=${latitude}&lon=${longitude}&appid=${api}`)
    const data = await response.json()
    console.log(data)
    sortData(data)
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    locationBar.innerHTML = "Ayyyyy, where you at?";
  }
}

function showPosition(position) {
  const latitude = position.coords.latitude
  const longitude = position.coords.longitude
  locationBar.innerHTML = `Latitude: ${position.coords.latitude} 
   Longitude: ${position.coords.longitude}`;
  getWeather(latitude, longitude, api)
}

function sortData(data){
  weatherContainer.style.visibility = 'visible';
    let dateTime = new Date(data.dt*1000)  
    document.querySelector('.date-container').innerHTML = `<h2 class='date-contents'>${dateTime.toLocaleString()}</h2>`
    
    // temp-container
    document.querySelector('.temp-container').innerHTML = `<div><p class='data-text'>Min Temp:</p> <p class='data-text'>${data.main.temp_min} F</p></div> <div><p class='data-text'>Current Temp:</p> <p class='data-text'>${data.main.temp} F</p></div> <div><p class='data-text'>Max Temp:</p> <p class='data-text'>${data.main.temp_max} F</p></div>`

    // location-container
    let sunset = new Date(data.sys.sunset*1000);
    let sunrise = new Date(data.sys.sunrise*1000);
    document.querySelector('.location-container').innerHTML = `<div class='data-text'>Sunrise: ${sunrise.toLocaleTimeString()}</div><br> <div class='data-text'>Sunset: ${sunset.toLocaleTimeString()}</div>`

    // forecast-container
    document.querySelector('.forecast-container').innerHTML = `<i class="owf owf-${data.weather[0].id}-d owf-5x"></i> <h2 class='forecast'>${data.weather[0].description}</h2>`
}
getLocation()





