// search bar
let search_flg = false;
let search_btn = document.querySelector('.top-search');
let search_bar = document.querySelector('.show-search');
let cancel_btn = document.querySelector('.top-cancel-btn')

search_btn.onclick = function () {
    if (search_flg === false) {
        cancel_btn.classList.add('search-active');
        search_bar.classList.add('search-active');
        
        search_flg = true;
    }
    else {
        cancel_btn.classList.remove('search-active');
        search_bar.classList.remove('search-active');
        
        search_flg = false;
    }
}
