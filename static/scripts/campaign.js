/**
 * This file is mainly for processing the campaign part.
 * @author: Po-Ting Ko
 * @date: 2023-05-20
 */

document.querySelector('.campaign-form-close')?.addEventListener('click', () => {
    /**
     * The function is to remove the overlay and form activate effect after 
     * close the campaign form popup pages.
     */
    document.querySelector('.campaign-form-container')?.classList.remove('form-active');
    document.querySelector('.campaign-form-overlay')?.classList.remove('overlay-active');
})

// query the campaign contents
const submit_btn = document.querySelector('.campaign-form-add');

submit_btn?.addEventListener('submit', (event) => {
    /**
     * The function that processing the query values from campaign form.
     * @param event the request event (submit) from the campagin form.
     * @returns none
     */

    const event_name = document.querySelector('#name-input').value;
    const event_date = document.querySelector('#date-input').value;
    const event_time = document.querySelector('#time-input').value;
    const event_loca = document.querySelector('#loca-input').value;
    const event_desc = document.querySelector('#desc-input').value;

    // create_campaign({
    //     'name': event_name, 'date': event_date, 'time': event_time,
    //     'loca': event_loca, 'desc': event_desc
    // });

    document.querySelector('.campaign-form-overlay').classList.remove('overlay-active');
    document.querySelector('.campaign-form-container').classList.remove('form-active');
    event.preventDefault();
});

function create_campaign(event) {
    /**
     * The function create the HTML block for campaign post
     * @param event the request event
     * @returns the HTML post div block
     */
    document.querySelector('.campaign-row').insertAdjacentHTML(
        'beforeend',
        `<div class="campaign-col">
            <div class="campaign-contents">
                <span class="campaign-date">${event.date}</span>
                <span class="campaign-name">${event.name}</span>
                <span class="campaign-people">0 人已報名</span>
                <div class="campaign-register">
                    <span>報名活動</span>
                </div>
            </div>
        </div>`
    )
}

// Handling the campaign dragger slider
const campaign_shelve = document.querySelector('.campaign-shelve');
let isDragStart = false, prePageX, preScrollLeft;

campaign_shelve?.addEventListener('mousedown', (event) => {
    /**
     * Handling `mousedown` event for the dragger.
     * @param event request event
     */
    isDragStart = true;
    prePageX = event.pageX;
    preScrollLeft = campaign_shelve.scrollLeft;
});

campaign_shelve?.addEventListener('mouseup', (event) => {
    /**
     * Handling `mouseup` event for the dragger.
     * @param event request event
     */
    isDragStart = false;
});

campaign_shelve?.addEventListener('mousemove', (event) => {
    /**
     * Handling `mousemove` event for the dragger.
     * @param event request event
     */
    if (!isDragStart) return;
    event.preventDefault();
    let positionDiff = event.pageX - prePageX;
    campaign_shelve.scrollLeft = preScrollLeft - positionDiff;
});
