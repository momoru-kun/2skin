<template>
  <div class="footer">
    <div class="footer-wrapper">
      <div><div class="logo"></div></div>
      <div>
        <div class="footer--heading upper">Каталог</div>
        <ul>
          <li>
            <a> SALE </a>
          </li>
          <li>
            <a> цветы </a>
          </li>
          <li>
            <a> веснушки </a>
          </li>
          <li>
            <a> слова </a>
          </li>
          <li>
            <a> животные </a>
          </li>
          <li>
            <a> другое </a>
          </li>
          <li>
            <a> однушки </a>
          </li>
          <li>
            <a> наборы </a>
          </li>
        </ul>
      </div>
      <div>
        <div class="footer--heading upper">о компании</div>
        <ul>
          <li>
            <a> о нас </a>
          </li>
          <li>
            <a> контакты </a>
          </li>
          <li>
            <a> доставка и оплата </a>
          </li>
          <li>
            <a> faq </a>
          </li>
          <li>
            <a> художники </a>
          </li>
        </ul>
      </div>
      <div class="contact">
        <div class="phone footer--heading">
          <img width="20px" height="20px" src="./../assets/phone.svg" style="margin-right: 10px;"/> +7 (999) 889-89-25
        </div>
        <div class="worktime">
          <div class="footer--heading"> с 10:00 до 19:00 </div>
          <div style="margin-top: 8px;"> Рабочие дни: Пн - Пт </div>
        </div>
        <div class="payment">
          <div>Мы принимаем к оплате</div>
          <div class="payment_systems">
            <img src="./../assets/master_card.png" width="50px" height="30px" />
            <img src="./../assets/visa.png" width="54px" height="16px" />
            <img src="./../assets/mir.png" width="50px" height="14px" />
          </div>
          <div class="payment_systems">
            <img src="./../assets/paypal.png" width="78px" height="19px" />
            <img src="./../assets/qiwi.png" width="78px" height="36px" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.footer {
  background-color: #c4c4c4;
  padding: 50px 0 0 0;
}
.footer-wrapper {
  margin-top: 10px;
  display: grid;
  grid-column-gap: 2rem;
  grid-template-columns: repeat(5, 1fr);
  text-align: left;
  font-size: 1rem;
  width: 1200px;
  margin: 0 auto;
}
ul {
  list-style-type: none;
  padding: 0;
  text-transform: uppercase;
  line-height: 3rem;
  font-size: 0.875rem;
}
.footer--heading {
  font-size: 1.2rem;
  line-height: 1.5rem;
}
.upper {text-transform: uppercase;}
.contact {
  grid-column-start: 4;
  grid-column-end: 6;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}
.phone {
  display: flex;
  align-items: center;
  justify-content: center;
}
.worktime {
  margin: 35px 0 0 30px;
}
.payment {
  margin: 100px 0 0 30px;  
}
.payment_systems {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-top: 10px;
}

</style>