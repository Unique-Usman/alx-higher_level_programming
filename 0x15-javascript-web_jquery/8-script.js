$(document).ready(function () {
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (data, status) {
    let res = data.results;

    for (const ele of res) {
      $("#list_movies").append(`<li>${ele.title}</li>`);
    }
  })
})
