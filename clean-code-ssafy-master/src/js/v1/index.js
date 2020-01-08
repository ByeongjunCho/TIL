const $ = s => document.querySelector(s);

const rend = d => (
$('#loan_list').innerHTML =
d.reduce((h, l) => (`
    ${h}
    <li class="loan_item">
        <div class="name_and_organization">
            <strong>${l.name}</strong>
            <span>${l.organization}</span>
        </div>
        <br/>
        <div class="limit_and_interest">
            <div class="limit">
                한도 <span>${l.limit}</span>
            </div>
            <div class="interest">
                금리 <span>${l.interest.min} ~ ${l.interest.max}</span>
            </div>
        </div>
    </li>
`), ''));

rend(loans);

const current = {
    loans: loans,
    sort_by: 'register'
};

const compare = {
    register: (a, b) => a.id - b.id,
    interest: (a, b) => a.interest.min - b.interest.min,
    limit: (a, b) => b.limit - a.limit
};

// s는 셀렉터, en은 이벤트명, f는 리스너
const add_event_listener = (s, en, f) => 
    $(s).addEventListener(en, f);
const on_click = (s, f) => 
    add_event_listener(s, 'click', f);
const evt2 = (s, f) => add_event_listener(s, 'change', f);
// el은 엘리먼트, cn은 클래스명
const has_class = (el, cn) => el.classList.contains(cn);
const toggle_class = (el, cn) => el.classList.toggle(cn);

on_click('#is_prime', ({ currentTarget }) => (
    rend(current.loans = has_class(currentTarget, 'all') ?
        current.loans.filter(loan => loan.is_prime) :
        loans.sort(compare[current.sort_by]))
    && toggle_class(currentTarget, 'all')
));

evt2('#sort', ({ currentTarget }) => (
    rend(current.loans = current.loans.sort(
        compare[current.sort_by = currentTarget.value]))
));
