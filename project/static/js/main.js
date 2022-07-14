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