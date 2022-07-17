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