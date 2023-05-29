
let btn = document.getElementsByClassName('btn');
let slide = document.getElementById('slide')

btn[0].onclick = function () {
    slide.style.transform = 'translateX(38%)';
    for (let i = 0; i < 4; i++) {
        btn[i].classList.remove('btn-active');
    }
    this.classList.add('btn-active');
}

btn[1].onclick = function () {
    slide.style.transform = 'translateX(13%)';
    for (let i = 0; i < 4; i++) {
        btn[i].classList.remove('btn-active');
    }
    this.classList.add('btn-active');
}

btn[2].onclick = function () {
    slide.style.transform = 'translateX(-12%)';
    for (let i = 0; i < 4; i++) {
        btn[i].classList.remove('btn-active');
    }
    this.classList.add('btn-active');
}

btn[3].onclick = function () {
    slide.style.transform = 'translateX(-37%)';
    for (let i = 0; i < 4; i++) {
        btn[i].classList.remove('btn-active');
    }
    this.classList.add('btn-active');
}


document.querySelector('#article-01').addEventListener('click', () => {
    document.querySelector('.popup-page').classList.add('active');
    document.getElementById('popup-title').innerHTML = '斷捨離妙招';
    document.getElementById('popup-contents').innerHTML = (
        '隨著現代社會的快速發展，人們的生活方式也越來越快節奏化，擁有更多的物品和資源似乎已成為一種追求。\
        然而，隨之而來的問題也逐漸浮現，例如物品的堆積、空間的狹窄和精神上的壓力等等。\
        因此，斷捨離已成為現代人注重健康生活的一種趨勢，讓人們擁有更簡潔、輕鬆、自由的生活。<br><br>\
        \
        斷捨離的概念是在日本被提出的，它是指在生活中捨去不必要的物品和過去的情感，以達到身心靈的平衡。\
        而要實現斷捨離的目的，人們需要找到一些妙招。<br><br>\
        \
        首先，可以利用物品的分類來協助斷捨離。例如，把物品分為「必要」和「不必要」，再進一步分為「可以賣」、\
        「可以捐」和「可以丟」等等，以便快速有效地處理物品。其次，對於那些無法決定是否要保留的物品，\
        可以利用時間的概念來幫助斷捨離。例如，把物品放置在一個指定的地方，如果在一定時間內沒有使用，就可以判定為不必要的物品。<br><br>\
        \
        最後，斷捨離的過程也需要持續不斷地進行，而不是一次性完成。人們可以每天挑選一個小的範圍進行斷捨離，\
        如此一來，不但可以避免過度疲勞，也可以保持良好的生活習慣。斷捨離的妙招不僅可以幫助人們擁有更整潔、\
        輕鬆、自由的生活，也可以幫助人們提高對物品和生活的意識。讓我們珍惜身邊的物品，保持一顆平靜的心，擁有一個簡潔而美好的生活。'
    );
});

document.querySelector('#article-02').addEventListener('click', () => {
    document.querySelector('.popup-page').classList.add('active');
    document.getElementById('popup-title').innerHTML = '二手市集，新的綠色?';
    document.getElementById('popup-contents').innerHTML = (
        '在現今世界，人們對於環保問題的關注越來越高，而二手市集便是一個新的綠色選擇。\
        在傳統的消費模式中，我們習慣了使用全新的物品，並把舊物品扔掉，這不僅浪費了有限的資源，\
        也增加了垃圾的量。而二手市集可以通過購買和出售二手物品，為環境保護和可持續發展做出貢獻。<br><br>\
        \
        首先，二手市集能夠減少消費中的浪費。二手市集是資源回收的一種方式，\
        它通過重新利用和轉售已經使用過的物品，減少了對資源的需求，從而減少了浪費。\
        這也是在一些經濟發展較快的國家中，二手市集越來越受歡迎的原因之一。<br><br>\
        \
        其次，二手市集能夠減少垃圾的生成。對於那些原本被丟到垃圾箱裡的物品，如果可以被轉售或者捐贈，\
        就可以減少垃圾的生成。這也是為什麼現在越來越多的人會選擇捐贈或者出售二手物品的原因之一。<br><br>\
        \
        最後，二手市集能夠幫助人們節省開支。二手物品的價格比新物品更低，人們可以通過購買二手物品來節省開支。\
        這對於那些希望節省開支或者為慈善事業做出貢獻的人來說，是一個非常好的選擇。<br><br>\
        \
        總之，二手市集是一個非常有意義的概念，它能夠幫助我們保護環境，減少浪費，減少垃圾的生成，\
        同時還能夠幫助人們節省開支。讓我們共同支持二手市集，為我們的地球環境和可持續發展做出貢獻。'
    );
});

document.querySelector('#article-03').addEventListener('click', () => {
    document.querySelector('.popup-page').classList.add('active');
    document.getElementById('popup-title').innerHTML = '網路市集挖寶!';
    document.getElementById('popup-contents').innerHTML = (
        '網路市集是一個充滿機會的世界，有時候，你可以在那裡找到一些稀世珍寶。\
        對於那些喜愛二手物品或者收集特殊物品的人來說，網路市集挖寶可以是一種非常有趣和有益的活動。<br><br>\
        \
        首先，網路市集是一個可以找到稀世珍寶的地方。網路市集的賣家來自各行各業，\
        他們可以出售各種各樣的物品。在網路市集中，你可能會發現從古董家具到罕見玩具，\
        再到珍貴書籍等等，只要你有耐心挖掘，就有可能發現一些稀世珍寶。<br><br>\
        \
        其次，網路市集可以讓你以非常便宜的價格獲得你喜歡的物品。在網路市集中，有時候你可以發現那些售價非常便宜但品質極好的物品，\
        這可能是因為賣家並不了解物品的價值或者需要迅速出售物品。這種情況通常是你挖掘網路市集的好處所在，因為你可以以非常便宜的價格獲得你喜歡的物品。<br><br>\
        \
        最後，網路市集也可以幫助你建立一個屬於你自己的收藏品。如果你喜歡收集特殊物品，\
        網路市集可以幫助你找到那些你一直在尋找的物品，進而幫助你建立一個屬於你自己的收藏品。<br><br>\
        \
        總之，網路市集挖寶是一種非常有趣和有益的活動。通過挖掘網路市集，你可以發現稀世珍寶、獲得非常便宜的物品，\
        甚至幫助你建立一個屬於自己的收藏品。讓我們一起開始網路市集挖寶之旅吧！'
    );
});

document.querySelector('#article-04').addEventListener('click', () => {
    document.querySelector('.popup-page').classList.add('active');
    document.getElementById('popup-title').innerHTML = '二手消費文化';
    document.getElementById('popup-contents').innerHTML = (
        '二手消費文化越來越受到人們的關注和重視。這種文化不僅可以幫助人們節省金錢，\
        還可以幫助保護環境。二手市集也成為了一個經濟生態系統，促進了物品再利用和回收。<br><br>\
        \
        首先，二手消費文化可以幫助人們節省金錢。二手市集中的物品大多是已經使用過一段時間的物品，\
        因此價格通常比新品便宜很多。這對那些預算有限的人來說是非常有利的。另外，一些品牌的二手物品也可能比新品更具價值，\
        因為它們可能是限量版或者是已經停產的產品，這些物品在二手市集中通常會有更高的價值。<br><br>\
        \
        其次，二手消費文化也可以幫助保護環境。當人們購買二手物品時，他們實際上是在幫助物品再利用和回收。\
        這不僅減少了對新原材料的需求，也減少了廢棄物的產生。此外，二手市集中的物品大多是已經過去一段時間的產品，\
        而當時的生產過程可能比現在更加環保，這也有助於減少對環境的影響。<br><br>\
        \
        最後，二手市集也成為了一個經濟生態系統，促進了物品再利用和回收。二手市集中的賣家和買家之間建立了一個互動的社群，\
        人們可以分享自己的收藏和經驗，還可以透過交易建立起友誼。這個社群的發展也促進了物品再利用和回收，從而減少了浪費和對環境的影響。<br><br>\
        \
        總之，二手消費文化是一個非常有意義和有益的文化。它可以幫助人們節省金錢、保護環境，\
        還可以促進物品再利用和回收。讓我們一起加入這個文化，為環境和社會做出貢獻。'
    );
});

document.querySelector('.popup-page .close-btn').addEventListener('click', () => {
    document.querySelector('.popup-page').classList.remove('active');
});


// article image parallax test 
window.addEventListener('scroll', () => {
    const scrollPositionY = window.pageYOffset;
    const backgorund = document.querySelector('.article-background');
    backgorund.style.transform = `translateY(${scrollPositionY * 0.3 - 100}px)`
})
