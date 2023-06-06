
// description slide
let btn = document.getElementsByClassName('preview-btn');
let slide = document.getElementById('t-item-slide')

btn[0].onclick = function () {
  slide.style.transform = 'translateX(34%)';
  for (let i = 0; i < 3; i++) {
    btn[i].classList.remove('preview-btn-active');
  }
  this.classList.add('preview-btn-active');
}

btn[1].onclick = function () {
  slide.style.transform = 'translateX(0%)';
  for (let i = 0; i < 3; i++) {
    btn[i].classList.remove('preview-btn-active');
  }
  this.classList.add('preview-btn-active');
}

btn[2].onclick = function () {
  slide.style.transform = 'translateX(-34%)';
  for (let i = 0; i < 3; i++) {
    btn[i].classList.remove('preview-btn-active');
  }
  this.classList.add('preview-btn-active');
}
