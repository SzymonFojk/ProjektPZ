const tl = gsap.timeline({ defaults: { ease: "power1.out" } });

tl.to(".text", { y: "0%", duration: 1, stagger: 0.25 });
tl.to(".slider", { y: "-100%", duration: 1.5, delay: 0.5 });
tl.to(".intro", { y: "-100%", duration: 1 }, "-=1");
tl.fromTo("nav", { opacity: 0 }, { opacity: 1, duration: 1 });
tl.fromTo(".big-text", { opacity: 0 }, { opacity: 1, duration: 1 }, "-=1");

//var xd2 = document.getElementById("circle");
    // var reg = document.getElementById("btn"
console.log("no elo")
var login = true;
function pressed_reg()
{
  console.log("KLIK");
   

  if (login){
  var zmienna = document.getElementById("circle");
  var rotateValue = circle.style.transform;
  var rotateSum = rotateValue + "rotate(-180deg)";
    console.log("xddddddddddd");

  console.log(rotateValue.size);
  console.log(rotateSum.lenght);
      console.log("********************");


  circle.style.transform = rotateSum;
  rotateValue = rotateSum;
  login = false;
}

}

function pressed_log()
{
  console.log("KLIK2");
   
  if (!login){
  var zmienna = document.getElementById("circle");
  var rotateValue = circle.style.transform;
  var rotateSum = rotateValue + "rotate(180deg)";
    console.log("xddddddddddd");

  console.log(rotateValue.size);
  console.log(rotateSum.lenght);
      console.log("********************");


  circle.style.transform = rotateSum;
  rotateValue = rotateSum;
  login = true;
}

}


