// function closeModal() {
//     document.getElementById('predictionModal').style.display = 'none'; 
//   }

function myFunction() {
document.getElementById("myDropdown").classList.toggle("show");
}

document.addEventListener('click', function (event) {
const textbox = document.getElementById('search-wrapper'); // Replace with your element's ID
const droplist = document.getElementById('myDropdown');
const classToAdd = 'show'; // Replace with the class you want to remove
if (!textbox.contains(event.target) && !droplist.contains(event.target)) {
    droplist.classList.remove(classToAdd);
    }
});

function filterFunction() {
//   var input, filter, ul, li, a, i;
input = document.getElementById("manufacturer");
filter = input.value.toUpperCase();
div = document.getElementById("myDropdown");
a = div.getElementsByTagName("div");
for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
    a[i].style.display = "";
    } else {
    a[i].style.display = "none";
    }
}
}
const dropdownItems = document.querySelectorAll('.dropdown-item');
dropdownItems.forEach(item => {
    item.addEventListener('click', function() {
        document.getElementById('manufacturer').value = this.textContent;
        myFunction(); // Call the function to close the dropdown
    });
});

// Post the form data
$(document).ready(function() {
    $('#car-info-form').submit(function(event) {
      event.preventDefault(); // Prevent default form submission
      $.ajax({
        url: '/features',
        type: 'POST',
        data: $(this).serialize(),
        dataType: 'json',
        success: function(response) {
          $('#predictionResult').text(response.price); 
          $('#pred-head').text('The model has returned this Prediction :')
        //   console.log(data)
          console.log(response.price)
        //   console.log(success)
          if (response.openModal) {
            setTimeout(function() {
              hideLoadingScreen();
              flipAndShowModal(); 
            },1000);

          } 
        }
      });
    });
  });
  function flipAndShowModal() {
    $('#form-container').removeClass('show').addClass('disappearing-form'); 
    setTimeout(function() {
      $('#form-container').removeClass('disappearing-form').addClass('hide'); // Hide after animation 
      $('#predictionModal').removeClass('hide').addClass('show'); 
    }, 435);
  }
  function flipAndHideModal() {
    $('#predictionModal').removeClass('show').addClass('disappearing-modal');
    setTimeout(function() {
      $('#predictionModal').removeClass('disappearing-modal').addClass('hide'); // Hide after animation 
      $('#form-container').removeClass('disappearing-form hide').addClass('show');
      
      $('#damageQuestion').removeClass('hide');
    }, 435);
  }






function handleDamageResponse(userHasDamage) {
  if (userHasDamage) {
    showLoadingScreen();
    setTimeout(function() {
      $('.feature-form-outer').removeClass('show-flex').addClass('hide');
      $('.image-form-outer').removeClass('hide').addClass('show-flex');
      hideLoadingScreen();
    }, 1000);
    }
  else {
    // Final predicted price remains the same
    $('#pred-head').text('The FINAL price of your car is :');
    $('#damageQuestion').addClass('hide');
  }
}




// || Scroll up the nav
let shouldScrollOnDivClick = true; 
let lastScrollPosition = 0; // Store the last recorded scroll position
let scrollTimeout = null; // Introduce a timeout variable 

function scrollDivToTop() {
  document.querySelector('.feature-form-outer').scrollIntoView({ 
    behavior: 'smooth' 
  });
  shouldScrollOnDivClick = false; // Disable automatic scrolling after a click 
}

// Attach click event listener to the div
document.querySelector('.feature-form-outer').addEventListener('click', function() {
  if (shouldScrollOnDivClick) {
    scrollDivToTop();
  }
});

// Listen for scroll events on the window
window.addEventListener('scroll', function() {
  clearTimeout(scrollTimeout);

  scrollTimeout = setTimeout(function() {
  const currentScrollPosition = window.scrollY || document.documentElement.scrollTop;
  // Check if scrolled up past a certain threshold
  if (currentScrollPosition < lastScrollPosition - 50) { // Adjust threshold as needed
    shouldScrollOnDivClick = true; // Re-enable automatic scrolling
  }
  console.log(currentScrollPosition, shouldScrollOnDivClick)
  lastScrollPosition = currentScrollPosition;
}, 500);
});


// || Loading Screen
function showLoadingScreen() {
  document.getElementById('loading-screen').style.display = 'flex';
}
function hideLoadingScreen() {
  document.getElementById('loading-screen').style.display = 'none';
}





$(document).ready(function() {
  $('#file-upload-form').submit(function(event) {
    event.preventDefault(); // Prevent default form submission
    showLoadingScreen();
    const formData = new FormData(this);
    $.ajax({
      url: '/',
      type: 'POST',
      data: formData,
      contentType: false,
      processData: false,
      success: function(response) {
        hideLoadingScreen();
        openImageModal(response.images); // Use received images
        showSlides(slideIndex);

      }
      });
  });
});

function closeImageModal() {
  $('#image-modal').removeClass('show-flex').addClass('hide'); 
}

function openImageModal(images) {
  const slideshowContainer = document.querySelector('.slideshow-container');
  // slideshowContainer.innerHTML = ''; // Clear previous content

  images.forEach((image, index) => {
    const slide = document.createElement('div');
    slide.classList.add('mySlides', 'fade');

    slide.innerHTML = `
        <div class="numbertext">${index + 1} / ${images.length}</div>
        <img src="data:image/jpeg;base64,${image}" alt="Uploaded Image" >
        <div class="text">Predicted Images</div>
    `;

    slideshowContainer.appendChild(slide);
  });

// ------------------------
  const dotsContainer = document.querySelector('.dots-container');
  images.forEach((image, index) => {
    const dot = document.createElement('span');
    // dot.classList.add('dot');

    dot.innerHTML = `
        <span class="dot" onclick="currentSlide(${index + 1})"></span> 
    `;

    dotsContainer.appendChild(dot);
  });
  $('#image-modal').removeClass('hide').addClass('show-flex'); 
}

// Carousel control ||
let slideIndex = 1;
// showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  console.log("showSlides",slideIndex);
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}


document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') { 
      closeImageModal();  
  } else if (event.code === 'ArrowLeft') {
      plusSlides(-1); // Previous image
  } else if (event.code === 'ArrowRight') {
      plusSlides(1); // Next image
  }
});


// final
function proceed() {
  fetch('/final.result')
    .then(response => response.json())
    .then(data => {
      const finalPrice = data.variable;
      // Do something with fetchedVariable
      $('#final-result').text(finalPrice)
    })
    .catch(error => console.error('Error fetching variable:', error));

  $('.final-modal').removeClass('hide');

}


function closeFinalModal() {
  $('#final-modal').addClass('hide'); 

}