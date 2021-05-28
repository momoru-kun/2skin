<template>
  <div id="app">
    <div id="container">
      <div class="notification-wrapper" v-if="notifications.length > 0">
        <div class="notification" v-for="(item, index) in notifications" :key="index">
          <span @click="notifications.splice(index)">x</span>  {{item.text}}
        </div>
      </div>
      <div id="header">
        <div>г. Москва</div>
        <div>c 10:00 до 19:00</div>
        <div class="logo" @click="openNavBar"></div>
        <div>+7 (999) 889-89-25</div>
        <div class="links">
          <a class="icon icon--insta">
            <svg
              width="25"
              height="25"
              viewBox="0 0 25 25"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g clip-path="url(#clip0)">
                <path
                  d="M12.5042 6.08125C8.95939 6.08125 6.0896 8.95416 6.0896 12.4958C6.0896 16.0406 8.96252 18.9104 12.5042 18.9104C16.049 18.9104 18.9188 16.0375 18.9188 12.4958C18.9188 8.95104 16.0458 6.08125 12.5042 6.08125ZM12.5042 16.6594C10.2031 16.6594 8.34064 14.7958 8.34064 12.4958C8.34064 10.1958 10.2042 8.33229 12.5042 8.33229C14.8042 8.33229 16.6677 10.1958 16.6677 12.4958C16.6688 14.7958 14.8052 16.6594 12.5042 16.6594Z"
                />
                <path
                  d="M17.6542 0.0791668C15.3542 -0.028125 9.65728 -0.0229166 7.3552 0.0791668C5.33228 0.173959 3.54791 0.6625 2.10937 2.10104C-0.294799 4.50521 0.0124926 7.7448 0.0124926 12.4958C0.0124926 17.3583 -0.258341 20.5229 2.10937 22.8906C4.52291 25.3031 7.80937 24.9875 12.5042 24.9875C17.3208 24.9875 18.9833 24.9906 20.6864 24.3313C23.0021 23.4323 24.75 21.3625 24.9208 17.6448C25.0292 15.3438 25.0229 9.64792 24.9208 7.34584C24.7146 2.95729 22.3594 0.295834 17.6542 0.0791668ZM21.2948 21.3C19.7187 22.8761 17.5323 22.7354 12.474 22.7354C7.26562 22.7354 5.17708 22.8125 3.65312 21.2844C1.89791 19.5375 2.21562 16.7323 2.21562 12.4792C2.21562 6.72396 1.62499 2.57917 7.40103 2.28333C8.72812 2.23646 9.11874 2.22083 12.4594 2.22083L12.5062 2.25208C18.0573 2.25208 22.4125 1.67083 22.674 7.44584C22.7333 8.76355 22.7469 9.15938 22.7469 12.4948C22.7458 17.6427 22.8437 19.7438 21.2948 21.3Z"
                />
                <path
                  d="M19.1729 7.32709C20.0008 7.32709 20.6719 6.65598 20.6719 5.82813C20.6719 5.00027 20.0008 4.32917 19.1729 4.32917C18.3451 4.32917 17.674 5.00027 17.674 5.82813C17.674 6.65598 18.3451 7.32709 19.1729 7.32709Z"
                />
              </g>
              <defs>
                <clipPath id="clip0">
                  <rect width="25" height="25" fill="white" />
                </clipPath>
              </defs>
            </svg>
          </a>
          <a class="icon icon--vk">
            <svg
              width="31"
              height="20"
              viewBox="0 0 31 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M15.6873 19.375C20.172 19.375 18.5729 16.6275 18.919 15.8375C18.9139 15.2475 18.9087 14.68 18.9294 14.335C19.2135 14.4125 19.8839 14.7412 21.2686 16.0437C23.4063 18.1312 23.9527 19.375 25.6796 19.375H28.8584C29.8659 19.375 30.3903 18.9712 30.6525 18.6325C30.9057 18.305 31.1537 17.73 30.8825 16.835C30.1733 14.68 26.0374 10.9587 25.7804 10.5662C25.8191 10.4937 25.8811 10.3975 25.9134 10.3475H25.9108C26.7272 9.30375 29.8427 4.78625 30.3012 2.97875C30.3025 2.97625 30.3038 2.9725 30.3038 2.96875C30.5518 2.14375 30.3245 1.60875 30.0894 1.30625C29.7355 0.85375 29.1723 0.625 28.4115 0.625H25.2327C24.1684 0.625 23.3611 1.14375 22.9529 2.09C22.2696 3.77125 20.3502 7.22875 18.9113 8.4525C18.8674 6.71875 18.8971 5.395 18.9203 4.41125C18.9668 2.4925 19.1167 0.625 17.059 0.625H12.0629C10.7738 0.625 9.54025 1.9875 10.8758 3.605C12.0435 5.0225 11.2956 5.8125 11.5475 9.745C10.5658 8.72625 8.8195 5.975 7.58467 2.45875C7.2385 1.5075 6.71408 0.62625 5.23771 0.62625H2.05892C0.769833 0.62625 0 1.30625 0 2.445C0 5.0025 5.84996 19.375 15.6873 19.375ZM5.23771 2.50125C5.518 2.50125 5.54642 2.50125 5.75437 3.0725C7.01892 6.67625 9.85542 12.0087 11.9272 12.0087C13.4837 12.0087 13.4837 10.465 13.4837 9.88375L13.4824 5.25625C13.3972 3.725 12.8211 2.9625 12.4426 2.5L16.9738 2.505C16.9764 2.52625 16.948 7.62375 16.9867 8.85875C16.9867 10.6125 18.4256 11.6175 20.6718 9.4175C23.042 6.82875 24.6812 2.95875 24.747 2.80125C24.8439 2.57625 24.9279 2.5 25.2327 2.5H28.4115H28.4244C28.4231 2.50375 28.4231 2.5075 28.4218 2.51125C28.1312 3.82375 25.2624 8.00625 24.3027 9.305C24.2872 9.325 24.273 9.34625 24.2588 9.3675C23.8364 10.035 23.4928 10.7725 24.3169 11.81H24.3182C24.3931 11.8975 24.5882 12.1025 24.8723 12.3875C25.7558 13.27 28.7861 16.2875 29.0547 17.4875C28.8765 17.515 28.6828 17.495 25.6796 17.5012C25.0403 17.5012 24.5404 16.5762 22.6326 14.7137C20.9172 13.0987 19.8038 12.4387 18.7899 12.4387C16.8214 12.4387 16.9647 13.985 16.9828 15.855C16.9893 17.8825 16.9764 17.2412 16.9906 17.3687C16.8756 17.4125 16.5462 17.5 15.6873 17.5C7.49167 17.5 2.1545 4.91125 1.94912 2.505C2.02017 2.49875 2.99796 2.5025 5.23771 2.50125Z"
              />
            </svg>
          </a>
          <a class="icon icon--fb">
            <svg
              width="15"
              height="28"
              viewBox="0 0 15 28"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M0.947388 16.2598H3.88505V27.1238C3.88505 27.6068 4.27589 27.9988 4.76005 27.9988L9.43489 28C9.91905 28 10.3099 27.6068 10.3099 27.125V16.261H13.0947C13.5357 16.261 13.9079 15.932 13.9627 15.4945L14.5437 10.8278C14.6091 10.3075 14.2019 9.84433 13.6757 9.84433H10.3099C10.4417 6.96149 9.80239 6.10866 11.6772 6.10866C12.9466 5.95699 14.9486 6.59983 14.9486 5.23366V1.06049C14.9486 0.622992 14.6254 0.253159 14.1926 0.193659C13.8262 0.143492 12.3784 -7.62939e-06 10.5829 -7.62939e-06C2.40455 -7.62939e-06 4.08805 9.06733 3.88622 9.84316H0.947388C0.464388 9.84316 0.0723877 10.2352 0.0723877 10.7182V15.3848C0.0723877 15.8678 0.464388 16.2598 0.947388 16.2598ZM1.82239 11.5943H4.76005C5.24305 11.5943 5.63505 11.2023 5.63505 10.7193V7.04316C5.63505 3.67966 7.43755 1.75116 10.5817 1.75116C11.6061 1.75116 12.5487 1.80133 13.1974 1.85266V4.35983C12.7284 4.59899 8.55872 3.32849 8.55872 7.50633V10.7205C8.55872 11.2035 8.95072 11.5955 9.43372 11.5955H12.6841L12.3201 14.5122H9.43372C8.95072 14.5122 8.55872 14.9042 8.55872 15.3872V26.25H5.63622V15.386C5.63622 14.903 5.24422 14.511 4.76122 14.511H1.82239V11.5943Z"
              />
            </svg>
          </a>
        </div>
        <div
          class="menu-triangle"
          v-bind:class="{ active: nav_opened }"
          @click="openNavBar"
        ></div>
      </div>
      <ul class="navigation-bar" ref="navigation">
        <div style="float: center">
          <li class="center">
            <router-link to="/sale" v-if="$router.currentRoute.path == '/'">
              SALE
            </router-link>
            <router-link to="/" v-if="$router.currentRoute.path != '/'">
              На главную
            </router-link>
          </li>
          <li>
            <a href="/#flowers"> цветы </a>
          </li>
          <li>
            <a href="/#dots"> веснушки </a>
          </li>
          <li>
            <a href="/#words"> слова </a>
          </li>
          <li>
            <a href="/#animals"> животные </a>
          </li>
          <li>
            <a href="/#other"> другое </a>
          </li>
          <li>
            <a href="/#once"> однушки </a>
          </li>
          <li>
            <a href="/#sets"> наборы </a>
          </li>
        </div>
        <div class="right">
          <li class="search icon">
            <a>
              <svg
                width="28"
                height="28"
                viewBox="0 0 32 32"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M31.609 29.7238L22.5091 20.6239C24.2718 18.4466 25.3331 15.6799 25.3331 12.6667C25.3331 5.68272 19.6504 8.39233e-05 12.6665 8.39233e-05C5.68257 8.39233e-05 0 5.68266 0 12.6666C0 19.6505 5.68263 25.3332 12.6666 25.3332C15.6798 25.3332 18.4465 24.2719 20.6238 22.5092L29.7237 31.6091C29.9837 31.8691 30.325 31.9998 30.6664 31.9998C31.0078 31.9998 31.3491 31.8691 31.6091 31.6091C32.1304 31.0878 32.1304 30.2451 31.609 29.7238ZM12.6666 22.6665C7.15193 22.6665 2.66666 18.1812 2.66666 12.6666C2.66666 7.15196 7.15193 2.66669 12.6666 2.66669C18.1812 2.66669 22.6665 7.15196 22.6665 12.6666C22.6665 18.1812 18.1811 22.6665 12.6666 22.6665Z"
                />
              </svg>
            </a>
          </li>
          <li class="shopping-cart icon">
            <router-link to="/cart">
              <svg
                width="27"
                height="36"
                viewBox="0 0 34 42"
                stroke="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M33.4806 40.5274L30.5925 10.1977C30.5319 9.56277 30.0465 9.08065 29.4676 9.08065H24.0392V7.71582C24.0392 3.46147 20.9003 0 17.0423 0C13.1841 0 10.0452 3.46147 10.0452 7.71582V9.08065H4.61682C4.03786 9.08065 3.55254 9.56277 3.49194 10.1977L0.603797 40.5274C0.570456 40.8787 0.673956 41.2295 0.888205 41.4923C1.10274 41.7547 1.40831 41.9047 1.72867 41.9047H32.3554C32.6761 41.9047 32.9817 41.7547 33.1959 41.4923C33.4107 41.2295 33.5139 40.8787 33.4806 40.5274ZM12.3071 7.71582C12.3071 4.83685 14.4314 2.49436 17.0423 2.49436C19.653 2.49436 21.7773 4.83685 21.7773 7.71582V9.08065H12.3071V7.71582ZM2.98459 39.4103L5.63529 11.575H10.0452V14.3235C10.0452 15.0122 10.5517 15.5707 11.1762 15.5707C11.8007 15.5707 12.3071 15.0122 12.3071 14.3235V11.575H21.7773V14.3235C21.7773 15.0122 22.2837 15.5707 22.9082 15.5707C23.5327 15.5707 24.0392 15.0122 24.0392 14.3235V11.575H28.4491L31.0998 39.4103H2.98459Z"
                />
              </svg>
              <span v-if="cart_amount > 0" class="cart-counter">
                {{ cart_amount }}
              </span>
            </router-link>
          </li>
        </div>
      </ul>
      <router-view />
    </div>
    <router-link to="/cart"><div class="mobile_shopping_cart">
      <span v-if="cart_amount > 0" class="cart-counter">
        {{ cart_amount }}
      </span>
    </div>
    </router-link>
    <Footer></Footer>
  </div>
</template>

<script>
import { mapGetters } from "vuex"
import Footer from "./components/Footer";
export default {
  components: {
    Footer,
  },
  computed: mapGetters(['notifications', 'cart_amount']),
  methods: {
    checkMobile: function () {
      return this.window.width < 1000;
    },
    openNavBar: function () {
      if (this.checkMobile()) {
        let styles = window.getComputedStyle(this.$refs.navigation);
        if (styles.height === "0px") {
          this.nav_opened = true;
          this.$refs.navigation.style.height = `${this.$refs.navigation.scrollHeight}px`;
        } else {
          this.nav_opened = false;
          this.$refs.navigation.style.height = 0;
        }
      }
    },
    handleResize: function () {
      this.window.width = window.innerWidth;
      this.window.height = window.innerHeight;
    },
    checkNav: function () {
      if (!this.checkMobile()) {
        if (
          document.body.scrollTop > 80 ||
          document.documentElement.scrollTop > 80
        ) {
          document.querySelector("ul.navigation-bar").classList.add("fixed");
        } else {
          document.querySelector("ul.navigation-bar").classList.remove("fixed");
        }
      }
    },
  },
  data: () => ({
    window: {
      width: 0,
      height: 0,
    },
    nav_opened: false
  }),
  created: function () {
    window.addEventListener("resize", this.handleResize);
    window.addEventListener("scroll", this.checkNav);
    this.handleResize();
  },
  mounted: function () {
    this.$store.dispatch('init_cart')
  },
  destroyed: function () {
    window.removeEventListener("resize", this.handleResize);
  },
};
</script>


<style>
html, body {
  min-width: 100vw;
  min-height: 100vh;
  margin:0;
  scroll-behavior: smooth;
}
#app {
  width: 100%;
  font-family: Montserrat;
  font-weight: 600;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;  
  font-size: 100%;
  overflow: hidden;
}

#container {
  margin: auto;
  padding: 0 0;
  width: 1200px;
}

#header {
  display: flex;
  padding: 2rem 4rem;
  flex-wrap: nowrap;
  justify-content: space-between;
  align-items: center;
  font-size: 1.2rem;
}
#header .links .icon {
  padding: 0 4px;
  align-items: center;
  display: flex;
  align-items: center;
  justify-content: center;
  float: left;
  margin: auto 0;
  fill: #000000; 
  transition: .3s;
  width: 32px; height: 32px;
}

#header .links  .icon:hover {
  cursor: pointer;
  fill: #C67BE4; 
}
#header .menu-triangle {display: none;}
div.logo {
  background-image: url('./assets/logo.svg');
  background-size: 150px 48px;
  width: 150px;
  height: 48px;
}

.hidden {
    display: none;
}
.navigation-bar {
    position: relative;
    width: 1200px;
    min-height: 50px;
    
    padding: 0;
    margin: 0;
    
    list-style-type: none;
    border-top: solid 1px #000000;
    border-bottom: solid 1px #000000;
    
    overflow: hidden;
    font-size: 16px;
    background-color: #ffffff;
}
.navigation-bar.fixed {
    position: fixed;
    top: 0;
    z-index: 2;
    
    border-top: none;
}
.navigation-bar li {
    float: left;
}
.navigation-bar li a {
    display: block;
    padding: 16px 20px;
    text-transform: uppercase;
    transition: .3s;
    text-decoration: none;
    color: #000000;
}
.navigation-bar li.icon {
    height: 100%;
}
.navigation-bar li.icon a {
    stroke: #000000;
    padding: 0;
    height: 100%;
}
.navigation-bar li.center a{
    color:#C67BE4;
}
.navigation-bar li.center a:hover {
  color: #ffffff;
}
.navigation-bar li a:hover {
    cursor: pointer;
    background-color: #F0A2F9;
}
.navigation-bar li a:active, .navigation-bar li a.active {
  background-color: #DC9EF4;
}

.navigation-bar li.icon a:hover{
    stroke: #F0A2F9 !important;
    background-color: transparent;
}

.navigation-bar li.shopping-cart a {
    position: relative;
    padding: 5px 20px;

}
.navigation-bar li.shopping-cart a:hover {
    fill: #C67BE4;
}
.navigation-bar li.shopping-cart .cart-counter {
    font-size: 1.35rem;
    position: absolute;
    color: #C67BE4;
    width: 100%;
    height: 100%;
    top: 16px; left: 0px;
}
.navigation-bar li.search {
    padding: 9px 20px;
}
.mobile_shopping_cart {
  display: none;
  position: fixed;
  bottom: 12px;
  right: 12px;
  width: 72px;
  height: 72px;
  border-radius: 100%;
  background-image: url('./assets/cart_white.svg');
  background-position: 15px 7px;
  background-repeat: no-repeat;
  background-size: 42px 54px;
  background-color: #DC9EF4;
}
.mobile_shopping_cart:hover {
  background-color: #e5b6f7;
}
div.right {
    float: right;
}

.notification-wrapper {
  position: fixed;
  top: 56px;
  left: 16px;
  height: fit-content;
  display: flex;
  flex-direction: column;
  gap: 8px;
  z-index: 3;
}

.notification-wrapper .notification {
  background-color: #DC9EF4;
  padding: 1.75rem 3rem 1.75rem 0.5rem;
  border-radius: 2px;
  font-size: 1.25rem;
  position: relative;

  animation: slide-left .3s ease-in-out;
}

.notification-wrapper .notification span {
  position: absolute;
  top: 0; right: 8px;
  font-size: 1.5rem;
  transition: color .3s;
}

.notification-wrapper .notification span:hover {
  cursor: pointer;
  color: white
}

@keyframes slide-left {
  0% {transform: translateX(-100%);}
  100% {transform: translateX(0);}
}

@media screen and (max-width: 800px) {
  #container {
    width: 100%;
    margin: 0;
  }
  #header {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 1rem 1rem .5rem 1rem;
    align-items: center;
    justify-content: center;
  }
  #header div {
    display: none;
  }
  #header div.logo {display: block; margin: 1rem;}
  .navigation-bar {
    height: 0;
    overflow: hidden;
    transition: height .3s ease;
    min-height: 0;
    width: 100vw;
  }
  #header .menu-triangle {
    display: block;
    
    width: 0; 
    height: 0; 
    border-left: 15px solid transparent;
    border-right: 15px solid transparent;
    border-bottom: 15px solid transparent;
  
    border-top: 15px solid #000;
    margin-bottom: -15px;
    transition: 0.3s;
  }

  #header .menu-triangle.active {
    margin-bottom: 0;
    transform: rotate(-180deg);
  }
  .navigation-bar li {
    float: none !important
  }
  .navigation-bar li a {
    width: calc(100% - 40px);
  }
  .navigation-bar div.right {
    display: flex;
    width: 100%;
    flex-direction: row-reverse;
    align-items: center;
    justify-content: center;
  }
  .navigation-bar .shopping-cart {display: none;}
  .mobile_shopping_cart {display: block;}
  .mobile_shopping_cart .cart-counter {
    position: absolute;
    color: #ffffff;
    font-size: 1.75rem;
    top: 26px;
    left: 29px;
  }
}

</style>
