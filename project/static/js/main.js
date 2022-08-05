//stuffs
watchTrailerPopupTrigger = document.querySelector('#trailerTriggerDiv');
trailerContainer = document.querySelector('#watchTrailerPopupContainer');
watchTrailerPopup = document.getElementById('watchTrailerPopup');

// Updating active page in navigation bar 
var currentPage = window.location.pathname;
currentPage = currentPage.slice(1, currentPage.length);
const navLink = document.querySelectorAll('nav a').
    forEach(link => {
        if (!(currentPage === "")){                         //checking url is home 
            if (link.href.includes(`${currentPage}`)) {
                link.classList.add('active')
            }
        }
        else {
            document.getElementById('homeA').classList.add('active')
        }
    })

//visiblity of dropdown content
function dropdown(dropdownBody){
    if (window.getComputedStyle(dropdownBody).display === 'none') {
        dropdownBody.style.display = "block";
    }
    else {
        dropdownBody.style.display = "none";
    }
}

function dropdownTime(){
    dropdownBody = document.querySelector('#dropDownTime');
    dropdown(dropdownBody);
}
function dropdownType() {
    dropdownBody = document.querySelector('#dropDownType');
    dropdown(dropdownBody);
}

// Trailer popup
// showing trailer popup and adding youtube id

//As we dont have simple method to pause youtube iframe.... here goes my logic....
//when user click for watch trailer setTrailer is triggered by the parameted id of the movie and it create iframe for that perticular movie then inject it in to html.... And when then click X-button it again reset  to null causing it to pause


function setTrailerId(id){
    const trailerIframe = `<iframe id="trailerYoutube" src="https://www.youtube.com/embed/${id}" title="Trailer" frameborder="0" allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen ></iframe >
<button id="crossButton" onclick="hideTrailer()">X</button>
`   
    if (id != '') { 
        watchTrailerPopup.innerHTML = trailerIframe
        trailerContainer.style.display = "flex";
        trailerContainer.style.opacity = "100%";
    }
    else{
        //function to call a notifier to show no Traier aviable
        alert("No Trailer")
    }
}

// hiding trailer on button clicked 
function hideTrailer(){
    watchTrailerPopup.innerHTML = ''
    trailerContainer.style.display = "none";
    trailerContainer.style.opacity = "0";
}