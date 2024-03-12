$(document).ready(function () {
  $("#toggle_header").click(function () {
    let header = $("header");
    let color = header.css("color");

    if (color === "rgb(255, 0, 0)" || color === "red") {
      header.css("color", "green");
    } else {
      header.css("color", "red");
    }
  });
});

