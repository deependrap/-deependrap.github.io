var images = [
    "images/slider1.jpg",
    "images/slider2.jpg",
    "images/slider4.jpg"

]; 

var i =0;

function slides()
{
    document.getElementById("slideimage").src= images[i];
    if (i<(images.length-1))
        i++;
    else
        i=0;    
}

setInterval(slides, 2000)