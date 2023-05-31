// The category effect
let c_btn = document.getElementsByClassName('c-btn')

c_btn[0].onclick = function () {
  for (let i = 0; i < 5; i++) {
    c_btn[i].classList.remove('category-active');
  }
  this.classList.add('category-active');
}

c_btn[1].onclick = function () {
  for (let i = 0; i < 5; i++) {
    c_btn[i].classList.remove('category-active');
  }
  this.classList.add('category-active');
}

c_btn[2].onclick = function () {
  for (let i = 0; i < 5; i++) {
    c_btn[i].classList.remove('category-active');
  }
  this.classList.add('category-active');
}

c_btn[3].onclick = function () {
  for (let i = 0; i < 5; i++) {
    c_btn[i].classList.remove('category-active');
  }
  this.classList.add('category-active');
}

c_btn[4].onclick = function () {
  for (let i = 0; i < 5; i++) {
    c_btn[i].classList.remove('category-active');
  }
  this.classList.add('category-active');
}
