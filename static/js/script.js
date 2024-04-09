document.addEventListener('DOMContentLoaded', () => {
    const stars = document.querySelectorAll('.rating .fa-star');
    const ratingInput = document.getElementById('rating');

    stars.forEach(star => {
      star.addEventListener('mouseover', (e) => {
        const value = e.target.dataset.value;
        highlightStars(value);
      });

      star.addEventListener('mouseout', () => {
        highlightStars(ratingInput.value || 0);
      });

      star.addEventListener('click', (e) => {
        const value = e.target.dataset.value;
        ratingInput.value = value;
        highlightStars(value);
      });
    });

    function highlightStars(value) {
      stars.forEach((star, index) => {
        if (index < value) {
          star.classList.add('selected');
          star.classList.remove('fa-regular');
          star.classList.add('fa-solid');
        } else {
          star.classList.remove('selected');
          star.classList.remove('fa-solid');
          star.classList.add('fa-regular');
        }
      });
    }
  });