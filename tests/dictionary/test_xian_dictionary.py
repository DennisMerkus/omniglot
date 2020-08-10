dictionary = """
<!DOCTYPE html>
<html lang="en">
  <head>


        <!-- Anti-flicker snippet (recommended)  -->
        <style>.async-hide { opacity: 0 !important} </style>
        <script>(function(a,s,y,n,c,h,i,d,e){s.className+=' '+y;h.start=1*new Date;
            h.end=i=function(){s.className=s.className.replace(RegExp(' ?'+y),'')};
                    (a[n]=a[n]||[]).hide=h;setTimeout(function(){i();h.end=null},c);h.timeout=c;
                    })(window,document.documentElement,'async-hide','dataLayer',1500,
                    {'GTM-KHNFZPT':true});</script>
            <meta charset="utf-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={licenseKey:"58013cabd7",applicationID:"375102748"};window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var i=n[t]={exports:{}};e[t][0].call(i.exports,function(n){var i=e[t][1][n];return r(i||n)},i,i.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var i=0;i<t.length;i++)r(t[i]);return r}({1:[function(e,n,t){function r(){}function i(e,n,t){return function(){return o(e,[u.now()].concat(f(arguments)),n?null:this,t),n?void 0:this}}var o=e("handle"),a=e(4),f=e(5),c=e("ee").get("tracer"),u=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var p=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",d=l+"ixn-";a(p,function(e,n){s[n]=i(l+n,!0,"api")}),s.addPageAction=i(l+"addPageAction",!0),s.setCurrentRouteName=i(l+"routeName",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,i="function"==typeof n;return o(d+"tracer",[u.now(),e,t],r),function(){if(c.emit((i?"":"no-")+"fn-start",[u.now(),r,i],t),i)try{return n.apply(this,arguments)}catch(e){throw c.emit("fn-err",[arguments,this,e],t),e}finally{c.emit("fn-end",[u.now()],t)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,n){m[n]=i(d+n)}),newrelic.noticeError=function(e,n){"string"==typeof e&&(e=new Error(e)),o("err",[e,u.now(),!1,n])}},{}],2:[function(e,n,t){function r(e,n){var t=e.getEntries();t.forEach(function(e){"first-paint"===e.name?c("timing",["fp",Math.floor(e.startTime)]):"first-contentful-paint"===e.name&&c("timing",["fcp",Math.floor(e.startTime)])})}function i(e,n){var t=e.getEntries();t.length>0&&c("lcp",[t[t.length-1]])}function o(e){if(e instanceof s&&!l){var n,t=Math.round(e.timeStamp);n=t>1e12?Date.now()-t:u.now()-t,l=!0,c("timing",["fi",t,{type:e.type,fid:n}])}}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var a,f,c=e("handle"),u=e("loader"),s=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){a=new PerformanceObserver(r),f=new PerformanceObserver(i);try{a.observe({entryTypes:["paint"]}),f.observe({entryTypes:["largest-contentful-paint"]})}catch(p){}}if("addEventListener"in document){var l=!1,d=["click","keydown","mousedown","pointerdown","touchstart"];d.forEach(function(e){document.addEventListener(e,o,!1)})}}},{}],3:[function(e,n,t){function r(e,n){if(!i)return!1;if(e!==i)return!1;if(!n)return!0;if(!o)return!1;for(var t=o.split("."),r=n.split("."),a=0;a<r.length;a++)if(r[a]!==t[a])return!1;return!0}var i=null,o=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var f=navigator.userAgent,c=f.match(a);c&&f.indexOf("Chrome")===-1&&f.indexOf("Chromium")===-1&&(i="Safari",o=c[1])}n.exports={agent:i,version:o,match:r}},{}],4:[function(e,n,t){function r(e,n){var t=[],r="",o=0;for(r in e)i.call(e,r)&&(t[o]=n(r,e[r]),o+=1);return t}var i=Object.prototype.hasOwnProperty;n.exports=r},{}],5:[function(e,n,t){function r(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,i=t-n||0,o=Array(i<0?0:i);++r<i;)o[r]=e[n+r];return o}n.exports=r},{}],6:[function(e,n,t){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function i(e){function n(e){return e&&e instanceof r?e:e?c(e,f,o):o()}function t(t,r,i,o){if(!l.aborted||o){e&&e(t,r,i);for(var a=n(i),f=v(t),c=f.length,u=0;u<c;u++)f[u].apply(a,r);var p=s[y[t]];return p&&p.push([b,t,r,a]),a}}function d(e,n){h[e]=v(e).concat(n)}function m(e,n){var t=h[e];if(t)for(var r=0;r<t.length;r++)t[r]===n&&t.splice(r,1)}function v(e){return h[e]||[]}function g(e){return p[e]=p[e]||i(t)}function w(e,n){u(e,function(e,t){n=n||"feature",y[t]=n,n in s||(s[n]=[])})}var h={},y={},b={on:d,addEventListener:d,removeEventListener:m,emit:t,get:g,listeners:v,context:n,buffer:w,abort:a,aborted:!1};return b}function o(){return new r}function a(){(s.api||s.feature)&&(l.aborted=!0,s=l.backlog={})}var f="nr@context",c=e("gos"),u=e(4),s={},p={},l=n.exports=i();l.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(i.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(o){}return e[n]=r,r}var i=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){i.buffer([e],r),i.emit(e,n,t)}var i=e("ee").get("handle");n.exports=r,r.ee=i},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:a(e,o,function(){return i++})}var i=1,o="nr@id",a=e("gos");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!x++){var e=E.info=NREUM.info,n=d.getElementsByTagName("script")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();u(y,function(n,t){e[n]||(e[n]=t)}),c("mark",["onload",a()+E.offset],null,"api");var t=d.createElement("script");t.src="https://"+e.agent,n.parentNode.insertBefore(t,n)}}function i(){"complete"===d.readyState&&o()}function o(){c("mark",["domContent",a()+E.offset],null,"api")}function a(){return O.exists&&performance.now?Math.round(performance.now()):(f=Math.max((new Date).getTime(),f))-E.offset}var f=(new Date).getTime(),c=e("handle"),u=e(4),s=e("ee"),p=e(3),l=window,d=l.document,m="addEventListener",v="attachEvent",g=l.XMLHttpRequest,w=g&&g.prototype;NREUM.o={ST:setTimeout,SI:l.setImmediate,CT:clearTimeout,XHR:g,REQ:l.Request,EV:l.Event,PR:l.Promise,MO:l.MutationObserver};var h=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1169.min.js"},b=g&&w&&w[m]&&!/CriOS/.test(navigator.userAgent),E=n.exports={offset:f,now:a,origin:h,features:{},xhrWrappable:b,userAgent:p};e(1),e(2),d[m]?(d[m]("DOMContentLoaded",o,!1),l[m]("load",r,!1)):(d[v]("onreadystatechange",i),l[v]("onload",r)),c("mark",["firstbyte",f],null,"api");var x=0,O=e(6)},{}],"wrap-function":[function(e,n,t){function r(e){return!(e&&e instanceof Function&&e.apply&&!e[a])}var i=e("ee"),o=e(5),a="nr@original",f=Object.prototype.hasOwnProperty,c=!1;n.exports=function(e,n){function t(e,n,t,i){function nrWrapper(){var r,a,f,c;try{a=this,r=o(arguments),f="function"==typeof t?t(r,a):t||{}}catch(u){l([u,"",[r,a,i],f])}s(n+"start",[r,a,i],f);try{return c=e.apply(a,r)}catch(p){throw s(n+"err",[r,a,p],f),p}finally{s(n+"end",[r,a,c],f)}}return r(e)?e:(n||(n=""),nrWrapper[a]=e,p(e,nrWrapper),nrWrapper)}function u(e,n,i,o){i||(i="");var a,f,c,u="-"===i.charAt(0);for(c=0;c<n.length;c++)f=n[c],a=e[f],r(a)||(e[f]=t(a,u?f+i:i,o,f))}function s(t,r,i){if(!c||n){var o=c;c=!0;try{e.emit(t,r,i,n)}catch(a){l([a,t,r,i])}c=o}}function p(e,n){if(Object.defineProperty&&Object.keys)try{var t=Object.keys(e);return t.forEach(function(t){Object.defineProperty(n,t,{get:function(){return e[t]},set:function(n){return e[t]=n,n}})}),n}catch(r){l([r])}for(var i in e)f.call(e,i)&&(n[i]=e[i]);return n}function l(n){try{e.emit("internal-error",n)}catch(t){}}return e||(e=i),t.inPlace=u,t.flag=a,t}},{}]},{},["loader"]);</script>
      <meta name="viewport" content="width=device-width">
      <meta name="description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans.">
      <meta property="og:site_name" content="
Xi'an Dictionary - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
" />
      <meta property="og:image" content="https://robertsspaceindustries.com/media/if6iwm4u5ojnqr/channel_item_full/LoreBuilderFI_Clean.jpg" />
      <meta property="og:description" content="Roberts Space Industries is the official go-to website for all news  about Star Citizen and Squadron 42. It also hosts the online store for game items and merch, as well as all the community tools used by our fans." />
      <meta property="og:type" content="website" />
      <meta property="og:url" content="https://robertsspaceindustries.com/comm-link/spectrum-dispatch/16202-Xian-Dictionary" />
      <meta property="og:locale" content="us_EN" />



            <link href="/rsi/static/css/cross-brand-less.css?v=4.2.0" media="all" rel="stylesheet">
      <link href='/rsi/static/packages/platformbar/rsi.platformbar.build.be48f.css' media="all" rel="stylesheet">
      <link href='/rsi/static/packages/enlist/rsi.enlist.build.4ef1c.css' media="all" rel="stylesheet"/>
            <script type="text/javascript" src="/cache/en/rsi-external-js.js?v=4.2.0"></script>
      <script type="text/javascript" src="/cache/en/rsi-templates-js.js?v=4.2.0"></script>

              <script id="Cookiebot" src="https://consent.cookiebot.com/uc.js" data-cbid="a687ee30-df65-45a0-9d22-90de6c1bb964" type="text/javascript"></script>


    <!-- Google Tag Manager -->
    <script data-cookieconsent="ignore">(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
          new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
        j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
        'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
      })(window,document,'script','dataLayer','GTM-KHNFZPT');</script>
    <!-- End Google Tag Manager -->


      <title>
Xi'an Dictionary - Roberts Space Industries | Follow the development of Star Citizen and Squadron 42
</title>

            <script type="text/javascript" src='/rsi/static/packages/core/rsi.core.build.d1dc3.js'></script>
      <script type="text/javascript" src='/rsi/static/packages/account/rsi.account.build.7723d.js'></script>
      <script type="text/javascript" src='/rsi/static/packages/store/rsi.store.build.86c84.js'></script>

      <script>
        $(document).ready(function() {
          window.Common = new RSI.Common({});
          window.Main = new RSI.Main({
            'is_mobile': 0,
            'probation_cookie' : '',
            'require_captcha': 0
          });
          window.Mark = new Turbulent.Mark({ 'name' : 'Rsi-XSRF', 'token' : '6JzoXg:weGGjsh2zGK5MLFEtDOCpQ', 'ttl' : 1800 });

          window.WscOverlay = new RSI.WscOverlay({});

          var destinations = [];

window.Main.destinations = destinations;
  window.PageStore = new RSI.Store({
    'store_prefix' : '/pledge',
    'bootstrapConfig': {"injection":{"attachmentClass":"RSIStoreApp","files":{"js":["bootstrap.js"],"css":["index.css"]}},"platform":{"api":"\/api"},"store":{"path":"\/pledge-store","manifest":"manifest.json"},"customizer":{"api":"\/pledge-store\/api\/customizer","ga_tracking_code":"UA-39586040-5"}}
  });



  var productsTracking = [];
  var eCommerceData = {
    'trackingAction': "",
    'currency': "",
    'trackingStep': "",
    'trackingProducts': productsTracking
  };
  window.eCommerceTracking = new RSI.Store.eCommerceTracking(
    eCommerceData
  );

        });

        $(window).load(function() {

        });

      </script>


      <script>
        window.recaptcha_is_loaded = false;
        window.on_recaptcha_load_callback = function() {
          window.recaptcha_is_loaded = true;
        };
      </script>

      <script src="https://www.google.com/recaptcha/api.js?onload=on_recaptcha_load_callback&render=explicit" async defer></script>

      <script type="text/javascript">



                                </script>



<style type="text/css">
  /* CSS from ATOM */
  table {
	display: table;
	border: 1px solid;
	border-color: white;
	border-collapse: collapse;
	padding: 11px
}

th, td {
	border: 1px solid #FFFFFF;
	vertical-align: top;
	text-align: left !important;
}

th {
	font-weight: bold;
        text-indent: 8px;
}
</style>

<script type="text/javascript">
  /* JS from ATOM */

</script>






  <style>

      background:url(/rsi/static/images/noisebg.gif) repeat center top #000b11;

  </style>

    <link href="//fonts.googleapis.com/css?family=Electrolize|Orbitron:400,500,700|Quantico|Share+Tech+Mono&display=swap" rel="stylesheet" type="text/css">

    <link href="/cache/en/rsi-css.css?v=4.2.0" media="all" rel="stylesheet">


  </head>
  <body id="" class="" >


      <div class="l-notification-bar l-notification-bar--rsi js-notification-bar" id="notification-bar-root">
  <c-notification-bar v-bind:latestagreementsslugs=[] v-bind:loggedin="0" v-bind:onhomepage="0"></c-notification-bar>
  <div class="l-notification-container l-notification-bar__boxes js-notification-bar-boxes">
    <div class="l-notification-wrapper">
              <div class="l-notification-bar__box is-hidden js-notification-bar-box js-notification-bar-box--announcement">
          <div class="c-notification c-notification--p c-notification--announcement js-bottom-notif-msg-announcement">
  <div class="c-notification__inner">

    <div class="c-notification__content">
      <div class="c-notification__title">
        Warbond Alien Week Offer - Upgrade to the Banu Defender!
      </div>
      <div class="c-notification__message">
        Take advantage of this limited-time upgrade and take on the ‘verse in a deadly extraterrestrial fighter. Add to your hangar before it vanishes on June 19 at 10am PDT!
      </div>
    </div>

    <div class="c-notification__actions">
              <div class="c-notification__wrapper-link">
                      <a href="https://robertsspaceindustries.com/pledge?openshipupgrade=1&amp;toshipid=129&amp;toskuid=13616" class="c-notification__button js-bottom-notif-link-announcement">

            <span class="c-notification__button-text">
              More info
            </span>
            <span class="c-iconed__icon c-iconed__icon--arrow"></span>
          </a>
        </div>

              <span class="c-notification__actions-label">or</span>

              <div class="c-notification__wrapper-link">
          <a class="c-notification__button js-bottom-notif-btn-announcement">

            <span class="c-notification__button-text">
              Close
            </span>

                          <span class="c-iconed__icon c-iconed__icon--close"></span>
                      </a>
        </div>
          </div>

  </div>
</div>
        </div>
          </div>
  </div>

</div>


    <div id="bodyWrapper">
      <header class='c-header-wrapper c-header-wrapper--rsi js-header-wrapper '  id='cross-brand-header'>
  <div id="platform-bar" class="c-header__platform-bar"></div>

      <div class='c-right-sidebar c-right-sidebar--signin' id="account-sidebar">
      <div class="js-toggle-account__backdrop invisible"></div>

      <a href="#" class='c-right-sidebar__back js-toggle-account'>Back
        <span></span>
        <span></span>
      </a>

      <div id="enlist-root" data-theme="rsi" data-enlisting="" data-ptu=""></div>
      <script type="text/javascript" src='/rsi/static/packages/enlist/rsi.enlist.build.4ef1c.js'></script>
    </div>

  <div class="c-header-wrapper__backdrop js-toggle-games"></div>
</header>

<div id="platform-backdrop"></div>

<script type='text/javascript'>
  RSI.Platformbar = {
    theme: "rsi",
    loggedState: "logged-out",
    tabs: [
      {
        type: 'brands',
        name: "Games",
        subItems: [
          {
            name: "sc",
            href: "/star-citizen",
            description: "Join the Universe"
          },
          {
            name: "s42",
            href: "/squadron42",
            description: "Start the adventure"
          },
          {
            name: "rsi",
            href: "/",
            description: "Follow the Development"
          }
        ]
      },
      {
        type: 'apps',
        name: "Apps",
        subItems: [
          [
            {
              name: "Spectrum",
              href: "/spectrum/community/SC",
              description: "Your communication platform"
            },
            {
              name: "Launcher",
              href: "/download",
              description: "Download Star Citizen",
                          }
          ],
          [
            {
              name: "Roadmap",
              href: "/roadmap",
              description: "Keep track of the development"
            },
            {
              name: "Telemetry",
              href: "/telemetry",
              description: "Keep track of the player’s performance"
            },
            {
              name: "Issue Council",
              href: "/community/issue-council",
              description: "Help us make the game better",
                          }
          ],
          [
            {
              name: "Starmap",
              href: "/starmap",
              description: "Your map to the universe"
            },
            {
              name: "Galactapedia",
              href: "/galactapedia",
              description: "Your guide to the universe"
            }
          ]
        ]
      },
          ],
    navigation: {
      store: {
        name: "Pledge Store",
        href: "/pledge",
        isHidden: false      },
      hub: {
        name: "Learn How to Play",
        href: "/playstarcitizen",
        show: false      },
      support: {
        name: "Support",
        href: "//support.robertsspaceindustries.com"
      },
      account: {
        name: "Account",
        href: "/account/settings",
        isHidden: false      }
    }
  };

  $(document).ready(function() {
    window.header = new RSI.Header({});
  });
</script>




<header class='c-brand-menu c-brand-menu----rsi' id='brand-menu'>
  <span class="c-brand-menu__section">

      Roberts Space Industries

  </span>
  <div class="c-brand-menu__backdrop"></div>
  <nav class="c-brand-menu__container">
    <div class="c-brand-menu__logo">
      <a href="/"><span class="h-svg h-svg__logo-rsi--fullcolor js-svg-inliner"></span> </a>
    </div>
    <div class="c-brand-menu__items-container">
      <ul class="c-brand-menu__items">
                <li class="c-brand-menu__item  ">
          <a class="c-menu-link c-menu-link----rsi c-brand-menu__link" href="/comm-link">
            <span class="c-brand-menu__item-text">Comm-Link</span>
                                  </a>
                  </li>
                <li class="c-brand-menu__item  has-submenu js-open-brand-submenu">
          <a class="c-menu-link c-menu-link----rsi c-brand-menu__link" href="/community">
            <span class="c-brand-menu__item-text">Community</span>
                                  </a>
                      <div class="c-brand-submenu">

                <a href="#" class="c-brand-submenu-back js-brand-submenu-close">
                  <span class="c-brand-submenu-back-text">Back /</span>
                  <span class="c-brand-submenu-back-section">Community</span>
                </a>
                <div class="c-brand-submenu__left"></div>
                <div class="c-brand-submenu__wrapper">
                  <ul class="c-brand-submenu__items">
                                      <li class="c-brand-submenu__item ">
                      <a href="/spectrum" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Spectrum
                      </a>
                    </li>
                                      <li class="c-brand-submenu__item ">
                      <a href="/community/orgs" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Organizations
                      </a>
                    </li>
                                      <li class="c-brand-submenu__item ">
                      <a href="/community/leaderboards/top" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Leaderboards
                      </a>
                    </li>
                                      <li class="c-brand-submenu__item ">
                      <a href="/community_events" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Event
                      </a>
                    </li>
                                      <li class="c-brand-submenu__item ">
                      <a href="/community" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Hub
                      </a>
                    </li>
                                      <li class="c-brand-submenu__item ">
                      <a href="/fankit" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Fankit
                      </a>
                    </li>
                                    </ul>
                </div>
                <div class="c-brand-submenu__right"></div>

            </div>
                  </li>
                <li class="c-brand-menu__item  has-submenu js-open-brand-submenu">
          <a class="c-menu-link c-menu-link----rsi c-brand-menu__link" href="/development">
            <span class="c-brand-menu__item-text">Development</span>
                                  </a>
                      <div class="c-brand-submenu">

                <a href="#" class="c-brand-submenu-back js-brand-submenu-close">
                  <span class="c-brand-submenu-back-text">Back /</span>
                  <span class="c-brand-submenu-back-section">Development</span>
                </a>
                <div class="c-brand-submenu__left"></div>
                <div class="c-brand-submenu__wrapper">
                  <ul class="c-brand-submenu__items">
                                      <li class="c-brand-submenu__item ">
                      <a href="/roadmap" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Roadmap
                      </a>
                    </li>
                                      <li class="c-brand-submenu__item ">
                      <a href="/community/devtracker" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Dev Tracker
                      </a>
                    </li>
                                      <li class="c-brand-submenu__item ">
                      <a href="/telemetry" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Telemetry
                      </a>
                    </li>
                                      <li class="c-brand-submenu__item ">
                      <a href="/community/issue-council" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Issue Council
                      </a>
                    </li>
                                      <li class="c-brand-submenu__item ">
                      <a href="/patch-notes" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Patch Notes
                      </a>
                    </li>
                                      <li class="c-brand-submenu__item ">
                      <a href="/ship-matrix" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Ship Matrix
                      </a>
                    </li>
                                      <li class="c-brand-submenu__item ">
                      <a href="/funding-goals" class="c-brand-submenu__link c-menu-link c-menu-link--small c-menu-link----rsi">
                        Funding
                      </a>
                    </li>
                                    </ul>
                </div>
                <div class="c-brand-submenu__right"></div>

            </div>
                  </li>
              </ul>
    </div>

    <div class="c-brand-menu__cta">

          <a href="/star-citizen/fly-now" class="c-brand-cta-btn js-google-analytics-event-tracker"
            data-event-category="FlyNow" data-event-label="navMenuClick">
            <div></div>
              <span class="c-brand-cta-btn__text">
                <strong>Fly now</strong>Alpha 3.9
              </span>
            <div></div>
          </a>

    </div>
  </nav>
</header>






  <div class="page-wrapper">

  <div id="post-background" ></div>


    <div id="contentbody" class="" style="">


<div id="post">
  <div class="title-section">

      <div class="wrapper title-bar-container">
        <div class="glow left"></div>
        <div class="title-bar">
          <div class="title with-subtitle">
            <h1>Spectrum Dispatch</h1>
            <h2>Lore</h2>
          </div>
          <div class="details">
            <div>
              <h3>ID:</h3>
              <p>16202</p>
              <div class="cboth"></div>
            </div>
            <div>
              <h3>Comments:</h3>
              <p class="comment-count">61</p>
              <div class="cboth"></div>
            </div>
            <div>
              <h3>Date:</h3>
              <p>October 27th 2017</p>
              <div class="cboth"></div>
            </div>
            <div></div>
          </div>
          <div class="cboth"></div>
        </div>
        <div class="glow right"></div>
      </div>

  <div class="title-container">
    <div class="title ">Xi'an Dictionary</div>
    <div class="subtitle">An ever-growing collection of words translated from Xi'an to UEE Standard</div>  </div>

  </div>


  <div class="lightbar toplightbar">
    <div class="lightbarlights"></div>
    <div class="footershadow"></div>
  </div>


  <div class="wrapper"><div class="hr"></div><div class="content-block4"><div class="content"><div class="top"></div><h1>Xi'an Dictionary</h1><div class="cboth"></div></div><div class="bottom"></div></div><div class="content-block2"><div class="content clearfix"><img src="/media/oh4sx3dwzk32sr/post_section_header/Ueecrest.png" /><div class="corner corner-top-left"></div><div class="corner corner-top-right"></div><div class="corner corner-bottom-left"></div><div class="corner corner-bottom-right"></div></div></div><div class="content-block1 rsi-markup">

<div  class=' segment' ><div class="content"><p><span class="initial">X</span>ē’suelen! Welcome to the Xi&#8217;an dictionary. In it, you will find a compilation Xi&#8217;an words, along with their translations. The legend at the top serves as a guide to the abbreviations for parts of speech used throughout the dictionary. This is a living document. It will change as the Xi&#8217;an and their language are developed.</p>

<p>If you&#8217;d like to participate in the development of the Xi&#8217;an language, we&#8217;d love to have your input! Please visit the Xi&#8217;an Language subgroup in Spectrum and <a href="https://robertsspaceindustries.com/spectrum/community/SC/forum/88013/thread/welcome-to-the-xi-an-language-uo-axy-an-thread" title="introduce yourself">introduce yourself</a>. You can also discuss <a href="https://robertsspaceindustries.com/spectrum/community/SC/forum/88008/thread/xi-an-dictionary" title="the development of the dictionary">the development of the dictionary</a>, <a href="https://robertsspaceindustries.com/spectrum/community/SC/forum/88013/thread/xi-an-language-discussion-1" title="discuss the language and culture">discuss the language and culture</a>, and <a href="https://robertsspaceindustries.com/spectrum/community/SC/forum/88012/thread/xi-an-language-learning-resources" title="look up useful resources">look up useful resources</a>.</p>

<p>Until next time, yanlēkol!</p></div><div class="cboth"></div></div>

<div  class=' segment' ><div class="content"><table>
<thead>
<tr>
<th colspan="2"><span class="caps">LEGEND</span> OF <span class="caps">ABBREVIATIONS</span></th>
</tr>
<tr>
<th>Abbreviation</th>
<th>Part of Speech</th>
</tr>
</thead>
<tbody>
<tr>
<td>cnj.</td>
<td>Conjunction</td>
</tr>
<tr>
<td>clq.</td>
<td>Colloquial</td>
</tr>
<tr>
<td>col.</td>
<td>Color</td>
</tr>
<tr>
<td>con.CAS</td>
<td>Conversational Phrase (Casual)</td>
</tr>
<tr>
<td>con.FOR</td>
<td>Conversational Phrase (Formal)</td>
</tr>
<tr>
<td>con.SEMFOR</td>
<td>Conversational Phrase (Semi-formal)</td>
</tr>
<tr>
<td>deix.</td>
<td>Deixis (Indicates distance from speaker or current point in time)</td>
</tr>
<tr>
<td>elm.</td>
<td>Elemental (more commonly referred to as <strong>tai</strong> when discussing Xi&rsquo;an grammar)</td>
</tr>
<tr>
<td>elm.CMP</td>
<td>Elemental Compound (typically behave like a normal <strong>tai</strong> in sentences)</td>
</tr>
<tr>
<td>elm.CMP.for</td>
<td>Formal Elemental Compound</td>
</tr>
<tr>
<td>elm.SRV</td>
<td>Elemental from the Service Dialect</td>
</tr>
<tr>
<td>idm.</td>
<td>Idiom</td>
</tr>
<tr>
<td>line</td>
<td>Xi&rsquo;an family Clan Name</td>
</tr>
<tr>
<td>n.</td>
<td>Noun</td>
</tr>
<tr>
<td>name</td>
<td>A name (Term of address for another person)</td>
</tr>
<tr>
<td>nlz.</td>
<td>Turns a <strong>tai</strong> or phrase overtly into a noun.</td>
</tr>
<tr>
<td>nlz.ClT</td>
<td>Enclitic Nominalizer (Binds to the front of <strong>tai</strong> to make them into nouns.)</td>
</tr>
<tr>
<td>num.</td>
<td>Number</td>
</tr>
<tr>
<td>pn.</td>
<td>Pronoun</td>
</tr>
<tr>
<td>PN.</td>
<td>Proper Noun (Name)</td>
</tr>
<tr>
<td>PN.feml</td>
<td>Proper Noun (Female Name)</td>
</tr>
<tr>
<td>PN.male</td>
<td>Proper Noun (Male Name)</td>
</tr>
<tr>
<td>pn.NEU</td>
<td>Neutral/Polite Pronoun (Safe for everyday use.)</td>
</tr>
<tr>
<td>pn.PEJ</td>
<td>Pejorative Pronoun (Caution. Highly insulting.)</td>
</tr>
<tr>
<td>pn.REV.for</td>
<td>Formal Reverential Pronoun (Rare in normal conversation.)</td>
</tr>
<tr>
<td>PN.role</td>
<td>Proper Noun (Occupation (Part of common Xi&rsquo;an names. Comes before the personal name.))</td>
</tr>
<tr>
<td>pn.SRV</td>
<td>Service Dialect Pronoun (Sometimes used when speaking the Proper language.)</td>
</tr>
<tr>
<td><span class="caps">POS</span></td>
<td>Part of Speech</td>
</tr>
<tr>
<td>Q</td>
<td>Question Term</td>
</tr>
<tr>
<td>Q.sffx</td>
<td>Question Term-forming Suffix</td>
</tr>
<tr>
<td>rel.</td>
<td>Relational Particle</td>
</tr>
<tr>
<td>slng.GEN</td>
<td>General Slang</td>
</tr>
<tr>
<td>slng.SRV</td>
<td>Service Dialect Slang</td>
</tr>
<tr>
<td>v.FAM</td>
<td>Familiar Verb Form (Use only with close friends or family members.)</td>
</tr>
<tr>
<td>v.IMP</td>
<td>Imperial Verb Form (Required when speaking about the Emperor or Empress)</td>
</tr>
<tr>
<td>v.LAUD</td>
<td>Laudative Verb Form (Used to praise people, things, situations, etc. Never use when referring to yourself.)</td>
</tr>
<tr>
<td>v.NEU</td>
<td>Neutral/Polite Verb Form (For everday use in public.)</td>
</tr>
<tr>
<td>v.PEJ</td>
<td>Pejorative Verb Form (Used to criticize or humiliate. (Do not use if not fluent.))</td>
</tr>
<tr>
<td>v.REV</td>
<td>Reverential Verb Form (Used to express deference or humility to listeners.)</td>
</tr>
<tr>
<td>vcp.</td>
<td>Verb Clarifying Particle (<strong>tai</strong> used to augment verb mood, aspect, etc. Immediately follows the verb.)</td>
</tr>
</tbody>
</table></div><div class="cboth"></div></div>

<div  class=' segment' ><div class="content"><table>
<tbody>
<tr>
<th colspan="3">XI&#8217;AN <span class="caps">DICTIONARY</span></th>
</tr>
<tr>
<th>Xi&#8217;an Term</th>
<th><span class="caps">POS</span></th>
<th>Translation to <span class="caps">UEE</span> Standard</th>
</tr>
<tr>
<td><strong> &ndash; (&empty; o) </strong></td>
<td>v.FAM</td>
<td>do (the <strong>o</strong> is dropped /null, missing/ in the Familiar verb paradigm)</td>
</tr>
<tr>
<td><strong> (e t.o kuai) si&rsquo;ping </strong></td>
<td>idm.</td>
<td>warmed (of food and beverages not at &#8220;room temperature&#8221; or 30 C)</td>
</tr>
<tr>
<td><strong> (e t.o kuai) tuiping </strong></td>
<td>idm.</td>
<td>cooled (of food and beverages not at &#8220;room temperature&#8221; or 30 C)</td>
</tr>
<tr>
<td><strong> .ā </strong></td>
<td>vcp.</td>
<td>(imperfective/progressive/contiuative) <strong>.āl</strong></td>
</tr>
<tr>
<td><strong> .ā </strong></td>
<td>elm.</td>
<td>continuation; (forward) movement</td>
</tr>
<tr>
<td><strong> .a&rsquo;u </strong></td>
<td>elm.</td>
<td>here/this</td>
</tr>
<tr>
<td><strong> .ā&rsquo;u </strong></td>
<td>pn.</td>
<td>this (thing)</td>
</tr>
<tr>
<td><strong> .āh&rsquo;o&rsquo;a </strong></td>
<td>con.FOR</td>
<td>Keep right (drift in a particular direction)</td>
</tr>
<tr>
<td><strong> .aiy&rsquo;a </strong></td>
<td>pn.</td>
<td>yon thing</td>
</tr>
<tr>
<td><strong> .ām </strong></td>
<td>col.</td>
<td>niveous</td>
</tr>
<tr>
<td><strong> .ān&rsquo;e&rsquo;a </strong></td>
<td>con.FOR</td>
<td>Keep left (drift in a particular direction)</td>
</tr>
<tr>
<td><strong> .ath </strong></td>
<td>elm.</td>
<td>getting along; managing; faring</td>
</tr>
<tr>
<td><strong> .ath&rsquo;a </strong></td>
<td>cnj.</td>
<td>and fittingly; and so; then (after &ldquo;if&rdquo;-clasue)</td>
</tr>
<tr>
<td><strong> .au&rsquo;o </strong></td>
<td>elm.</td>
<td>ice; snow; frozen liquid</td>
</tr>
<tr>
<td><strong> .au&rsquo;o&rsquo;longsea </strong></td>
<td>elm.CMP</td>
<td>slush; half melted ice</td>
</tr>
<tr>
<td><strong> .au&rsquo;o&rsquo;rathpunpuāng </strong></td>
<td>elm.CMP</td>
<td>heavy snow (with a great deal of accumulation)</td>
</tr>
<tr>
<td><strong> .au&rsquo;okyu </strong></td>
<td>elm.CMP</td>
<td>contrail</td>
</tr>
<tr>
<td><strong> .au&rsquo;opuāng </strong></td>
<td>elm.CMP</td>
<td>glacier; ice sheet</td>
</tr>
<tr>
<td><strong> .axy.oa? </strong></td>
<td>con.CAS</td>
<td>&Ccedil;a va? How&#8217;s it going? (cf: o .ath .u m.uexy.oa?)</td>
</tr>
<tr>
<td><strong> .ay&rsquo;ā </strong></td>
<td>elm.</td>
<td>dream; see a vision</td>
</tr>
<tr>
<td><strong> .ay&rsquo;o </strong></td>
<td>pn.</td>
<td>that (thing)</td>
</tr>
<tr>
<td><strong> .ē </strong></td>
<td>v.REV</td>
<td>eminate/reflect</td>
</tr>
<tr>
<td><strong> .e&rsquo;o </strong></td>
<td>elm.</td>
<td>there/that (near the listener)</td>
</tr>
<tr>
<td><strong> .eu&rsquo;a </strong></td>
<td>deix.</td>
<td>that distant (after an indicated noun)</td>
</tr>
<tr>
<td><strong> .ey&rsquo;o </strong></td>
<td>deix.</td>
<td>that (near you) (after an indicated noun)</td>
</tr>
<tr>
<td><strong> .i </strong></td>
<td>elm.</td>
<td>choice; selection</td>
</tr>
<tr>
<td><strong> .i&rsquo;a </strong></td>
<td>elm.</td>
<td>there/that (away from both speaker and listener)</td>
</tr>
<tr>
<td><strong> .ii </strong></td>
<td>elm.</td>
<td>multiply; duplicate; breed</td>
</tr>
<tr>
<td><strong> .ithl&rsquo;e&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>moral; ethical; &ldquo;the right choice&rdquo;</td>
</tr>
<tr>
<td><strong> .ō </strong></td>
<td>v.REV</td>
<td>do</td>
</tr>
<tr>
<td><strong> .oa&rsquo;i </strong></td>
<td>rel.</td>
<td>until</td>
</tr>
<tr>
<td><strong> .ōn </strong></td>
<td>col.</td>
<td>viridian</td>
</tr>
<tr>
<td><strong> .u&rsquo;a </strong></td>
<td>elm.</td>
<td>over there/that (remote (and out of view or reach))</td>
</tr>
<tr>
<td><strong> .u&rsquo;uth </strong></td>
<td>elm.CMP</td>
<td>also (as an adverb)</td>
</tr>
<tr>
<td><strong> .uai </strong></td>
<td>elm.</td>
<td>go</td>
</tr>
<tr>
<td><strong> .uaih&rsquo;o&rsquo;a </strong></td>
<td>con.FOR</td>
<td>Go right (follow the arrow, etc.)</td>
</tr>
<tr>
<td><strong> .uaik&rsquo;ongsam </strong></td>
<td>elm.CMP</td>
<td>hike (for recreation); stroll; wander (on foot)</td>
</tr>
<tr>
<td><strong> .uain&rsquo;e&rsquo;a </strong></td>
<td>con.FOR</td>
<td>Go left (follow the arrow, etc.)</td>
</tr>
<tr>
<td><strong> .um&rsquo;a </strong></td>
<td>elm.</td>
<td>wet; moist; damp</td>
</tr>
<tr>
<td><strong> .un&rsquo;ii&rsquo;kuam </strong></td>
<td>elm.CMP</td>
<td>orchard</td>
</tr>
<tr>
<td><strong> .un&rsquo;ii&rsquo;sauo </strong></td>
<td>elm.CMP</td>
<td>grove (of trees)</td>
</tr>
<tr>
<td><strong> .unt&rsquo;ang&rsquo;puāng </strong></td>
<td>elm.CMP</td>
<td>mountain range</td>
</tr>
<tr>
<td><strong> .Uy&rsquo;ii </strong></td>
<td>PN.feml</td>
<td>Uy&iacute;&iacute;</td>
</tr>
<tr>
<td><strong> (h)ai </strong></td>
<td>pn.SRV</td>
<td>you</td>
</tr>
<tr>
<td><strong> (V.) sā tao&rsquo;ra </strong></td>
<td>idm.</td>
<td>&ldquo;perhaps one day ____&rdquo;</td>
</tr>
<tr>
<td><strong> a </strong></td>
<td>elm.</td>
<td>object; tangible thing</td>
</tr>
<tr>
<td><strong> a. </strong></td>
<td>nlz.CLTC</td>
<td>(concrete/tangible thing; object)</td>
</tr>
<tr>
<td><strong> a.thl&rsquo;ē&rsquo;kol </strong></td>
<td>con.FOR</td>
<td>&ldquo;Goodbye; Farewell&rdquo;</td>
</tr>
<tr>
<td><strong> a&rsquo;k.ēt&rsquo;aongchui </strong></td>
<td>elm.CMP</td>
<td>drainage ditch</td>
</tr>
<tr>
<td><strong> a&rsquo;k.ii </strong></td>
<td>elm.</td>
<td>aunt (mother&rsquo;s or grandmother&rsquo;s younger sister when elder)</td>
</tr>
<tr>
<td><strong> a&rsquo;ki </strong></td>
<td>elm.</td>
<td>aunt (mother&rsquo;s or grandmother&rsquo;s younger sister)</td>
</tr>
<tr>
<td><strong> a&rsquo;o.u&rsquo;a </strong></td>
<td>pn.</td>
<td>that thing beyond</td>
</tr>
<tr>
<td><strong> a&rsquo;ran </strong></td>
<td>elm.</td>
<td>tenacious; stubborn; relentless</td>
</tr>
<tr>
<td><strong> a&rsquo;rath(xyikyu) </strong></td>
<td>elm.CMP</td>
<td>precipitation</td>
</tr>
<tr>
<td><strong> a&rsquo;t.oy&rsquo;onai </strong></td>
<td>elm.CMP</td>
<td>Countermeasure</td>
</tr>
<tr>
<td><strong> a&rsquo;xy.oa </strong></td>
<td>Q.</td>
<td>what (concrete) thing?</td>
</tr>
<tr>
<td><strong> a&rsquo;yanrath </strong></td>
<td>elm.CMP</td>
<td>stairs/step/staircase</td>
</tr>
<tr>
<td><strong> a&rdquo; </strong></td>
<td>elm.</td>
<td>fit; fit into</td>
</tr>
<tr>
<td><strong> aho&#8217;a </strong></td>
<td>noun</td>
<td>right side (in physical terms)</td>
</tr>
<tr>
<td><strong> ahual </strong></td>
<td>elm.CMP</td>
<td>anything (any physical thing)</td>
</tr>
<tr>
<td><strong> ahyan </strong></td>
<td>elm.CMP</td>
<td>everything (of physical things)</td>
</tr>
<tr>
<td><strong> Āi </strong></td>
<td>PN.feml</td>
<td>Aai</td>
</tr>
<tr>
<td><strong> aith </strong></td>
<td>elm.</td>
<td>health; good health; healthy</td>
</tr>
<tr>
<td><strong> aklu </strong></td>
<td>noun</td>
<td>back side (in physical terms)</td>
</tr>
<tr>
<td><strong> al </strong></td>
<td>rel.</td>
<td>out; outside</td>
</tr>
<tr>
<td><strong> al </strong></td>
<td>elm.</td>
<td>outgoing; external; projecting externally; depart; exit; export</td>
</tr>
<tr>
<td><strong> āl </strong></td>
<td>elm.</td>
<td>sub conscious meditation; fugue meditation; reverie</td>
</tr>
<tr>
<td><strong> aloa </strong></td>
<td>elm.CMP</td>
<td>meal (also <strong>atenloa</strong> in more formal contexts)</td>
</tr>
<tr>
<td><strong> alue </strong></td>
<td>elm.CMP</td>
<td>bridge, connector (for crossing or gaining access to another location); connector, adaptor (for different cabling systems, etc.)</td>
</tr>
<tr>
<td><strong> aluekeng </strong></td>
<td>elm.CMP</td>
<td>isthmus; land bridge</td>
</tr>
<tr>
<td><strong> aluenoklo </strong></td>
<td>elm.CMP</td>
<td>foot bridge (not set up for traffic by vehicles)</td>
</tr>
<tr>
<td><strong> alueseth </strong></td>
<td>elm.CMP</td>
<td>bridge (for walking across); tressel (for a train, etc.)</td>
</tr>
<tr>
<td><strong> āluo&#8217;a </strong></td>
<td>elm.CMP</td>
<td>Xi&#8217;an &#8220;opera,&#8221; a type of song or vocal performance in which the singer skillfully adjusts their own metabolism to create the illusion of time manipulation</td>
</tr>
<tr>
<td><strong> alye&rsquo;lye </strong></td>
<td>elm.CMP</td>
<td>arrow; spear</td>
</tr>
<tr>
<td><strong> ān </strong></td>
<td>pn.SRV</td>
<td>we (exclusive)</td>
</tr>
<tr>
<td><strong> an&rdquo; </strong></td>
<td>vcp.</td>
<td> conditonal <strong>an&rsquo;lai</strong> (often followed by <strong>.ath&rsquo;a</strong>)</td>
</tr>
<tr>
<td><strong> an&rdquo; </strong></td>
<td>elm.</td>
<td>inevitability</td>
</tr>
<tr>
<td><strong> ane&#8217;a </strong></td>
<td>noun</td>
<td>left side (in physical terms)</td>
</tr>
<tr>
<td><strong> ang </strong></td>
<td>nlz.</td>
<td>(noun phrase clause head)</td>
</tr>
<tr>
<td><strong> a•o </strong></td>
<td>elm.</td>
<td>company; corporation; corporate; business entity</td>
</tr>
<tr>
<td><strong> a•oō&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>umbrella corporation; &ldquo;Aggregate&rdquo;</td>
</tr>
<tr>
<td><strong> ari&rsquo;akyu&rsquo;ā </strong></td>
<td>elm.CMP</td>
<td>windward side</td>
</tr>
<tr>
<td><strong> aryā&rsquo;s.us&rsquo;an </strong></td>
<td>elm.CMP</td>
<td>Signature (of a ship, etc.)</td>
</tr>
<tr>
<td><strong> aryā&rsquo;su </strong></td>
<td>elm.CMP</td>
<td>flavor or smell (of food, etc.); trace (of something no longer present)</td>
</tr>
<tr>
<td><strong> asang </strong></td>
<td>noun</td>
<td>front side (in physical terms)</td>
</tr>
<tr>
<td><strong> ataie&rsquo;nu; ataye&rsquo;nu; taye&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>Sub-Component</td>
</tr>
<tr>
<td><strong> ateyā </strong></td>
<td>elm.CMP</td>
<td>the thing preferred; the preference; what &lsquo;I&rsquo; want.</td>
</tr>
<tr>
<td><strong> athlalsēngnya; sēngnya </strong></td>
<td>elm.CMP</td>
<td>Personal Armor</td>
</tr>
<tr>
<td><strong> auingtyikyu; tyikyu </strong></td>
<td>elm.CMP</td>
<td>Airlock</td>
</tr>
<tr>
<td><strong> ch.iing </strong></td>
<td>elm.</td>
<td>salt</td>
</tr>
<tr>
<td><strong> ch.ūl </strong></td>
<td>elm.</td>
<td>dry crisp; crispy like a leaf (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> athlalsēngsan; sēngsan </strong></td>
<td>elm.CMP</td>
<td>Ship Armor</td>
</tr>
<tr>
<td><strong> cha </strong></td>
<td>v.FAM</td>
<td>cause/produce/effect</td>
</tr>
<tr>
<td><strong> chā&rsquo;e </strong></td>
<td>elm.</td>
<td>eye; vision; look at; regard; spy</td>
</tr>
<tr>
<td><strong> chai </strong></td>
<td>elm.</td>
<td>technology; </td>
</tr>
<tr>
<td><strong> chai </strong></td>
<td>elm.</td>
<td>informatics; technology; engineering; hyper-complex tool</td>
</tr>
<tr>
<td><strong> chai.t&rsquo;ao&#8217;ru </strong></td>
<td>elm.CMP</td>
<td>grav-lev technology</td>
</tr>
<tr>
<td><strong> chai&rsquo;t.os&rsquo;ēng </strong></td>
<td>elm.CMP</td>
<td>Shield Generator</td>
</tr>
<tr>
<td><strong> chailaXa </strong></td>
<td>elm.CMP</td>
<td>Jump Drive</td>
</tr>
<tr>
<td><strong> chaileth&rsquo;uiiyōn </strong></td>
<td>elm.CMP</td>
<td>Quantum Drive</td>
</tr>
<tr>
<td><strong> chainunya </strong></td>
<td>elm.CMP</td>
<td>robot; (speficially an android)</td>
</tr>
<tr>
<td><strong> chao </strong></td>
<td>elm.</td>
<td>organization (for societal good)</td>
</tr>
<tr>
<td><strong> che&rsquo;a </strong></td>
<td>num.</td>
<td>million 1,000,000</td>
</tr>
<tr>
<td><strong> che&rsquo;aile&rsquo;a </strong></td>
<td>num.</td>
<td>6,000,000</td>
</tr>
<tr>
<td><strong> che&rsquo;aile&rsquo;a u le&rsquo;a </strong></td>
<td>num.</td>
<td>6,000,006</td>
</tr>
<tr>
<td><strong> che&rsquo;ny.ax&rsquo;ē </strong></td>
<td>elm.CMP</td>
<td>society; societal (<strong>chen nya xē&rdquo;</strong>)</td>
</tr>
<tr>
<td><strong> chen </strong></td>
<td>elm.</td>
<td>life and its associated experiences; live (one&rsquo;s life)</td>
</tr>
<tr>
<td><strong> chi </strong></td>
<td>vcp.</td>
<td>(temporal inflective) <strong>chil</strong></td>
</tr>
<tr>
<td><strong> chi </strong></td>
<td>elm.</td>
<td>now (in juxtaposition to the immediate past)</td>
</tr>
<tr>
<td><strong> chi&rsquo;a </strong></td>
<td>v.LAUD</td>
<td>equate</td>
</tr>
<tr>
<td><strong> chi&rsquo;li </strong></td>
<td>n.</td>
<td>peppers (specifically capiscum and similar noted for their spicy seeds)</td>
</tr>
<tr>
<td><strong> chi&rsquo;li.m&rsquo;a&rsquo;kr.ōng </strong></td>
<td>elm.CMP</td>
<td>&#8220;demon&#8221; pepper &#8211; a hybrid of the notorious Terran ghost jolokia intensified 7-fold by Xi&rsquo;an herbo-cuisinologists.</td>
</tr>
<tr>
<td><strong> chi&rsquo;sa </strong></td>
<td>elm.</td>
<td>facet; aspect; attribute</td>
</tr>
<tr>
<td><strong> Chii </strong></td>
<td>line</td>
<td>Chii</td>
</tr>
<tr>
<td><strong> chii&rsquo;hua </strong></td>
<td>elm.</td>
<td>zesty; spicy; burning (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> chii&rsquo;konglo </strong></td>
<td>elm.CMP</td>
<td>crawling insect; centipede, etc.</td>
</tr>
<tr>
<td><strong> chii&rsquo;ngeasui </strong></td>
<td>elm.CMP</td>
<td>pickled larvae (pickled dish prepared from larve of chiinu&#8217;a that have eaten their fill of decaying meat)</td>
</tr>
<tr>
<td><strong> chii&rsquo;syu </strong></td>
<td>elm.CMP</td>
<td>flying insect</td>
</tr>
<tr>
<td><strong> chii&rdquo; </strong></td>
<td>elm.</td>
<td>bug; insectoid</td>
</tr>
<tr>
<td><strong> chiin </strong></td>
<td>elm.</td>
<td>round; circular; oval</td>
</tr>
<tr>
<td><strong> chiing.ch&rsquo;i </strong></td>
<td>elm.</td>
<td>salty; saliva-inducing (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> chiinu&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>corpse bug (bug that produces very fat larvae that eats decaying meat)</td>
</tr>
<tr>
<td><strong> chik&rsquo;chak </strong></td>
<td>elm.</td>
<td>wet crisp; crispy like a pickle (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> ching </strong></td>
<td>elm.</td>
<td>true; truth</td>
</tr>
<tr>
<td><strong> chith </strong></td>
<td>elm.</td>
<td>fungus, mushroom; toadstool</td>
</tr>
<tr>
<td><strong> chithpun </strong></td>
<td>elm.CMP</td>
<td>yeast</td>
</tr>
<tr>
<td><strong> chō&rsquo;a </strong></td>
<td>elm.</td>
<td>thanks; appreciation; gratitude</td>
</tr>
<tr>
<td><strong> cho&rsquo;ro </strong></td>
<td>slng.GEN</td>
<td>we inclusive (dual (pejorative)) slang (I + you)</td>
</tr>
<tr>
<td><strong> chong </strong></td>
<td>pn.PEJ</td>
<td>I (note: only in specific cases)</td>
</tr>
<tr>
<td><strong> chu&rsquo;a </strong></td>
<td>v.FAM</td>
<td>be of a class</td>
</tr>
<tr>
<td><strong> chu&rsquo;ro </strong></td>
<td>slng.GEN</td>
<td>we inclusive (plural (pejorative)) slang (we (exclu.) + you)</td>
</tr>
<tr>
<td><strong> chuai </strong></td>
<td>elm.</td>
<td>rock; stone</td>
</tr>
<tr>
<td><strong> chuai&rsquo;l.ongx&rsquo;ā&rsquo;ye </strong></td>
<td>elm.CMP</td>
<td>lava rock (cooled and solid)</td>
</tr>
<tr>
<td><strong> chuai&rsquo;rathyeng </strong></td>
<td>elm.CMP</td>
<td>meteor; shooting star</td>
</tr>
<tr>
<td><strong> chuaihyao </strong></td>
<td>elm.CMP</td>
<td>asteroid</td>
</tr>
<tr>
<td><strong> chuaixyihyao </strong></td>
<td>elm.CMP</td>
<td>meteorite</td>
</tr>
<tr>
<td><strong> chuaiyeng </strong></td>
<td>elm.CMP</td>
<td>lava; magma (while still hot)</td>
</tr>
<tr>
<td><strong> chuao </strong></td>
<td>elm.</td>
<td>give (sense of &ldquo;a gift&rdquo;; something beneficial; donattion; grant)</td>
</tr>
<tr>
<td><strong> chue </strong></td>
<td>pn.PEJ</td>
<td>we (note: only in specific cases)</td>
</tr>
<tr>
<td><strong> chui </strong></td>
<td>elm.</td>
<td>water; liquid</td>
</tr>
<tr>
<td><strong> chui.y&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>blood; plasma (of fauna)</td>
</tr>
<tr>
<td><strong> chui.y&rsquo;o&#8217;sui </strong></td>
<td>elm.CMP</td>
<td>&#8220;shrub sanglant&rdquo; a.k.a. &ldquo;sour blood&rdquo; (vinegar mixed with fermented blood; used as an apertif and palate cleanser)</td>
</tr>
<tr>
<td><strong> chui&rsquo;.ā&rsquo;e&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>stream; creek; brook (tributary in the context of a major river)</td>
</tr>
<tr>
<td><strong> chui&rsquo;.ā&rsquo;e&rsquo;nulath </strong></td>
<td>elm.CMP</td>
<td>gully; gulch; arroyo</td>
</tr>
<tr>
<td><strong> chui&rsquo;.ā&rsquo;ō&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>river (major (cf: Colorado/Mississippi))</td>
</tr>
<tr>
<td><strong> chui&rsquo;.uait&rsquo;yon </strong></td>
<td>elm.CMP</td>
<td>tide</td>
</tr>
<tr>
<td><strong> chui&rsquo;ā </strong></td>
<td>elm.CMP</td>
<td>flowing water (generic term for river)</td>
</tr>
<tr>
<td><strong> chui&rsquo;ār.ath </strong></td>
<td>elm.CMP</td>
<td>waterfall</td>
</tr>
<tr>
<td><strong> chui&rsquo;ās.oa </strong></td>
<td>elm.CMP</td>
<td>current</td>
</tr>
<tr>
<td><strong> chui&rsquo;r.ath&rsquo;e&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>drizzle; light rain</td>
</tr>
<tr>
<td><strong> chui&rsquo;r.athh&rsquo;ā&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>flood (caused by weather)</td>
</tr>
<tr>
<td><strong> chui&rsquo;r.athh&rsquo;ā&rsquo;aleth </strong></td>
<td>elm.CMP</td>
<td>flash flood</td>
</tr>
<tr>
<td><strong> chui&rsquo;rath.au&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>freezing rain</td>
</tr>
<tr>
<td><strong> chuihā&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>flood (not caused naturally (as in &ldquo;flood the chamber&rdquo; intentionally))</td>
</tr>
<tr>
<td><strong> chuihai&rsquo;pe </strong></td>
<td>elm.CMP</td>
<td>&#8220;tea&#8221; as a beverage (made from hai&rsquo;pe needles)</td>
</tr>
<tr>
<td><strong> chuikyu&rsquo;ām </strong></td>
<td>elm.CMP</td>
<td>condensation; water vapor; dew</td>
</tr>
<tr>
<td><strong> chuipuāng </strong></td>
<td>elm.CMP</td>
<td>ocean; sea</td>
</tr>
<tr>
<td><strong> chuipuinuam </strong></td>
<td>elm.CMP</td>
<td>groundwater</td>
</tr>
<tr>
<td><strong> chuipuong </strong></td>
<td>elm.CMP</td>
<td>saliva</td>
</tr>
<tr>
<td><strong> chuiso&rsquo;i.r&rsquo;o&rsquo;ang </strong></td>
<td>elm.CMP</td>
<td>soy sauce (literally: &#8220;red-brown soy liquid&#8221;) as it was originally named by the Xi&rsquo;an when borrored. The more epicurian crowd calls it xyo&rsquo;yu.</td>
</tr>
<tr>
<td><strong> chuitung </strong></td>
<td>elm.CMP</td>
<td>drinking water (enhanced with minerals and microorganisms for health and flavor)</td>
</tr>
<tr>
<td><strong> chuiyo.y&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>clean; potable; purified; sterilized water (literally: &ldquo;dead water&rdquo; or &ldquo;water lacking life&rdquo;)</td>
</tr>
<tr>
<td><strong> chuo </strong></td>
<td>elm.</td>
<td>status; conditon</td>
</tr>
<tr>
<td><strong> chuokyukeng </strong></td>
<td>elm.CMP</td>
<td>climate</td>
</tr>
<tr>
<td><strong> chy.a </strong></td>
<td>elm.</td>
<td>change, modify, manipulate, alter</td>
</tr>
<tr>
<td><strong> chy.ak&rsquo;a&rsquo;xyo </strong></td>
<td>elm.CMP</td>
<td>migration; (also &lsquo;move away&rsquo; (of people))</td>
</tr>
<tr>
<td><strong> chy.at&rsquo;eth </strong></td>
<td>elm.CMP</td>
<td>terraforming (o chy.at&rsquo;eth = to terraform)</td>
</tr>
<tr>
<td><strong> Chy.ōn.uā </strong></td>
<td>name</td>
<td>step-mother (mother&#8217;s spouse who does not parent you directly)</td>
</tr>
<tr>
<td><strong> Chy.ōny.ū </strong></td>
<td>name</td>
<td>step-father (mother&#8217;s spouse who does not parent you directly)</td>
</tr>
<tr>
<td><strong> Chya&rsquo;na </strong></td>
<td>name</td>
<td>&ldquo;Mommy&rdquo; (pre-Service)</td>
</tr>
<tr>
<td><strong> chye&rsquo;o </strong></td>
<td>elm.</td>
<td>large city; metropolis</td>
</tr>
<tr>
<td><strong> chye&rsquo;ol&rsquo;e </strong></td>
<td>elm.CMP</td>
<td>main city; primary city of importance for a region</td>
</tr>
<tr>
<td><strong> chye&rsquo;ol&rsquo;etao&rdquo; </strong></td>
<td>elm.CMP</td>
<td>Capital City; seat of government</td>
</tr>
<tr>
<td><strong> chyi </strong></td>
<td>elm.</td>
<td>&ldquo;parent&rdquo; (member of a mother&rsquo;s <strong>pyā&rsquo;hai</strong>); nurture</td>
</tr>
<tr>
<td><strong> Chyi&rsquo;n.ā </strong></td>
<td>name</td>
<td>&ldquo;Mom&rdquo; (post-Service)</td>
</tr>
<tr>
<td><strong> Chyi&rsquo;y.ū </strong></td>
<td>name</td>
<td>&ldquo;Dad&rdquo; (post-Service)</td>
</tr>
<tr>
<td><strong> Chyu&rsquo;i </strong></td>
<td>name</td>
<td>&ldquo;Daddy&rdquo; (pre-Service)</td>
</tr>
<tr>
<td><strong> e </strong></td>
<td>v.NEU</td>
<td>eminate/reflect</td>
</tr>
<tr>
<td><strong> e </strong></td>
<td>v.FAM</td>
<td>eminate/reflect</td>
</tr>
<tr>
<td><strong> e </strong></td>
<td>rel.</td>
<td>of</td>
</tr>
<tr>
<td><strong> e (e&rsquo;.ā) yo&rdquo; </strong></td>
<td>idm.</td>
<td>stay alive; survive; live (especially of the elderly)</td>
</tr>
<tr>
<td><strong> e huang (yo X)/(ang X) </strong></td>
<td>idm.</td>
<td>important that</td>
</tr>
<tr>
<td><strong> e lathkyu </strong></td>
<td>idm.</td>
<td>cured; air cured</td>
</tr>
<tr>
<td><strong> e ngiing (yo X)/(ang X) </strong></td>
<td>idm.</td>
<td>doubtful that</td>
</tr>
<tr>
<td><strong> e ngimyā (yo X)/(ang X) </strong></td>
<td>idm.</td>
<td>imperative that/a must that</td>
</tr>
<tr>
<td><strong> e ngisū (yo X)/(ang X) </strong></td>
<td>idm.</td>
<td>certain that</td>
</tr>
<tr>
<td><strong> e ngisya (yo X)/(ang X) </strong></td>
<td>idm.</td>
<td>necessary that</td>
</tr>
<tr>
<td><strong> e ngumthle&rsquo;a </strong></td>
<td>idm.</td>
<td>well-colonized (positive attribute of food that has been aged or fermented especially well)</td>
</tr>
<tr>
<td><strong> e ngye&rsquo;a (yo X)/(ang X) </strong></td>
<td>idm.</td>
<td>likely that</td>
</tr>
<tr>
<td><strong> e nya&rsquo;to </strong></td>
<td>idm.</td>
<td>&#8220;artificial&#8221;; Xy&rsquo;an-made; not a pure product of nature</td>
</tr>
<tr>
<td><strong> e pyan .u po _____ </strong></td>
<td>idm.</td>
<td>intuit that X; sense that X</td>
</tr>
<tr>
<td><strong> e syengum </strong></td>
<td>idm.</td>
<td>ripe</td>
</tr>
<tr>
<td><strong> e ta&rsquo;kya </strong></td>
<td>idm.</td>
<td>be drunk; be high; be wasted</td>
</tr>
<tr>
<td><strong> e thle&rsquo;a </strong></td>
<td>idm.</td>
<td>be proper; be correct;</td>
</tr>
<tr>
<td><strong> e ya&rsquo;ue (yo X)/(ang X) </strong></td>
<td>idm.</td>
<td>possible that</td>
</tr>
<tr>
<td><strong> e yal </strong></td>
<td>idm.</td>
<td>be conscious; have consciousness</td>
</tr>
<tr>
<td><strong> e yo hyē </strong></td>
<td>idm.</td>
<td>be simple</td>
</tr>
<tr>
<td><strong> e yo to&#8217;ath </strong></td>
<td>idm.</td>
<td>lack a talent for X</td>
</tr>
<tr>
<td><strong> e yo tūn </strong></td>
<td>idm.</td>
<td>simpleminded; be dumb</td>
</tr>
<tr>
<td><strong> e yo yal </strong></td>
<td>idm.</td>
<td>lack consciousness</td>
</tr>
<tr>
<td><strong> e yongum </strong></td>
<td>idm.</td>
<td>unripe</td>
</tr>
<tr>
<td><strong> e.ny&rsquo;ii </strong></td>
<td>elm.</td>
<td>biological sibling (younger)</td>
</tr>
<tr>
<td><strong> e&rsquo;a </strong></td>
<td>vcp.</td>
<td>(predictable (&ldquo;likely&rdquo;)) <strong>e&rsquo;al</strong></td>
</tr>
<tr>
<td><strong> e&rsquo;a </strong></td>
<td>elm.</td>
<td>likely; predictable but not assured</td>
</tr>
<tr>
<td><strong> e&rsquo;e (pred.) .u _____ (subj.) </strong></td>
<td>idm.</td>
<td>resemblance; X resembles Y in Z</td>
</tr>
<tr>
<td><strong> E&rsquo;n.ā </strong></td>
<td>name</td>
<td>Little Sis (endearment term from older sibling to younger sister as an adult)</td>
</tr>
<tr>
<td><strong> E&rsquo;na </strong></td>
<td>name</td>
<td>Lil&rsquo; Sis (enderment term from older sister or brother to younger sister)</td>
</tr>
<tr>
<td><strong> e&rsquo;nu </strong></td>
<td>elm.</td>
<td>minor; lesser; smaller; enclosed; inferior; encompassed</td>
</tr>
<tr>
<td><strong> ē&rsquo;pua(s) </strong></td>
<td>n.</td>
<td>cheese (borrowed from the French &laquo;&Eacute;poisses&raquo;, but in Xi&rsquo;an refers to all varieties of what Humans call &ldquo;cheese&rdquo;)</td>
</tr>
<tr>
<td><strong> e&rsquo;so </strong></td>
<td>col.</td>
<td>transparent; clear</td>
</tr>
<tr>
<td><strong> E&rsquo;ui </strong></td>
<td>name</td>
<td>Lil&rsquo; Bro (endearent term from older sister or brother to younger brother)</td>
</tr>
<tr>
<td><strong> e&rsquo;xyoa? </strong></td>
<td>con.CAS</td>
<td>&ldquo;How are you? (feeling)&rdquo;</td>
</tr>
<tr>
<td><strong> E&rsquo;y.ū </strong></td>
<td>name</td>
<td>Little Brother (endearment term from older sibling to youger brother as an adult)</td>
</tr>
<tr>
<td><strong> en </strong></td>
<td>elm.</td>
<td><strong>pyā&rsquo;hai</strong> sibling (younger)</td>
</tr>
<tr>
<td><strong> gu </strong></td>
<td>pn.SRV</td>
<td>It (inanimate)</td>
</tr>
<tr>
<td><strong> gun </strong></td>
<td>pn.SRV</td>
<td>they (inanimate)</td>
</tr>
<tr>
<td><strong> h.ān </strong></td>
<td>elm.</td>
<td>internal turmoil; being conflicted</td>
</tr>
<tr>
<td><strong> h.eng </strong></td>
<td>elm.</td>
<td>broken; break; flaw; inconsistency</td>
</tr>
<tr>
<td><strong> h.ey&rsquo;an </strong></td>
<td>elm.</td>
<td>patience; waiting patiently</td>
</tr>
<tr>
<td><strong> h.in&rsquo;e </strong></td>
<td>elm.</td>
<td>circumference; measurement around a sphere or circle</td>
</tr>
<tr>
<td><strong> h.in&rsquo;eō&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>equator</td>
</tr>
<tr>
<td><strong> h.o&rsquo;a </strong></td>
<td>elm.</td>
<td>sound</td>
</tr>
<tr>
<td><strong> h.oa </strong></td>
<td>elm.</td>
<td>variation, irregularity, exception, unusual</td>
</tr>
<tr>
<td><strong> h.uet&rsquo;eth </strong></td>
<td>col.</td>
<td>aurulent</td>
</tr>
<tr>
<td><strong> h.uis&rsquo;eyo&rdquo; </strong></td>
<td>elm.CMP</td>
<td>Life Support</td>
</tr>
<tr>
<td><strong> h.uiy&rsquo;ole&rdquo; </strong></td>
<td>elm.CMP</td>
<td>metabolism</td>
</tr>
<tr>
<td><strong> h.ūn </strong></td>
<td>elm.</td>
<td>labor; work (manual work)</td>
</tr>
<tr>
<td><strong> h&rsquo;ā </strong></td>
<td>elm.</td>
<td>punch; hit; strike</td>
</tr>
<tr>
<td><strong> h&rsquo;āha&rdquo; </strong></td>
<td>elm.CMP</td>
<td>pummel; batter; bash</td>
</tr>
<tr>
<td><strong> hā&rsquo;a </strong></td>
<td>elm.</td>
<td>excess; over; excessive; exceed</td>
</tr>
<tr>
<td><strong> ha&rsquo;ha </strong></td>
<td>vcp.</td>
<td>[moderate emphatic]</td>
</tr>
<tr>
<td><strong> hā&rsquo;hi </strong></td>
<td>elm.</td>
<td>numbing; tingling (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> ha&rsquo;nue </strong></td>
<td>elm.</td>
<td>excited; engaged; turned on; enthusiastic</td>
</tr>
<tr>
<td><strong> ha&rdquo; </strong></td>
<td>vcp.</td>
<td>[strong emphatic]</td>
</tr>
<tr>
<td><strong> hai </strong></td>
<td>elm.</td>
<td>confidant; buddy; friendship with trust</td>
</tr>
<tr>
<td><strong> hai&rsquo;pe </strong></td>
<td>n.</td>
<td>A Xi&rsquo;an plant similar to Terran tea, but loaded with beneficial bacteria. Instead of the leaves of a bush, it&#8217;s the leaves of a tropical pine tree.</td>
</tr>
<tr>
<td><strong> han </strong></td>
<td>elm</td>
<td>map; draw (an image of something); illustrate an (idea)</td>
</tr>
<tr>
<td><strong> hankeng </strong></td>
<td>elm.CMP</td>
<td>a map (of territory)</td>
</tr>
<tr>
<td><strong> hanxiin(uo&rsquo;a) </strong></td>
<td>elm.CMP</td>
<td>written instructions or directions</td>
</tr>
<tr>
<td><strong> hao </strong></td>
<td>v.LAUD</td>
<td>be of a class</td>
</tr>
<tr>
<td><strong> he&rsquo;.u&rsquo;i </strong></td>
<td>rel.</td>
<td>on top of; on (touching)</td>
</tr>
<tr>
<td><strong> he&rsquo;a </strong></td>
<td>elm.</td>
<td>sensation; physical feeling; ability to feel</td>
</tr>
<tr>
<td><strong> he&rsquo;o </strong></td>
<td>elm.</td>
<td>dedicaiton; commmitment; commit to</td>
</tr>
<tr>
<td><strong> he&rsquo;u </strong></td>
<td>rel.</td>
<td>above</td>
</tr>
<tr>
<td><strong> hela.t&rsquo;or </strong></td>
<td>n.</td>
<td>freezer (for food (borrowed from Spanish &laquo;(con)gelador&raquo;))</td>
</tr>
<tr>
<td><strong> hi&rsquo;ch.oy&rsquo;othle&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>Healthpak</td>
</tr>
<tr>
<td><strong> hi&rsquo;cho </strong></td>
<td>elm.</td>
<td>kit; set of tools; gear</td>
</tr>
<tr>
<td><strong> hi&rsquo;chōklo </strong></td>
<td>elm.CMP</td>
<td>Landing Gear</td>
</tr>
<tr>
<td><strong> hi&rsquo;ho </strong></td>
<td>elm.</td>
<td>infant cousin (neice or nephew) &ldquo;any baby to whom one is related&rdquo;</td>
</tr>
<tr>
<td><strong> hii </strong></td>
<td>elm.</td>
<td>younger juvenile cousin of a juvenile</td>
</tr>
<tr>
<td><strong> Hiin </strong></td>
<td>line</td>
<td>Hiin</td>
</tr>
<tr>
<td><strong> ho </strong></td>
<td>elm.</td>
<td>quiet; silent; secret; hidden</td>
</tr>
<tr>
<td><strong> ho&rsquo;a </strong></td>
<td>rel.</td>
<td>right of; on the right of; toward the right</td>
</tr>
<tr>
<td><strong> hon </strong></td>
<td>vcp.</td>
<td>[tendential (&ldquo;tendency&rdquo;)]; X tends to do/be Y</td>
</tr>
<tr>
<td><strong> hoth </strong></td>
<td>elm.</td>
<td>read</td>
</tr>
<tr>
<td><strong> hu </strong></td>
<td>num.</td>
<td>zero 0</td>
</tr>
<tr>
<td><strong> hū&rsquo;hu tā&rsquo;ta </strong></td>
<td>elm.</td>
<td>so so; mediocre; not good and not bad</td>
</tr>
<tr>
<td><strong> huā </strong></td>
<td>elm.</td>
<td>most; (superlative)</td>
</tr>
<tr>
<td><strong> hua&rsquo;ua </strong></td>
<td>elm.</td>
<td>humor; joke; funny</td>
</tr>
<tr>
<td><strong> hual </strong></td>
<td>elm.</td>
<td>any; whichever; whatever</td>
</tr>
<tr>
<td><strong> huang </strong></td>
<td>elm.</td>
<td>important; importance; matter; import</td>
</tr>
<tr>
<td><strong> hue </strong></td>
<td>rel.</td>
<td>between (2); among (many)</td>
</tr>
<tr>
<td><strong> huen </strong></td>
<td>elm.</td>
<td>split; share; divide</td>
</tr>
<tr>
<td><strong> hui </strong></td>
<td>elm.</td>
<td>system; organized set; layout</td>
</tr>
<tr>
<td><strong> hui&rsquo;a </strong></td>
<td>elm.</td>
<td>contemplate; conscious meditation; iterative thought</td>
</tr>
<tr>
<td><strong> huiāl </strong></td>
<td>elm.CMP</td>
<td>explore through meditative contemplation</td>
</tr>
<tr>
<td><strong> huing </strong></td>
<td>elm</td>
<td>wave; pulse</td>
</tr>
<tr>
<td><strong> huing&rsquo;puay&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>heat wave</td>
</tr>
<tr>
<td><strong> huingchuikr.ūth </strong></td>
<td>elm.CMP</td>
<td>tsunami</td>
</tr>
<tr>
<td><strong> huingchuokyu </strong></td>
<td>elm.CMP</td>
<td>front</td>
</tr>
<tr>
<td><strong> huinge&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>ripple</td>
</tr>
<tr>
<td><strong> huiso&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>musculature</td>
</tr>
<tr>
<td><strong> huisuhyoton </strong></td>
<td>elm.CMP</td>
<td>Starmap</td>
</tr>
<tr>
<td><strong> huitā </strong></td>
<td>elm.CMP</td>
<td>neighborhood</td>
</tr>
<tr>
<td><strong> huitia </strong></td>
<td>elm.CMP</td>
<td>mathematics</td>
</tr>
<tr>
<td><strong> huityi se lye&rsquo;hung </strong></td>
<td>elm.CMP</td>
<td>Missile Rack</td>
</tr>
<tr>
<td><strong> huityi se lye&rsquo;p.ānp&rsquo;uāng </strong></td>
<td>elm.CMP</td>
<td>Torpedo Rack</td>
</tr>
<tr>
<td><strong> huityi se lye&rsquo;ri </strong></td>
<td>elm.CMP</td>
<td>Rocket Rack</td>
</tr>
<tr>
<td><strong> huityunguo&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>grammar (of a language)</td>
</tr>
<tr>
<td><strong> huiu&rsquo;oa; huichaiu&rsquo;oa; chaiu&rsquo;oa </strong></td>
<td>elm.CMP</td>
<td>Comms</td>
</tr>
<tr>
<td><strong> hung </strong></td>
<td>elm.</td>
<td>older; senior; sr.; high in status; high-grade</td>
</tr>
<tr>
<td><strong> huo </strong></td>
<td>elm.</td>
<td>hearing; audio input</td>
</tr>
<tr>
<td><strong> hyan </strong></td>
<td>elm.</td>
<td>each; every</td>
</tr>
<tr>
<td><strong> hyao </strong></td>
<td>elm.</td>
<td>sky; space (outer space); the area between planets.</td>
</tr>
<tr>
<td><strong> hyaok&#8217;ya </strong></td>
<td>elm.CMP</td>
<td>Dogfight (in space )</td>
</tr>
<tr>
<td><strong> hyaokyu </strong></td>
<td>elm.CMP</td>
<td>sky (daytime) on a world with an atmosphere</td>
</tr>
<tr>
<td><strong> hyaokyu&rsquo;ām </strong></td>
<td>elm.CMP</td>
<td>overcast or cloudy sky</td>
</tr>
<tr>
<td><strong> hyaokyue&rsquo;so </strong></td>
<td>elm.CMP</td>
<td>clear sky</td>
</tr>
<tr>
<td><strong> hyaotan </strong></td>
<td>elm.CMP</td>
<td>outer space; (&ldquo;the black sky&rdquo;)</td>
</tr>
<tr>
<td><strong> hyath </strong></td>
<td>elm.</td>
<td>military</td>
</tr>
<tr>
<td><strong> hyē </strong></td>
<td>elm.</td>
<td>complexity</td>
</tr>
<tr>
<td><strong> Hyen&rdquo; </strong></td>
<td>line</td>
<td>Hy&eacute;n</td>
</tr>
<tr>
<td><strong> hyi </strong></td>
<td>elm.</td>
<td>prestige; fame</td>
</tr>
<tr>
<td><strong> hyo </strong></td>
<td>elm.</td>
<td>sphere; spherical; orb; ball</td>
</tr>
<tr>
<td><strong> hyo&rsquo;ii </strong></td>
<td>elm.CMP</td>
<td>pollen; spore</td>
</tr>
<tr>
<td><strong> hyoii </strong></td>
<td>elm.CMP</td>
<td>sun</td>
</tr>
<tr>
<td><strong> hyopā&rsquo;an; hyo&rsquo;pān </strong></td>
<td>elm.CMP</td>
<td>Grenade</td>
</tr>
<tr>
<td><strong> hyopyen </strong></td>
<td>elm.CMP</td>
<td>ammunition; bullets; ammo (<strong>hyopy.enr&rsquo;o</strong>)</td>
</tr>
<tr>
<td><strong> hyopyen; hyopy.enr&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>Ammo</td>
</tr>
<tr>
<td><strong> hyothen </strong></td>
<td>elm.CMP</td>
<td>eyeball</td>
</tr>
<tr>
<td><strong> hyotonxyiing; hyoton </strong></td>
<td>elm.CMP</td>
<td>Star</td>
</tr>
<tr>
<td><strong> Hyū&rsquo;m&acirc;n </strong></td>
<td>elm.</td>
<td>Human</td>
</tr>
<tr>
<td><strong> hyūn </strong></td>
<td>elm.</td>
<td>part; role; function</td>
</tr>
<tr>
<td><strong> i&rdquo; </strong></td>
<td>elm.</td>
<td>touch; contact with X</td>
</tr>
<tr>
<td><strong> ia </strong></td>
<td>elm.</td>
<td>&ldquo;epic&rdquo; (holy, in the sense of &lsquo;beyond belief&rsquo;)</td>
</tr>
<tr>
<td><strong> ii </strong></td>
<td>elm.</td>
<td>light; brightness; shine</td>
</tr>
<tr>
<td><strong> ii&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>plant (generic term for plant); flora (juxtaposed to fauna)</td>
</tr>
<tr>
<td><strong> ii&rsquo;axye </strong></td>
<td>elm.CMP</td>
<td>bulb</td>
</tr>
<tr>
<td><strong> ii&rsquo;ken </strong></td>
<td>elm.CMP</td>
<td>long vegetable that grows on vines and is popular as a pickle</td>
</tr>
<tr>
<td><strong> ii&rsquo;lio </strong></td>
<td>elm.CMP</td>
<td>moss; lichen</td>
</tr>
<tr>
<td><strong> ii&rsquo;puongchiin </strong></td>
<td>elm.CMP</td>
<td>astringent fruit (berry-like fruit that greatly increases tannin levels in dishes)</td>
</tr>
<tr>
<td><strong> ii&rsquo;sauo </strong></td>
<td>elm.CMP</td>
<td>tree or very large bush</td>
</tr>
<tr>
<td><strong> ii&rsquo;sauo </strong></td>
<td>elm.CMP</td>
<td>tree</td>
</tr>
<tr>
<td><strong> ii&rsquo;ten </strong></td>
<td>elm.CMP</td>
<td>vegetable; fruit; edible leaves; etc.</td>
</tr>
<tr>
<td><strong> ii&rsquo;tenkuam </strong></td>
<td>elm.CMP</td>
<td>fruit (also simply ii&rsquo;kuam (can be used for human &lsquo;dessert&rsquo;))</td>
</tr>
<tr>
<td><strong> ii&rsquo;tung </strong></td>
<td>elm.CMP</td>
<td>plant; bush; groundcover</td>
</tr>
<tr>
<td><strong> ii&rdquo;. </strong></td>
<td>nlz.CLTC</td>
<td>[vegitation; plant; tree; moss; lichen, etc.]</td>
</tr>
<tr>
<td><strong> ii&rdquo;puith&rdquo; </strong></td>
<td>elm.CMP</td>
<td>itchy plant (nettle-like plant used to create seasoning that causes itching sensation)</td>
</tr>
<tr>
<td><strong> iikyu </strong></td>
<td>elm.CMP</td>
<td>aurora</td>
</tr>
<tr>
<td><strong> iikyuxuith </strong></td>
<td>elm.CMP</td>
<td>polar aurora</td>
</tr>
<tr>
<td><strong> ii&#8217;pun </strong></td>
<td>elm.CMP</td>
<td>grass</td>
</tr>
<tr>
<td><strong> IIth </strong></td>
<td>PN.feml</td>
<td>Iith</td>
</tr>
<tr>
<td><strong> iixue&rsquo;aye </strong></td>
<td>elm.CMP</td>
<td>new light of the day (sunrise)</td>
</tr>
<tr>
<td><strong> iiyonai </strong></td>
<td>elm.CMP</td>
<td>Flare</td>
</tr>
<tr>
<td><strong> in.che&rsquo;ra </strong></td>
<td>n.</td>
<td>&#8220;bread&#8221; (borrowed from the Ethiopic &laquo;injera&raquo;)</td>
</tr>
<tr>
<td><strong> ing </strong></td>
<td>vcp.</td>
<td>[dubiative (&ldquo;dout&rdquo;)]</td>
</tr>
<tr>
<td><strong> ing </strong></td>
<td>elm.</td>
<td>doubt</td>
</tr>
<tr>
<td><strong> Jh&rsquo;an </strong></td>
<td>elm.SRV</td>
<td>Xi&rsquo;an</td>
</tr>
<tr>
<td><strong> k.ay&rsquo;o </strong></td>
<td>deix.</td>
<td>there (near you the listener or where we both can see I&Otilde;m indicating)</td>
</tr>
<tr>
<td><strong> k.ē </strong></td>
<td>elm.</td>
<td>fold; bend; crease</td>
</tr>
<tr>
<td><strong> k.ēk&rsquo;eng </strong></td>
<td>elm.CMP</td>
<td>valley</td>
</tr>
<tr>
<td><strong> k.eng&rsquo;a&rsquo;chui </strong></td>
<td>elm.CMP</td>
<td>island (in a large body of water)</td>
</tr>
<tr>
<td><strong> k.eng&rsquo;ii&rsquo;pun </strong></td>
<td>elm.CMP</td>
<td>meadow</td>
</tr>
<tr>
<td><strong> k.et&rsquo;ao </strong></td>
<td>elm.</td>
<td>promise; assure</td>
</tr>
<tr>
<td><strong> k.eth </strong></td>
<td>elm.</td>
<td>weapon; simple weapon (as a knife; club; (with no moving parts))</td>
</tr>
<tr>
<td><strong> k.ethxy&rsquo;iing </strong></td>
<td>elm.CMP</td>
<td>Melee</td>
</tr>
<tr>
<td><strong> k.ik&rsquo;a </strong></td>
<td>elm.</td>
<td>surprise (happy; positive)</td>
</tr>
<tr>
<td><strong> k.o&rsquo;a </strong></td>
<td>elm.</td>
<td>wall; vertical surface used for building or environmental separation</td>
</tr>
<tr>
<td><strong> k.o&rsquo;ahe&#8217;u </strong></td>
<td>elm.CMP</td>
<td>ceiling (of a room)</td>
</tr>
<tr>
<td><strong> k.o&rsquo;ahe&#8217;uten </strong></td>
<td>elm.CMP</td>
<td>growth ceiling (special grooved surface innoculated with healthy/flavorful yeast, bacteria, and other microorgamisms to promote fermentation)</td>
</tr>
<tr>
<td><strong> k.o&rsquo;aten </strong></td>
<td>elm.CMP</td>
<td>growth wall (special grooved surface innoculated with healthy/flavorful yeast, bacteria, and other microorgamisms to promote fermentation)</td>
</tr>
<tr>
<td><strong> K.om&rsquo;o </strong></td>
<td>PN.feml</td>
<td>Kom&oacute;</td>
</tr>
<tr>
<td><strong> k.ua </strong></td>
<td>num.</td>
<td>five 5</td>
</tr>
<tr>
<td><strong> k.ūng </strong></td>
<td>elm.</td>
<td>overwhelm; overwhelming</td>
</tr>
<tr>
<td><strong> k.uot&rsquo;aouin </strong></td>
<td>elm.CMP</td>
<td>Cooler</td>
</tr>
<tr>
<td><strong> k.uoy&rsquo;o&rsquo;thli </strong></td>
<td>elm.CMP</td>
<td>Battery</td>
</tr>
<tr>
<td><strong> k.ur&#8217;a </strong></td>
<td>elm.</td>
<td>excitement; intense physical or mental joy; exciting</td>
</tr>
<tr>
<td><strong> k.yāi </strong></td>
<td>elm.</td>
<td>genuine fear; being frightened; afraid; fright (internal sense)</td>
</tr>
<tr>
<td><strong> k.yāo </strong></td>
<td>elm.</td>
<td>danger</td>
</tr>
<tr>
<td><strong> k.yeth </strong></td>
<td>elm.</td>
<td>caution</td>
</tr>
<tr>
<td><strong> k&rsquo;ya </strong></td>
<td>elm.</td>
<td>fighting; fight; battle</td>
</tr>
<tr>
<td><strong> k&rsquo;yah&rsquo;āno </strong></td>
<td>elm.CMP</td>
<td>&ldquo;fist fight&rdquo;</td>
</tr>
<tr>
<td><strong> k&rsquo;yano (e sol k.eth) </strong></td>
<td>elm.CMP</td>
<td>Martial Arts</td>
</tr>
<tr>
<td><strong> ka </strong></td>
<td>rel.</td>
<td>in; at; on</td>
</tr>
<tr>
<td><strong> ka&#8220;ho&#8217;a </strong></td>
<td>elm.CMP</td>
<td>starbord/right side (of a ship)</td>
</tr>
<tr>
<td><strong> ka&#8220;ne&#8217;a </strong></td>
<td>elm.CMP</td>
<td>port/left side (of a ship)</td>
</tr>
<tr>
<td><strong> ka&rsquo;hual </strong></td>
<td>elm.CMP</td>
<td>anywhere</td>
</tr>
<tr>
<td><strong> ka&rsquo;i.y&rsquo;a </strong></td>
<td>deix.</td>
<td>yonder (far away from both of us, but at a perceptible distance)</td>
</tr>
<tr>
<td><strong> ka&rsquo;loa </strong></td>
<td>elm.CMP</td>
<td>dining area</td>
</tr>
<tr>
<td><strong> ka&rsquo;loatō </strong></td>
<td>elm.CMP</td>
<td>restaurant</td>
</tr>
<tr>
<td><strong> ka&rsquo;lye </strong></td>
<td>elm.CMP</td>
<td>goal; destination; target</td>
</tr>
<tr>
<td><strong> ka&rsquo;m.e&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>elevation; a high point; lookout over lower territory</td>
</tr>
<tr>
<td><strong> ka&rsquo;o.u&rsquo;a </strong></td>
<td>deix.</td>
<td>beyond (so far away that we cannot see or easily reach that place)</td>
</tr>
<tr>
<td><strong> ka&rsquo;t.op&rsquo;ui&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>flower/botanical garden</td>
</tr>
<tr>
<td><strong> ka&rsquo;t.ot&rsquo;enxyo </strong></td>
<td>elm.CMP</td>
<td>garden (non-commercial vegetable patch, etc.)</td>
</tr>
<tr>
<td><strong> ka&rsquo;uōng </strong></td>
<td>elm.</td>
<td>toilette room; place to relieve onself</td>
</tr>
<tr>
<td><strong> ka&rsquo;Xa </strong></td>
<td>elm.CMP</td>
<td>Interspace</td>
</tr>
<tr>
<td><strong> ka&rsquo;xuel </strong></td>
<td>elm.CMP</td>
<td>cave; cavern</td>
</tr>
<tr>
<td><strong> ka&rsquo;xy.oa </strong></td>
<td>Q.</td>
<td>where?</td>
</tr>
<tr>
<td><strong> ka&rsquo;yāng </strong></td>
<td>elm.CMP</td>
<td>Bunk (bed or other specifically designated area when one is assigned to sleep)</td>
</tr>
<tr>
<td><strong> ka&rdquo; </strong></td>
<td>elm.</td>
<td>place; location</td>
</tr>
<tr>
<td><strong> ka&rdquo;ii&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>farm for crops</td>
</tr>
<tr>
<td><strong> ka&rdquo;ma&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>animal farm</td>
</tr>
<tr>
<td><strong> kāi </strong></td>
<td>elm.</td>
<td>maintain; maintenance; repair</td>
</tr>
<tr>
<td><strong> ka&#8217;klu </strong></td>
<td>elm.CMP</td>
<td>Aft (of a ship)</td>
</tr>
<tr>
<td><strong> kal&rsquo;tu </strong></td>
<td>n.</td>
<td>dire fly (a deadly flying insectoid)</td>
</tr>
<tr>
<td><strong> ka&#8217;nāl; kahyonāl </strong></td>
<td>elm.CMP</td>
<td>Cockpit</td>
</tr>
<tr>
<td><strong> kao&rdquo; </strong></td>
<td>deix.</td>
<td>here (near me the speaker)</td>
</tr>
<tr>
<td><strong> kar&rsquo;tu </strong></td>
<td>n.</td>
<td>dire fly (variant pronunciation of <strong>kal&rsquo;tu</strong>)</td>
</tr>
<tr>
<td><strong> ka&#8217;san </strong></td>
<td>elm.CMP</td>
<td>Cabin (as in a general room on a ship)</td>
</tr>
<tr>
<td><strong> ka&#8217;sang </strong></td>
<td>elm.CMP</td>
<td>Fore (of a ship)</td>
</tr>
<tr>
<td><strong> kē&rsquo;hith </strong></td>
<td>elm.</td>
<td>obliterate / obliteration; extinct / extinction; annihilation; sterilize (of contamination)</td>
</tr>
<tr>
<td><strong> ke&rsquo;u </strong></td>
<td>elm.</td>
<td>size</td>
</tr>
<tr>
<td><strong> kea </strong></td>
<td>elm.</td>
<td>independent; unfettered; lone; solitary, alone (but not lonely)</td>
</tr>
<tr>
<td><strong> ken </strong></td>
<td>elm.</td>
<td>long (of a physical thing); tall (of a person or animal)</td>
</tr>
<tr>
<td><strong> keng </strong></td>
<td>elm.</td>
<td>land; ground; territory (not a body of water)</td>
</tr>
<tr>
<td><strong> keng.au&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>arctic regions</td>
</tr>
<tr>
<td><strong> keng&rsquo;.au&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>ice fields; frozen (waste)lands; frozen tundra</td>
</tr>
<tr>
<td><strong> keng&rsquo;.um&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>bog; swamp; fen</td>
</tr>
<tr>
<td><strong> keng&rsquo;.un&rsquo;ii </strong></td>
<td>elm.CMP</td>
<td>forest</td>
</tr>
<tr>
<td><strong> keng&rsquo;hoa </strong></td>
<td>elm.CMP</td>
<td>uneven/rough terrain</td>
</tr>
<tr>
<td><strong> kengchuiha&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>floodplain</td>
</tr>
<tr>
<td><strong> kenglath </strong></td>
<td>elm.CMP</td>
<td>desert (a particularly dry territory)</td>
</tr>
<tr>
<td><strong> kengli&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>plain; savanna</td>
</tr>
<tr>
<td><strong> kengli&rsquo;olath </strong></td>
<td>elm.CMP</td>
<td>tundra (dry); steppe</td>
</tr>
<tr>
<td><strong> kengli&rsquo;om.e&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>plateau; mesa</td>
</tr>
<tr>
<td><strong> kengmuiima </strong></td>
<td>elm.CMP</td>
<td>nature preserve (as in &lsquo;national park&rsquo;)</td>
</tr>
<tr>
<td><strong> kengmuima </strong></td>
<td>elm.CMP</td>
<td>pasture (for grazing); paddock</td>
</tr>
<tr>
<td><strong> kengp.uay&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>tropics</td>
</tr>
<tr>
<td><strong> kengten </strong></td>
<td>elm.CMP</td>
<td>field (for the cultivation of crops)</td>
</tr>
<tr>
<td><strong> kengunii&rsquo;.um&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>jungle; rainforest</td>
</tr>
<tr>
<td><strong> kengye&rsquo;u </strong></td>
<td>elm.CMP</td>
<td>basin</td>
</tr>
<tr>
<td><strong> kengyeng </strong></td>
<td>elm.CMP</td>
<td>desert (metaphorical &ldquo;burning land&rdquo;)</td>
</tr>
<tr>
<td><strong> ki.s&rsquo;a </strong></td>
<td>elm.</td>
<td>ammoniac; chemical; bitter (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> ki&rsquo;a </strong></td>
<td>vcp.</td>
<td>[abstractive; metaphorical mood] <strong>ki&rsquo;al</strong></td>
</tr>
<tr>
<td><strong> ki&rsquo;m.ethl&rsquo;e </strong></td>
<td>elm.CMP</td>
<td>headache</td>
</tr>
<tr>
<td><strong> ki&rsquo;meth </strong></td>
<td>elm.</td>
<td>pain; physical suffering</td>
</tr>
<tr>
<td><strong> ki&rdquo; </strong></td>
<td>elm.</td>
<td>attach; hook up; hook into; plug in</td>
</tr>
<tr>
<td><strong> kii&rsquo;uo </strong></td>
<td>elm.</td>
<td>intoxicating; aluring; draw; charm; seduction</td>
</tr>
<tr>
<td><strong> kiil </strong></td>
<td>col.</td>
<td>cerulean</td>
</tr>
<tr>
<td><strong> Kl.ō </strong></td>
<td>line</td>
<td>Kloh</td>
</tr>
<tr>
<td><strong> kl.u&rsquo;i </strong></td>
<td>rel.</td>
<td>touching or attached or riding on the back of</td>
</tr>
<tr>
<td><strong> kl.u&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>previous (in sequence) <strong>klu + o&rdquo;</strong></td>
</tr>
<tr>
<td><strong> Kli&rsquo;thla </strong></td>
<td>PN.male</td>
<td>Klithla</td>
</tr>
<tr>
<td><strong> klo </strong></td>
<td>elm.</td>
<td>ground; surface of a planet; touching down</td>
</tr>
<tr>
<td><strong> klom.e&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>tree crab (from klon + m.e&rsquo;a) (a food animal that lives in trees)</td>
</tr>
<tr>
<td><strong> klon </strong></td>
<td>elm.</td>
<td>spider-crab (general term for all species of insects and crustacean with spider/crab shaped bodies)</td>
</tr>
<tr>
<td><strong> klu </strong></td>
<td>rel.</td>
<td>behind</td>
</tr>
<tr>
<td><strong> ko </strong></td>
<td>vcp.</td>
<td>[preistantiative (&ldquo;already&rdquo;] kol (&ldquo;not yet&rdquo;)</td>
</tr>
<tr>
<td><strong> ko&rsquo;i </strong></td>
<td>rel.</td>
<td>into (sense of dividing)</td>
</tr>
<tr>
<td><strong> ko&rsquo;t.a </strong></td>
<td>elm.</td>
<td>question; inqiry; inquisitive</td>
</tr>
<tr>
<td><strong> ko&rdquo; </strong></td>
<td>elm.</td>
<td>distance</td>
</tr>
<tr>
<td><strong> koa </strong></td>
<td>elm.</td>
<td>race</td>
</tr>
<tr>
<td><strong> kōl </strong></td>
<td>elm.</td>
<td>positivity; approval; satisfaction</td>
</tr>
<tr>
<td><strong> kon </strong></td>
<td>elm.</td>
<td>get; acquire; obtain; buy</td>
</tr>
<tr>
<td><strong> kong </strong></td>
<td>elm.</td>
<td>walk; go on foot</td>
</tr>
<tr>
<td><strong> kongleth </strong></td>
<td>elm.CMP</td>
<td>run; hurry; dash</td>
</tr>
<tr>
<td><strong> konglo </strong></td>
<td>elm.CMP</td>
<td>crawl (of bipedal infants or insects, etc. (from kong+klo))</td>
</tr>
<tr>
<td><strong> Kr.ē </strong></td>
<td>line</td>
<td>Kray</td>
</tr>
<tr>
<td><strong> kr.ōng </strong></td>
<td>elm.</td>
<td>vile; disgusting; grotesque; abhorent; barbaric; degenerate</td>
</tr>
<tr>
<td><strong> Kr.ū </strong></td>
<td>PN.male</td>
<td>Krew</td>
</tr>
<tr>
<td><strong> kr.ūth </strong></td>
<td>elm.</td>
<td>death; dead; die; perish</td>
</tr>
<tr>
<td><strong> kra&rsquo;pāng </strong></td>
<td>elm.CMP</td>
<td>extatic; bliss; exultant</td>
</tr>
<tr>
<td><strong> kran </strong></td>
<td>elm.</td>
<td>work (non-laborious); mental focus and effort; contribution to society</td>
</tr>
<tr>
<td><strong> kren </strong></td>
<td>elm.</td>
<td>enough; suffice; sufficient</td>
</tr>
<tr>
<td><strong> kri </strong></td>
<td>elm.</td>
<td>sense of one&rsquo;s genuine feelings juxtaposed against what society might consider proper and polite</td>
</tr>
<tr>
<td><strong> kro </strong></td>
<td>elm.</td>
<td>contamination; pollutant</td>
</tr>
<tr>
<td><strong> krokyu </strong></td>
<td>elm.CMP</td>
<td>air pollution</td>
</tr>
<tr>
<td><strong> ku </strong></td>
<td>pn.NEU</td>
<td>It (inanimate)</td>
</tr>
<tr>
<td><strong> kū </strong></td>
<td>num.</td>
<td>ten thousand 10,000</td>
</tr>
<tr>
<td><strong> ku&rsquo;ngo </strong></td>
<td>elm.</td>
<td>firm; needs to be cut into small pieces to eat; like cooked vegetables (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> ku&rsquo;ya </strong></td>
<td>elm.</td>
<td>rude; impolite</td>
</tr>
<tr>
<td><strong> kua </strong></td>
<td>elm.</td>
<td>feeling (opinon; non-religious belief based on experience)</td>
</tr>
<tr>
<td><strong> kuai </strong></td>
<td>vcp.</td>
<td>[passive/ergative]</td>
</tr>
<tr>
<td><strong> kuai.x&rsquo;uā&rsquo;cha </strong></td>
<td>idm.</td>
<td>burnt; charred; food that&#8217;s been exposed to high temperatures; &ldquo;cooked&rdquo; based on the sensibilities of most Humans. (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> kuair </strong></td>
<td>elm.</td>
<td>class of light (space) fighter; also scalpel; blade (for surgery) alt: <span class="caps">QHIRE</span> (marketing spelling)</td>
</tr>
<tr>
<td><strong> kuām </strong></td>
<td>rel.</td>
<td>beyond</td>
</tr>
<tr>
<td><strong> kuāo </strong></td>
<td>elm.</td>
<td>ancient word for a defunct Xi&rsquo;an currency; slang for money; &ldquo;dough, bills, etc.&rdquo;; idiom e yo kuāo y.ui ____ &ldquo;don&#8217;t have it in one to do something about ________&rdquo;</td>
</tr>
<tr>
<td><strong> kuaxue&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>neophyte; inexperienced; novice (<strong>nyakuaxue&rsquo;a</strong>)</td>
</tr>
<tr>
<td><strong> kue&rdquo; </strong></td>
<td>elm.</td>
<td>force; thrust; push</td>
</tr>
<tr>
<td><strong> kuen </strong></td>
<td>elm.</td>
<td>money; currency; credit(s)</td>
</tr>
<tr>
<td><strong> kui </strong></td>
<td>elm.</td>
<td>amount</td>
</tr>
<tr>
<td><strong> kui&rsquo;xy.oa </strong></td>
<td>Q</td>
<td>how much (volume)?</td>
</tr>
<tr>
<td><strong> kuihual </strong></td>
<td>elm.CMP</td>
<td>any amount; however much</td>
</tr>
<tr>
<td><strong> kuing </strong></td>
<td>elm.</td>
<td>practice; exercise</td>
</tr>
<tr>
<td><strong> kuinghankeng </strong></td>
<td>elm.CMP</td>
<td>the practice of cartography</td>
</tr>
<tr>
<td><strong> kum </strong></td>
<td>pn.NEU</td>
<td>they (inanimate)</td>
</tr>
<tr>
<td><strong> kuo. </strong></td>
<td>nlz.CLTC</td>
<td>[complex tool for X]</td>
</tr>
<tr>
<td><strong> kuo&rsquo;p.ānh&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>Mine</td>
</tr>
<tr>
<td><strong> kuo&rsquo;p.ap&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>Repeater</td>
</tr>
<tr>
<td><strong> kuo&rsquo;t.oku&rsquo;e; k.uok&rsquo;ue </strong></td>
<td>elm.CMP</td>
<td>Engine</td>
</tr>
<tr>
<td><strong> kuo&rsquo;t.or&rsquo;u </strong></td>
<td>elm.CMP</td>
<td>Gravity Generator</td>
</tr>
<tr>
<td><strong> kuo&rsquo;t.othl&rsquo;i </strong></td>
<td>elm.CMP</td>
<td>Power Plant</td>
</tr>
<tr>
<td><strong> kuo&rsquo;to.t&rsquo;uing </strong></td>
<td>elm.CMP</td>
<td>cooler (smaler scale device) (used to cool food to cave-like temperatures)</td>
</tr>
<tr>
<td><strong> kuo&rsquo;yan </strong></td>
<td>elm.CMP</td>
<td>Up Escalator (for signage)</td>
</tr>
<tr>
<td><strong> kuōa </strong></td>
<td>elm.CMP</td>
<td>Computer</td>
</tr>
<tr>
<td><strong> kuōanāl </strong></td>
<td>elm.CMP</td>
<td>Avionics</td>
</tr>
<tr>
<td><strong> kuochā&rsquo;eoa; kuochā&rsquo;e </strong></td>
<td>elm.CMP</td>
<td>Display</td>
</tr>
<tr>
<td><strong> kuohe&rsquo;.uhy&rsquo;aokyu </strong></td>
<td>elm.CMP</td>
<td>Satellite</td>
</tr>
<tr>
<td><strong> kuolaXa </strong></td>
<td>elm.CMP</td>
<td>Jump Module</td>
</tr>
<tr>
<td><strong> kuom&rsquo;pon </strong></td>
<td>n.</td>
<td>food ape (orangutan-like creature raised for meat)</td>
</tr>
<tr>
<td><strong> kuongyaiya </strong></td>
<td>elm.CMP</td>
<td>Radar</td>
</tr>
<tr>
<td><strong> kuo&#8217;rath </strong></td>
<td>elm.CMP</td>
<td>Down Escalator (for signage)</td>
</tr>
<tr>
<td><strong> kuos.uk&rsquo;ue; kuosu </strong></td>
<td>elm.CMP</td>
<td>Thruster</td>
</tr>
<tr>
<td><strong> kuotaisan; taisan; atai </strong></td>
<td>elm.CMP</td>
<td>Component</td>
</tr>
<tr>
<td><strong> Kuoth </strong></td>
<td>line</td>
<td>Quoth</td>
</tr>
<tr>
<td><strong> kuotyisāo </strong></td>
<td>elm.CMP</td>
<td>Escape Pod</td>
</tr>
<tr>
<td><strong> kuoxuan </strong></td>
<td>elm.CMP</td>
<td>complex game; video game console; jet ski, etc. for entertainment</td>
</tr>
<tr>
<td><strong> kuoyanō </strong></td>
<td>elm.CMP</td>
<td>Scanner</td>
</tr>
<tr>
<td><strong> kuth </strong></td>
<td>col.</td>
<td>xanthic</td>
</tr>
<tr>
<td><strong> kuam </strong></td>
<td>elm</td>
<td>sweet (sweet-tasting for the Xi&rsquo;an pallet (be careful)); sugar-sweet; not properly fermented or decayed</td>
</tr>
<tr>
<td><strong> kye </strong></td>
<td>elm.</td>
<td>letter; character; glyph; symbol</td>
</tr>
<tr>
<td><strong> Kye&rsquo;na </strong></td>
<td>name</td>
<td>&ldquo;Daughter&rdquo; (endearment term for non-biological daughter)</td>
</tr>
<tr>
<td><strong> kye&rsquo;nua </strong></td>
<td>elm.CMP</td>
<td><strong>pyā&rsquo;hai</strong> daughter</td>
</tr>
<tr>
<td><strong> kyen&rsquo;yu </strong></td>
<td>elm.CMP</td>
<td><strong>pyā&rsquo;hai</strong> son</td>
</tr>
<tr>
<td><strong> Kyen&rsquo;yu </strong></td>
<td>name</td>
<td>&ldquo;Son&rdquo; (endearment term for non-biological son)</td>
</tr>
<tr>
<td><strong> kyen&rdquo; </strong></td>
<td>elm.</td>
<td>non-biological child within a <strong>pyā&rsquo;hai</strong> (<strong>kye&rsquo;nua</strong> (d.), <strong>kyen&rsquo;yu</strong>)</td>
</tr>
<tr>
<td><strong> kyengchui </strong></td>
<td>elm.CMP</td>
<td>evaporation (of liquids); transformation of liquids into their gaseous states</td>
</tr>
<tr>
<td><strong> kyeng </strong></td>
<td>elm.</td>
<td>evaporation; dissolve; vanish; disappear</td>
</tr>
<tr>
<td><strong> kyengii </strong></td>
<td>elm.CMP</td>
<td>sunset</td>
</tr>
<tr>
<td><strong> kyexiin </strong></td>
<td>elm.CMP</td>
<td>script; alphabetic letter</td>
</tr>
<tr>
<td><strong> kyi </strong></td>
<td>elm.</td>
<td>breath; breathing; respiraiton; sigh</td>
</tr>
<tr>
<td><strong> kyi&rsquo;yāngp.uāng </strong></td>
<td>elm.CMP</td>
<td>snoring; making breathing noises while asleep</td>
</tr>
<tr>
<td><strong> kyo </strong></td>
<td>elm.</td>
<td>department; group; section; troup</td>
</tr>
<tr>
<td><strong> kyōhuitō </strong></td>
<td>elm.CMP</td>
<td>department/division/office of operational affairs (lit. <strong>kyo o hui tō</strong>)</td>
</tr>
<tr>
<td><strong> kyu </strong></td>
<td>elm.</td>
<td>air (to breathe); gas</td>
</tr>
<tr>
<td><strong> kyu(loa); kyuteth (planetary) </strong></td>
<td>elm.CMP</td>
<td>Atmosphere</td>
</tr>
<tr>
<td><strong> kyu&rsquo;.um&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>humidity (in the sense of mugginess)</td>
</tr>
<tr>
<td><strong> kyu&rsquo;ā&rsquo;e&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>breeze</td>
</tr>
<tr>
<td><strong> kyu&rsquo;ām </strong></td>
<td>elm.CMP</td>
<td>fog; mist</td>
</tr>
<tr>
<td><strong> kyu&rsquo;ām.e&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>high-altitude wind</td>
</tr>
<tr>
<td><strong> kyu&rsquo;kūng.au&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>ice storm</td>
</tr>
<tr>
<td><strong> kyu&rsquo;kūng.au&rsquo;opun </strong></td>
<td>elm.CMP</td>
<td>blizzard</td>
</tr>
<tr>
<td><strong> kyu&rsquo;kūng.yu&rsquo;ā </strong></td>
<td>elm.CMP</td>
<td>windstorm</td>
</tr>
<tr>
<td><strong> kyu&rsquo;kūngchuaipun </strong></td>
<td>elm.CMP</td>
<td>dust storm; sand storm</td>
</tr>
<tr>
<td><strong> kyuk&#8217;ya </strong></td>
<td>elm.CMP</td>
<td>Dogfight (in a planetary atmosphere)</td>
</tr>
<tr>
<td><strong> kyul </strong></td>
<td>elm.</td>
<td>bird; (especially feathered) animal that flies</td>
</tr>
<tr>
<td><strong> kyul.t&rsquo;e&rsquo;ka </strong></td>
<td>elm.</td>
<td>sticky bird (delicacy prepared from the aged meat of kyulkuam bird that has gorged on fruit and died afterbeing stuck on sap for several days)</td>
</tr>
<tr>
<td><strong> kyulkuam </strong></td>
<td>elm.CMP</td>
<td>fruit bird (type of fruit-eating bird used in kyul.t&rsquo;e&rsquo;ka)</td>
</tr>
<tr>
<td><strong> kyun </strong></td>
<td>num.</td>
<td>ten 10</td>
</tr>
<tr>
<td><strong> kyuni&rsquo;pu.ai </strong></td>
<td>num.</td>
<td>thirty 30&hellip;</td>
</tr>
<tr>
<td><strong> kyunisyen </strong></td>
<td>num.</td>
<td>twenty 20</td>
</tr>
<tr>
<td><strong> kyuyoaith </strong></td>
<td>elm.CMP</td>
<td>smog; unhealthy air; unbreathable air</td>
</tr>
<tr>
<td><strong> kyuyoe&rsquo;so </strong></td>
<td>elm.CMP</td>
<td>haze</td>
</tr>
<tr>
<td><strong> L.ao </strong></td>
<td>PN.male</td>
<td>Lao</td>
</tr>
<tr>
<td><strong> l.oa&rsquo;alsāo </strong></td>
<td>elm.CMP</td>
<td>Emergency/Escape Exit</td>
</tr>
<tr>
<td><strong> l.e&rsquo;a </strong></td>
<td>elm.</td>
<td>arm; tentacle; wing of a bird</td>
</tr>
<tr>
<td><strong> l.ea </strong></td>
<td>elm.</td>
<td>feeling (emotional status)</td>
</tr>
<tr>
<td><strong> l.ō </strong></td>
<td>v.REV</td>
<td>be of a class</td>
</tr>
<tr>
<td><strong> l.o&rsquo;a </strong></td>
<td>num.</td>
<td>nine 9</td>
</tr>
<tr>
<td><strong> l.oa </strong></td>
<td>elm.</td>
<td>Door/Portal/Window</td>
</tr>
<tr>
<td><strong> l.oa&rsquo;al </strong></td>
<td>elm.CMP</td>
<td>Exit (as in physical exit)</td>
</tr>
<tr>
<td><strong> l.oach&rsquo;ā&rsquo;e </strong></td>
<td>elm.CMP</td>
<td>Window (if it needs to be referred to formally or specifically)</td>
</tr>
<tr>
<td><strong> l.oal&rsquo;aōng </strong></td>
<td>elm.CMP</td>
<td>Automatic Door</td>
</tr>
<tr>
<td><strong> l.oau&rsquo;ing </strong></td>
<td>elm.CMP</td>
<td>Entrance (as in physical entrance)</td>
</tr>
<tr>
<td><strong> l.uotht&rsquo;ang </strong></td>
<td>elm.CMP</td>
<td>hillside; slope</td>
</tr>
<tr>
<td><strong> L&rsquo;ai </strong></td>
<td>elm.CMP</td>
<td>&ldquo;Boy&rdquo;/Grand-son (endearment term from grandmother to child or adult)</td>
</tr>
<tr>
<td><strong> la </strong></td>
<td>elm.</td>
<td>open</td>
</tr>
<tr>
<td><strong> lā </strong></td>
<td>elm.</td>
<td>art</td>
</tr>
<tr>
<td><strong> la.thl&rsquo;e&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>dry; like salted &amp; cured meat (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> La&rsquo;na </strong></td>
<td>elm.CMP</td>
<td>&ldquo;Girl&rdquo;/Grand-daughter (endearment term from grandmother to child or adult)</td>
</tr>
<tr>
<td><strong> la&rsquo;nua </strong></td>
<td>elm.CMP</td>
<td>grand-daughter</td>
</tr>
<tr>
<td><strong> lain </strong></td>
<td>elm.</td>
<td>cone; conical</td>
</tr>
<tr>
<td><strong> lainchuiyuao </strong></td>
<td>elm.CMP</td>
<td>water spout</td>
</tr>
<tr>
<td><strong> lainpunyuao </strong></td>
<td>elm.CMP</td>
<td>dust devil</td>
</tr>
<tr>
<td><strong> lang&rsquo;yōn </strong></td>
<td>elm.CMP</td>
<td>quasi-grand-child</td>
</tr>
<tr>
<td><strong> lang&rsquo;yōnua </strong></td>
<td>elm.CMP</td>
<td>quasi-grand-daughter</td>
</tr>
<tr>
<td><strong> lang&rsquo;yōnyu </strong></td>
<td>elm.CMP</td>
<td>quasi-grand-son</td>
</tr>
<tr>
<td><strong> lang&rsquo;yu </strong></td>
<td>elm.CMP</td>
<td>grand-son</td>
</tr>
<tr>
<td><strong> lang&rdquo; </strong></td>
<td>elm.</td>
<td>grand-child</td>
</tr>
<tr>
<td><strong> lath </strong></td>
<td>elm.</td>
<td>dry; dessicated</td>
</tr>
<tr>
<td><strong>lāuo&#8217;a</strong></td>
<td>elm.CMP</td>
<td>song</td>
</tr>
<tr>
<td><strong> lē </strong></td>
<td>pn.NEU</td>
<td>you</td>
</tr>
<tr>
<td><strong> le&rsquo;.au&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>ice cap</td>
</tr>
<tr>
<td><strong> le&rsquo;a </strong></td>
<td>num.</td>
<td>six 6</td>
</tr>
<tr>
<td><strong> le&rdquo; </strong></td>
<td>elm.</td>
<td>head (of a body); center (of an activity); central</td>
</tr>
<tr>
<td><strong> len </strong></td>
<td>elm.</td>
<td>peace; peaceful; without issue; smooth</td>
</tr>
<tr>
<td><strong> leth </strong></td>
<td>elm.</td>
<td>speed; fast; quickly</td>
</tr>
<tr>
<td><strong> leth&rsquo;uii </strong></td>
<td>elm.CMP</td>
<td>Lightspeed</td>
</tr>
<tr>
<td><strong> li&#8217;chen </strong></td>
<td>elm.CMP</td>
<td>&ldquo;one&rsquo;s life&rdquo; &#8211; the course of life that a person lives including experiences</td>
</tr>
<tr>
<td><strong> lio </strong></td>
<td>elm.</td>
<td>soft or silky (to the touch), not rough or bristly; smooth (of solid objects)</td>
</tr>
<tr>
<td><strong> li&rsquo;o </strong></td>
<td>elm.</td>
<td>flat; low to the ground</td>
</tr>
<tr>
<td><strong> li&rdquo; </strong></td>
<td>elm.</td>
<td>one&#8217;s path in life; the course of one&#8217;s life</td>
</tr>
<tr>
<td><strong> lo </strong></td>
<td>v.NEU</td>
<td>be of a class</td>
</tr>
<tr>
<td><strong> lo&rsquo;e </strong></td>
<td>rel.</td>
<td>in; into (sense of putting inside or entering)</td>
</tr>
<tr>
<td><strong> loa </strong></td>
<td>elm.</td>
<td>eat; drink; consume; swallow</td>
</tr>
<tr>
<td><strong> long </strong></td>
<td>elm.</td>
<td>melt; unfreeze</td>
</tr>
<tr>
<td><strong> lū&rsquo;.i&rsquo;a </strong></td>
<td>elm.</td>
<td>pray; prayer; entreatment to the supernatural</td>
</tr>
<tr>
<td><strong> thaxiin </strong></td>
<td>elm.CMP</td>
<td>sign; signboard (non-electronic) with written guidance</td>
</tr>
<tr>
<td><strong> lu&rdquo; </strong></td>
<td>elm.</td>
<td>town; medium-sized city</td>
</tr>
<tr>
<td><strong> lua </strong></td>
<td>pn.REV</td>
<td>It (inanimate)</td>
</tr>
<tr>
<td><strong> luai </strong></td>
<td>elm.</td>
<td>alien; foreign; strange</td>
</tr>
<tr>
<td><strong> luam </strong></td>
<td>pn.REV</td>
<td>they (inanimate)</td>
</tr>
<tr>
<td><strong> lue </strong></td>
<td>elm.</td>
<td>relate; relate to; be realated to; connect; relationship; connection</td>
</tr>
<tr>
<td><strong> lui </strong></td>
<td>elm.</td>
<td>knife; cut; slice</td>
</tr>
<tr>
<td><strong> lui&rsquo;tu </strong></td>
<td>elm.CMP</td>
<td>Dagger</td>
</tr>
<tr>
<td><strong> luiken </strong></td>
<td>elm.CMP</td>
<td>Sword</td>
</tr>
<tr>
<td><strong> lūl </strong></td>
<td>col.</td>
<td>ianthine</td>
</tr>
<tr>
<td><strong> lung </strong></td>
<td>elm.</td>
<td>guess; estimate; approximate; roughly; more-or-less</td>
</tr>
<tr>
<td><strong> luoth </strong></td>
<td>elm.</td>
<td>slope; angle</td>
</tr>
<tr>
<td><strong> luoth.au&rsquo;o&rsquo;rath </strong></td>
<td>elm.CMP</td>
<td>avalanche</td>
</tr>
<tr>
<td><strong> Lyā </strong></td>
<td>line</td>
<td>Lyaa</td>
</tr>
<tr>
<td><strong> lye </strong></td>
<td>rel.</td>
<td>targeting; focusing on (from <strong>lye&rsquo;lye</strong>)</td>
</tr>
<tr>
<td><strong> lye&rsquo;lye </strong></td>
<td>elm.</td>
<td>direct; direcly; directness; n. &ldquo;arrow&rdquo; alyelye</td>
</tr>
<tr>
<td><strong> lye&rsquo;p.ānp&rsquo;uāng </strong></td>
<td>elm.CMP</td>
<td>Torpedoes</td>
</tr>
<tr>
<td><strong> lye&rsquo;pānhung; lye&rsquo;hung </strong></td>
<td>elm.CMP</td>
<td>Missiles</td>
</tr>
<tr>
<td><strong> lye&rsquo;pānri; lye&rsquo;ri </strong></td>
<td>elm.CMP</td>
<td>Rockets</td>
</tr>
<tr>
<td><strong> lyii </strong></td>
<td>num.</td>
<td>hundred 100</td>
</tr>
<tr>
<td><strong> lyon </strong></td>
<td>elm.</td>
<td>advice; counsel; recommendation (when asked); analysis</td>
</tr>
<tr>
<td><strong> m.a </strong></td>
<td>pn.SRV</td>
<td>he/she</td>
</tr>
<tr>
<td><strong> m..aman&rdquo; </strong></td>
<td>slng.SRV</td>
<td>&ldquo;crazy like a human&rdquo; (positive connotation when having a good time)</td>
</tr>
<tr>
<td><strong> m.an </strong></td>
<td>pn.SRV</td>
<td>they</td>
</tr>
<tr>
<td><strong> m.e&rsquo;a </strong></td>
<td>elm.</td>
<td>high (above ground); elevated; towering</td>
</tr>
<tr>
<td><strong> m.oa </strong></td>
<td>elm.</td>
<td>all, whole, entirety; complete</td>
</tr>
<tr>
<td><strong> m.oat&rsquo;en </strong></td>
<td>elm.CMP</td>
<td>almost all; almost to the last</td>
</tr>
<tr>
<td><strong> m.ue </strong></td>
<td>elm.</td>
<td>method</td>
</tr>
<tr>
<td><strong> m.ueh&rsquo;ual </strong></td>
<td>elm.CMP</td>
<td>any way</td>
</tr>
<tr>
<td><strong> m.uexy.oa </strong></td>
<td>Q.</td>
<td>how (which method)?</td>
</tr>
<tr>
<td><strong> m.ūng </strong></td>
<td>elm.</td>
<td>sadness; gloom; depression</td>
</tr>
<tr>
<td><strong> ma. </strong></td>
<td>nlz.CLTC</td>
<td>[animal; creature (incablabe of communication with people)]</td>
</tr>
<tr>
<td><strong> ma&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>animal (generic term); fauna (juxtaposed to flora)</td>
</tr>
<tr>
<td><strong> ma&rsquo;kr.ōng </strong></td>
<td>elm.CMP</td>
<td>monster; &ldquo;demon&rdquo;</td>
</tr>
<tr>
<td><strong> ma&rsquo;ma </strong></td>
<td>slng.SRV</td>
<td>&ldquo;beast, monster&rdquo; (a person behavng like an animal; out of her/his mind)</td>
</tr>
<tr>
<td><strong> ma&rsquo;nāng </strong></td>
<td>elm.CMP</td>
<td>predator; carniverous animal</td>
</tr>
<tr>
<td><strong> mā&rsquo;nga </strong></td>
<td>elm.</td>
<td>struggle; challenge</td>
</tr>
<tr>
<td><strong> ma&rsquo;tok.yāi </strong></td>
<td>n.</td>
<td>tokyai. Arboreal apex predator native to and endangered on the Xi&rsquo;an world Xi; now conserved and flourishing on Koli. Feeds on smaller herbivorous forest creatures.</td>
</tr>
<tr>
<td><strong> ma&rsquo;tu </strong></td>
<td>elm.CMP</td>
<td>predator</td>
</tr>
<tr>
<td><strong> ma&rsquo;xy.un </strong></td>
<td>n.</td>
<td>shoon. Xi&rsquo;an domesticated yak-like beast valued for its silken fur.</td>
</tr>
<tr>
<td><strong> makyul </strong></td>
<td>elm.CMP</td>
<td>flying mammals, pteradons, etc.</td>
</tr>
<tr>
<td><strong> mām </strong></td>
<td>elm.</td>
<td>rich; hearty; full; robust</td>
</tr>
<tr>
<td><strong> mam&rsquo;pa </strong></td>
<td>n.</td>
<td>fat bear (racoon-like animal harvested for its fat)</td>
</tr>
<tr>
<td><strong> mang&rsquo;huen </strong></td>
<td>elm.CMP</td>
<td>serving ladels</td>
</tr>
<tr>
<td><strong> mang&rsquo;tām uoth&rsquo;tōm </strong></td>
<td>idm.</td>
<td>&#8220;Empty &#8216;bowl&#8217;, full belly&#8221; &#8211; traditonal phrase at the ending of a Xi&rsquo;an meal to thank the cook or host.</td>
</tr>
<tr>
<td><strong> mang&rdquo; </strong></td>
<td>elm.</td>
<td>plate; bowl; cup (the primary piece of Xi&rsquo;an tableware)</td>
</tr>
<tr>
<td><strong> maloa </strong></td>
<td>elm.CMP</td>
<td>prey</td>
</tr>
<tr>
<td><strong> mangel </strong></td>
<td>elm.CMP</td>
<td>amphibian</td>
</tr>
<tr>
<td><strong> maten </strong></td>
<td>elm.CMP</td>
<td>meat; animal parts eaten as food; animal protein</td>
</tr>
<tr>
<td><strong> maxyiing </strong></td>
<td>elm.CMP</td>
<td>wild animal; beast; monster; monsterous</td>
</tr>
<tr>
<td><strong> mē&rsquo;o </strong></td>
<td>n.</td>
<td>mayo; mayonnaise (borrowed from English &laquo;mayo&raquo;)</td>
</tr>
<tr>
<td><strong> men </strong></td>
<td>elm.</td>
<td>juvenile cousin, niece or nephew (of an adult)</td>
</tr>
<tr>
<td><strong> mi&rsquo;n.iT&rsquo;yūm </strong></td>
<td>elm.CMP</td>
<td>a standard Human minute (lit. <strong>mi&rsquo;nit&acirc; se Hyū&rsquo;m&acirc;n</strong> &ndash; borrowed from <span class="caps">UEE</span> Standard)</td>
</tr>
<tr>
<td><strong> mi&rsquo;so </strong></td>
<td>n.</td>
<td>miso (borrowed from Japanese &laquo;miso&raquo;)</td>
</tr>
<tr>
<td><strong> mo </strong></td>
<td>vcp.</td>
<td>[presumptive (&ldquo;seeming&rdquo;/&ldquo;apparent&rdquo;]</td>
</tr>
<tr>
<td><strong> mo </strong></td>
<td>elm.</td>
<td>appearance; seem; seems (<span class="caps">VCP</span>)</td>
</tr>
<tr>
<td><strong> mo&rsquo;u </strong></td>
<td>v.LAUD</td>
<td>try/attempt (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> mu&rsquo;.a&rsquo;ōng </strong></td>
<td>elm.CMP</td>
<td>indulgence; guilty pleasure</td>
</tr>
<tr>
<td><strong> mu&rsquo;a </strong></td>
<td>elm.</td>
<td>pleasure; delight</td>
</tr>
<tr>
<td><strong> mu&rsquo;la </strong></td>
<td>n.</td>
<td>round fruit that grows in marshland and is a source of food for the Ngii</td>
</tr>
<tr>
<td><strong> mua </strong></td>
<td>elm.</td>
<td>small town; village</td>
</tr>
<tr>
<td><strong> muakahyao </strong></td>
<td>elm.CMP</td>
<td>Space Station</td>
</tr>
<tr>
<td><strong> mui </strong></td>
<td>elm.</td>
<td>preserve; conserve; set aside; save (for later)</td>
</tr>
<tr>
<td><strong> my.ū </strong></td>
<td>elm.</td>
<td>aunt (mother&#8217;s older sister when elder)</td>
</tr>
<tr>
<td><strong> n.āng </strong></td>
<td>elm.</td>
<td>prowl; stalk; hunt</td>
</tr>
<tr>
<td><strong> mya </strong></td>
<td>elm.</td>
<td>clean; untained; cleanliness</td>
</tr>
<tr>
<td><strong> myā </strong></td>
<td>vcp.</td>
<td>[firm imperative] <strong>myāl</strong></td>
</tr>
<tr>
<td><strong> myii&rsquo;sa </strong></td>
<td>elm.</td>
<td>yawn; yawning; displaying exhaustion</td>
</tr>
<tr>
<td><strong> myu </strong></td>
<td>elm.</td>
<td>aunt (mother&rsquo;s or grandmother&rsquo;s older sister)</td>
</tr>
<tr>
<td><strong> n.ao </strong></td>
<td>elm.</td>
<td>tint; color</td>
</tr>
<tr>
<td><strong> n.eng </strong></td>
<td>elm.CMP</td>
<td>visit; travel to</td>
</tr>
<tr>
<td><strong> N.il&rsquo;ē </strong></td>
<td>PN.feml</td>
<td>Niley</td>
</tr>
<tr>
<td><strong> nā </strong></td>
<td>v.FAM</td>
<td>want/desire (<strong>&rsaquo;&rsaquo;&rsaquo; yo _____</strong>)</td>
</tr>
<tr>
<td><strong> na&rsquo;to </strong></td>
<td>n.</td>
<td>natto (borrowed from Japanese &laquo;natto&raquo; )</td>
</tr>
<tr>
<td><strong> na&rdquo; </strong></td>
<td>vcp.</td>
<td>[interrogative]</td>
</tr>
<tr>
<td><strong> nai </strong></td>
<td>elm.</td>
<td>grasp; perception; understanding; having caught soemthing (said or presented visually))</td>
</tr>
<tr>
<td><strong> nai&rsquo;an </strong></td>
<td>rel.</td>
<td>in exchange for</td>
</tr>
<tr>
<td><strong> Nai&rsquo;na </strong></td>
<td>name</td>
<td>&ldquo;Sweetie&rdquo; (to a female from a male or female)</td>
</tr>
<tr>
<td><strong> nai&rsquo;yeth </strong></td>
<td>elm.CMP</td>
<td>knowledge and understanding (knowing grasp)</td>
</tr>
<tr>
<td><strong> naihuo </strong></td>
<td>elm.CMP</td>
<td>having heard something; catching something by hearing it</td>
</tr>
<tr>
<td><strong> nāl </strong></td>
<td>elm.</td>
<td>piloting (in 3D space)</td>
</tr>
<tr>
<td><strong> nāl </strong></td>
<td>elm.</td>
<td>piloting; flying (in 3D space)</td>
</tr>
<tr>
<td><strong> nān&rsquo;yo </strong></td>
<td>n.</td>
<td>lizard-class of reptiles</td>
</tr>
<tr>
<td><strong> ne&rsquo;a </strong></td>
<td>rel.</td>
<td>left of; on the left of; toward the left</td>
</tr>
<tr>
<td><strong> Nē&rdquo; </strong></td>
<td>PN.feml</td>
<td>Nay</td>
</tr>
<tr>
<td><strong> Ng.ām </strong></td>
<td>PN.male</td>
<td>Ngaam</td>
</tr>
<tr>
<td><strong> ng.au&rsquo;ii </strong></td>
<td>elm.CMP</td>
<td>leaf (of flora)</td>
</tr>
<tr>
<td><strong> nga.u&rsquo;ii&rsquo;yēl </strong></td>
<td>elm.CMP</td>
<td>noodle leaf (cultivated leaf that can easily be torn into strips. Used in traditional dish uea&rsquo;yēl.)</td>
</tr>
<tr>
<td><strong> ngā&rsquo;l.o </strong></td>
<td>elm.</td>
<td>honor; respect (external (between parties))</td>
</tr>
<tr>
<td><strong> ngao </strong></td>
<td>elm.</td>
<td>collect; absorb; internalize (information (in the sense of remembering what&#8217;s been learned))</td>
</tr>
<tr>
<td><strong> manuiten </strong></td>
<td>elm.CMP</td>
<td>livestock (fauna cultivated/farmed for the purpose of becoming food)</td>
</tr>
<tr>
<td><strong> ngaochui </strong></td>
<td>elm.CMP</td>
<td>root</td>
</tr>
<tr>
<td><strong> ngea </strong></td>
<td>elm.</td>
<td>preliminary; pre-; underdeveloped stage of growth</td>
</tr>
<tr>
<td><strong> ngel </strong></td>
<td>elm.</td>
<td>fish; animal that breathes water (via gills or other such organs)</td>
</tr>
<tr>
<td><strong> ngel e lu&rsquo;te </strong></td>
<td>idm.</td>
<td>lutefisk (borrowed from Norwegian &laquo;lutefisk&raquo;)</td>
</tr>
<tr>
<td><strong> ngeltui </strong></td>
<td>elm.CMP</td>
<td>fermented fish (one of any variety of fish-based meals that have been fermented over months. Can have a wide variety of base flavors)</td>
</tr>
<tr>
<td><strong> ngi </strong></td>
<td>elm.</td>
<td>essence; core; central concept; constitution; crux</td>
</tr>
<tr>
<td><strong> ngi. </strong></td>
<td>nlz.CLTC</td>
<td>[&ldquo;-ness&rdquo;/&ldquo;-ment&rdquo;/&ldquo;-cy&rdquo;]; essence of X</td>
</tr>
<tr>
<td><strong> ngi&rsquo;kr.ōng </strong></td>
<td>elm.CMP</td>
<td>depravity; wickedness</td>
</tr>
<tr>
<td><strong> ngi&rsquo;pi </strong></td>
<td>elm.</td>
<td>itching; buzzing; pain (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> ngi&rsquo;yēl </strong></td>
<td>elm.CMP</td>
<td>fibrous; stringy; like chewing on a leaf or eating coconut (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> ngia.u&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>frozen; icy (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> ngii </strong></td>
<td>n.</td>
<td>yengi. Xi&rsquo;an domesticated pet that natively keeps vermin populations down. Nickname, <strong>yao&rsquo;yao</strong> (based on the animal&rsquo;s vocalizations)</td>
</tr>
<tr>
<td><strong> ngilen </strong></td>
<td>elm.CMP</td>
<td>peaceful; peace-centric; peace&ldquo;loving&rdquo;</td>
</tr>
<tr>
<td><strong> nginguichui </strong></td>
<td>elm.CMP</td>
<td>milky; creamy; like fresh animal milk (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> ngisath </strong></td>
<td>elm.CMP</td>
<td>style; aesthetics; the way something is designed</td>
</tr>
<tr>
<td><strong> ngiti </strong></td>
<td>elm.CMP</td>
<td>useful; utilitarian; functional</td>
</tr>
<tr>
<td><strong> ngiton </strong></td>
<td>elm.CMP</td>
<td>full of nourishement; nourishing; energizing</td>
</tr>
<tr>
<td><strong> ngitonten </strong></td>
<td>elm.CMP</td>
<td>nutritious (specifically of food); also often simply ngiton.</td>
</tr>
<tr>
<td><strong> ngi&#8217;u.in&#8217;a </strong></td>
<td>elm.CMP</td>
<td>freedom; the essense of being free, unfettered, unbound</td>
</tr>
<tr>
<td><strong> ngixuthle&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>dedication (to an effort or cause); effort</td>
</tr>
<tr>
<td><strong> ngo </strong></td>
<td>elm.</td>
<td>sweet, as in the sense of a gesture made by a child or a pet animal</td>
</tr>
<tr>
<td><strong> ngua </strong></td>
<td>elm.</td>
<td>sex; sexuality; sensual; physical pleaure from intimate contact</td>
</tr>
<tr>
<td><strong> ngui </strong></td>
<td>elm.</td>
<td>albumen; milk (of mammals); liquid protein</td>
</tr>
<tr>
<td><strong> ngui (nguita&rsquo;a) </strong></td>
<td>elm.CMP</td>
<td>egg white</td>
</tr>
<tr>
<td><strong> ngum </strong></td>
<td>elm.</td>
<td>mold; rot</td>
</tr>
<tr>
<td><strong> ngumpuāng </strong></td>
<td>elm.CMP</td>
<td>earthy; moldy; pungent (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> nguok </strong></td>
<td>n.</td>
<td>eel whale (animal with high levels of urea that is farmed on most developed Xi&#8217;an worlds)</td>
</tr>
<tr>
<td><strong> ngya </strong></td>
<td>vcp.</td>
<td>[subjunctive (&ldquo;if&ldquo;)] <strong>ngyal</strong> (often followed by <strong>.ath&rsquo;a</strong>)</td>
</tr>
<tr>
<td><strong> ngya </strong></td>
<td>elm.</td>
<td>ambiguity</td>
</tr>
<tr>
<td><strong> ngyai </strong></td>
<td>elm.</td>
<td>search (for something); seek out</td>
</tr>
<tr>
<td><strong> ni </strong></td>
<td>elm.</td>
<td>biological child (daughter (<strong>ni&rsquo;nua</strong>) or son (<strong>ni&rsquo;yu</strong>))</td>
</tr>
<tr>
<td><strong> ni&rsquo;nua </strong></td>
<td>elm.CMP</td>
<td>biological daughter</td>
</tr>
<tr>
<td><strong> ni&rsquo;yu </strong></td>
<td>elm.CMP</td>
<td>biological son</td>
</tr>
<tr>
<td><strong> nii </strong></td>
<td>elm.</td>
<td>just; only; limit</td>
</tr>
<tr>
<td><strong> niichā&rsquo;e </strong></td>
<td>elm.CMP</td>
<td>horizon</td>
</tr>
<tr>
<td><strong> ning </strong></td>
<td>rel.</td>
<td>against; opposing (as in battle or negotiations)</td>
</tr>
<tr>
<td><strong> no </strong></td>
<td>elm.</td>
<td>hand</td>
</tr>
<tr>
<td><strong> nō </strong></td>
<td>elm.</td>
<td>detail; precision</td>
</tr>
<tr>
<td><strong> no&rsquo;a </strong></td>
<td>pn.NEU</td>
<td>I</td>
</tr>
<tr>
<td><strong> no&rsquo;e </strong></td>
<td>elm.</td>
<td>gender; sex; sexual differentiation</td>
</tr>
<tr>
<td><strong> noklo </strong></td>
<td>elm.CMP</td>
<td>foot; hoof</td>
</tr>
<tr>
<td><strong> noth </strong></td>
<td>vcp.</td>
<td>[reccomendational (&ldquo;suggestion to do X&rdquo; (to someone else) from <strong>noth</strong>, suggestion)]</td>
</tr>
<tr>
<td><strong> nu </strong></td>
<td>elm.</td>
<td>form; shape; in the form of; in the likeness of</td>
</tr>
<tr>
<td><strong> nū </strong></td>
<td>pn.SRV</td>
<td>I</td>
</tr>
<tr>
<td><strong> nu&rsquo;a </strong></td>
<td>elm.</td>
<td>fresh dead meat ready for consumption</td>
</tr>
<tr>
<td><strong> nu&rsquo;a e nya&rsquo;to </strong></td>
<td>idm.</td>
<td>food that has been killed prematurely</td>
</tr>
<tr>
<td><strong> nu&rsquo;a.thl&rsquo;e&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>food that has died naturally</td>
</tr>
<tr>
<td><strong> nu&rsquo;axy.uai </strong></td>
<td>elm.CMP</td>
<td>meat dishes composed of exotic ingredients</td>
</tr>
<tr>
<td><strong> nua </strong></td>
<td>elm.</td>
<td>female</td>
</tr>
<tr>
<td><strong> nua.yii&rdquo; </strong></td>
<td>elm.</td>
<td>mother (clinical term)</td>
</tr>
<tr>
<td><strong> nua.yii&rdquo; </strong></td>
<td>elm.CMP</td>
<td>biological mother, clinical term</td>
</tr>
<tr>
<td><strong> Nua&rsquo;n.ā </strong></td>
<td>name</td>
<td>Mother (reverential)</td>
</tr>
<tr>
<td><strong> Nua&rsquo;n.ā </strong></td>
<td>name</td>
<td>Mother &#8211; The polite &amp; reverant word for another&rsquo;s mother or one&rsquo;s own</td>
</tr>
<tr>
<td><strong> Nuana </strong></td>
<td>name</td>
<td>Mom (post-Service)</td>
</tr>
<tr>
<td><strong> Nuana </strong></td>
<td>name</td>
<td>Mom &#8211; what adults call their mothers affectionately</td>
</tr>
<tr>
<td><strong> nuang </strong></td>
<td>cnj.</td>
<td>nui + ang (<strong>&ldquo;in order to&rdquo;</strong>)</td>
</tr>
<tr>
<td><strong> nuate&rsquo;.ah&rsquo;a </strong></td>
<td>n.</td>
<td>hot woman; babe; belle</td>
</tr>
<tr>
<td><strong> Nuaxyii&rsquo;ua </strong></td>
<td>PN.role</td>
<td>Matriarch</td>
</tr>
<tr>
<td><strong> nui </strong></td>
<td>rel.</td>
<td>for; toward</td>
</tr>
<tr>
<td><strong> nuika&rsquo;lye </strong></td>
<td>cnj.</td>
<td>in order that</td>
</tr>
<tr>
<td><strong> nūn </strong></td>
<td>col.</td>
<td>luteous</td>
</tr>
<tr>
<td><strong> ny.as&rsquo;eyo&rdquo; </strong></td>
<td>PN.role</td>
<td><span class="caps">EMS</span></td>
</tr>
<tr>
<td><strong> nya </strong></td>
<td>elm.</td>
<td>person</td>
</tr>
<tr>
<td><strong> nya. </strong></td>
<td>nlz.CLTC</td>
<td>[person who does X; &ldquo;-er&rdquo;]</td>
</tr>
<tr>
<td><strong> nya.li&rdquo; </strong></td>
<td>PN.role</td>
<td>clergy</td>
</tr>
<tr>
<td><strong> nya&rsquo;h.ūn </strong></td>
<td>PN.role</td>
<td>laborer</td>
</tr>
<tr>
<td><strong> nyā&rsquo;i </strong></td>
<td>elm.CMP</td>
<td>spouse</td>
</tr>
<tr>
<td><strong> nya&rsquo;kr.ōng </strong></td>
<td>elm.CMP</td>
<td>barbarian; degenrate; criminal guilty of unspeakable acts</td>
</tr>
<tr>
<td><strong> nya&rsquo;m.oa </strong></td>
<td>PN.role</td>
<td>philosopher</td>
</tr>
<tr>
<td><strong> nya&rsquo;n.āngk&rsquo;uāo </strong></td>
<td>PN.role</td>
<td>pirate; robber (also <strong>n.āngk&rsquo;uāo, o n.āngk&rsquo;uāo</strong>: loot, pilfer)</td>
</tr>
<tr>
<td><strong> nya&rsquo;n.eng </strong></td>
<td>elm.</td>
<td>visitor; guest</td>
</tr>
<tr>
<td><strong> nya&rsquo;nāng </strong></td>
<td>PN.role</td>
<td>hunter</td>
</tr>
<tr>
<td><strong> nya&rsquo;p.ū </strong></td>
<td>PN.role</td>
<td>politician</td>
</tr>
<tr>
<td><strong> nya&rsquo;p.ūh&rsquo;uesao </strong></td>
<td>PN.role</td>
<td>diplomat</td>
</tr>
<tr>
<td><strong> nya&rsquo;s.āth </strong></td>
<td>elm.CMP.for</td>
<td>&ldquo;your people&rdquo; (contraction of <strong>nya se s.āth</strong>) <span class="caps">FORMAL</span></td>
</tr>
<tr>
<td><strong> nya&rsquo;t.ōng </strong></td>
<td>PN.role</td>
<td>caregiver</td>
</tr>
<tr>
<td><strong> nya&rsquo;t.ōng&bull;&rsquo;o </strong></td>
<td>PN.role</td>
<td>supervisor; manager; director (of programs or processes)</td>
</tr>
<tr>
<td><strong> nya&rsquo;t.ōngn&rsquo;ya </strong></td>
<td>PN.role</td>
<td>supervisor; manager; director (of people)</td>
</tr>
<tr>
<td><strong> nya&rsquo;t.ōngya </strong></td>
<td>PN.role</td>
<td>(legitimate professional certified) bodyguard</td>
</tr>
<tr>
<td><strong> nya&rsquo;t.ot&rsquo;en </strong></td>
<td>PN.role</td>
<td>farmer</td>
</tr>
<tr>
<td><strong> nya&rsquo;t.oy&rsquo;an </strong></td>
<td>PN.role</td>
<td>teacher</td>
</tr>
<tr>
<td><strong> nya&rsquo;tye </strong></td>
<td>elm.CMP</td>
<td>thief; pirate</td>
</tr>
<tr>
<td><strong> nya&rsquo;xy.oa </strong></td>
<td>Q.</td>
<td>who?</td>
</tr>
<tr>
<td><strong> nya&bull;o.se&rdquo; </strong></td>
<td>PN.role</td>
<td>assistant</td>
</tr>
<tr>
<td><strong> nya&bull;oa </strong></td>
<td>PN.role</td>
<td>programmer/computation engineer</td>
</tr>
<tr>
<td><strong> nya&bull;osen&rsquo;p.u </strong></td>
<td>PN.role</td>
<td>promoter (advertiser, marketer, etc.)</td>
</tr>
<tr>
<td><strong> nya&bull;oten </strong></td>
<td>PN.role</td>
<td>cook</td>
</tr>
<tr>
<td><strong> nya&bull;otō </strong></td>
<td>PN.role</td>
<td>financial person</td>
</tr>
<tr>
<td><strong> nyaāluo&#8217;a </strong></td>
<td>PN.role</td>
<td>Xi&#8217;an &#8220;opera&#8221; singer</td>
</tr>
<tr>
<td><strong> nyachai </strong></td>
<td>PN.role</td>
<td>technician</td>
</tr>
<tr>
<td><strong> nyahai </strong></td>
<td>elm.CMP</td>
<td>friend; trusted ally</td>
</tr>
<tr>
<td><strong> nyahaipāng </strong></td>
<td>elm.</td>
<td>trusted intimate parter; lover (<strong>haipāng</strong> colloqially)</td>
</tr>
<tr>
<td><strong> nyahual </strong></td>
<td>elm.CMP</td>
<td>anyone (any person)</td>
</tr>
<tr>
<td><strong> nyahuitia </strong></td>
<td>PN.role</td>
<td>mathematician</td>
</tr>
<tr>
<td><strong> nyahyan </strong></td>
<td>elm.CMP</td>
<td>everyone</td>
</tr>
<tr>
<td><strong> nyāi&rsquo;na </strong></td>
<td>elm.CMP</td>
<td>wife</td>
</tr>
<tr>
<td><strong> nyāi&rsquo;ny.ū </strong></td>
<td>elm.CMP</td>
<td>&ldquo;Son in Law&rdquo; of biological son</td>
</tr>
<tr>
<td><strong> nyāi&rsquo;nyaiyu </strong></td>
<td>elm.CMP</td>
<td>&ldquo;Son in Law&rdquo; of biological daughter</td>
</tr>
<tr>
<td><strong> nyāi&rsquo;nyana </strong></td>
<td>elm.CMP</td>
<td>&ldquo;Daugher in Law&rdquo; of biological daughter</td>
</tr>
<tr>
<td><strong> nyāi&rsquo;nyuna </strong></td>
<td>elm.CMP</td>
<td>&ldquo;Daugher in Law&rdquo; of bioligical son</td>
</tr>
<tr>
<td><strong> nyāi&rsquo;yu </strong></td>
<td>elm.CMP</td>
<td>husband</td>
</tr>
<tr>
<td><strong> nyalā </strong></td>
<td>PN.role</td>
<td>artist</td>
</tr>
<tr>
<td><strong> nyalāuo’a </strong></td>
<td>PN.role</td>
<td>singer</td>
</tr>
<tr>
<td><strong> nyanāl </strong></td>
<td>PN.role</td>
<td>pilot</td>
</tr>
<tr>
<td><strong> nyapōnghyi </strong></td>
<td>PN.role</td>
<td>augur (professional mating advisor)</td>
</tr>
<tr>
<td><strong> nyarai </strong></td>
<td>PN.role</td>
<td>hauler</td>
</tr>
<tr>
<td><strong> nyasaotō </strong></td>
<td>PN.role</td>
<td>business person</td>
</tr>
<tr>
<td><strong> nyasath </strong></td>
<td>PN.role</td>
<td>designer</td>
</tr>
<tr>
<td><strong> nyasathtā </strong></td>
<td>PN.role</td>
<td>architect</td>
</tr>
<tr>
<td><strong> nyasēng </strong></td>
<td>PN.role</td>
<td>police</td>
</tr>
<tr>
<td><strong> nyaten&rsquo;xyuai </strong></td>
<td>elm.CMP</td>
<td>gourmand; cuisine consultant; menu consultant (for extravagant meals)</td>
</tr>
<tr>
<td><strong> nyatiing </strong></td>
<td>PN.role</td>
<td>doctor/medic (non-emergency)</td>
</tr>
<tr>
<td><strong> nyatyung </strong></td>
<td>PN.role</td>
<td>lawyer</td>
</tr>
<tr>
<td><strong> nyaxiin </strong></td>
<td>PN.role</td>
<td>writer</td>
</tr>
<tr>
<td><strong> nyaxyiing </strong></td>
<td>elm.CMP</td>
<td>wild person; barbarian; slang for &lsquo;pirate&rsquo;</td>
</tr>
<tr>
<td><strong> nyaxyo </strong></td>
<td>PN.role</td>
<td>home-keeper (staff member of an estate)</td>
</tr>
<tr>
<td><strong> nyayā&rsquo;suith </strong></td>
<td>PN.role</td>
<td>terrorist; bully</td>
</tr>
<tr>
<td><strong> nyayan </strong></td>
<td>PN.role</td>
<td>student</td>
</tr>
<tr>
<td><strong> nyayan&rsquo;u.ii </strong></td>
<td>PN.role</td>
<td>scientist</td>
</tr>
<tr>
<td><strong> nyayan&bull;uo&rsquo;a </strong></td>
<td>PN.role</td>
<td>linguist</td>
</tr>
<tr>
<td><strong> Nyii&rsquo;ni </strong></td>
<td>name</td>
<td>Mommy (pre-Service)</td>
</tr>
<tr>
<td><strong> Nyii&rsquo;ni </strong></td>
<td>name</td>
<td>Mommy &#8211; what small children call their mothers</td>
</tr>
<tr>
<td><strong> nyo.āng&rdquo; </strong></td>
<td>pn.REV</td>
<td>we (exclusive)</td>
</tr>
<tr>
<td><strong> nyo.uē&rdquo; </strong></td>
<td>pn.REV</td>
<td>We (inclusive)</td>
</tr>
<tr>
<td><strong> yue&rsquo;soryā </strong></td>
<td>elm.CMP</td>
<td>savory bacteria (ultimately derived from yo&rdquo;e&#8217;so + ryā, but phonologically distinct) (used to make savory seasoning for meals)</td>
</tr>
<tr>
<td><strong> nyo.uēm&rdquo; </strong></td>
<td>pn.REV.for</td>
<td>&ldquo;All of us&rdquo; (<span class="caps">FORMAL</span>)</td>
</tr>
<tr>
<td><strong> nyo&rsquo;a </strong></td>
<td>pn.REV</td>
<td>I</td>
</tr>
<tr>
<td><strong> Nyū&rsquo;nu </strong></td>
<td>name</td>
<td>&ldquo;Darling&rdquo; (to a male from a female)</td>
</tr>
<tr>
<td><strong> nyun </strong></td>
<td>elm.</td>
<td>room; chamber</td>
</tr>
<tr>
<td><strong> nyun&rsquo;y.ānghy&rsquo;i </strong></td>
<td>elm.CMP</td>
<td>Officer/Dignitary&#8217;s Quarters</td>
</tr>
<tr>
<td><strong> nyun&rsquo;y.āngt&#8217;ung </strong></td>
<td>elm.CMP</td>
<td>Crew Quarters</td>
</tr>
<tr>
<td><strong> nyun&rsquo;y.āngu&rsquo;ao </strong></td>
<td>elm.CMP</td>
<td>Captain&#8217;s Quarters</td>
</tr>
<tr>
<td><strong> nyun&rsquo;yāng </strong></td>
<td>elm.CMP</td>
<td>Quarters (personal assigned living/sleeping cabin on a ship)</td>
</tr>
<tr>
<td><strong> nyun&rsquo;yanrath </strong></td>
<td>elm.CMP</td>
<td>Elevator (signage word)</td>
</tr>
<tr>
<td><strong> nyuntui </strong></td>
<td>elm.CMP</td>
<td>fermentation chamber; food prep room; &#8220;kitchen&#8221; (area where food ferments or ages)</td>
</tr>
<tr>
<td><strong> nyuntuing </strong></td>
<td>elm.CMP</td>
<td>cooling closet (a room used to cool food to cave-like temperatures)</td>
</tr>
<tr>
<td><strong> o </strong></td>
<td>v.NEU</td>
<td>do</td>
</tr>
<tr>
<td><strong> o lo&rsquo;.ep&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>Reload (as in a weapon)</td>
</tr>
<tr>
<td><strong> o p.ān&rsquo;al </strong></td>
<td>elm.CMP</td>
<td>Eject</td>
</tr>
<tr>
<td><strong> o ta&rsquo;kya </strong></td>
<td>idm.</td>
<td>get drunk; get high; get wasted</td>
</tr>
<tr>
<td><strong> o ten </strong></td>
<td>idm.</td>
<td>&#8220;cook&#8221;; cooking (via aging or fermentation, not by applied heat)</td>
</tr>
<tr>
<td><strong> o tengea </strong></td>
<td>idm.</td>
<td>pre-&#8220;cook&#8221;; maintain all of the elements of a Xi&rsquo;an larder/pantry/fermentation cave</td>
</tr>
<tr>
<td><strong> ō&rsquo;nu </strong></td>
<td>elm.</td>
<td>greater; larger; enclosing; superior; umbrella; encompasing</td>
</tr>
<tr>
<td><strong> o&rsquo;s.o&rsquo;e </strong></td>
<td>elm.CMP</td>
<td>engagement; interaction</td>
</tr>
<tr>
<td><strong> o&rdquo; </strong></td>
<td>elm.</td>
<td>order; sequence (ordinal number marker, eg. <strong>y.ath&rsquo;o</strong> = first)</td>
</tr>
<tr>
<td><strong> oa </strong></td>
<td>elm.</td>
<td>information</td>
</tr>
<tr>
<td><strong> oe </strong></td>
<td>elm.</td>
<td>close (as in close the door)</td>
</tr>
<tr>
<td><strong> okuaichyo&rsquo;a </strong></td>
<td>cnj.</td>
<td>however; &ldquo;that having been just said&rdquo;</td>
</tr>
<tr>
<td><strong> ōm </strong></td>
<td>elm.</td>
<td>magnetism; magnet; magnetic; something magnetized</td>
</tr>
<tr>
<td><strong> ōng </strong></td>
<td>elm.</td>
<td>the self; reflexive</td>
</tr>
<tr>
<td><strong> p.ān </strong></td>
<td>elm.</td>
<td>explode; &ldquo;boom&rdquo;; &ldquo;bang&rdquo;</td>
</tr>
<tr>
<td><strong> p.ān.ām </strong></td>
<td>elm.CMP</td>
<td>thunder</td>
</tr>
<tr>
<td><strong> p.ap&rsquo;a </strong></td>
<td>elm.</td>
<td>sameness</td>
</tr>
<tr>
<td><strong> p.i&rsquo;t&rsquo;an </strong></td>
<td>n.</td>
<td>Century Egg (borrowed from Mandarin &laquo;p&iacute;d&agrave;n&raquo;)</td>
</tr>
<tr>
<td><strong> p.oa&rsquo;u </strong></td>
<td>pn.</td>
<td>this (idea; situation, condition)</td>
</tr>
<tr>
<td><strong> p.u </strong></td>
<td>elm.</td>
<td>good</td>
</tr>
<tr>
<td><strong> p.ū </strong></td>
<td>elm.</td>
<td>politics; government (administrators)</td>
</tr>
<tr>
<td><strong> p.uai </strong></td>
<td>num.</td>
<td>three 3</td>
</tr>
<tr>
<td><strong> p.uan&rsquo;i </strong></td>
<td>rel.</td>
<td>touching or attached to the underside of</td>
</tr>
<tr>
<td><strong> p.uay&rsquo;a </strong></td>
<td>elm.</td>
<td>hot (of tempearature)</td>
</tr>
<tr>
<td><strong> p.ue&rsquo;o </strong></td>
<td>pn.</td>
<td>that (idea; situation, condition)</td>
</tr>
<tr>
<td><strong> p.ui&rsquo;a </strong></td>
<td>pn.</td>
<td>yon somewhat atypical idea; situation, condition</td>
</tr>
<tr>
<td><strong> p.ūnt.a </strong></td>
<td>elm.</td>
<td>alcoholic; warming (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> p.uthl&rsquo;e&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>&ldquo;good and proper&rdquo; &#8211; beneficent</td>
</tr>
<tr>
<td><strong> pa </strong></td>
<td>vcp.</td>
<td>[perfective] <strong>pal</strong></td>
</tr>
<tr>
<td><strong> pa </strong></td>
<td>elm.</td>
<td>completion</td>
</tr>
<tr>
<td><strong> pa.pa&rsquo; </strong></td>
<td>elm.CMP</td>
<td>(precisely the) same</td>
</tr>
<tr>
<td><strong> pā&rsquo;an </strong></td>
<td>elm.</td>
<td>explode; &ldquo;boom&rdquo;; &ldquo;bang&rdquo;</td>
</tr>
<tr>
<td><strong> pa&rdquo; </strong></td>
<td>elm.</td>
<td>same; repeat</td>
</tr>
<tr>
<td><strong> pai&rsquo;lio </strong></td>
<td>elm.CMP</td>
<td>smooth bean (bean used in pai&rsquo;paitui)</td>
</tr>
<tr>
<td><strong> pai&rsquo;paitui </strong></td>
<td>elm.CMP</td>
<td>fermented bean and grain paste (traditional fermented gooey paste made from pai&rsquo;lio bean or pai&#8217;pun grain or a combination of both)</td>
</tr>
<tr>
<td><strong> pai&rsquo;pun </strong></td>
<td>elm.CMP</td>
<td>grain; grains (in the general sense) (grain used in pai&#8217;paitui)</td>
</tr>
<tr>
<td><strong> pai&rdquo; </strong></td>
<td>elm.</td>
<td>&#8220;plant egg&#8221; (generic term for seeds; beans; peas; grains, etc. of flora)</td>
</tr>
<tr>
<td><strong> pait&rsquo;eng.h&rsquo;e&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>Xi&#8217;an peppercorn (creates a spice that causes tingly numbness in the mouth)</td>
</tr>
<tr>
<td><strong> pān </strong></td>
<td>elm.</td>
<td>mathematics; math</td>
</tr>
<tr>
<td><strong> pāng </strong></td>
<td>elm.</td>
<td>sexual activity</td>
</tr>
<tr>
<td><strong> pārsa.n&rsquo;ak </strong></td>
<td>n.</td>
<td>&#8220;snack bar&#8221; See also sa.n&rsquo;ak. (borrowed from English &laquo;snack bar&raquo;)</td>
</tr>
<tr>
<td><strong> pe </strong></td>
<td>pn.PEJ</td>
<td>It (inanimate)</td>
</tr>
<tr>
<td><strong> pe&rsquo;ath </strong></td>
<td>col.</td>
<td>xanadu</td>
</tr>
<tr>
<td><strong> pem </strong></td>
<td>pn.PEJ</td>
<td>they (inamt.)</td>
</tr>
<tr>
<td><strong> pen </strong></td>
<td>rel.</td>
<td>after; following</td>
</tr>
<tr>
<td><strong> peng </strong></td>
<td>num.</td>
<td>thousand 1,000</td>
</tr>
<tr>
<td><strong> pi&rsquo;a </strong></td>
<td>elm.</td>
<td>edge; border</td>
</tr>
<tr>
<td><strong> pi&rsquo;achui </strong></td>
<td>elm.CMP</td>
<td>beach; shore; coast; water&#8217;s edge</td>
</tr>
<tr>
<td><strong> pi&rsquo;akeng </strong></td>
<td>elm.CMP</td>
<td>border (between physical (land) territories)</td>
</tr>
<tr>
<td><strong> pi&rsquo;ar.ath </strong></td>
<td>elm.CMP</td>
<td>cliff (as experienced from the upper edge or &ldquo;drop off&rdquo;)</td>
</tr>
<tr>
<td><strong> pi&rsquo;auamchuai </strong></td>
<td>elm.CMP</td>
<td>a sandy beach</td>
</tr>
<tr>
<td><strong> piith </strong></td>
<td>elm.</td>
<td>line (of something); row; column of writing</td>
</tr>
<tr>
<td><strong> ping </strong></td>
<td>elm.</td>
<td>small; little; few</td>
</tr>
<tr>
<td><strong> ping&rdquo;xyang&rdquo; </strong></td>
<td>n.</td>
<td>refridgerator (borrowed from Mandarin &laquo;bīngxiāng&raquo;)</td>
</tr>
<tr>
<td><strong> po </strong></td>
<td>nlz.</td>
<td>[noun phrase clause head for &ldquo;the case that&rdquo;]</td>
</tr>
<tr>
<td><strong> po </strong></td>
<td>elm.</td>
<td>abstract; abstraction; idea or feeling of X</td>
</tr>
<tr>
<td><strong> pō </strong></td>
<td>nlz.</td>
<td><strong>po</strong> contracted with <strong>o</strong></td>
</tr>
<tr>
<td><strong> pō&rsquo;uai (.u) leth&rsquo;uiiyōn </strong></td>
<td>elm.CMP</td>
<td>Quantum Travel</td>
</tr>
<tr>
<td><strong> po. </strong></td>
<td>nlz.CLTC</td>
<td>[intangible thing or condition; abstract idea]</td>
</tr>
<tr>
<td><strong> pō. </strong></td>
<td>nlz.CLTC</td>
<td>[act of doing X]</td>
</tr>
<tr>
<td><strong> po&rsquo;.u&rsquo;a </strong></td>
<td>pn.</td>
<td>such an (&ldquo;out there&rdquo;) idea; situation, condition</td>
</tr>
<tr>
<td><strong> Po&rsquo;a </strong></td>
<td>line</td>
<td>P&oacute;a</td>
</tr>
<tr>
<td><strong> po&rsquo;e </strong></td>
<td>nlz.</td>
<td><strong>po</strong> contracted with <strong>e</strong></td>
</tr>
<tr>
<td><strong> po&rsquo;kr.ōng </strong></td>
<td>elm.CMP</td>
<td>an arocity; heinous violation of moraility or the law (used to explain the concept of &ldquo;sin&rdquo; to The Xi&rsquo;an)</td>
</tr>
<tr>
<td><strong> po&rsquo;lo </strong></td>
<td>nlz.</td>
<td><strong>po</strong> contracted with <strong>lo</strong></td>
</tr>
<tr>
<td><strong> pō&rsquo;po </strong></td>
<td>elm.CMP</td>
<td>intense activity; exertion; effort; going at it; intensity; fervor</td>
</tr>
<tr>
<td><strong> pō&#8217;syu</strong></td>
<td>elm.CMP</td>
<td>the act of flying in general; flight</td>
</tr>
<tr>
<td><strong> pō&rsquo;t.ōngp.ū </strong></td>
<td>elm.CMP</td>
<td>compulsory service to the Empire</td>
</tr>
<tr>
<td><strong> po&rsquo;to </strong></td>
<td>nlz.</td>
<td><strong>po</strong> contracted with <strong>t.o</strong></td>
</tr>
<tr>
<td><strong> po&rsquo;xy.oa </strong></td>
<td>Q.</td>
<td>what (abstract) thing?</td>
</tr>
<tr>
<td><strong> pohual </strong></td>
<td>elm.CMP</td>
<td>anything (any idea; solution; strategy; etc.)</td>
</tr>
<tr>
<td><strong> pohyan </strong></td>
<td>elm.CMP</td>
<td>everything (of situations or abstractions)</td>
</tr>
<tr>
<td><strong> pok&rsquo;ya </strong></td>
<td>elm.CMP</td>
<td>war</td>
</tr>
<tr>
<td><strong> pōsanal; o sanal </strong></td>
<td>elm.CMP</td>
<td><span class="caps">EVA</span></td>
</tr>
<tr>
<td><strong> poxu </strong></td>
<td>elm.CMP</td>
<td>effort; attempt; initiative</td>
</tr>
<tr>
<td><strong> poyai </strong></td>
<td>elm.CMP</td>
<td>the matter; the topic; the issue</td>
</tr>
<tr>
<td><strong> puan </strong></td>
<td>rel.</td>
<td>below; underneath</td>
</tr>
<tr>
<td><strong> puāng </strong></td>
<td>elm.</td>
<td>big; great; many</td>
</tr>
<tr>
<td><strong> pui&rsquo;a </strong></td>
<td>elm.</td>
<td>flower (specifically the flowery parts of a flowering plant)</td>
</tr>
<tr>
<td><strong> pui&rsquo;achui </strong></td>
<td>elm.CMP</td>
<td>lotus</td>
</tr>
<tr>
<td><strong> pui&rsquo;axye </strong></td>
<td>elm.CMP</td>
<td>bud</td>
</tr>
<tr>
<td><strong> Puii </strong></td>
<td>line</td>
<td>Pwii</td>
</tr>
<tr>
<td><strong> puin </strong></td>
<td>elm.</td>
<td>source; origin</td>
</tr>
<tr>
<td><strong> puinchui </strong></td>
<td>elm.CMP</td>
<td>well; wellspring; spring; waterhole</td>
</tr>
<tr>
<td><strong> puith&rdquo; </strong></td>
<td>elm.</td>
<td>itch; irritation; stinging sensation</td>
</tr>
<tr>
<td><strong> pun </strong></td>
<td>elm.</td>
<td>light; fluffy; ethereal; diaphanous; fine</td>
</tr>
<tr>
<td><strong> pun&rsquo;.au&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>frost</td>
</tr>
<tr>
<td><strong> punxā&rsquo;ye </strong></td>
<td>elm.CMP</td>
<td>coarse; overly sandy; doesn&#8217;t dissolve in the mouth (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> puo </strong></td>
<td>elm.</td>
<td>criminal (convictable)</td>
</tr>
<tr>
<td><strong> Puo-________ </strong></td>
<td>PN.role</td>
<td>Convict employed in _________</td>
</tr>
<tr>
<td><strong> puo&rsquo;ya </strong></td>
<td>elm.</td>
<td>surrender; giving up; yield; yielding</td>
</tr>
<tr>
<td><strong> puong </strong></td>
<td>elm.</td>
<td>mouth</td>
</tr>
<tr>
<td><strong> puongpān </strong></td>
<td>elm.CMP</td>
<td>delicous; tasty</td>
</tr>
<tr>
<td><strong> puongtuāl </strong></td>
<td>elm.CMP</td>
<td>sublimely delicious; exquisitely refined meal</td>
</tr>
<tr>
<td><strong> puothao </strong></td>
<td>elm.CMP</td>
<td>guilty in reality; truly culpable</td>
</tr>
<tr>
<td><strong> pyā </strong></td>
<td>elm.</td>
<td>close-knit group; bond; &ldquo;family&rdquo;; team or section in a work environment</td>
</tr>
<tr>
<td><strong> pyā&rsquo;h.ūn </strong></td>
<td>elm.CMP</td>
<td>corporate organization term for group; section; team (manual labor focused context)</td>
</tr>
<tr>
<td><strong> pyā&rsquo;hai </strong></td>
<td>elm.CMP</td>
<td>&ldquo;family&rdquo; &mdash; the Xi&rsquo;an nuclear &lsquo;bond-group&rsquo;</td>
</tr>
<tr>
<td><strong> pyā&rsquo;kran </strong></td>
<td>elm.CMP</td>
<td>corporate organization term for group; section; team (non-labor focused)</td>
</tr>
<tr>
<td><strong> pyen </strong></td>
<td>elm.</td>
<td>metal; metallic; ore</td>
</tr>
<tr>
<td><strong> pyen&rsquo;pyen </strong></td>
<td>elm.CMP</td>
<td>metallic; mineral; iron (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> pyi </strong></td>
<td>elm</td>
<td>less</td>
</tr>
<tr>
<td><strong> pyō </strong></td>
<td>elm.</td>
<td>the last stage of life; extremely elderly;</td>
</tr>
<tr>
<td><strong> r.ai </strong></td>
<td>elm.</td>
<td>year (Xi&rsquo;an year)</td>
</tr>
<tr>
<td><strong> r.aiHy&rsquo;ūm </strong></td>
<td>elm.CMP</td>
<td>Human year (unit of time)</td>
</tr>
<tr>
<td><strong> r.am </strong></td>
<td>v.PEJ</td>
<td>be of a class</td>
</tr>
<tr>
<td><strong> r.ānu&rsquo;in </strong></td>
<td>elm.CMP</td>
<td>measure of temperature</td>
</tr>
<tr>
<td><strong> r.ao </strong></td>
<td>v.PEJ</td>
<td>try/attempt (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> r.ath </strong></td>
<td>elm.</td>
<td>descend; drop; fall; cascade</td>
</tr>
<tr>
<td><strong> R.ēth </strong></td>
<td>PN.male</td>
<td>Rayth</td>
</tr>
<tr>
<td><strong> r.o </strong></td>
<td>pn.PEJ</td>
<td>you</td>
</tr>
<tr>
<td><strong> r.om </strong></td>
<td>pn.PEJ</td>
<td>y&rsquo;all</td>
</tr>
<tr>
<td><strong> r.u </strong></td>
<td>elm.</td>
<td>bad; improper; inferior</td>
</tr>
<tr>
<td><strong> r.uang </strong></td>
<td>elm.</td>
<td>pardon; forgiveness</td>
</tr>
<tr>
<td><strong> r.uangō&rsquo;l </strong></td>
<td>elm.CMP</td>
<td>manners; politeness</td>
</tr>
<tr>
<td><strong> r.uo </strong></td>
<td>v.PEJ</td>
<td>do</td>
</tr>
<tr>
<td><strong> r.ut&rsquo;ang </strong></td>
<td>elm.</td>
<td>strict; rigid; inflexible; harsh</td>
</tr>
<tr>
<td><strong> ra </strong></td>
<td>elm.</td>
<td>some; indefinite; non-specified</td>
</tr>
<tr>
<td><strong> rai </strong></td>
<td>elm.</td>
<td>haul; transport; carry (something)</td>
</tr>
<tr>
<td><strong> rān </strong></td>
<td>elm.</td>
<td>level; degree</td>
</tr>
<tr>
<td><strong> rānchuikyu </strong></td>
<td>elm.CMP</td>
<td>relative humidity (meteorological measurement)</td>
</tr>
<tr>
<td><strong> rānke&rsquo;u </strong></td>
<td>elm.</td>
<td>the size of an item (like clothing)</td>
</tr>
<tr>
<td><strong> rānke&rsquo;u </strong></td>
<td>elm.CMP</td>
<td>scale (as it relates to physical size)</td>
</tr>
<tr>
<td><strong> reth </strong></td>
<td>v.PEJ</td>
<td>eminate/reflect</td>
</tr>
<tr>
<td><strong> ri </strong></td>
<td>elm.</td>
<td>middle; in the middle; median in status; mid-grade</td>
</tr>
<tr>
<td><strong> ri&rsquo;.ah&rsquo;a </strong></td>
<td>cnj.</td>
<td>even though</td>
</tr>
<tr>
<td><strong> ri&rsquo;.at&rsquo;ō </strong></td>
<td>elm.CMP</td>
<td>negotiation; posture for leverage; (lit: &ldquo;business face&rdquo;)</td>
</tr>
<tr>
<td><strong> ri&rsquo;a </strong></td>
<td>rel.</td>
<td>in the face of; facing; standing before X looking at it; dealing with X</td>
</tr>
<tr>
<td><strong> ri&rsquo;a </strong></td>
<td>elm.</td>
<td>face; visage; countenance</td>
</tr>
<tr>
<td><strong> rii </strong></td>
<td>v.PEJ</td>
<td>cause/produce/effect</td>
</tr>
<tr>
<td><strong> riing </strong></td>
<td>v.PEJ</td>
<td>please</td>
</tr>
<tr>
<td><strong> rin </strong></td>
<td>elm.</td>
<td>disrupt; break; destabalize; disturb</td>
</tr>
<tr>
<td><strong> ro&rsquo;a </strong></td>
<td>v.PEJ</td>
<td>equate</td>
</tr>
<tr>
<td><strong> ro&rsquo;ang </strong></td>
<td>col.</td>
<td>titian</td>
</tr>
<tr>
<td><strong> ro&rsquo;hyoping </strong></td>
<td>elm.CMP</td>
<td>Shotgun</td>
</tr>
<tr>
<td><strong> ro&rsquo;kya.thl&rsquo;e&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>Assault Rifle</td>
</tr>
<tr>
<td><strong> ro&rsquo;kyaxyiing </strong></td>
<td>elm.CMP</td>
<td>Machine Gun</td>
</tr>
<tr>
<td><strong> ro&rsquo;no </strong></td>
<td>elm.CMP</td>
<td>Pistol</td>
</tr>
<tr>
<td><strong> ro&rsquo;nonō (ro&rsquo;nō) </strong></td>
<td>elm.CMP</td>
<td>Sniper Rifle</td>
</tr>
<tr>
<td><strong> ro&rsquo;noy.ithly&rsquo;ehung </strong></td>
<td>elm.CMP</td>
<td>Missile Launcher</td>
</tr>
<tr>
<td><strong> ro&rsquo;noy.ithly&rsquo;eri </strong></td>
<td>elm.CMP</td>
<td>Rocket Launcher</td>
</tr>
<tr>
<td><strong> ro&rsquo;noyithhyo&rsquo;pān </strong></td>
<td>elm.CMP</td>
<td>Grenade Launcher</td>
</tr>
<tr>
<td><strong> ro&rsquo;p.uto&rsquo;ath </strong></td>
<td>PN.role</td>
<td>sharpshooter assassin</td>
</tr>
<tr>
<td><strong> ro&rsquo;t.os&rsquo;ānka&rsquo;Xa </strong></td>
<td>elm.CMP</td>
<td>Disrupter Weapon</td>
</tr>
<tr>
<td><strong> ro&rsquo;thli </strong></td>
<td>elm.CMP</td>
<td>Energy Weapon</td>
</tr>
<tr>
<td><strong> ro&rsquo;tik </strong></td>
<td>n.</td>
<td>rotik (borrowed from Kalenjin &laquo;rotik&raquo;)</td>
</tr>
<tr>
<td><strong> Ro&rsquo;to </strong></td>
<td>PN.male</td>
<td>Roto</td>
</tr>
<tr>
<td><strong> ro&rsquo;yith </strong></td>
<td>elm.CMP</td>
<td>Ballistic (Weapon)</td>
</tr>
<tr>
<td><strong> ro&rsquo;yithhpyen </strong></td>
<td>elm.CMP</td>
<td>Cannon</td>
</tr>
<tr>
<td><strong> ro&rsquo;yithleth </strong></td>
<td>elm.CMP</td>
<td>Gatling</td>
</tr>
<tr>
<td><strong> ro&rdquo; </strong></td>
<td>elm.</td>
<td>gun; (complex) weapon</td>
</tr>
<tr>
<td><strong> rōm </strong></td>
<td>v.PEJ</td>
<td>need (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> rōm&rsquo;xy.uny.uo </strong></td>
<td>elm.CMP</td>
<td>tough; difficult to chew (used only for the context of eating) (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> rōm&rsquo;xyun.s&rsquo;uā&rsquo;moa </strong></td>
<td>elm.CMP</td>
<td>stretchy; chewy; like bubblegum (used only for the context of eating) (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> ru </strong></td>
<td>elm.</td>
<td>pull; attraction; gravity</td>
</tr>
<tr>
<td><strong> ruxyiing </strong></td>
<td>elm.CMP</td>
<td>Natural gravity (created by heavenly bodies)</td>
</tr>
<tr>
<td><strong> Ru&rsquo;a </strong></td>
<td>line</td>
<td>Ruah</td>
</tr>
<tr>
<td><strong> ru&rsquo;t.ony&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>Artificial Gravity</td>
</tr>
<tr>
<td><strong> run </strong></td>
<td>elm.</td>
<td>possession; possess; have</td>
</tr>
<tr>
<td><strong> rung </strong></td>
<td>elm.</td>
<td>tired; exhaustion</td>
</tr>
<tr>
<td><strong> ruo </strong></td>
<td>rel.</td>
<td>across; on the other side of something</td>
</tr>
<tr>
<td><strong> ruōm </strong></td>
<td>elm.CMP</td>
<td>magnetic pull</td>
</tr>
<tr>
<td><strong> ruthliōm </strong></td>
<td>elm.CMP</td>
<td>Electromagnetic</td>
</tr>
<tr>
<td><strong> ryā </strong></td>
<td>elm.</td>
<td>bright flavor; pungent smell</td>
</tr>
<tr>
<td><strong> ryā&rsquo;ra </strong></td>
<td>elm.</td>
<td>savory; glutamates; umami (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> ryāi </strong></td>
<td>elm.</td>
<td>goop; gel; sticky</td>
</tr>
<tr>
<td><strong> ryāi&rsquo;xy.un </strong></td>
<td>elm.CMP</td>
<td>cud (of an animal); slobber (when eating imprecisely)</td>
</tr>
<tr>
<td><strong> ryāimam&rsquo;pa </strong></td>
<td>elm.CMP</td>
<td>Fat Bear Butter (aged fat of a mam&rsquo;pa; used like butter)</td>
</tr>
<tr>
<td><strong> ryāingea </strong></td>
<td>elm.CMP</td>
<td>gelatinous; firm but with a bit of a give (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> ryāingum </strong></td>
<td>elm.CMP</td>
<td>viscous (and tangy) mold gel (often used by the Xi&rsquo;an as &lsquo;sauce&rsquo; on their food)</td>
</tr>
<tr>
<td><strong> ryāipuāng </strong></td>
<td>eim.CMP</td>
<td>smooth; mushy; pudding-like (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> ryāitith </strong></td>
<td>elm.CMP</td>
<td>fatty; greasy; coats the inside of one&#8217;s mouth (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> ryāiuam </strong></td>
<td>elm.CMP</td>
<td>mud (generic)</td>
</tr>
<tr>
<td><strong> ryath </strong></td>
<td>v.PEJ</td>
<td>want/desire (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> ryāthli </strong></td>
<td>elm.CMP</td>
<td>Plasma</td>
</tr>
<tr>
<td><strong> ryi </strong></td>
<td>elm.</td>
<td>bed; cradle; basket; cocoon</td>
</tr>
<tr>
<td><strong> s.ang&rsquo;i </strong></td>
<td>rel.</td>
<td>on the front of (touching or attached)</td>
</tr>
<tr>
<td><strong> s.ang&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>next (in sequence) <strong>sang + o&rdquo;</strong></td>
</tr>
<tr>
<td><strong> s.āoth </strong></td>
<td>n.</td>
<td>Egg Lizard (domestic reptile raised for its eggs and meat)</td>
</tr>
<tr>
<td><strong> s.ap&rsquo;ua </strong></td>
<td>elm.</td>
<td>storm; disturbance</td>
</tr>
<tr>
<td><strong> s.āth </strong></td>
<td>pn.REV</td>
<td>y&rsquo;all</td>
</tr>
<tr>
<td><strong> s.eu&rsquo;a </strong></td>
<td>deix.</td>
<td>those distant (after an indicated noun)</td>
</tr>
<tr>
<td><strong> s.ey&rsquo;ā </strong></td>
<td>col.</td>
<td>vermillion</td>
</tr>
<tr>
<td><strong> s.ey&rsquo;o </strong></td>
<td>deix.</td>
<td>those (near you) (after an indicated noun)</td>
</tr>
<tr>
<td><strong> s.i </strong></td>
<td>elm.</td>
<td>lesser animal, generic term for small insects, larvae, mites, etc.</td>
</tr>
<tr>
<td><strong> s.ik&rsquo;i </strong></td>
<td>elm.CMP</td>
<td>parasite (non-microscopic)</td>
</tr>
<tr>
<td><strong> s.o&rsquo;e </strong></td>
<td>elm.</td>
<td>reciprication; sharing; back and forth; mutual (se <strong>s.o&rsquo;e</strong> = each other&rsquo;)</td>
</tr>
<tr>
<td><strong> s.oa </strong></td>
<td>elm.</td>
<td>way; path; route; road</td>
</tr>
<tr>
<td><strong> s.oach&rsquo;ui </strong></td>
<td>elm.CMP</td>
<td>canal; waterway; channel</td>
</tr>
<tr>
<td><strong> s.oak&rsquo;yu&rsquo;ā </strong></td>
<td>elm.CMP</td>
<td>jet stream</td>
</tr>
<tr>
<td><strong> S.oam </strong></td>
<td>PN.male</td>
<td>Soahm</td>
</tr>
<tr>
<td><strong> s.ōng </strong></td>
<td>vcp.</td>
<td>[permissive] (&ldquo;allowed to&rdquo;)</td>
</tr>
<tr>
<td><strong> s.ōng </strong></td>
<td>elm.</td>
<td>permission; right; empowerment; allowance</td>
</tr>
<tr>
<td><strong> S.un&rsquo;a </strong></td>
<td>name</td>
<td>Big Sis (endearment term from younger sister to older sister)</td>
</tr>
<tr>
<td><strong> S.un&rsquo;ath </strong></td>
<td>PN.feml</td>
<td>Sun&aacute;th</td>
</tr>
<tr>
<td><strong> s.uny&rsquo;ii </strong></td>
<td>elm.</td>
<td>biological sibling (older)</td>
</tr>
<tr>
<td><strong> s.yā </strong></td>
<td>v.REV</td>
<td>need (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> s.ya&rsquo;u </strong></td>
<td>deix.</td>
<td>these (after an indicated noun)</td>
</tr>
<tr>
<td><strong> s.ye&rsquo;a </strong></td>
<td>deix.</td>
<td>those yonder (away from both of us) (after an indicated noun)</td>
</tr>
<tr>
<td><strong> sā </strong></td>
<td>vcp.</td>
<td>[potential] <strong>sāl</strong></td>
</tr>
<tr>
<td><strong> sā </strong></td>
<td>elm.</td>
<td>potential; possibility</td>
</tr>
<tr>
<td><strong> sa.n&rsquo;ak </strong></td>
<td>n.</td>
<td>&#8220;snack&#8221; (borrowed from English &laquo;snack&raquo;)</td>
</tr>
<tr>
<td><strong> sa&rsquo;a </strong></td>
<td>elm.</td>
<td>friend; friendly</td>
</tr>
<tr>
<td><strong> sa&rsquo;na </strong></td>
<td>col.</td>
<td>amaranthine</td>
</tr>
<tr>
<td><strong> sa&rsquo;uo </strong></td>
<td>elm.</td>
<td>tall; big in stature; &ldquo;gigantic&rdquo;</td>
</tr>
<tr>
<td><strong> sam </strong></td>
<td>elm.</td>
<td>slow; slow; leisurely</td>
</tr>
<tr>
<td><strong> san </strong></td>
<td>elm.</td>
<td>ship; craft; vehicle; vessel (for transportation); car; truck</td>
</tr>
<tr>
<td><strong> sān </strong></td>
<td>elm.</td>
<td>end; ending; finish</td>
</tr>
<tr>
<td><strong> san&rsquo;hyao </strong></td>
<td>elm.CMP</td>
<td>flying craft; space-faring vessel</td>
</tr>
<tr>
<td><strong> san&rsquo;kyu </strong></td>
<td>elm.CMP</td>
<td>airplane; vehicle that flies in air (only)</td>
</tr>
<tr>
<td><strong> sang </strong></td>
<td>rel.</td>
<td>in front of</td>
</tr>
<tr>
<td><strong> sank&rsquo;ya </strong></td>
<td>elm.CMP</td>
<td>Fighter ship</td>
</tr>
<tr>
<td><strong> sanla; sanle&rsquo;al </strong></td>
<td>elm.CMP</td>
<td>Open Canopy ship</td>
</tr>
<tr>
<td><strong> sanō&rsquo;nu; sanō&rsquo;nuhyath </strong></td>
<td>elm.CMP</td>
<td>Capital ship</td>
</tr>
<tr>
<td><strong> sanrai </strong></td>
<td>elm.CMP</td>
<td>Cargo ship</td>
</tr>
<tr>
<td><strong> sao </strong></td>
<td>elm.</td>
<td>empire; kingdom</td>
</tr>
<tr>
<td><strong> sāo </strong></td>
<td>elm.</td>
<td>flee; escape; run from danger</td>
</tr>
<tr>
<td><strong> sao&rsquo;teth </strong></td>
<td>elm.CMP</td>
<td>planetary empire</td>
</tr>
<tr>
<td><strong> saotō </strong></td>
<td>elm.CMP</td>
<td>related to the economy</td>
</tr>
<tr>
<td><strong> sath </strong></td>
<td>elm.</td>
<td>design</td>
</tr>
<tr>
<td><strong> se </strong></td>
<td>rel.</td>
<td>of (a plural entities)</td>
</tr>
<tr>
<td><strong> sē&#8217;a </strong></td>
<td>pn.NEU</td>
<td>y&rsquo;all</td>
</tr>
<tr>
<td><strong> Se&rsquo;ang </strong></td>
<td>PN.male</td>
<td>S&eacute;ang</td>
</tr>
<tr>
<td><strong> se&rsquo;lan </strong></td>
<td>pn.NEU</td>
<td>they</td>
</tr>
<tr>
<td><strong> se&rsquo;lanua </strong></td>
<td>pn.NEU</td>
<td>they (female exclusive overt)</td>
</tr>
<tr>
<td><strong> se&rsquo;lanyu </strong></td>
<td>pn.NEU</td>
<td>they (male exclusive overt)</td>
</tr>
<tr>
<td><strong> se&rsquo;u </strong></td>
<td>v.LAUD</td>
<td>want/desire (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> se&rdquo; </strong></td>
<td>elm.</td>
<td>assist; help</td>
</tr>
<tr>
<td><strong> sea </strong></td>
<td>elm.</td>
<td>half (of a whole)</td>
</tr>
<tr>
<td><strong> seahyo </strong></td>
<td>elm.CMP</td>
<td>hemisphere</td>
</tr>
<tr>
<td><strong> seahyothlal </strong></td>
<td>elm.CMP</td>
<td>dome</td>
</tr>
<tr>
<td><strong> sen </strong></td>
<td>rel.</td>
<td>named/called</td>
</tr>
<tr>
<td><strong> sen </strong></td>
<td>elm.</td>
<td>name; be called</td>
</tr>
<tr>
<td><strong> sēng </strong></td>
<td>elm.</td>
<td>protect; defend; vouch for</td>
</tr>
<tr>
<td><strong> sēnge&rsquo;so </strong></td>
<td>elm.CMP</td>
<td>Shields (force field around a spacecraft)</td>
</tr>
<tr>
<td><strong> Senhyi </strong></td>
<td>PN.role</td>
<td>&ldquo;Prestigious Name&rdquo; (cf: Lord, Lady, Sir)</td>
</tr>
<tr>
<td><strong> senping </strong></td>
<td>elm.CMP</td>
<td>affectionate name, nickname</td>
</tr>
<tr>
<td><strong> senxiin </strong></td>
<td>elm.CMP</td>
<td>signature; written seal</td>
</tr>
<tr>
<td><strong> seth </strong></td>
<td>elm.</td>
<td>cross; traverse</td>
</tr>
<tr>
<td><strong> si </strong></td>
<td>v.FAM</td>
<td>equate</td>
</tr>
<tr>
<td><strong> si&rsquo;p.eh&rsquo;a&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>Overheat</td>
</tr>
<tr>
<td><strong> si&rsquo;pe </strong></td>
<td>elm.</td>
<td>hot</td>
</tr>
<tr>
<td><strong> si&rsquo;ping </strong></td>
<td>elm.CMP</td>
<td>warm</td>
</tr>
<tr>
<td><strong> siin </strong></td>
<td>elm.</td>
<td>older juvenile cousin of a juvenile</td>
</tr>
<tr>
<td><strong> siing </strong></td>
<td>elm.</td>
<td>interrupt, intervene (in a situation); block (progress); break (in a flow)</td>
</tr>
<tr>
<td><strong> siingk.engt&rsquo;ang </strong></td>
<td>elm.CMP</td>
<td>monumental mountain/range, etc. that must be circumnavigated or flown over</td>
</tr>
<tr>
<td><strong> siingkeng </strong></td>
<td>elm.CMP</td>
<td>geographic obstacle, impass</td>
</tr>
<tr>
<td><strong> siingkeng&rsquo;kē </strong></td>
<td>elm.CMP</td>
<td>crevasse; abyss (impasasble (on foot) chasm, etc.)</td>
</tr>
<tr>
<td><strong> so </strong></td>
<td>rel.</td>
<td>with; accompanying</td>
</tr>
<tr>
<td><strong> so&rsquo;a </strong></td>
<td>elm.</td>
<td>muscle; muscle tissue</td>
</tr>
<tr>
<td><strong> So&rsquo;lo </strong></td>
<td>name</td>
<td>&ldquo;My Elder&rdquo; (respectful term of address for any adult to whom one is realted who is older than oneself)</td>
</tr>
<tr>
<td><strong> so&rdquo; </strong></td>
<td>elm.</td>
<td>adult kin (older); cousin or uncle/&ldquo;aunt&rdquo; who is senior, older than oneself</td>
</tr>
<tr>
<td><strong> soa </strong></td>
<td>elm.</td>
<td>plan; planning; strategy</td>
</tr>
<tr>
<td><strong> sol </strong></td>
<td>rel.</td>
<td>without</td>
</tr>
<tr>
<td><strong> Sol&rsquo;na </strong></td>
<td>name</td>
<td>&ldquo;My Aunt&rdquo; (respectful term of address for a female to whom one is realted who is older than oneself)</td>
</tr>
<tr>
<td><strong> Sol&rsquo;yu </strong></td>
<td>name</td>
<td>&ldquo;My Uncle&rdquo; (respectful term of address for male to whom one is realted who is older than oneself)</td>
</tr>
<tr>
<td><strong> su </strong></td>
<td>elm.</td>
<td>guide; channel; funnel; direct (in a direction)</td>
</tr>
<tr>
<td><strong> sū </strong></td>
<td>vcp.</td>
<td>[securative (&ldquo;sure that&rdquo;)] <strong>sūl</strong></td>
</tr>
<tr>
<td><strong> sū </strong></td>
<td>elm.</td>
<td>assurance; complete faith (non-religious)</td>
</tr>
<tr>
<td><strong>S.ura&#8217;</strong></td>
<td>line</td>
<td>Sur&aacute;</td>
</tr>
<tr>
<td><strong> Su&rsquo;lo </strong></td>
<td>name</td>
<td>Big Bro (endearment term from younger to older brother)</td>
</tr>
<tr>
<td><strong> Su&rsquo;n.ā </strong></td>
<td>name</td>
<td>Big Sister (endearment term from younger brother to older sister as an adult)</td>
</tr>
<tr>
<td><strong> su&rsquo;sa </strong></td>
<td>elm.</td>
<td>hint of flavor; light aroma</td>
</tr>
<tr>
<td><strong> Su&rsquo;su </strong></td>
<td>name</td>
<td>Big Sister (endearment term from younger brother to older sister)</td>
</tr>
<tr>
<td><strong> suā </strong></td>
<td>rel.</td>
<td>during (an event, etc.)</td>
</tr>
<tr>
<td><strong> suā </strong></td>
<td>elm.</td>
<td>amount of time</td>
</tr>
<tr>
<td><strong> sua. </strong></td>
<td>nlz.CLTC</td>
<td>[in a state of X]</td>
</tr>
<tr>
<td><strong> suā&rsquo;moa </strong></td>
<td>elm.CMP</td>
<td>forever</td>
</tr>
<tr>
<td><strong> sua&rsquo;sa </strong></td>
<td>elm</td>
<td>happy; joyful</td>
</tr>
<tr>
<td><strong> suā&rsquo;xy.oa </strong></td>
<td>Q.</td>
<td>how long (of time)?</td>
</tr>
<tr>
<td><strong> sua&rsquo;yu </strong></td>
<td>pn.REV</td>
<td>they (male)</td>
</tr>
<tr>
<td><strong> suāhual </strong></td>
<td>elm.CMP</td>
<td>any amount of time; however long (in terms of time)</td>
</tr>
<tr>
<td><strong> suao </strong></td>
<td>v.LAUD</td>
<td>eminate/reflect</td>
</tr>
<tr>
<td><strong> suarungua </strong></td>
<td>elm.CMP</td>
<td>estrus; fertile; fertility</td>
</tr>
<tr>
<td><strong> suāye </strong></td>
<td>elm.CMP</td>
<td>a day; a day&rsquo;s worth of time (generic and context sensitive)</td>
</tr>
<tr>
<td><strong> sue </strong></td>
<td>elm.</td>
<td>conversation (tone is somewhat formal)</td>
</tr>
<tr>
<td><strong> suen </strong></td>
<td>pn.REV</td>
<td>they (female)</td>
</tr>
<tr>
<td><strong> sueu&rsquo;oa </strong></td>
<td>elm.CMP</td>
<td>a talk; chit-chat; banter (informal)</td>
</tr>
<tr>
<td><strong> sui </strong></td>
<td>elm.</td>
<td>acid</td>
</tr>
<tr>
<td><strong> sui&rsquo;sui </strong></td>
<td>elm.CMP</td>
<td>acidic; sharp; sour; tangy (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> suiloa </strong></td>
<td>elm.CMP</td>
<td>vinegar</td>
</tr>
<tr>
<td><strong> suingui </strong></td>
<td>elm.CMP</td>
<td>lactic acid</td>
</tr>
<tr>
<td><strong> suiuōng </strong></td>
<td>elm.CMP</td>
<td>uric acid</td>
</tr>
<tr>
<td><strong> sun </strong></td>
<td>elm.</td>
<td><strong>pyā&rsquo;hai</strong> sibling (older)</td>
</tr>
<tr>
<td><strong> sunen </strong></td>
<td>elm.CMP</td>
<td>all of one&rsquo;s siblings in a <strong>pyā&rsquo;hai</strong> (younger and older)</td>
</tr>
<tr>
<td><strong> Sungā </strong></td>
<td>name</td>
<td>Big Brother (endearment term from younger sister to older brother)</td>
</tr>
<tr>
<td><strong> sya </strong></td>
<td>v.NEU</td>
<td>need (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> Syang </strong></td>
<td>line</td>
<td>Syang</td>
</tr>
<tr>
<td><strong> syath </strong></td>
<td>elm.</td>
<td>pressure, push, force (in the sense of intensity)</td>
</tr>
<tr>
<td><strong> syathkyu </strong></td>
<td>elm.CMP</td>
<td>air pressure</td>
</tr>
<tr>
<td><strong> syathlyekyu&rsquo;ā </strong></td>
<td>elm.CMP</td>
<td>wind shear</td>
</tr>
<tr>
<td><strong> sye </strong></td>
<td>elm.</td>
<td>becoming; become; inception</td>
</tr>
<tr>
<td><strong> syen </strong></td>
<td>num.</td>
<td>two 2</td>
</tr>
<tr>
<td><strong> syengum </strong></td>
<td>elm.CMP</td>
<td>decompose; decompositon; rot; decay; putrify</td>
</tr>
<tr>
<td><strong> syu </strong></td>
<td>elm.</td>
<td>fly (general sense) through air or vacuum; travel by flying (not on the ground).</td>
</tr>
<tr>
<td><strong> syuhyao </strong></td>
<td>elm.CMP</td>
<td>fly in space; flight in the vacuum of space</td>
</tr>
<tr>
<td><strong> syukyu </strong></td>
<td>elm.CMP</td>
<td>fly through air; flight in an atmosphere</td>
</tr>
<tr>
<td><strong> T.ai </strong></td>
<td>PN.male</td>
<td>Tai</td>
</tr>
<tr>
<td><strong> t.āth </strong></td>
<td>pn.REV</td>
<td>you</td>
</tr>
<tr>
<td><strong> t.ē </strong></td>
<td>v.REV</td>
<td>please</td>
</tr>
<tr>
<td><strong> t.e&rsquo;i </strong></td>
<td>elm.</td>
<td>pride; self-assuredness (internal (private sense))</td>
</tr>
<tr>
<td><strong> t.e&rsquo;i&rsquo;xān </strong></td>
<td>elm.</td>
<td>emotionally bold; fully realized vis-&agrave;-vis personality</td>
</tr>
<tr>
<td><strong> t.ea </strong></td>
<td>elm</td>
<td>function; work; peform; behave (of machines)</td>
</tr>
<tr>
<td><strong> t.et&rsquo;o </strong></td>
<td>elm.</td>
<td>enemy</td>
</tr>
<tr>
<td><strong> t.ethl&rsquo;etao&rdquo; </strong></td>
<td>elm.CMP</td>
<td>Capital Planet; seat of government</td>
</tr>
<tr>
<td><strong> t.i </strong></td>
<td>elm.</td>
<td>young; younger; jr.; lesser in status; low-grade</td>
</tr>
<tr>
<td><strong> t.ii </strong></td>
<td>v.REV</td>
<td>equate</td>
</tr>
<tr>
<td><strong> T.il&rsquo;a </strong></td>
<td>PN.feml</td>
<td>Til&aacute;</td>
</tr>
<tr>
<td><strong> t.o </strong></td>
<td>v.NEU</td>
<td>cause/produce/effect</td>
</tr>
<tr>
<td><strong> t.ō </strong></td>
<td>v.REV</td>
<td>cause/produce/effect</td>
</tr>
<tr>
<td><strong> t.o yo </strong></td>
<td>idm.</td>
<td>prevent</td>
</tr>
<tr>
<td><strong> t.o&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>manufacturing; producing (products; things)</td>
</tr>
<tr>
<td><strong> t.o&#8217;a </strong></td>
<td>elm.CMP</td>
<td>fabricate; manufacture, manufacturing</td>
</tr>
<tr>
<td><strong> t.ōng </strong></td>
<td>elm.</td>
<td>care; oversight</td>
</tr>
<tr>
<td><strong> t.ot&rsquo;en </strong></td>
<td>elm.CMP</td>
<td>farming; agriculture (producing food)</td>
</tr>
<tr>
<td><strong> t.u </strong></td>
<td>elm.</td>
<td>kill; murder; snuff out; extinguish; turn off</td>
</tr>
<tr>
<td><strong> t.ū&rsquo;ong </strong></td>
<td>elm.CMP</td>
<td>suicide; self-destruct</td>
</tr>
<tr>
<td><strong> t.ū&rsquo;ong&rsquo;pān; t.ū&rsquo;ong </strong></td>
<td>elm.CMP</td>
<td>Self Destruct</td>
</tr>
<tr>
<td><strong> t.uōn </strong></td>
<td>v.REV</td>
<td>want/desire (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> t.ye </strong></td>
<td>elm.</td>
<td>steal; rob; hold up (in robbery); vandalize</td>
</tr>
<tr>
<td><strong> t.yonk&rsquo;ao </strong></td>
<td>elm.CMP</td>
<td>arrive (here)</td>
</tr>
<tr>
<td><strong> t&rsquo;uoa </strong></td>
<td>col.</td>
<td>sarcoline</td>
</tr>
<tr>
<td><strong> tā </strong></td>
<td>elm.</td>
<td>building; dwelling; habitable structure</td>
</tr>
<tr>
<td><strong> ta&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>egg (tangible, that can be laid and handled)</td>
</tr>
<tr>
<td><strong> ta&rsquo;atui </strong></td>
<td>elm.CMP</td>
<td>fermented fertilized eggs; fermented balut (fertilized eggs that have been aged over a few months)</td>
</tr>
<tr>
<td><strong> ta&rsquo;ayo.t&rsquo;a(tui) </strong></td>
<td>elm.CMP</td>
<td>fermented unfertilized eggs (unfertilized eggs that have been aged over a few months)</td>
</tr>
<tr>
<td><strong> ta&rsquo;hyē </strong></td>
<td>elm.CMP</td>
<td>hybrid</td>
</tr>
<tr>
<td><strong> ta&rsquo;kya </strong></td>
<td>elm.</td>
<td>intoxicating; high (on some substance)</td>
</tr>
<tr>
<td><strong> tā&rsquo;t.ot&rsquo;enii </strong></td>
<td>elm.CMP</td>
<td>greenhouse (for growing plants for food)</td>
</tr>
<tr>
<td><strong> ta&rsquo;u </strong></td>
<td>elm.</td>
<td>future; the future (also <strong>tao</strong> as a variant, especially in compounds)</td>
</tr>
<tr>
<td><strong> ta&rdquo; </strong></td>
<td>elm.</td>
<td>seed; egg; genetic material</td>
</tr>
<tr>
<td><strong>tāma’a</strong></td>
<td>elm.CMP</td>
<td>barn; animal processing facility</td>
</tr>
<tr>
<td><strong> tāmuii </strong></td>
<td>elm.CMP</td>
<td>conservatory of plants; greenhouse</td>
</tr>
<tr>
<td><strong> tai </strong></td>
<td>elm.</td>
<td>element; part; piece</td>
</tr>
<tr>
<td><strong> taichiin&rsquo;nao </strong></td>
<td>elm.CMP</td>
<td>rainbow</td>
</tr>
<tr>
<td><strong> tailue </strong></td>
<td>elm.CMP</td>
<td>connector; fastner</td>
</tr>
<tr>
<td><strong> taipui&rsquo;apun </strong></td>
<td>elm.</td>
<td>petal</td>
</tr>
<tr>
<td><strong> taipunl.e&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>feather</td>
</tr>
<tr>
<td><strong> taixauo&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>a particle of speech (a prefix or suffix, etc.)</td>
</tr>
<tr>
<td><strong> tām </strong></td>
<td>elm.</td>
<td>empty; void of contents</td>
</tr>
<tr>
<td><strong> tan </strong></td>
<td>col.</td>
<td>onyx</td>
</tr>
<tr>
<td><strong> tang&rsquo;kea </strong></td>
<td>elm.CMP</td>
<td>prominent hill or mountain (cf: Mt. Fuji, Uluru, Devil&rsquo;s Tower)</td>
</tr>
<tr>
<td><strong> tang&rsquo;keng </strong></td>
<td>elm.CMP</td>
<td>island (in a large body of water); isolated hill or mountain</td>
</tr>
<tr>
<td><strong> tang&rsquo;no </strong></td>
<td>elm.CMP</td>
<td>finger; digit (of a hand or paw)</td>
</tr>
<tr>
<td><strong> tang&rsquo;nokeng </strong></td>
<td>elm.CMP</td>
<td>peninsula (of land)</td>
</tr>
<tr>
<td><strong> tang&rsquo;puāng </strong></td>
<td>elm.CMP</td>
<td>mountain</td>
</tr>
<tr>
<td><strong> tang&rsquo;puāngpuinchuaiyeng </strong></td>
<td>elm.CMP</td>
<td>volcano (dormant or dead)</td>
</tr>
<tr>
<td><strong> tang&rsquo;puāngyeng </strong></td>
<td>elm.CMP</td>
<td>volcano (active)</td>
</tr>
<tr>
<td><strong> tang&rsquo;uamchuai </strong></td>
<td>elm.CMP</td>
<td>sand dune</td>
</tr>
<tr>
<td><strong> tang&rsquo;ue </strong></td>
<td>elm.</td>
<td>ask (for); request; beseech</td>
</tr>
<tr>
<td><strong> tang&rdquo; </strong></td>
<td>elm.</td>
<td>island; isolated segment (of something larger); bump arising from a surface</td>
</tr>
<tr>
<td><strong> tang̦&rdquo;e&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>hill; knoll; bute</td>
</tr>
<tr>
<td><strong> tao </strong></td>
<td>elm.</td>
<td>variant of <strong>ta&rsquo;u</strong> (especially in compounds) the future; future; coming</td>
</tr>
<tr>
<td><strong> tao&rsquo;moa </strong></td>
<td>elm.CMP</td>
<td>forever (into the future); evermore</td>
</tr>
<tr>
<td><strong> Tao&rsquo;nuasao </strong></td>
<td>PN.</td>
<td>Empress</td>
</tr>
<tr>
<td><strong> tao&rsquo;ra </strong></td>
<td>elm.CMP</td>
<td>&ldquo;some day&rdquo;; at some point in the future.</td>
</tr>
<tr>
<td><strong> Tao&rsquo;yusao </strong></td>
<td>PN.</td>
<td>Emperor</td>
</tr>
<tr>
<td><strong> tao&rdquo; </strong></td>
<td>elm.</td>
<td>rein; rule; control</td>
</tr>
<tr>
<td><strong> taong </strong></td>
<td>elm.</td>
<td>remove; subtract from</td>
</tr>
<tr>
<td><strong> taoyo&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>time; the abstract sense of time as a dimension</td>
</tr>
<tr>
<td><strong> te </strong></td>
<td>v.NEU</td>
<td>please</td>
</tr>
<tr>
<td><strong> te </strong></td>
<td>v.FAM</td>
<td>please</td>
</tr>
<tr>
<td><strong> te sā </strong></td>
<td>con.CAS</td>
<td>&ldquo;Please.&rdquo; (lit: &ldquo;It would make me happy.&rdquo;)</td>
</tr>
<tr>
<td><strong> te&rsquo;.ah&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>tantalizing; sexy; &ldquo;hot&rdquo;</td>
</tr>
<tr>
<td><strong> te&rsquo;a </strong></td>
<td>elm.</td>
<td>adult kin (younger); cousin who is jr., younger than oneself</td>
</tr>
<tr>
<td><strong> te&rsquo;an </strong></td>
<td>elm.</td>
<td>skeleton; crust; remains (of something eaten or destroyed)</td>
</tr>
<tr>
<td><strong> te&rsquo;anchiin (te&rsquo;anch.iing&rsquo;a&rsquo;chui) </strong></td>
<td>elm.CMP</td>
<td>atoll</td>
</tr>
<tr>
<td><strong> te&rsquo;anhā </strong></td>
<td>elm.CMP</td>
<td>crater; specifically the crater walls and rim</td>
</tr>
<tr>
<td><strong> te&rsquo;ka </strong></td>
<td>elm.</td>
<td>sticky; wet and gooey (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> tē&rsquo;kui </strong></td>
<td>elm.</td>
<td>arrogance; haughtiness; false-pride; arrogant</td>
</tr>
<tr>
<td><strong> te&rsquo;o </strong></td>
<td>elm.</td>
<td>find; locate; determined; identify</td>
</tr>
<tr>
<td><strong> te&rsquo;o.ka&rdquo; </strong></td>
<td>elm.CMP</td>
<td>locate; discover physically after a search</td>
</tr>
<tr>
<td><strong> te&rsquo;ping </strong></td>
<td>elm.CMP</td>
<td>Dwarf Planet</td>
</tr>
<tr>
<td><strong> te&rsquo;te </strong></td>
<td>elm.CMP</td>
<td>interest (in something)</td>
</tr>
<tr>
<td><strong> te&rsquo;xye </strong></td>
<td>elm.CMP</td>
<td>Moon</td>
</tr>
<tr>
<td><strong> t&#8217;ek </strong></td>
<td>slng.GEN</td>
<td>See <strong>t&rsquo;eng</strong>.</td>
</tr>
<tr>
<td><strong> ten </strong></td>
<td>elm.</td>
<td>food; edible; nourishment</td>
</tr>
<tr>
<td><strong> ten&rsquo;ā </strong></td>
<td>elm.CMP</td>
<td>&#8220;leftovers&#8221;</td>
</tr>
<tr>
<td><strong> ten&rsquo;xyuai </strong></td>
<td>elm.CMP</td>
<td>delicacy; delicacies; gourmet</td>
</tr>
<tr>
<td><strong> ten&rdquo; </strong></td>
<td>elm.</td>
<td>almost; the great majority</td>
</tr>
<tr>
<td><strong> tenchui </strong></td>
<td>elm.CMP</td>
<td>soup; broth</td>
</tr>
<tr>
<td><strong> teng </strong></td>
<td>elm.</td>
<td>halt; stop (re: action or movement). Also <strong>t&rsquo;ek</strong> (a slang term including sense of the speaker being annoyed).</td>
</tr>
<tr>
<td><strong> teth </strong></td>
<td>elm.</td>
<td>planet, world</td>
</tr>
<tr>
<td><strong> teth </strong></td>
<td>elm.CMP</td>
<td>Planet</td>
</tr>
<tr>
<td><strong> teth&rsquo;.au&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>Ice Planet</td>
</tr>
<tr>
<td><strong> tethmuiima </strong></td>
<td>elm.CMP</td>
<td>nature preserve planet</td>
</tr>
<tr>
<td><strong> tethngikyu </strong></td>
<td>elm.CMP</td>
<td>Gas Planet</td>
</tr>
<tr>
<td><strong> teyā </strong></td>
<td>elm.CMP</td>
<td>prefer; preference</td>
</tr>
<tr>
<td><strong> t&#8217;h.at&rsquo;ao </strong></td>
<td>elm.CMP</td>
<td>electronic interface/keyboard (one touches to issue commands, etc)</td>
</tr>
<tr>
<td><strong> tha </strong></td>
<td>elm</td>
<td>plane; surface; board (of wood); fin (of an animal or craft)</td>
</tr>
<tr>
<td><strong> tha&rsquo;h.ūn </strong></td>
<td>elm.CMP</td>
<td>workbench</td>
</tr>
<tr>
<td><strong> thachā&rsquo;e </strong></td>
<td>elm.CMP</td>
<td>monitor/screen (typicaly for generic viewing of entertainment; etc.)</td>
</tr>
<tr>
<td><strong> thai </strong></td>
<td>elm.</td>
<td>ease; easy; simplicity; facile</td>
</tr>
<tr>
<td><strong> thakōl </strong></td>
<td>con.FOR</td>
<td>&ldquo;I insist.&rdquo;</td>
</tr>
<tr>
<td><strong> thakran </strong></td>
<td>elm.CMP</td>
<td>table or desk at which non-manual-labor work is done</td>
</tr>
<tr>
<td><strong> thalā </strong></td>
<td>elm.CMP</td>
<td>easel or digital tablet at which one produces art</td>
</tr>
<tr>
<td><strong> thaloa </strong></td>
<td>elm</td>
<td>table at which one eats</td>
</tr>
<tr>
<td><strong> Thāng </strong></td>
<td>line</td>
<td>Thaang</td>
</tr>
<tr>
<td><strong> thao </strong></td>
<td>elm.</td>
<td>reality; precise truth; essence</td>
</tr>
<tr>
<td><strong> thaoa(chā&rsquo;e) </strong></td>
<td>elm.CMP</td>
<td>screen; computer screen; display that shows information</td>
</tr>
<tr>
<td><strong>thasyu </strong></td>
<td>elm.CMP</td>
<td>wing; wing of a flying vehicle such as a starship</td>
</tr>
<tr>
<td><strong> thāth </strong></td>
<td>con.FOR</td>
<td>&ldquo;Please.&rdquo; (entreatment)</td>
</tr>
<tr>
<td><strong> thāth </strong></td>
<td>elm.</td>
<td>entreatment; begging; supplication</td>
</tr>
<tr>
<td><strong> thatua </strong></td>
<td>elm.CMP</td>
<td>chair</td>
</tr>
<tr>
<td><strong> thauil </strong></td>
<td>elm.CMP</td>
<td>condiments platter (dish in center of table used to hold the many condiments used in Xi&#8217;an meals)</td>
</tr>
<tr>
<td><strong> thaxyam </strong></td>
<td>elm.CMP</td>
<td>access panel/removable wall</td>
</tr>
<tr>
<td><strong> The&rsquo;so </strong></td>
<td>PN.male</td>
<td>Theso</td>
</tr>
<tr>
<td><strong> then </strong></td>
<td>elm.</td>
<td>eye; ocular</td>
</tr>
<tr>
<td><strong> then.u&rsquo;ā&rsquo;uang </strong></td>
<td>elm.CMP</td>
<td>sulfurous; eye-watering; eggy (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> thing </strong></td>
<td>elm.</td>
<td>orifice, specifically <span class="caps">NOT</span> the mouth; anus; operculum</td>
</tr>
<tr>
<td><strong> thingchuaiyeng </strong></td>
<td>elm.CMP</td>
<td>magma vent</td>
</tr>
<tr>
<td><strong> thl.eh&rsquo;a </strong></td>
<td>cnj.</td>
<td>but nonetheless</td>
</tr>
<tr>
<td><strong> Thl.oan </strong></td>
<td>PN.male</td>
<td>Thloan</td>
</tr>
<tr>
<td><strong> thla&rsquo;nua </strong></td>
<td>pn.NEU</td>
<td>she (overt (rare))</td>
</tr>
<tr>
<td><strong> thlai </strong></td>
<td>n.</td>
<td>fermentation vessel (container that can be sealed for long-term fermentation of food. Most important item in Xi&#8217;an kitchen)</td>
</tr>
<tr>
<td><strong> thlaing </strong></td>
<td>elm.</td>
<td>vicera (intestines, organs, etc. from the inside of the bodies of fauna); guts</td>
</tr>
<tr>
<td><strong> thlaingtui </strong></td>
<td>elm.CMP</td>
<td>fermented animal guts (entrails spiced and sealed in a jar for long-term fermenting)</td>
</tr>
<tr>
<td><strong> thlal </strong></td>
<td>rel.</td>
<td>covering; spread over; spread across; draped over</td>
</tr>
<tr>
<td><strong> thlal.au&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>ice sheet (covering a frozen body of water)</td>
</tr>
<tr>
<td><strong> thlalta&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>egg membrane; shell (of an egg specifically)</td>
</tr>
<tr>
<td><strong> thlan </strong></td>
<td>pn.NEU</td>
<td>he/she</td>
</tr>
<tr>
<td><strong> thlan&rsquo;yu </strong></td>
<td>pn.NEU</td>
<td>he (overt (rare))</td>
</tr>
<tr>
<td><strong> thlang </strong></td>
<td>elm.</td>
<td>love; genuine affection (emotional) for people or creatures that can return it</td>
</tr>
<tr>
<td><strong> thlao </strong></td>
<td>elm.</td>
<td>teeth (generic)</td>
</tr>
<tr>
<td><strong> thlao&rsquo;xyun </strong></td>
<td>elm.CMP</td>
<td>teeth for chewing; back teeth</td>
</tr>
<tr>
<td><strong> thlaokyul </strong></td>
<td>elm.CMP</td>
<td>beak</td>
</tr>
<tr>
<td><strong> thlaolui </strong></td>
<td>elm.CMP</td>
<td>sharp teeth</td>
</tr>
<tr>
<td><strong> thle </strong></td>
<td>cnj.</td>
<td>but</td>
</tr>
<tr>
<td><strong> thle&rsquo;a </strong></td>
<td>elm.</td>
<td>propriety</td>
</tr>
<tr>
<td><strong> thlēng </strong></td>
<td>elm.</td>
<td>begin; start; emerge; beginning</td>
</tr>
<tr>
<td><strong> thli </strong></td>
<td>elm.</td>
<td>harnessed energy; electricity; burst of energy; power (for machines)</td>
</tr>
<tr>
<td><strong> thlihyo </strong></td>
<td>elm.CMP</td>
<td>ball lightening</td>
</tr>
<tr>
<td><strong> thliin </strong></td>
<td>elm.</td>
<td>specialized knowledge; (deep) expertise</td>
</tr>
<tr>
<td><strong> thlikyu&rsquo;ām </strong></td>
<td>elm.CMP</td>
<td>sheet lightening (in or above clouds)</td>
</tr>
<tr>
<td><strong> thlilye </strong></td>
<td>elm.CMP</td>
<td>bolt lightning</td>
</tr>
<tr>
<td><strong> thlo </strong></td>
<td>elm.</td>
<td>reason; cause; genesis</td>
</tr>
<tr>
<td><strong> Thlō </strong></td>
<td>line</td>
<td>Thloh</td>
</tr>
<tr>
<td><strong> thlo&rsquo;xy.oa </strong></td>
<td>Q.</td>
<td>why?</td>
</tr>
<tr>
<td><strong> thlohual </strong></td>
<td>elm.CMP</td>
<td>any reason</td>
</tr>
<tr>
<td><strong> thlōm </strong></td>
<td>elm.</td>
<td>clumsiness (opposite of <strong>to&rsquo;ath</strong>)</td>
</tr>
<tr>
<td><strong> thlūn </strong></td>
<td>elm.</td>
<td>heart-soul; spirit; essence of a person (within the body and after death)</td>
</tr>
<tr>
<td><strong> thlyiik </strong></td>
<td>n.</td>
<td>stinging bug (tiny, bright red bugs that are ground up to make a stinging/buzzing seasoning)</td>
</tr>
<tr>
<td><strong> thōa </strong></td>
<td>elm.</td>
<td>decide; decision; make up one&rsquo;s mind</td>
</tr>
<tr>
<td><strong> thōapuo </strong></td>
<td>elm.CMP</td>
<td>guilty (by opinon); convict (of a crime)</td>
</tr>
<tr>
<td><strong> thōayopuo </strong></td>
<td>elm.CMP</td>
<td>innocent (by opinon); find not guilty (of a crime)</td>
</tr>
<tr>
<td><strong> thoth </strong></td>
<td>elm.</td>
<td>irony; ironic</td>
</tr>
<tr>
<td><strong> thyōng </strong></td>
<td>elm.</td>
<td>sad</td>
</tr>
<tr>
<td><strong> ti </strong></td>
<td>rel.</td>
<td>with (in the sense of using a tool)</td>
</tr>
<tr>
<td><strong> ti </strong></td>
<td>elm.</td>
<td>use; make use of; utilize; using</td>
</tr>
<tr>
<td><strong> tia </strong></td>
<td>elm.</td>
<td>number; numeric value; numeric</td>
</tr>
<tr>
<td><strong> tii </strong></td>
<td>v.NEU</td>
<td>equate</td>
</tr>
<tr>
<td><strong> tiing </strong></td>
<td>elm.</td>
<td>medical science</td>
</tr>
<tr>
<td><strong> tiith </strong></td>
<td>num.</td>
<td>eight 8</td>
</tr>
<tr>
<td><strong> tin&rsquo;tang </strong></td>
<td>elm.</td>
<td>difference; different</td>
</tr>
<tr>
<td><strong> ting </strong></td>
<td>rel.</td>
<td>than; compared to</td>
</tr>
<tr>
<td><strong> ting </strong></td>
<td>elm.</td>
<td>comparison; compare; relatively</td>
</tr>
<tr>
<td><strong> tith </strong></td>
<td>elm.</td>
<td>flesh (of an animal (generic term that can include layers of skin+fat+muscle tissue))</td>
</tr>
<tr>
<td><strong> tith&rsquo;.au&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>frostbite</td>
</tr>
<tr>
<td><strong> tō </strong></td>
<td>elm.</td>
<td>business; trade; commerce</td>
</tr>
<tr>
<td><strong> to&rsquo;.e&rsquo;i </strong></td>
<td>rel.</td>
<td>stuck to the side of; huddling right next to</td>
</tr>
<tr>
<td><strong> to&rsquo;ath </strong></td>
<td>elm.</td>
<td>&eacute;lan (grace, professionalism, enthusiasm)</td>
</tr>
<tr>
<td><strong> to&rsquo;athlōm </strong></td>
<td>elm.CMP</td>
<td>normal; average; median; mediocre (of something graded or scored)</td>
</tr>
<tr>
<td><strong> to&rsquo;e </strong></td>
<td>rel.</td>
<td>beside</td>
</tr>
<tr>
<td><strong> tōal </strong></td>
<td>elm.CMP</td>
<td>trade out (sell) &#8211; what you give away when you trade</td>
</tr>
<tr>
<td><strong> tōlo&rsquo;e </strong></td>
<td>elm.CMP</td>
<td>trade in (buy) &#8211; what you receive when you trade</td>
</tr>
<tr>
<td><strong> tōm </strong></td>
<td>elm.</td>
<td>full; replete</td>
</tr>
<tr>
<td><strong> ton </strong></td>
<td>elm.</td>
<td>fuel; energy; nourishment</td>
</tr>
<tr>
<td><strong> tonleth&rsquo;uiiyōn </strong></td>
<td>elm.CMP</td>
<td>Quantum Fuel</td>
</tr>
<tr>
<td><strong> tonten </strong></td>
<td>elm.CMP</td>
<td>nutrients</td>
</tr>
<tr>
<td><strong> tu&rsquo;sem </strong></td>
<td>elm.</td>
<td>fear (angst); worry; sense of uneasiness</td>
</tr>
<tr>
<td><strong> tua </strong></td>
<td>elm.</td>
<td>sit, be seated</td>
</tr>
<tr>
<td><strong> tuai&rsquo;su </strong></td>
<td>elm.</td>
<td>sandy; crumbly; food that breaks apart like sand but dissolves in the mouth (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> tuāl </strong></td>
<td>elm.</td>
<td>dance; fluid (senuous) movement</td>
</tr>
<tr>
<td><strong> tue&rdquo; </strong></td>
<td>vcp.</td>
<td>[hortative (&ldquo;let&rsquo;s (do something)!&rdquo;)</td>
</tr>
<tr>
<td><strong> Tuēl </strong></td>
<td>line</td>
<td>Twayl</td>
</tr>
<tr>
<td><strong> tui </strong></td>
<td>elm</td>
<td>ferment; fermentation; ripe; ripening</td>
</tr
<tr>
<td><strong> tui&rsquo;lui </strong></td>
<td>elm.CMP</td>
<td>sharp claw, talon</td>
</tr>
<tr>
<td><strong> tui&rdquo; </strong></td>
<td>elm.</td>
<td>claw (of an animal); fingernail or toenail (of a person)</td>
</tr>
<tr>
<td><strong> tuing </strong></td>
<td>elm.</td>
<td>cold; frigid</td>
</tr>
<tr>
<td><strong> tuingkyu&rsquo;ā </strong></td>
<td>elm.CMP</td>
<td>wind chill</td>
</tr>
<tr>
<td><strong> tuiping </strong></td>
<td>elm.CMP</td>
<td>cool</td>
</tr>
<tr>
<td><strong> tuithlōm </strong></td>
<td>elm.CMP</td>
<td>foul; incorrectly aged; incorrectly fermented; incorrectly pickled (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> tūn </strong></td>
<td>elm.</td>
<td>intelligence; smart</td>
</tr>
<tr>
<td><strong> tung </strong></td>
<td>elm.</td>
<td>typical; normally ocurring; everyday (thing or situation); general; generic</td>
</tr>
<tr>
<td><strong> tuo </strong></td>
<td>pn.PEJ</td>
<td>he/she</td>
</tr>
<tr>
<td><strong> tuom </strong></td>
<td>pn.PEJ</td>
<td>they</td>
</tr>
<tr>
<td><strong> tuon </strong></td>
<td>v.NEU</td>
<td>want/desire (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> Ty.on </strong></td>
<td>line</td>
<td>Tyon</td>
</tr>
<tr>
<td><strong> tya </strong></td>
<td>elm.</td>
<td>kind; type; version</td>
</tr>
<tr>
<td><strong> tya e Yii&rsquo;ua </strong></td>
<td>idm.</td>
<td>House strain (a strain of yeast, bacteria, and other microorgamisms used to promote flavorful/healthy fermentation. Cultivated by Xi&#8217;an Houses over generations and closely-guarded)</td>
</tr>
<tr>
<td><strong> tya&#8217;xy.oa </strong></td>
<td>Q.</td>
<td>what kind?</td>
</tr>
<tr>
<td><strong> tyahual </strong></td>
<td>elm.CMP</td>
<td>any kind</td>
</tr>
<tr>
<td><strong> tyao </strong></td>
<td>cnj.</td>
<td>or</td>
</tr>
<tr>
<td><strong> Tye&rsquo;lo </strong></td>
<td>name</td>
<td>&ldquo;My Jr.&rdquo; / &ldquo;Cousin&rdquo; (respectful term of address for any adult to whom one is realted who is younger than oneself)</td>
</tr>
<tr>
<td><strong> Tyel&rsquo;na </strong></td>
<td>name</td>
<td>&ldquo;My Jr.&rdquo; / &ldquo;Cousin&rdquo; (respectful term of address for any female to whom one is realted who is younger than oneself)</td>
</tr>
<tr>
<td><strong> Tyel&rsquo;yu </strong></td>
<td>name</td>
<td>&ldquo;My Jr.&rdquo; / &ldquo;Cousin&rdquo; (respectful term of address for any male to whom one is realted who is younger than oneself)</td>
</tr>
<tr>
<td><strong> tyi </strong></td>
<td>elm.</td>
<td>chamber; pocket; enclosing holder; sheath</td>
</tr>
<tr>
<td><strong> tyichuipuāng </strong></td>
<td>elm.CMP</td>
<td>lagoon (of sea water)</td>
</tr>
<tr>
<td><strong> tyihyopyen </strong></td>
<td>elm.CMP</td>
<td>Magazine</td>
</tr>
<tr>
<td><strong> tyiloachui, tyichui </strong></td>
<td>elm.CMP</td>
<td>drinking pouch; &#8220;canteen&#8221;</td>
</tr>
<tr>
<td><strong> tyimuichui </strong></td>
<td>elm.CMP</td>
<td>water tank; canteen (personal)</td>
</tr>
<tr>
<td><strong> tyipuāngchui </strong></td>
<td>elm.CMP</td>
<td>aquifer; natural resevoir (often underground)</td>
</tr>
<tr>
<td><strong> tyipuāngmuichui </strong></td>
<td>elm.CMP</td>
<td>resevoir (intentionally created)</td>
</tr>
<tr>
<td><strong> tyiton </strong></td>
<td>elm.CMP</td>
<td>Fuel Tank</td>
</tr>
<tr>
<td><strong> tyo&rsquo;ma </strong></td>
<td>elm.</td>
<td>culture; unified system of value</td>
</tr>
<tr>
<td><strong> tyon </strong></td>
<td>elm.</td>
<td>come</td>
</tr>
<tr>
<td><strong> tyonxy.a&rsquo;u </strong></td>
<td>elm.CMP</td>
<td>arrive (at a point in time), spend time up to a point</td>
</tr>
<tr>
<td><strong> tyung </strong></td>
<td>elm.</td>
<td>law; legality; rules</td>
</tr>
<tr>
<td><strong> ū </strong></td>
<td>elm.</td>
<td>lust; physical attraction; sexual arousal</td>
</tr>
<tr>
<td><strong> U.al </strong></td>
<td>PN.male</td>
<td>Wal</td>
</tr>
<tr>
<td><strong> u.an.ath </strong></td>
<td>elm.</td>
<td>shock (rage; anger; negative)</td>
</tr>
<tr>
<td><strong> U.e&rsquo;o </strong></td>
<td>PN.feml</td>
<td>We&oacute;</td>
</tr>
<tr>
<td><strong> u.ii </strong></td>
<td>elm.</td>
<td>the unknown; lack of knowledge</td>
</tr>
<tr>
<td><strong> u.in&rsquo;a </strong></td>
<td>elm.</td>
<td>release; letting go; being unfettered; free; unbound</td>
</tr>
<tr>
<td><strong> u.m&rsquo;athle&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>moist; both wet and soft (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> u.o </strong></td>
<td>num.</td>
<td>seven 7</td>
</tr>
<tr>
<td><strong> u.on </strong></td>
<td>elm.</td>
<td>responsibility; perseverance; seeing-it-through</td>
</tr>
<tr>
<td><strong> u&rsquo;ngu </strong></td>
<td>elm.</td>
<td>mucilaginous; slimy; like natto or raw sliced okra (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> u&#8217;ua </strong></td>
<td>v.LAUD</td>
<td>cause/produce/effect</td>
</tr>
<tr>
<td><strong> u&rsquo;nyaxyetao </strong></td>
<td>elm.CMP</td>
<td>future generations (<strong>un nya xye ta&rsquo;u</strong> (<strong>tao</strong>))</td>
</tr>
<tr>
<td><strong> u&rsquo;oalye </strong></td>
<td>elm.CMP</td>
<td>address; give a speech to</td>
</tr>
<tr>
<td><strong> u&rsquo;oalyeyan </strong></td>
<td>elm.CMP</td>
<td>lecture (in an academic setting)</td>
</tr>
<tr>
<td><strong> u&rsquo;to </strong></td>
<td>coj.</td>
<td>to (in the pattern &ldquo;go (<strong>.uai</strong>) to make X,&rdquo; or &ldquo;come (<strong>tyon</strong>) to make Y&rdquo;) contraction of <strong>u (uth) + t.o</strong></td>
</tr>
<tr>
<td><strong> ua </strong></td>
<td>elm.</td>
<td>peace; serenity; calmness; &ldquo;inner peace&rdquo;</td>
</tr>
<tr>
<td><strong> uā&rsquo;uang </strong></td>
<td>elm.</td>
<td>whine; make a fuss over something</td>
</tr>
<tr>
<td><strong> ua&rsquo;yu </strong></td>
<td>pn.REV</td>
<td>he</td>
</tr>
<tr>
<td><strong> Uai&rsquo;i </strong></td>
<td>line</td>
<td>Wy&rsquo;i</td>
</tr>
<tr>
<td><strong> uai&rsquo;sa </strong></td>
<td>elm.</td>
<td>ready; readiness; prepared; set up; all set; standing by</td>
</tr>
<tr>
<td><strong> uain </strong></td>
<td>n.</td>
<td>&#8220;wine&#8221; (borrowed from English &laquo;wine&raquo;)</td>
</tr>
<tr>
<td><strong> uam </strong></td>
<td>elm.</td>
<td>soil; &ldquo;earth&rdquo; (the soil medium); dirt</td>
</tr>
<tr>
<td><strong> uam&rsquo;rath </strong></td>
<td>elm.CMP</td>
<td>landslide</td>
</tr>
<tr>
<td><strong> uamchuai </strong></td>
<td>elm.CMP</td>
<td>sand; granular soil</td>
</tr>
<tr>
<td><strong> uamchuaipuāng </strong></td>
<td>elm.CMP</td>
<td>desert (sandy)</td>
</tr>
<tr>
<td><strong> uamchui </strong></td>
<td>elm.CMP</td>
<td>thin (very liquid) mud</td>
</tr>
<tr>
<td><strong> uamm.e&rsquo;aha&rdquo; </strong></td>
<td>elm.CMP</td>
<td>thick (very viscous) mud</td>
</tr>
<tr>
<td><strong> uampun </strong></td>
<td>elm.CMP</td>
<td>clay</td>
</tr>
<tr>
<td><strong> uan </strong></td>
<td>elm.</td>
<td>comfort; be comfortable</td>
</tr>
<tr>
<td><strong> uang </strong></td>
<td>elm.</td>
<td>wise (through experience and older age); naming infix for older relatives after yue</td>
</tr>
<tr>
<td><strong> uangpyō </strong></td>
<td>elm.CMP</td>
<td>&ldquo;senior sage&rdquo; also <strong>uangpyōhyi</strong> (prestigious senior sage)</td>
</tr>
<tr>
<td><strong> uao </strong></td>
<td>elm.</td>
<td>boss; chief; leader</td>
</tr>
<tr>
<td><strong> uāo </strong></td>
<td>elm.</td>
<td>cry; cry out; howl</td>
</tr>
<tr>
<td><strong> ue </strong></td>
<td>rel.</td>
<td>special version of e with multiple singular attributes</td>
</tr>
<tr>
<td><strong> uē </strong></td>
<td>pn.SRV</td>
<td>We (inclusive)</td>
</tr>
<tr>
<td><strong> ue&rsquo;a </strong></td>
<td>elm.</td>
<td>describe; talk about; tell about; present</td>
</tr>
<tr>
<td><strong> uea&rsquo;xyuai </strong></td>
<td>elm.CMP</td>
<td>vegetarian dishes composed of exotic ingredients</td>
</tr>
<tr>
<td><strong> uea&rsquo;yēl </strong></td>
<td>elm.CMP</td>
<td>leaf noodle dish (traditional meal made from pickled strips of the nga.u&rsquo;ii&rsquo;yēl leaf)</td>
</tr>
<tr>
<td><strong> uea&rdquo; </strong></td>
<td>elm.</td>
<td>prepared dish composed (primarily) of vegetables; vegetarian food; &#8220;salad&#8221;</td>
</tr>
<tr>
<td><strong> uea&rdquo;hai&#8217;pe(tui) </strong></td>
<td>elm.CMP</td>
<td>(fermented) tea leaf dish (traditional dish used as appetizer or palate cleanser; Houses have very old, closely-guarded versions of this dish)</td>
</tr>
<tr>
<td><strong> uen </strong></td>
<td>pn.REV</td>
<td>she</td>
</tr>
<tr>
<td><strong> ueng </strong></td>
<td>elm.</td>
<td>hair; fur (of an animal or humanoid)</td>
</tr>
<tr>
<td><strong> uengTuēl </strong></td>
<td>n.</td>
<td>Xi&rsquo;an &ldquo;cashmere/silk&rdquo; wool (in its freshly harvested raw form)</td>
</tr>
<tr>
<td><strong> ueth </strong></td>
<td>nlz.</td>
<td>[objective]</td>
</tr>
<tr>
<td><strong> ueth </strong></td>
<td>elm.</td>
<td>target; objective</td>
</tr>
<tr>
<td><strong> ui&rsquo;la </strong></td>
<td>col.</td>
<td>umber</td>
</tr>
<tr>
<td><strong> uil </strong></td>
<td>elm.</td>
<td>spice; spices; flavor-adding substances; condiments (general term)</td>
</tr>
<tr>
<td><strong> uil.&rsquo;ii </strong></td>
<td>elm.CMP</td>
<td>herb; herbs</td>
</tr>
<tr>
<td><strong> uil&rsquo;ki.s&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>ammonia sauce (complex condiment that grants ammoniac flavor to food_</td>
</tr>
<tr>
<td><strong> uilchui </strong></td>
<td>elm.CMP</td>
<td>liquid aminos (savory liquid used to add flavor to food)</td>
</tr>
<tr>
<td><strong> uilpyenpun </strong></td>
<td>elm.CMP</td>
<td>powdered minerals (used for seasoning food)</td>
</tr>
<tr>
<td><strong> uilyāi </strong></td>
<td>n.</td>
<td>glop sauce (thick and slimy sauce that can be poured over food or used for dipping; Xi&#8217;an Houses have old, closely-guarded recipes)</td>
</tr>
<tr>
<td><strong> uin&rsquo;tung </strong></td>
<td>elm.CMP</td>
<td>room temperature (30 C)</td>
</tr>
<tr>
<td><strong> uin&rdquo; </strong></td>
<td>elm.</td>
<td>temperature</td>
</tr>
<tr>
<td><strong> uing </strong></td>
<td>elm.</td>
<td>incoming; internal; interior; arrive; enter; import</td>
</tr>
<tr>
<td><strong> uingka&rsquo;Xa; uingXa </strong></td>
<td>elm.CMP</td>
<td>Jump Point</td>
</tr>
<tr>
<td><strong> un </strong></td>
<td>elm.</td>
<td>set; collection; series</td>
</tr>
<tr>
<td><strong> unch.uaiy&rsquo;o </strong></td>
<td>elm.CMP</td>
<td>coral reef</td>
</tr>
<tr>
<td><strong> unchui(e&rsquo;nu) </strong></td>
<td>elm.CMP</td>
<td>pool</td>
</tr>
<tr>
<td><strong> unhankeng </strong></td>
<td>elm.CMP</td>
<td>atlas</td>
</tr>
<tr>
<td><strong> unk.eng&rsquo;a&rsquo;chui </strong></td>
<td>elm.CMP</td>
<td>archipelago</td>
</tr>
<tr>
<td><strong> unkengpuāng </strong></td>
<td>elm.CMP</td>
<td>continent</td>
</tr>
<tr>
<td><strong> unkyu&rsquo;ām </strong></td>
<td>elm.CMP</td>
<td>cloud; cloudy</td>
</tr>
<tr>
<td><strong> unngaoii </strong></td>
<td>elm.CMP</td>
<td>solar collector; solar panel; solar array</td>
</tr>
<tr>
<td><strong> unxauo&rsquo;.a&rsquo;e&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>a phrase (a subset of a sentence (also <strong>unuo&rsquo;.a&rsquo;e&rsquo;nu</strong>)</td>
</tr>
<tr>
<td><strong> unxauo&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>sentence (a string of words)</td>
</tr>
<tr>
<td><strong> uo </strong></td>
<td>cnj.</td>
<td>to (in the pattern &ldquo;go (<strong>.uai</strong>) to do X,&rdquo; or &ldquo;come (<strong>tyon</strong>) to do Y&rdquo;) contraction of <strong>u (uth) + o</strong></td>
</tr>
<tr>
<td><strong> uo&rsquo;a </strong></td>
<td>elm.</td>
<td>speech; talking; speak; talk say</td>
</tr>
<tr>
<td><strong> Uo&rsquo;al </strong></td>
<td>PN.male</td>
<td>W&oacute;al</td>
</tr>
<tr>
<td><strong> uōching </strong></td>
<td>elm.CMP</td>
<td>confess; tell the truth; admit (something)</td>
</tr>
<tr>
<td><strong> uong </strong></td>
<td>elm.</td>
<td>bits; particles; dust; fragments</td>
</tr>
<tr>
<td><strong> uōng </strong></td>
<td>elm.</td>
<td>urinate; deficate; spit; eject (liquid)</td>
</tr>
<tr>
<td><strong> uongyonai </strong></td>
<td>elm.CMP</td>
<td>Chaff</td>
</tr>
<tr>
<td><strong> uoth&rdquo; </strong></td>
<td>elm.</td>
<td>stomach; belly; craw</td>
</tr>
<tr>
<td><strong> uth (u) </strong></td>
<td>cnj.</td>
<td>and</td>
</tr>
<tr>
<td><strong> uth (u) </strong></td>
<td>elm.</td>
<td>add</td>
</tr>
<tr>
<td><strong> x.ū </strong></td>
<td>v.REV</td>
<td>try/attempt (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> x.uith&rsquo;ii&rsquo;xye </strong></td>
<td>elm.CMP</td>
<td>sprout; shoot</td>
</tr>
<tr>
<td><strong> X&rsquo;yan </strong></td>
<td>elm.</td>
<td>Xi&rsquo;an (formal abbreviation)</td>
</tr>
<tr>
<td><strong> X&rsquo;yan </strong></td>
<td>elm.</td>
<td>Xi&rsquo;an (official abbreviation used by the Xi&rsquo;an)</td>
</tr>
<tr>
<td><strong> Xa </strong></td>
<td>name</td>
<td>nano-second</td>
</tr>
<tr>
<td><strong> xa. </strong></td>
<td>nlz.CLTC</td>
<td>[simple tool or biological organ for X]</td>
</tr>
<tr>
<td><strong> xā&rsquo;ye </strong></td>
<td>elm.</td>
<td>rigid; firm; unbending; hard; crunchy (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> xān </strong></td>
<td>elm.</td>
<td>confident; bold;</td>
</tr>
<tr>
<td><strong> xauo&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>word; discrete part of speech (divided by spaces (also <strong>taiuo&rsquo;a</strong> in the technical sense))</td>
</tr>
<tr>
<td><strong> xauo&rsquo;alue </strong></td>
<td>elm.CMP</td>
<td>relational particle or elemental used in this fashion (also <strong>taiuo&rsquo;alue</strong> and <strong>taixauo&rsquo;alue</strong>)</td>
</tr>
<tr>
<td><strong> xaxuan </strong></td>
<td>elm.CMP</td>
<td>toy (as children might play with); piece of sports equipment</td>
</tr>
<tr>
<td><strong> xē&rsquo;loa </strong></td>
<td>elm.CMP</td>
<td>meal; dining experience</td>
</tr>
<tr>
<td><strong> xe&rsquo;ri </strong></td>
<td>elm.</td>
<td>clever; smart; creative</td>
</tr>
<tr>
<td><strong> xē&rsquo;s.o&rsquo;e </strong></td>
<td>elm.CMP</td>
<td>collaboration; cooperation; cooperative; cooperate</td>
</tr>
<tr>
<td><strong> xē&rsquo;suelen </strong></td>
<td>con.FOR</td>
<td>&ldquo;Greetings&rdquo; &ldquo;How do you do&rdquo;</td>
</tr>
<tr>
<td><strong> xē&rsquo;sueren </strong></td>
<td>con.SEMFOR</td>
<td>&ldquo;Greetings&rdquo; &ldquo;How do you do&rdquo;</td>
</tr>
<tr>
<td><strong> xe&rsquo;thlūn </strong></td>
<td>elm.</td>
<td>commune; connect deeply (emotionally)</td>
</tr>
<tr>
<td><strong> xē&rdquo; </strong></td>
<td>elm.</td>
<td>meeting; coming together; joining</td>
</tr>
<tr>
<td><strong> xēl </strong></td>
<td>elm.</td>
<td>impress; impressive; amaze; amazing; (interjection: &ldquo;Wow!&rdquo; or &ldquo;Whoa!&rdquo;)</td>
</tr>
<tr>
<td><strong> xēlxān </strong></td>
<td>elm.CMP</td>
<td>shock; overwhelm</td>
</tr>
<tr>
<td><strong> xi.&rsquo;oka&rsquo;ra </strong></td>
<td>n.</td>
<td>shiokara (borrowed from Japanese &laquo;shiokara&raquo;)</td>
</tr>
<tr>
<td><strong> Xi&rsquo;an </strong></td>
<td>elm.</td>
<td>Xi&rsquo;an</td>
</tr>
<tr>
<td><strong> xii </strong></td>
<td>rel.</td>
<td>at a point in time (of the clock)</td>
</tr>
<tr>
<td><strong> xii </strong></td>
<td>chj.</td>
<td>when (point in time)</td>
</tr>
<tr>
<td><strong> xii </strong></td>
<td>elm.</td>
<td>a point or some points in time</td>
</tr>
<tr>
<td><strong> xii&rsquo;hyan </strong></td>
<td>elm.CMP</td>
<td>always; consistently (from <strong>xii e hyan</strong>)</td>
</tr>
<tr>
<td><strong> xii&rsquo;ra </strong></td>
<td>elm.CMP</td>
<td>sometime; sometimes (from <strong>xii e ra</strong>)</td>
</tr>
<tr>
<td><strong> xii&rsquo;xi </strong></td>
<td>elm.CMP</td>
<td>often; a lot; all the time</td>
</tr>
<tr>
<td><strong> xii&rsquo;xy.oa </strong></td>
<td>Q.</td>
<td>when (at what (point in) time?</td>
</tr>
<tr>
<td><strong> xiihual </strong></td>
<td>elm.CMP</td>
<td>whenever</td>
</tr>
<tr>
<td><strong> xiin </strong></td>
<td>elm.</td>
<td>writing; composing</td>
</tr>
<tr>
<td><strong> xiin&rsquo;t.osy&rsquo;e&rsquo;yan </strong></td>
<td>elm.CMP</td>
<td>introduction</td>
</tr>
<tr>
<td><strong> xiiyā </strong></td>
<td>elm.CMP</td>
<td>again (adv.); o xiiya (repeat); o xiiyāxue&rsquo;a (update)</td>
</tr>
<tr>
<td><strong> xiiyāxue&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>renewal; update</td>
</tr>
<tr>
<td><strong> xo&rsquo;ma </strong></td>
<td>elm.</td>
<td>success; succeed; win (a competitino)</td>
</tr>
<tr>
<td><strong> xo&rsquo;xyo </strong></td>
<td>elm.</td>
<td>similarity</td>
</tr>
<tr>
<td><strong> xōm </strong></td>
<td>elm.</td>
<td>bother; harass; antagonize; &ldquo;troll&rdquo;</td>
</tr>
<tr>
<td><strong> xu </strong></td>
<td>v.NEU</td>
<td>try/attempt (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> xua </strong></td>
<td>v.FAM</td>
<td>need (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> xuā&rsquo;cha </strong></td>
<td>elm.</td>
<td>fire; burning; combustion</td>
</tr>
<tr>
<td><strong> xuai </strong></td>
<td>elm.</td>
<td>give (sense of hand over; deliver)</td>
</tr>
<tr>
<td><strong> xuan </strong></td>
<td>elm.</td>
<td>game; play; fun</td>
</tr>
<tr>
<td><strong> xue&rsquo;a </strong></td>
<td>elm.</td>
<td>new; novel; innovation</td>
</tr>
<tr>
<td><strong> xuel </strong></td>
<td>elm.</td>
<td>a portion that is carved out; to carve; dig; a hole</td>
</tr>
<tr>
<td><strong> xuel&rsquo;hā </strong></td>
<td>elm.CMP</td>
<td>crater; the area inside a crater</td>
</tr>
<tr>
<td><strong> xuelch.ui&rsquo;e&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>pond</td>
</tr>
<tr>
<td><strong> xuelch.ui&rsquo;ō&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>great lake</td>
</tr>
<tr>
<td><strong> xuelchui </strong></td>
<td>elm.CMP</td>
<td>lake; pond</td>
</tr>
<tr>
<td><strong> xuelchuipuāng </strong></td>
<td>elm.CMP</td>
<td>bay; gulf</td>
</tr>
<tr>
<td><strong> xuelchuipuāng </strong></td>
<td>elm.CMP</td>
<td>inland sea</td>
</tr>
<tr>
<td><strong> xuelkengpuāng </strong></td>
<td>elm.CMP</td>
<td>canyon</td>
</tr>
<tr>
<td><strong> xuelpenchui </strong></td>
<td>elm.CMP</td>
<td>erosion</td>
</tr>
<tr>
<td><strong> xueltaong </strong></td>
<td>elm.CMP</td>
<td>a mine</td>
</tr>
<tr>
<td><strong> xueltaongpyen </strong></td>
<td>elm.CMP</td>
<td>an ore mine; mine for (precious) metals</td>
</tr>
<tr>
<td><strong> xui </strong></td>
<td>v.FAM</td>
<td>try/attempt (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> xui&rsquo;a </strong></td>
<td>elm.</td>
<td>shake; tremble; vibrate</td>
</tr>
<tr>
<td><strong> xui&rsquo;ak.eng&rsquo;e&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>minor earthquake; seismic tremors</td>
</tr>
<tr>
<td><strong> xui&rsquo;akeng </strong></td>
<td>elm.CMP</td>
<td>earthquake; seismic activity; tremor</td>
</tr>
<tr>
<td><strong> xui&rsquo;akengpuāng </strong></td>
<td>elm.CMP</td>
<td>major earthquake (of a disaster level)</td>
</tr>
<tr>
<td><strong> xuith </strong></td>
<td>elm.</td>
<td>axis; centerline</td>
</tr>
<tr>
<td><strong> xuithe&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>branch</td>
</tr>
<tr>
<td><strong> xuithō&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>trunk</td>
</tr>
<tr>
<td><strong> xuithpui&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>stem</td>
</tr>
<tr>
<td><strong> xuo </strong></td>
<td>elm.</td>
<td>period (of time); season</td>
</tr>
<tr>
<td><strong> xuochui&rsquo;rath </strong></td>
<td>elm.CMP</td>
<td>monsoon; seasonal wind; tropical rainy season</td>
</tr>
<tr>
<td><strong> xy.ai </strong></td>
<td>num.</td>
<td>hundred thousand 100,000</td>
</tr>
<tr>
<td><strong> xy.ams&rsquo;a&rsquo;uo </strong></td>
<td>elm.CMP</td>
<td>cliff (as experienced from the bottom)</td>
</tr>
<tr>
<td><strong> xy.ii&rsquo;u(ang)/(pyō) </strong></td>
<td>elm.CMP</td>
<td>great great great grandmother (mother&rsquo;s lineage)</td>
</tr>
<tr>
<td><strong> xy.iikua(p&rsquo;yō) </strong></td>
<td>elm.CMP</td>
<td>great great great great grandmother (mother&rsquo;s lineage)</td>
</tr>
<tr>
<td><strong> xy.iip&rsquo;ua(ng) </strong></td>
<td>elm.CMP</td>
<td>great great grandmother (mother&rsquo;s lineage)</td>
</tr>
<tr>
<td><strong> xy.iis&rsquo;ye </strong></td>
<td>elm.CMP</td>
<td>great grandmother (mother&rsquo;s lineage)</td>
</tr>
<tr>
<td><strong> xy.iiy&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>grandmother (mother&rsquo;s mother)</td>
</tr>
<tr>
<td><strong> xy.ik </strong></td>
<td>elm.</td>
<td>astringent; drying; tannic (considered a favorable flavor)</td>
</tr>
<tr>
<td><strong> Xy.ō </strong></td>
<td>line</td>
<td>Shoh</td>
</tr>
<tr>
<td><strong> xy.oa </strong></td>
<td>Q.sffx</td>
<td>which (what)?</td>
</tr>
<tr>
<td><strong> xy.uai </strong></td>
<td>elm.</td>
<td>special; rare; extraordinary; a treat</td>
</tr>
<tr>
<td><strong> xy.un </strong></td>
<td>elm.</td>
<td>chew; chewing (typically in a &lsquo;munching&rsquo; or &lsquo;crunching&rsquo; manner that makes noise); masticate; grind</td>
</tr>
<tr>
<td><strong> Xyā&rsquo;xya </strong></td>
<td>name</td>
<td>&#8220;Granny&rdquo;/&ldquo;Nana&rdquo; (endearment term used by children for any grand-mother)</td>
</tr>
<tr>
<td><strong> xyam </strong></td>
<td>elm.</td>
<td>barrier; wall; shield</td>
</tr>
<tr>
<td><strong> xyang </strong></td>
<td>cnj.</td>
<td>due to the matter of</td>
</tr>
<tr>
<td><strong> xyao </strong></td>
<td>elm.</td>
<td>mean; meaning; semantic; signify; significance</td>
</tr>
<tr>
<td><strong> xye </strong></td>
<td>elm.</td>
<td>child; immaturity</td>
</tr>
<tr>
<td><strong> xyē&rsquo;na </strong></td>
<td>elm.</td>
<td>relax and have a good time; chill out; relaxation</td>
</tr>
<tr>
<td><strong> xye&rsquo;pi </strong></td>
<td>elm.CMP</td>
<td>infant; baby; pre-toddler (of a stranger or any unrelated person)</td>
</tr>
<tr>
<td><strong> xye&rsquo;uai </strong></td>
<td>elm.CMP</td>
<td>toddler; young child who has begun to walk</td>
</tr>
<tr>
<td><strong> xyengea </strong></td>
<td>elm.CMP</td>
<td>developing fetus (in an egg)</td>
</tr>
<tr>
<td><strong> xyi </strong></td>
<td>rel.</td>
<td>from; eminating from; starting with</td>
</tr>
<tr>
<td><strong> xyiing </strong></td>
<td>elm.</td>
<td>wild; raw; fresh; untamed; untameable; food that hasn&#8217;t been aged (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> xyo </strong></td>
<td>elm.</td>
<td>home; residence</td>
</tr>
<tr>
<td><strong> xyo.y&rsquo;en </strong></td>
<td>elm.CMP</td>
<td>rented/tempoary houseing; an apartment; a dormitory; etc.</td>
</tr>
<tr>
<td><strong> xyo&rsquo;yu </strong></td>
<td>n.</td>
<td>soy sauce (borrowed from Japanese &laquo;shoyu&raquo;) See also: so&rsquo;ichui.r&rsquo;o&rsquo;ang</td>
</tr>
<tr>
<td><strong> xyopuānghui </strong></td>
<td>elm.</td>
<td>apartment complex</td>
</tr>
<tr>
<td><strong> xyū </strong></td>
<td>v.LAUD</td>
<td>do</td>
</tr>
<tr>
<td><strong> xyun.xy&rsquo;un </strong></td>
<td>idm.</td>
<td>spongy; rubbery (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> y.a&rsquo;u </strong></td>
<td>deix.</td>
<td>this (after an indicated noun)</td>
</tr>
<tr>
<td><strong> Y.ah&rsquo;a </strong></td>
<td>PN.feml</td>
<td>Yah&aacute;</td>
</tr>
<tr>
<td><strong> y.an </strong></td>
<td>elm.</td>
<td>rise/ascend/go up/lift</td>
</tr>
<tr>
<td><strong> y.āng </strong></td>
<td>elm.</td>
<td>sleep; rest; uncounscious</td>
</tr>
<tr>
<td><strong> y.e </strong></td>
<td>cnj.</td>
<td>while (durative)</td>
</tr>
<tr>
<td><strong> y.e&rsquo;a </strong></td>
<td>deix.</td>
<td>yon (away from both of us) (after an indicated noun)</td>
</tr>
<tr>
<td><strong> y.e&rsquo;i </strong></td>
<td>elm.</td>
<td>convex; bulge</td>
</tr>
<tr>
<td><strong> y.e&rsquo;i&rsquo;uam </strong></td>
<td>elm.CMP</td>
<td>mound (of soil)</td>
</tr>
<tr>
<td><strong> y.ēl </strong></td>
<td>elm.</td>
<td>fiber; fiberous; string; stringy; thread (of sewing) (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> y.i&rsquo;i </strong></td>
<td>col.</td>
<td>eburnian</td>
</tr>
<tr>
<td><strong> y.iy&rsquo;a </strong></td>
<td>elm.</td>
<td>texture</td>
</tr>
<tr>
<td><strong> y.iy&rsquo;a&rsquo;yuo </strong></td>
<td>elm.CMP</td>
<td>too firm; can&#8217;t be cut without effort (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> y.iy&rsquo;atin&rsquo;tang </strong></td>
<td>elm.CMP</td>
<td>multitextured; an agreeable mixture of textures</td>
</tr>
<tr>
<td><strong> y.om </strong></td>
<td>elm.</td>
<td>tunnel; hallway; passageway connecting rooms or caves; tubing</td>
</tr>
<tr>
<td><strong> y.omt&rsquo;on </strong></td>
<td>elm.CMP</td>
<td>fuel line</td>
</tr>
<tr>
<td><strong> y.omt&rsquo;onlo&rsquo;e </strong></td>
<td>elm.CMP</td>
<td>Fuel Intake</td>
</tr>
<tr>
<td><strong> y.omX&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>Jump Tunnel</td>
</tr>
<tr>
<td><strong> y.ong </strong></td>
<td>elm.</td>
<td>point (in physical space); location (on a map, etc.)</td>
</tr>
<tr>
<td><strong> y.ongk&rsquo;ilo&rsquo;e </strong></td>
<td>elm.CMP</td>
<td>Hardpoint</td>
</tr>
<tr>
<td><strong> y.ongs&rsquo;ānxuith </strong></td>
<td>elm.CMP</td>
<td>pole (north or south)</td>
</tr>
<tr>
<td><strong> y.ongx&rsquo;uith&rsquo;r.ath </strong></td>
<td>elm.CMP</td>
<td>South Pole</td>
</tr>
<tr>
<td><strong> y.ongx&rsquo;uith&rsquo;y.an </strong></td>
<td>elm.CMP</td>
<td>North Pole</td>
</tr>
<tr>
<td><strong> Y.ū </strong></td>
<td>PN.male</td>
<td>Yuu</td>
</tr>
<tr>
<td><strong> y.ui </strong></td>
<td>rel.</td>
<td>in response to</td>
</tr>
<tr>
<td><strong> y.un&rsquo;i </strong></td>
<td>elm.</td>
<td>alternate; option; other; another (different) one</td>
</tr>
<tr>
<td><strong> y.uo </strong></td>
<td>elm.</td>
<td>excess; exceed; excessive; surpluss; glut (too; too much: <strong>e ku&rsquo;ya y.uo R.ēth</strong> (Rayth is too rude (vis-&agrave;-vis his general character).)</td>
</tr>
<tr>
<td><strong> Y&rsquo;ū </strong></td>
<td>name</td>
<td>&ldquo;Hubs&rdquo;/&ldquo;Husby&rdquo;/&ldquo;Man&rdquo; (to a male from a male partner (typically))</td>
</tr>
<tr>
<td><strong> ya </strong></td>
<td>elm.</td>
<td>sense; detect; intuit (from avaialbe information)</td>
</tr>
<tr>
<td><strong> ya </strong></td>
<td>elm.SRV</td>
<td>&ldquo;epic&rdquo; (holy, in the sense of &lsquo;beyond belief&rsquo;)</td>
</tr>
<tr>
<td><strong> yā </strong></td>
<td>elm.</td>
<td>more</td>
</tr>
<tr>
<td><strong> ya&rsquo;i </strong></td>
<td>v.LAUD</td>
<td>need (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> yā&rsquo;i </strong></td>
<td>elm.</td>
<td>patience and perseverence</td>
</tr>
<tr>
<td><strong> ya&rsquo;nai </strong></td>
<td>elm.CMP</td>
<td>learn; commit to memory</td>
</tr>
<tr>
<td><strong> yā&rsquo;suith </strong></td>
<td>elm.</td>
<td>fright; terror (sense of external threat (<strong>yiyā’suith</strong> = “terrorism; policy of engendering fear”)</td>
</tr>
<tr>
<td><strong> ya&rsquo;t.at&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>eggshell</td>
</tr>
<tr>
<td><strong> ya&rsquo;t.aT&rsquo;uēl </strong></td>
<td>n.</td>
<td>Xi&rsquo;an &ldquo;cashmere/silk&rdquo; fabric</td>
</tr>
<tr>
<td><strong> ya&rsquo;ta </strong></td>
<td>elm.</td>
<td>cloth; fabric; organic membane (<strong>o ya&rsquo;ta</strong>: weave)</td>
</tr>
<tr>
<td><strong> ya&rsquo;than </strong></td>
<td>col.</td>
<td>caesious</td>
</tr>
<tr>
<td><strong> yai </strong></td>
<td>rel.</td>
<td>regarding; about; on the matter of</td>
</tr>
<tr>
<td><strong> yāi </strong></td>
<td>elm.</td>
<td>clothing; garments</td>
</tr>
<tr>
<td><strong> yāihyao; yāisēnghyao; yāisēngkahyao </strong></td>
<td>elm.CMP</td>
<td>Space Suit</td>
</tr>
<tr>
<td><strong> yāiuengTuēl </strong></td>
<td>n.</td>
<td>Xi&rsquo;an &ldquo;cashmere/silk&rdquo; garments made famous by House Twayl (<strong>Tuēl</strong>)</td>
</tr>
<tr>
<td><strong> yal </strong></td>
<td>elm.</td>
<td>sentient being; sentient; posessing consciousness</td>
</tr>
<tr>
<td><strong> yāl </strong></td>
<td>elm.</td>
<td>female sex; female organ</td>
</tr>
<tr>
<td><strong> yal&rsquo;ma </strong></td>
<td>elm.CMP</td>
<td>animal (with which a relationshiop is possible); pet</td>
</tr>
<tr>
<td><strong> yalnya </strong></td>
<td>elm.CMP</td>
<td>&ldquo;a people&rdquo;; race; species (of intelligent creatures with culture)</td>
</tr>
<tr>
<td><strong> yalyuai </strong></td>
<td>elm.CMP</td>
<td>an &ldquo;alien intelligence&rdquo;; sentience (of an unidentified nature)</td>
</tr>
<tr>
<td><strong> yan </strong></td>
<td>elm.</td>
<td>study; examine closely</td>
</tr>
<tr>
<td><strong> yāng̦ </strong></td>
<td>pn.NEU</td>
<td>we (exclusive)</td>
</tr>
<tr>
<td><strong> yankeng </strong></td>
<td>elm.CMP</td>
<td>geography</td>
</tr>
<tr>
<td><strong> yannukeng </strong></td>
<td>elm.CMP</td>
<td>topology</td>
</tr>
<tr>
<td><strong> yao </strong></td>
<td>vcp.</td>
<td>[abilitive (&ldquo;can&rdquo;)] <strong>yaol</strong></td>
</tr>
<tr>
<td><strong> yao </strong></td>
<td>elm.</td>
<td>ability; skill</td>
</tr>
<tr>
<td><strong> yao&rsquo;yao </strong></td>
<td>n.</td>
<td>nickname for the <strong>ngii</strong>, a common Xi&rsquo;an pet animal</td>
</tr>
<tr>
<td><strong> yaonai e ti ngisi&rsquo;pe; naitingsi&rsquo;pe </strong></td>
<td>elm.CMP</td>
<td>Infrared</td>
</tr>
<tr>
<td><strong> yath </strong></td>
<td>num.</td>
<td>one 1</td>
</tr>
<tr>
<td><strong> ye </strong></td>
<td>elm.</td>
<td>a generic day (not necessarily corresponding to celestial movements)</td>
</tr>
<tr>
<td><strong> ye&rsquo;a </strong></td>
<td>elm.</td>
<td>pluck; tweeze; tongs; pincer</td>
</tr>
<tr>
<td><strong> ye&rsquo;a&bull;oten </strong></td>
<td>elm.CMP</td>
<td>cooking tongs</td>
</tr>
<tr>
<td><strong> ye&rsquo;ahuen </strong></td>
<td>elm.CMP</td>
<td>serving tongs</td>
</tr>
<tr>
<td><strong> ye&rsquo;aloa </strong></td>
<td>elm.CMP</td>
<td>eating tongs</td>
</tr>
<tr>
<td><strong> ye&rsquo;u </strong></td>
<td>elm.</td>
<td>concave; dip; depression</td>
</tr>
<tr>
<td><strong> Ye&rsquo;ua </strong></td>
<td>line</td>
<td>Yewa</td>
</tr>
<tr>
<td><strong> ye&rsquo;uchuiyuao </strong></td>
<td>elm.CMP</td>
<td>whirlpool</td>
</tr>
<tr>
<td><strong> ye&rsquo;ukyuyuao </strong></td>
<td>elm.CMP</td>
<td>wind vortex</td>
</tr>
<tr>
<td><strong> ye&rsquo;uyuao </strong></td>
<td>elm.CMP</td>
<td>vortex</td>
</tr>
<tr>
<td><strong> yeā </strong></td>
<td>v.IMP</td>
<td>do</td>
</tr>
<tr>
<td><strong> yekrū </strong></td>
<td>v.IMP</td>
<td>need (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> yem&rsquo;pi; chairinthli </strong></td>
<td>elm.CMP</td>
<td>Distortion Damage</td>
</tr>
<tr>
<td><strong> yemā </strong></td>
<td>v.IMP</td>
<td>try/attempt (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> yen </strong></td>
<td>cnj.</td>
<td>as X (of &ldquo;as X as Y&rdquo;)</td>
</tr>
<tr>
<td><strong> yen _____ yon _____ </strong></td>
<td>cnj.</td>
<td>as X as Y</td>
</tr>
<tr>
<td><strong> yen&rdquo; </strong></td>
<td>elm.</td>
<td>temporary; impermaent; fading (of colors, etc.)</td>
</tr>
<tr>
<td><strong> yeng </strong></td>
<td>elm.</td>
<td>fire; burn</td>
</tr>
<tr>
<td><strong> yeng&#8217;tu </strong></td>
<td>n.</td>
<td>a type of flying insectoid with a painful, burning sting</td>
</tr>
<tr>
<td><strong> yenū </strong></td>
<td>v.IMP</td>
<td>be of a class</td>
</tr>
<tr>
<td><strong> yeōn </strong></td>
<td>v.IMP</td>
<td>cause/produce/effect</td>
</tr>
<tr>
<td><strong> yepa </strong></td>
<td>elm.CMP</td>
<td>yesterday</td>
</tr>
<tr>
<td><strong> yepa </strong></td>
<td>elm.CMP</td>
<td>yesterday</td>
</tr>
<tr>
<td><strong> yesā </strong></td>
<td>v.IMP</td>
<td>eminate/reflect</td>
</tr>
<tr>
<td><strong> yesye </strong></td>
<td>elm.CMP</td>
<td>tomorrow</td>
</tr>
<tr>
<td><strong> yesye </strong></td>
<td>elm.CMP</td>
<td>tomorrow</td>
</tr>
<tr>
<td><strong> yeth </strong></td>
<td>elm.</td>
<td>knowledge; awareness</td>
</tr>
<tr>
<td><strong> yethē </strong></td>
<td>v.IMP</td>
<td>please</td>
</tr>
<tr>
<td><strong> yetō </strong></td>
<td>v.IMP</td>
<td>want/desire (&rsaquo;&rsaquo;&rsaquo; <strong>yo _____</strong>)</td>
</tr>
<tr>
<td><strong> yeyiing </strong></td>
<td>v.IMP</td>
<td>equate</td>
</tr>
<tr>
<td><strong> yi </strong></td>
<td>elm.</td>
<td>belief; adherence to</td>
</tr>
<tr>
<td><strong> yi. </strong></td>
<td>nlz.CLTC</td>
<td>[&ldquo;-ism&rdquo;/&ldquo;-ity&rdquo;]; system of; belief in; dogma of X; affinity or proclivity towards X</td>
</tr>
<tr>
<td><strong> yi&rsquo;.ān </strong></td>
<td>elm.</td>
<td>beautiful; attractive; compelling; beauty</td>
</tr>
<tr>
<td><strong> yi&rsquo;a </strong></td>
<td>elm.</td>
<td>convey; transmit; communicate; message</td>
</tr>
<tr>
<td><strong> yi&rsquo;achuokyu </strong></td>
<td>elm.CMP</td>
<td>weather advisory</td>
</tr>
<tr>
<td><strong> yi&rsquo;kr.ōng </strong></td>
<td>elm.CMP</td>
<td>barbarism; brutality; savegry (as dogma or policy)</td>
</tr>
<tr>
<td><strong> yi&rsquo;o </strong></td>
<td>v.LAUD</td>
<td>please</td>
</tr>
<tr>
<td><strong> yi&rsquo;oa </strong></td>
<td>n.</td>
<td>data</td>
</tr>
<tr>
<td><strong> yi&rsquo;p.ūh&rsquo;yath </strong></td>
<td>elm.CMP</td>
<td>the military (defense) branch of the bureaucracy</td>
</tr>
<tr>
<td><strong> yi&rsquo;p.ūt&rsquo;ung </strong></td>
<td>elm.CMP</td>
<td>the general bureaucracy (non-military service)</td>
</tr>
<tr>
<td><strong> yii&rsquo;lai </strong></td>
<td>elm.CMP</td>
<td>non-kindred</td>
</tr>
<tr>
<td><strong> Yii&rsquo;ua </strong></td>
<td>elm.CMP</td>
<td>Line (a Xi&rsquo;an hereditary House)</td>
</tr>
<tr>
<td><strong> yii&rsquo;yu </strong></td>
<td>elm.CMP</td>
<td>paternal ancestor (grandfather)</td>
</tr>
<tr>
<td><strong> yii&rdquo; </strong></td>
<td>elm.</td>
<td>flow; transmission (biological); fertility</td>
</tr>
<tr>
<td><strong> Yiim </strong></td>
<td>PN.feml</td>
<td>Yiim</td>
</tr>
<tr>
<td><strong> yilen </strong></td>
<td>elm.CMP</td>
<td>harmony; peace among different factions</td>
</tr>
<tr>
<td><strong> yin </strong></td>
<td>elm.</td>
<td>bump; swelling; mound</td>
</tr>
<tr>
<td><strong> yith </strong></td>
<td>elm.</td>
<td>fire; eject (non-liquid); expel (non-liquid)</td>
</tr>
<tr>
<td><strong> yiyā&rsquo;suith </strong></td>
<td>elm.CMP</td>
<td>terrorism; policy of engendering fear</td>
</tr>
<tr>
<td><strong> yo </strong></td>
<td>nlz.</td>
<td>[subjuntive clause head]</td>
</tr>
<tr>
<td><strong> yo </strong></td>
<td>elm.</td>
<td>missing element; lack (<strong>e yo to&#8217;ath (e) no&rsquo;a</strong>)</td>
</tr>
<tr>
<td><strong> yō </strong></td>
<td>nlz.</td>
<td><strong>yo</strong> contracted with <strong>o</strong></td>
</tr>
<tr>
<td><strong> yo. </strong></td>
<td>nlz.CLTC</td>
<td>[lacking X; without X]</td>
</tr>
<tr>
<td><strong> yo&rsquo;ii </strong></td>
<td>elm.CMP</td>
<td>virus (scientific/medical term)</td>
</tr>
<tr>
<td><strong> yo&rsquo;kr.ūth </strong></td>
<td>elm.CMP</td>
<td>Non-lethal</td>
</tr>
<tr>
<td><strong> yo&rsquo;n.ao </strong></td>
<td>col.</td>
<td>white (lacking all color)</td>
</tr>
<tr>
<td><strong> yo&rdquo; </strong></td>
<td>elm.</td>
<td>alive; living; surviving</td>
</tr>
<tr>
<td><strong> yo&rdquo;e&rsquo;nu </strong></td>
<td>elm.CMP</td>
<td>embryo (in an egg)</td>
</tr>
<tr>
<td><strong> yo&rdquo;e&rsquo;so </strong></td>
<td>elm.CMP</td>
<td>bacteria (scientific/medical term)</td>
</tr>
<tr>
<td><strong> yo&rdquo;ki&rdquo; </strong></td>
<td>elm.CMP</td>
<td>mcroscopic parasite</td>
</tr>
<tr>
<td><strong> yo&rdquo;ta&rsquo;a </strong></td>
<td>elm.CMP</td>
<td>egg yolk</td>
</tr>
<tr>
<td><strong> yo&rdquo;xē&rdquo; </strong></td>
<td>elm.CMP</td>
<td>symbiote</td>
</tr>
<tr>
<td><strong> yo&rdquo;yoaith </strong></td>
<td>elm.CMP</td>
<td>germ (common term for infections (bacteria/virus)); infection</td>
</tr>
<tr>
<td><strong> yoa </strong></td>
<td>elm.</td>
<td>past; the past; history</td>
</tr>
<tr>
<td><strong> yoaith </strong></td>
<td>elm.CMP</td>
<td>sickness; disorder; disease</td>
</tr>
<tr>
<td><strong> yoii </strong></td>
<td>elm.CMP</td>
<td>darkness; blackness</td>
</tr>
<tr>
<td><strong> yokyu; yokyu(hyao) </strong></td>
<td>elm.CMP</td>
<td>Vacuum</td>
</tr>
<tr>
<td><strong> yon </strong></td>
<td>cnj.</td>
<td>as Y (of &ldquo;as X as Y&rdquo;)</td>
</tr>
<tr>
<td><strong> yōn </strong></td>
<td>elm.</td>
<td>pseudo; unofficial; quasi (infix)</td>
</tr>
<tr>
<td><strong> yonai </strong></td>
<td>elm.CMP</td>
<td>confusion</td>
</tr>
<tr>
<td><strong> yong&rsquo;m.e&rsquo;ahuā </strong></td>
<td>elm.CMP</td>
<td>peak; zenith</td>
</tr>
<tr>
<td><strong> yopuo </strong></td>
<td>elm.CMP</td>
<td>judged innocent of a wrongdoing (regardless of reality)</td>
</tr>
<tr>
<td><strong> yopuothao </strong></td>
<td>elm.CMP</td>
<td>in reality innocent of accusations; truly innocent</td>
</tr>
<tr>
<td><strong> yoru </strong></td>
<td>elm.CMP</td>
<td>Zero Gravity (slang: <strong>rul</strong>)</td>
</tr>
<tr>
<td><strong> yoryā </strong></td>
<td>elm.CMP</td>
<td>bland; unseasoned (considered an undesirable food quality)</td>
</tr>
<tr>
<td><strong> yoso </strong></td>
<td>elm.CMP</td>
<td>alone; on one&rsquo;s on; without help or assistance</td>
</tr>
<tr>
<td><strong> yoten </strong></td>
<td>elm.CMP</td>
<td>famine; a lack of food</td>
</tr>
<tr>
<td><strong> yothai </strong></td>
<td>elm.CMP</td>
<td>hard; difficult; not easy</td>
</tr>
<tr>
<td><strong> yothōa </strong></td>
<td>elm.CMP</td>
<td>undecided; (still) not having made up the mind</td>
</tr>
<tr>
<td><strong> yoxii </strong></td>
<td>elm.CMP</td>
<td>infrequent; not often</td>
</tr>
<tr>
<td><strong> yoyāi </strong></td>
<td>elm.CMP</td>
<td>naked; nude; without clothing</td>
</tr>
<tr>
<td><strong> yu </strong></td>
<td>elm.</td>
<td>male</td>
</tr>
<tr>
<td><strong> yu.yii&rdquo; </strong></td>
<td>elm.</td>
<td>father (clinical term); stud</td>
</tr>
<tr>
<td><strong> yu.yii&rdquo; </strong></td>
<td>elm.CMP</td>
<td>biological father, clinical term</td>
</tr>
<tr>
<td><strong> Yu&rsquo;.ii </strong></td>
<td>name</td>
<td>Father (reverential)</td>
</tr>
<tr>
<td><strong> Yu&rsquo;.ii </strong></td>
<td>name</td>
<td>Father &#8211; The polite &amp; reverant word for another&rsquo;s father or one&rsquo;s own</td>
</tr>
<tr>
<td><strong> yu&rsquo;.o </strong></td>
<td>elm.</td>
<td>try out; taste; try on; give something new a chance</td>
</tr>
<tr>
<td><strong> yu&rsquo;.och&rsquo;ā&rsquo;e </strong></td>
<td>elm.</td>
<td>a guided visual introduction or tour</td>
</tr>
<tr>
<td><strong> yu&rsquo;a </strong></td>
<td>elm.</td>
<td>gray to black market; quasi-criminal</td>
</tr>
<tr>
<td><strong> Yu&rsquo;a-________ </strong></td>
<td>PN.role</td>
<td>Quasi-criminal employed in _________</td>
</tr>
<tr>
<td><strong> yu&rsquo;a.r&rsquo;o </strong></td>
<td>PN.role</td>
<td>&lsquo;heavy&rsquo; who carries weapons</td>
</tr>
<tr>
<td><strong> yu&rsquo;a.r&rsquo;o&rsquo;p.ut&rsquo;o&rsquo;ath </strong></td>
<td>PN.role</td>
<td>sharpshooter assassin</td>
</tr>
<tr>
<td><strong> yu&rsquo;a&bull;o.r&rsquo;o </strong></td>
<td>PN.role</td>
<td>non-sharpshooter assasin; &ldquo;mercenary&rdquo;</td>
</tr>
<tr>
<td><strong> yu&rsquo;anāng </strong></td>
<td>PN.role</td>
<td>bounty hunter; mercenary</td>
</tr>
<tr>
<td><strong> yu&rsquo;aoa&rsquo;u.ii </strong></td>
<td>PN.role</td>
<td>snitch; informant</td>
</tr>
<tr>
<td><strong> yu&rsquo;ariimya(tō) </strong></td>
<td>PN.role</td>
<td>(money) launderer</td>
</tr>
<tr>
<td><strong> yu&rsquo;ariioa&rsquo;r.u </strong></td>
<td>PN.role</td>
<td>rumor monger; fake news creator; double-agent misinformant</td>
</tr>
<tr>
<td><strong> yu&rsquo;at.o&rsquo;a&rsquo;r.u </strong></td>
<td>PN.role</td>
<td>rumor monger; fake news creator; double-agent misinformant</td>
</tr>
<tr>
<td><strong> yu&rsquo;at.ōngh&rsquo;uitā </strong></td>
<td>PN.role</td>
<td>collector (for a loanshark or security bribe) literally: &lsquo;caregiver for the neighborhood&rsquo;</td>
</tr>
<tr>
<td><strong> yu&rsquo;at.ōngya </strong></td>
<td>PN.role</td>
<td>bodyguard</td>
</tr>
<tr>
<td><strong> Yu&rsquo;i </strong></td>
<td>name</td>
<td>Daddy, Dad</td>
</tr>
<tr>
<td><strong> Yu&rsquo;i </strong></td>
<td>name</td>
<td>Father &#8211; what children and adults call their fathers</td>
</tr>
<tr>
<td><strong> yu&rsquo;pa </strong></td>
<td>elm.</td>
<td>soft; squishy; flexible; easily falls apart (considered a favorable texture)</td>
</tr>
<tr>
<td><strong> yu&rdquo; </strong></td>
<td>num.</td>
<td>four 4</td>
</tr>
<tr>
<td><strong> yuai </strong></td>
<td>elm.</td>
<td>value; worth</td>
</tr>
<tr>
<td><strong> yuao </strong></td>
<td>elm.</td>
<td>spin; rotate</td>
</tr>
<tr>
<td><strong> yue </strong></td>
<td>elm.</td>
<td>experience; go through/live through something; immersiion in X; naming element for elders</td>
</tr>
<tr>
<td><strong> yue </strong></td>
<td>elm.</td>
<td>naming suffix for mature experienced professionals</td>
</tr>
<tr>
<td><strong> yuē </strong></td>
<td>pn.NEU</td>
<td>We (inclusive)</td>
</tr>
<tr>
<td><strong> yueuang </strong></td>
<td>elm.CMP</td>
<td>generic title word for &ldquo;elder&rdquo;</td>
</tr>
<tr>
<td><strong> yuexuan </strong></td>
<td>elm.CMP</td>
<td>gaming experience; simulation (for fun)</td>
</tr>
<tr>
<td><strong> yute&rsquo;.ah&rsquo;a </strong></td>
<td>n.</td>
<td>hot man; stud; beaux</td>
</tr>
<tr>
<td><strong> yuth </strong></td>
<td>elm.</td>
<td>reward; compensation (for effort); salary</td>
</tr>
<tr>
<td><strong> zai </strong></td>
<td>pn.SRV</td>
<td>y&rsquo;all</td>
</tr>
</tbody>
</table></div><div class="cboth"></div></div>

<div  class=' segment' ><div class="content"><p>Updates:<br />
November 10, 2017: <a href="https://robertsspaceindustries.com/spectrum/community/SC/forum/88008/thread/gameplay-terms-added-to-dictionary" title="98 gameplay terms">98 gameplay terms</a> added<br />
November 15, 2017: <a href="https://robertsspaceindustries.com/spectrum/community/SC/forum/88008/thread/seven-new-terms-added-to-dictionary" title="7 new terms">7 new terms</a> added<br />
November 22nd, 2017: <a href="https://robertsspaceindustries.com/spectrum/community/SC/forum/88008/thread/46-new-terms-added-to-dictionary-plus-6-correction" title="46 new terms ">46 new terms</a> added, six corrections made</p></div><div class="cboth"></div></div>
<div class="top-line-thin"></div><div class="top-line"></div><div class="corner corner-top-left"></div><div class="corner corner-top-right"></div><div class="corner corner-bottom-left"></div><div class="corner corner-bottom-right"></div></div></div>


  <div class="wrapper">

    <div class="end-transmission-container">
      <div class="glow left"></div>
      <div class="title-bar">
        <h1>End Transmission</h1>
      </div>
      <div class="glow right"></div>
    </div>
  </div>



    <div class="two-line-separator"></div>
  <div class="channel-banner">
  <div class="header-container">
                  <div>
      <div class="header">
        <div class="wrapper">
                      <div class="image" style="background-image:url('/media/uet01vnp422zfr/post_section_header/LoreBuilderFI.jpg');"></div>
                    <div class="texts">
            <div class="title">
              <div class="presented-by">Part of</div>
              <div class="cboth"></div>
              <h1>Lore Builder</h1>
              <a  class="holobtn " href="/comm-link?series=lore-builder"  >
  <span class="holobtn-top abs-overlay trans-02s">More in this series </span>
  <span class="holobtn-bottom abs-overlay trans-02s"></span>
</a>
              <div class="cboth"></div>
            </div>
            <p><p>Working with the community to help develop the <em>Star Citizen</em> universe.</p></p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="content-carousel">
    <div class="carousel-mask">
      <div class="left-shadow shadow"></div>
      <a href="" class="prev js-prev"><div class="hover trans-03s trans-opacity"></div></a>
      <div class="centerer">
        <div class="carousel">
                      <a href="/comm-link/spectrum-dispatch/13327-Lore-Builder-Racing" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">Lore Builder: Racing</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2013-10-18 03:20:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13339-Lore-Builder-Two-Murray-Cup-Racing" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">Lore Builder: Two: Murray Cup Racing</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2013-10-24 21:30:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13355-Lore-Builder-Three-Racing-Events-Sataball" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">Lore Builder: Three: Racing Events & Sataball</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2013-10-31 23:10:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13365-Lore-Builder-Four-Sataball" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">Lore Builder: Four: Sataball </div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2013-11-07 23:40:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13375-Lore-Builder-Five-Sataball-Format" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">Lore Builder: Five: Sataball Format</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2013-11-14 23:00:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13387-Lore-Builder-Six-Sataball-Criminals" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">Lore Builder: Six: Sataball & Criminals</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2013-11-22 04:40:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13416-LORE-BUILDER-SEVEN-FINAL-SATABALL-VOTE-PIRATES-GALORE" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: SEVEN: FINAL SATABALL VOTE & PIRATES GALORE</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2013-12-06 03:10:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13428-LORE-BUILDER-EIGHT-FIELD-GOALS-BARRIERS" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: EIGHT: FIELD/GOALS/BARRIERS</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2013-12-13 03:30:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13443-LORE-BUILDER-NINE-SQUADRON-NUMBERING-SATABALL" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: NINE: SQUADRON NUMBERING & SATABALL</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2013-12-20 04:45:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13462-LORE-BUILDER-TEN-NUMBERING-AND-SATABALL-WRAP-UP" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: TEN: NUMBERING AND SATABALL WRAP-UP</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-01-03 02:45:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13471-LORE-BUILDER-ELEVEN-SQUADRON-NUMBERING-CELEBRITIES" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: ELEVEN: SQUADRON NUMBERING & CELEBRITIES</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-01-10 05:30:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13481-LORE-BUILDER-TWELVE-SQUADRONS-ECCENTRICS" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: TWELVE: SQUADRONS & ECCENTRICS</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-01-17 02:40:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/13492-LORE-BUILDER-THIRTEEN-ORGANIZATION-NUMBERING" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: THIRTEEN: ORGANIZATION / NUMBERING</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-01-24 02:00:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14157-LORE-BUILDER-FOURTEEN-Welcome-To-V2" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: FOURTEEN: Welcome to v2</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-09-19 02:10:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14174-LORE-BUILDER-FIFTEEN-Beverages" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: FIFTEEN: Beverages</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-09-26 01:40:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14190-LORE-BUILDER-SIXTEEN-B-B" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: SIXTEEN: B&B</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-10-03 01:40:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14205-LORE-BUILDER-SEVENTEEN-Departments-Division" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: SEVENTEEN: Departments & Division</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-10-10 03:30:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14232-LORE-BUILDER-EIGHTEEN-Government-Guns" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: EIGHTEEN: Government & Guns</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-10-17 01:43:48</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14245-LORE-BUILDER-NINETEEN-Cannons-Commandments" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: NINETEEN: Cannons & Commandments</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-10-24 02:30:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14262-LORE-BUILDER-TWENTY-Journeys-Generators" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: TWENTY: Journeys & Generators</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-10-31 02:40:02</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14287-LORE-BUILDER-TWENTY-ONE-ARTIFICIAL-GRAVITY" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: TWENTY-ONE: ARTIFICIAL GRAVITY</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-11-07 02:54:34</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14300-LORE-BUILDER-TWENTY-TWO-LAG-And-Tags" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: TWENTY-TWO: LAG and Tags</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-11-14 02:25:31</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14316-LORE-BUILDER-TWENTY-THREE-Apparel-Approach" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: TWENTY-THREE: Apparel & Approach</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-11-21 02:41:22</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14349-LORE-BUILDER-TWENTY-FOUR-Free-Time" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: TWENTY-FOUR: Free Time</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-12-05 02:00:00</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14371-LORE-BUILDER-TWENTY-FIVE-More-Free-Time" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: TWENTY-FIVE: More Free Time</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-12-12 02:49:04</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/14391-LORE-BUILDER-TWENTY-SIX-Finale" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">LORE BUILDER: TWENTY-SIX: Finale</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">2014-12-19 02:18:51</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/16202-Xian-Dictionary" class="series-carousel-item content-block3 trans-05s  on">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">Xi'an Dictionary</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">3 years ago</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/16214-A-Quick-Guide-To-SRX" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">A Quick Guide to SRX</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">3 years ago</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/16220-An-Overview-Of-The-Xian-Language-For-Diplomats" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">An Overview of the Xi'an Language for Diplomats</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">7 months ago</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/16246-Naming-Animals-From-The-Xian-Empire" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">Naming Animals from the Xi'an Empire</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">3 years ago</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/16272-Adapting-Human-Names-To-Xi-an-Language" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">Adapting Human Names to Xi’an Language</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">3 years ago</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/16282-Results-Of-The-Animal-Naming-Contest" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">Results of the Animal Naming Contest</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">3 years ago</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                      <a href="/comm-link/spectrum-dispatch/17357-Smoother-Sailing-In-The-Protectorate" class="series-carousel-item content-block3 trans-05s  ">
  <div class="selected-top trans-05s"><div class="arrow"></div></div>
  <div class="type post"><div class="icon"></div><span>post</span></div>
      <div class="image" style="background-image:url('/media/if6iwm4u5ojnqr/home_transmissions_item_expanded/LoreBuilderFI_Clean.jpg');"></div>
    <div class="title trans-opacity trans-03s">Smoother Sailing in the Protectorate</div>
  <div class="text">
        <div class="time_ago">Posted:<span class="value">7 months ago</span></div>
    <div class="section">spectrum-dispatch</div>
  </div>
  <div class="selected-bottom trans-05s"><div class="arrow"></div></div>
  <div class="corner corner-top-left"></div>
<div class="corner corner-top-right"></div>
<div class="corner corner-bottom-left"></div>
<div class="corner corner-bottom-right"></div>
</a>
                  </div>
      </div>
      <a href="" class="next js-next"><div class="hover trans-03s trans-opacity"></div></a>
      <div class="right-shadow shadow"></div>
    </div>
  </div>
</div>

<script type="text/javascript">
  $(document).ready(function() {
    $(".channel-banner .content-carousel").each(function(index, element) {
      $(element).data("carousel", new RSI.FullCarousel({
        holder:$(element).find(".carousel"),
        prevButton:$(element).find(".js-prev"),
        nextButton:$(element).find(".js-next"),
        circular:true,
        displayItems:3 // healthy amount so that we never see empty
      }));
    });
  });
</script>


  <div class="two-line-separator"></div>


<div class="wrapper force-one-column" id="comments">
  <div class="holder">
    <div class="title-bar">
      <div class="count">
        <div class="label">Comments</div>
        <div class="value">061.<span class="js-comment-decimal">0</span></div>
        <div class="cboth"></div>
      </div>
      <div class="title">
        <h1>Feedback</h1>
      </div>
      <div class="cboth"></div>
    </div>

    <div class="main-buttons-holder-container">
      <div class="main-buttons-holder">
        <a href="/connect?jumpto=/comm-link/spectrum-dispatch/16202-Xian-Dictionary" class="add-comment js-add-comment trans-02s js-modal-login">Add New Comment</a>
        <div class="settings js-settings">
          <h1>Settings</h1>
          <label>View mode:</label>
          <a href="#" class="js-comments-view to-one-column js-to-one-column trans-01s on">One column</a>
          <a href="#" class="js-comments-view to-two-columns js-to-two-columns trans-01s ">Two columns</a>
          <label>Sort by:</label>
          <a href="#" class="js-comments-sort to-oldest js-to-oldest trans-01s on">Oldest first</a>
          <a href="#" class="js-comments-sort to-newest js-to-newest trans-01s ">Newest first</a>
          <a href="#" class="js-comments-sort to-appreciated js-to-appreciated trans-01s ">Most appreciated first</a>

                  </div>
        <a href="" class="view-settings js-view-settings"><div class="hover trans-02s"></div></a>
        <div class="triangle"></div>
      </div>
    </div>


    <div class="comment-listing"></div>

    <div class="comment-loader traj-loader">
      <div class="fast-blink"></div>
      <span>Loading Additional Feedback</span>
    </div>

    <div class="cboth"></div>

  </div>
</div>

<script type="text/javascript">
  $(document).ready(function() {
    window.comments = new RSI.Comments({
      atom_url:"/comm-link/spectrum-dispatch/16202-Xian-Dictionary",
      comment_listing_el:$(".comment-listing"),
      comment_submission_form_el:$(".comment-submission"),
      api_object:RSI.Api.Comments,
      lazyLoading: true,
      comment_count: 61,
      subject_id:16202,
      append:false,
      texts: {
        "edit": {
          "cancel": "Cancel",
          "submit": "Save Changes"
        },
        "reply": {
          "cancel": "Cancel",
          "submit": "Save Changes"
        }
      },
      "insertion_conf": {
        "mode":"html"
      },
      "api_function_names": {
        "delete":"erase",
        "load":"listing",
        "sort":"listing"
      }
    });
  });
</script>

</div>

    </div>


  </div>


<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.17.1/moment-with-locales.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.5.11/moment-timezone-with-data.min.js"></script>

<script type="text/plain" data-cookieconsent="statistics">
  $.cookie('moment_timezone', moment.tz.guess(), { expires: 31, path: '/' });
</script>




               <script id="tpl_number_counter_digits" type="text/x-jsmart-tmpl">{if !$seperator}{$seperator=','}{/if}
{if !$first_max}{$first_max=9}{/if}
{for $digit = 0 to $length-1}
  <div class="mask">
    <div class="carousel">
      {if $digit == 0}
        {$max = $first_max}
      {else}
        {$max = 9}
      {/if}
      {for $i=0 to $max}
        <div class="item {if $val_arr[$digit] == $i}on{/if}" rel="{$i}">{$i}</div>
      {/for}
    </div>
  </div>
  {if ($length - $digit) % 3 == 1 && $digit != $length-1}
  <div class="seperator">{$seperator}</div>
  {/if}
{/for}</script>
<script id="base_modal" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">
  <div class="top-border">
    {block name="modal_lines"}
    <img src="/rsi/static/images/modal_blue_line.png" />
    {/block}
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    {block name="modal_content"}{/block}
    {block name="modal_footer"}{/block}
  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
    {block name="modal_lines"}
    <img src="/rsi/static/images/modal_blue_line.png" />
    {/block}
  </div>
</div></script>
<script id="base_modal_flat" type="text/x-jsmart-tmpl"><div class="modal-wrapper {block name="modal_wrapper_class"}{/block}">

  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>
    {block name="modal_content"}{/block}
    {block name="modal_footer"}{/block}
  </div>

</div></script>
<script id="tpl_modals_slideshow" type="text/x-jsmart-tmpl"><img class="top-border" src="/rsi/static/images/modal_top.png">
<a href="" class="close js-close"></a>
<div class="mask">
  <a class="js-prev prev control"></a>
  <a class="js-next next control"></a>
  <div class="slideshow-carousel carousel" rel="{$index}">
    {foreach from=$images item="image"}
      <div class="{if $index == $image@index}on{/if}">
      {if $image.is_video}
        <div class="video-holder">
          <div id="slideshow_video_{$image@index}" data-source="{$image->source_url}">
            <video width="100%" height="100%" preload="auto" {if $video}src="{$image->source_url}"{/if} controls></video>
          </div>
        </div>
      {else}
        <div class="media js-media-slideshow-{$image@iteration}">
        {if $image.low_res}
          <picture>
            <!--[if IE 9]><video style="display: none;"><![endif]-->
            <source data-srcset="{$image.full_res}" media="(min-width: 300px)" />
            <!--[if IE 9]></video><![endif]-->
            <img data-srcset="{$image.low_res}" alt="{$image.title}" />
          </picture>
        {else}
          <img data-src="{$image.source_url}" />
        {/if}
        </div>
      {/if}
        <div class="text">
          {if !$image.is_video}
          <a href="{$image.source_url}" class="download"></a>
          {/if}
          <div class="copyright">© 2012-{$year}<br />Cloud Imperium Games Corporation &<br />Roberts Space Industries Corp.</div>
          <div class="page-number">{$image@iteration} / {count($images)}</div>
          <div class="caption v-center">{if $image.title && $image.title != "undefined"}{$image.title}{/if}</div>
          <div class="cboth"></div>
        </div>
      </div>
    {/foreach}
  </div>
</div>
<img class="bottom-border" src="/rsi/static/images/modal_bottom.png"></script>
<script id="tpl_contact_us" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
  <div class="top-border">

    <img src="/rsi/static/images/modal_blue_line.png" />

    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>

<div id="contact" class="inner-content on">
  <h2><span class="icon"></span>CONTACT</h2>
  <div class="padder">
    <div class="separator"></div>
    <form name="" action="" method="POST">
  <div class="error-message js-error-message"></div>
  <div class="success-message js-success-message"></div>
    <fieldset class="last">
    <label for="contact_email">Email Address</label>
    <input type="text" name="email" value="" class="trans-02s trans-color trans-box-shadow" id="contact_email" />
  </fieldset>
    <fieldset>
    <label for="contact_subject">Subject</label>
    <input type="text" name="subject" value="" class="trans-02s trans-color trans-box-shadow" id="contact_subject" />
    <label>Contacting us for:</label>
    <ul class="category-info">
            <li id="tech_support_info">Questions about download, installation, networking, or in-game client problems</li>
            <li id="subscription_info">Questions about monthly and yearly subscription plans</li>
            <li id="account_billing_info">Issues related to your account, such as incorrect information or ability to access account, or Billing with regards to payments and payment methods</li>
            <li id="melt_request_info">To reclaim a pledge over $1,000 for store credit (please note - this is a permanent action)</li>
            <li id="merchandise_info">Questions about physical and/or shipped merchandise</li>
            <li id="hacked_info">Issues related to compromised account or missing pledge.</li>
            <li id="account_recovery_info">For issues with account authentication, lost passwords and related queries</li>
            <li id="probation_info">Issues related to forums probation or ban</li>
            <li id="refund_request_info">Refund requests and related inquiries</li>
            <li id="customer_support_info">For general questions and queries regarding Star Citizen</li>
          </ul>
  </fieldset>
  <fieldset>
    <label for="contact_text">Fescription</label>
    <textarea name="text" class="trans-02s trans-color trans-box-shadow" id="contact_text"></textarea>
  </fieldset>
  <div class="contact-submit-wrapper">
    <div class="line"></div>
    <button class="submit js-submit"><strong>submit your message</strong></button>
  </div>
</form>
    <div class="separator"></div>
  </div>
</div>


  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>

    <img src="/rsi/static/images/modal_blue_line.png" />

  </div>
</div></script>
<script id="tpl_error" type="text/x-jsmart-tmpl"><div class="modal-error js-modal-error">
  <p class="modal-text js-modal-text"></p>
  <a class="close js-close trans-03s .trans-opacity" href=""></a>
</div></script>
<script id="tpl_success" type="text/x-jsmart-tmpl"><div class="modal-success js-modal-success">
  <p class="modal-text js-modal-text"></p>
  <a class="close js-close trans-03s .trans-opacity" href=""></a>
</div></script>
<script id="tpl_progress" type="text/x-jsmart-tmpl"><div class="modal-progress js-modal-progress">
  <div class="traj-loader">
    <div class="fast-blink"></div>
    <span class="modal-text js-modal-text"></span>
  </div>
</div></script>
<script id="tpl_outbound" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
  <div class="top-border">

    <img src="/rsi/static/images/modal_blue_line.png" />

    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>

<div id="outbound" class="inner-content on">
  <h2><span class="icon"></span>OUTBOUND LINK</h2>
  <div class="padder">
    <div class="separator"></div>
    <form name="" action="" method="POST">
      <div class="error-message js-error-message"> <span class=important>WARNING</span><br/><br/> This link will bring you outside of the RSI site and into the depths of the internet. Continue?<br/><br/><span class="url"></span> </div>
      <div class="success-message js-success-message"><span class=important>STAND BY</span><br/><br/> Initiating hyperlink.<br/><br/></div>

      <fieldset class="clearfix last">
        <span class="submit-wrapper">
          <span class="submit-hover trans-02s trans-opacity"></span>
          <input type="submit" value="WARP" class="trans-02s trans-color trans-background" />
        </span>
      </fieldset>
    </form>
    <div class="separator"></div>
  </div>
</div>


  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>

    <img src="/rsi/static/images/modal_blue_line.png" />

  </div>
</div></script>

<script id="tpl_l-notification-bar" type="text/x-jsmart-tmpl"><div class="l-notification-bar js-notification-bar">

  <div class="l-notification-bar__watermark js-svg-inliner h-svg__logo-star-citizen"></div>

  <div class="l-notification-bar__boxes">
    {if !$viewedCookieNotif}
      <div class="l-notification-bar__box">
        {include file='tpl_c-notification'
          type='cookie'
          title='COOKIES:'
          message="Our website uses Google Analytics to analyze our traffic. <br/>To learn how you can control Google's use of your data and how you can opt out <a href='https://www.google.com/policies/privacy/partners/'>click here</a>."
          linkText='See Details'
          buttonText='Got it!'}
      </div>
    {/if}

    {if !$viewedPrivacyNotif}
      <div class="l-notification-bar__box">
        {include file='tpl_c-notification'
          type='privacy'
          title='PRIVACY POLICY:'
          message='We adjusted the PP to reflect the decision of the European Court of Justice regarding Safe Harbor, the fact that RSI has moved and added some services providers.'
          linkText='View Privacy Policy'
          buttonText='Got it!'}
      </div>
    {/if}
  </div>

</div>
</script>
<script id="tpl_c-notification" type="text/x-jsmart-tmpl"><div class="c-notification js-bottom-notif-msg-{$type}">
    <div class="c-notification__title">{$title}</div>
    <div class="c-notification__message">
      {$message}
    </div>

    {if $linkText}
        <div class="c-notification__wrapper-link">
            <a class="c-notification__link js-bottom-notif-link-{$type}">
            {$linkText}
            </a>
        </div>
    {/if}

    <a class="c-notification__button js-bottom-notif-btn-{$type}">

      <span class="c-notification__button-text">
       {$buttonText}
      </span>

      {if $type neq 'announcement'}
        <div class="c-iconed__icon c-iconed__icon--checkmark"></div>
      {/if}
    </a>
</div>
</script>

<script id="tpl_confirm" type="text/x-jsmart-tmpl"><div class="modal-confirm js-modal-confirm clearfix">
  <p class="modal-text js-modal-text"></p>
  <a class="bt-close js-close trans-03s trans-opacity" href=""></a>
  <a class="bt-confirm js-confirm trans-03s trans-opacity" href=""></a>
	<div class="buttons">
		<a class="shadow-button trans-02s trans-color js-close bt-close rm"     >
  <span class="label js-label trans-02s">Cancel</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
		<a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
  <span class="label js-label trans-02s">Confirm</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
	</div>
</div>
</script>
<script id="tpl_alert" type="text/x-jsmart-tmpl"><div class="modal-alert js-modal-alert clearfix">
  <p class="modal-text js-modal-text"></p>
  <div class="buttons">
    <a class="shadow-button trans-02s trans-color js-confirm bt-confirm green"     >
  <span class="label js-label trans-02s">OK</span>
  <span class="icon trans-02s"><span class="effect trans-opacity trans-03s"></span></span>
  <span class="left-section"></span>
  <span class="right-section"></span>
</a>
  </div>
</div></script>
<script id="tpl_video" type="text/x-jsmart-tmpl">{extends file="base_modal"}
{block name='modal_content'}
<div id="ship-commercial" class="inner-content">

  <div class="hr"></div>
  <div class="content-block4">

    <div class="bottom"></div>
  </div>
  {if $distant_source=="vimeo"}
  <iframe id="commercial" src="//player.vimeo.com/video/{$video_id}?wmode=transparent" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>
  {else}
  <iframe id="commercial" frameborder="0" allowfullscreen="1" title="YouTube video player" width="100%" height="100%" src="https://www.youtube.com/embed/{$video_id}?autoplay=1"></iframe>
  {/if}
</div>
{/block}
</script>

  <script id="tpl_comment_report" type="text/x-jsmart-tmpl"><div class="modal-wrapper ">
  <div class="top-border">

    <img src="/rsi/static/images/modal_blue_line.png" />

    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>
  </div>
  <div class="modal-inner">
    <a class="close js-close trans-03s .trans-opacity" href=""></a>

<div id="comment-report" class="inner-content on">
  <h2><span class="icon"></span>Report this comment</h2>
  <div class="padder">
    <div class="separator"></div>
    <form name="" action="" method="POST">
<input type="hidden" name="comment_id" value="">
  <div class="error-message js-error-message"></div>
  <div class="success-message js-success-message"></div>
    <fieldset class="last">
    <label for="report_email">Email Address</label>
    <span class="corner-wrapper">
      <input type="text" name="email" value="" class="trans-02s trans-color trans-box-shadow js-form-data" id="report_email" />
      <span class="corner corner-top-left"></span>
      <span class="corner corner-top-right"></span>
      <span class="corner corner-bottom-left"></span>
      <span class="corner corner-bottom-right"></span>
    </span>
  </fieldset>
    <fieldset>
    <label>Report Type</label>




    <a class="js-selectlist selectlist " rel="" href="">
    <div class="arrow"></div>
    <span>Please select the type best matching your report</span>
              <ul class="body">

                                                              <li class="js-option option " rel="obscenity" >
                                                                        Obscene Content
                                                    </li>
                                                                <li class="js-option option " rel="abuse" >
                                                                        Abusive Conduct
                                                    </li>
                                                                <li class="js-option option " rel="other" >
                                                                        Other
                                                    </li>

            </ul>
        <input type="hidden" name="category" class="js-category js-form-data" id="category"/>
  </a>
    </fieldset>
  <fieldset>
    <label for="report_text">Details</label>
    <span class="corner-wrapper">
      <textarea name="text" class="trans-02s trans-color trans-box-shadow js-form-data" id="report_text" maxlength="2500"></textarea>
      <span class="corner corner-top-left"></span>
      <span class="corner corner-top-right"></span>
      <span class="corner corner-bottom-left"></span>
      <span class="corner corner-bottom-right"></span>
    </span>
  </fieldset>
  <fieldset class="clearfix last">
    <span class="submit-wrapper">
      <span class="submit-hover trans-02s trans-opacity"></span>
      <input type="submit" value="Submit" class="trans-02s trans-color trans-background" />
    </span>
  </fieldset>
</form>
    <div class="separator"></div>
  </div>
</div>


  </div>
  <div class="bottom-border">
    <div class="h-border"></div>
    <div class="l-corner"></div>
    <div class="r-corner"></div>

    <img src="/rsi/static/images/modal_blue_line.png" />

  </div>
</div></script>



        <footer class="c-platform-footer c-platform-footer--rsi">
  <div class="l-platform-footer-container">

    <div class="c-platform-footer__column l-column ">
      <ul class="c-platform-footer-brand c-platform-footer-brand--sc">
        <li class="c-platform-footer-brand__item">

          <span class="c-brand c-brand--sc js-footer-open-sub-menu">
            <span class="c-brand__logo c-brand__logo--sc">
              <span class="js-svg-inliner h-svg h-svg__logo-star-citizen"></span>
              <span class="js-svg-inliner h-svg h-svg__logo-star-citizen--fullcolor"></span>
            </span>

            <span class="c-brand__label">
              Join the<br>Universe
            </span>

            <span class="c-brand__arrow">
              <svg width="10px" height="17px" viewBox="0 0 10 17" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">   <path transform="translate(-8.000000, -5.000000)" d="M15.3610114,5.87946602 L8.86459388,12.5876406 C8.62203758,12.8388577 8.50002884,13.1692873 8.50002884,13.499717 C8.49783707,13.8331643 8.6205764,14.1628395 8.86459388,14.4140566 L15.3610114,21.1229856 C15.8468546,21.6246653 16.6424685,21.6269285 17.1312341,21.1222312 C17.6236526,20.6130074 17.6214608,19.7982494 17.1334258,19.2943064 L11.5232155,13.5012258 L17.1334258,7.7088996 C17.6185384,7.20721987 17.6214608,6.38567218 17.1312341,5.88022042 C16.8857554,5.62674014 16.5657564,5.5 16.246488,5.5 C15.9257585,5.5 15.6057595,5.62749455 15.3610114,5.87946602 Z" id="path-1"></path> </svg>
            </span>
          </span>

          <ul class="c-platform-footer-list c-platform-footer-list--sc">
            <li class="c-platform-footer-list__item">
              <a href="/star-citizen" class="c-platform-footer-link">About the Game</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/star-citizen/howto/1" class="c-platform-footer-link">How to Play</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/star-citizen/universe" class="c-platform-footer-link">The Universe</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/star-citizen/media" class="c-platform-footer-link">Media</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/star-citizen/fly-now"
                class="c-platform-footer-link js-google-analytics-event-tracker"
                data-event-category="FlyNow" data-event-label="footerClick">
                Fly Now
              </a>
            </li>
          </ul>
        </li>
      </ul>

      <ul class="c-platform-footer-social">
        <li class="c-platform-footer-social__item">
          <a class="c-arrow-link js-toggle-arrow" href="#social-links__sc">
            <span class="c-arrow-link__text c-arrow-link__text--underline">
              Social Links
            </span>
            <span class="c-arrow-link__arrow js-svg-inliner"></span>
          </a>

          <ul id="social-links__sc" class="l-social-links">
            <li class="c-social-links__item">
              <a class="c-platform-footer-link c-platform-footer-link--icon" href="https://www.facebook.com/RobertsSpaceIndustries/">
                <span class="c-iconed__icon c-iconed__icon--facebook"></span>
                Facebook
              </a>
            </li>

            <li class="c-social-links__item">
              <a class="c-platform-footer-link c-platform-footer-link--icon" href="https://twitter.com/RobertsSpaceInd">
                <span class="c-iconed__icon c-iconed__icon--twitter"></span>
                Twitter
              </a>
            </li>

            <li class="c-social-links__item">
              <a class="c-platform-footer-link c-platform-footer-link--icon" href="https://www.instagram.com/robertsspaceind">
                <span class="c-iconed__icon c-iconed__icon--instagram"></span>
                Instagram
              </a>
            </li>

            <li class="c-social-links__item">
              <a class="c-platform-footer-link c-platform-footer-link--icon" href=" https://www.youtube.com/channel/UCTeLqJq1mXUX5WWoNXLmOIA">
                <span class="c-iconed__icon c-iconed__icon--youtube"></span>
                Youtube
              </a>
            </li>

            <li class="c-social-links__item">
              <a class="c-platform-footer-link c-platform-footer-link--icon" href="https://www.twitch.tv/starcitizen">
                <span class="c-iconed__icon c-iconed__icon--twitch"></span>
                Twitch
              </a>
            </li>
          </ul>

        </li>
      </ul>
    </div>

    <div class="c-platform-footer__column l-column ">
      <ul class="c-platform-footer-brand c-platform-footer-brand--s42">
        <li class="c-platform-footer-brand__item">
          <span class="c-brand c-brand--s42 js-footer-open-sub-menu">
            <span class="c-brand__logo c-brand__logo--s42">
              <span class="js-svg-inliner h-svg h-svg__logo-squadron42"></span>
              <span class="js-svg-inliner h-svg h-svg__logo-squadron42--fullcolor"></span>
            </span>

            <span class="c-brand__label">
              Start the<br>Adventure
            </span>

            <span class="c-brand__arrow">
              <svg width="10px" height="17px" viewBox="0 0 10 17" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">   <path transform="translate(-8.000000, -5.000000)" d="M15.3610114,5.87946602 L8.86459388,12.5876406 C8.62203758,12.8388577 8.50002884,13.1692873 8.50002884,13.499717 C8.49783707,13.8331643 8.6205764,14.1628395 8.86459388,14.4140566 L15.3610114,21.1229856 C15.8468546,21.6246653 16.6424685,21.6269285 17.1312341,21.1222312 C17.6236526,20.6130074 17.6214608,19.7982494 17.1334258,19.2943064 L11.5232155,13.5012258 L17.1334258,7.7088996 C17.6185384,7.20721987 17.6214608,6.38567218 17.1312341,5.88022042 C16.8857554,5.62674014 16.5657564,5.5 16.246488,5.5 C15.9257585,5.5 15.6057595,5.62749455 15.3610114,5.87946602 Z" id="path-1"></path> </svg>
            </span>
          </span>

          <ul class="c-platform-footer-list c-platform-footer-list--s42">
            <li class="c-platform-footer-list__item">
              <a href="/squadron42" class="c-platform-footer-link">The Game</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/squadron42#enlist" class="c-platform-footer-link">Enlist Today</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/squadron42#roadmap" class="c-platform-footer-link">Status</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/pledge/Packages/Squadron-42-Standalone-Pledge" class="c-platform-footer-link">Pledge</a>
            </li>
          </ul>
        </li>
      </ul>

      <ul class="c-platform-footer-social">
        <li class="c-platform-footer-social__item">
          <a class="c-arrow-link js-toggle-arrow" href="#social-links__s42">
            <span class="c-arrow-link__text c-arrow-link__text--underline">Social Links</span>
            <span class="c-arrow-link__arrow js-svg-inliner"></span>
          </a>

          <ul id="social-links__sc" class="l-social-links">
            <li class="c-social-links__item">
              <a class="c-platform-footer-link c-platform-footer-link--icon" href="https://www.facebook.com/Squad42/">
                <span class="c-iconed__icon c-iconed__icon--facebook"></span>
                Facebook
              </a>
            </li>

            <li class="c-social-links__item">
              <a class="c-platform-footer-link c-platform-footer-link--icon" href="https://twitter.com/squadron_42">
                <span class="c-iconed__icon c-iconed__icon--twitter"></span>
                Twitter
              </a>
            </li>

            <li class="c-social-links__item">
              <a class="c-platform-footer-link c-platform-footer-link--icon" href="https://www.instagram.com/squadron42">
                <span class="c-iconed__icon c-iconed__icon--instagram"></span>
                Instagram
              </a>
            </li>
          </ul>

        </li>
      </ul>
    </div>

    <div class="c-platform-footer__column l-column is-active">
      <ul class="c-platform-footer-brand c-platform-footer-brand--rsi">
        <li class="c-platform-footer-brand__item">
          <span class="c-brand c-brand--rsi js-footer-open-sub-menu">
            <span class="c-brand__logo c-brand__logo--rsi">
              <span class="js-svg-inliner h-svg h-svg__logo-rsi"></span>
              <span class="js-svg-inliner h-svg h-svg__logo-rsi--fullcolor"></span>
            </span>
            <span class="c-brand__label">
              Follow the Development
            </span>
            <span class="c-brand__arrow">
              <svg width="10px" height="17px" viewBox="0 0 10 17" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">   <path transform="translate(-8.000000, -5.000000)" d="M15.3610114,5.87946602 L8.86459388,12.5876406 C8.62203758,12.8388577 8.50002884,13.1692873 8.50002884,13.499717 C8.49783707,13.8331643 8.6205764,14.1628395 8.86459388,14.4140566 L15.3610114,21.1229856 C15.8468546,21.6246653 16.6424685,21.6269285 17.1312341,21.1222312 C17.6236526,20.6130074 17.6214608,19.7982494 17.1334258,19.2943064 L11.5232155,13.5012258 L17.1334258,7.7088996 C17.6185384,7.20721987 17.6214608,6.38567218 17.1312341,5.88022042 C16.8857554,5.62674014 16.5657564,5.5 16.246488,5.5 C15.9257585,5.5 15.6057595,5.62749455 15.3610114,5.87946602 Z" id="path-1"></path> </svg>
            </span>
          </span>

          <ul class="c-platform-footer-list c-platform-footer-list--rsi">
            <li class="c-platform-footer-list__item">
              <a href="/" class="c-platform-footer-link">Home</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/comm-link" class="c-platform-footer-link">Transmissions</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/community" class="c-platform-footer-link">Community</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/roadmap" class="c-platform-footer-link">Development</a>
            </li>
          </ul>
        </li>
      </ul>
    </div>

    <div class="c-platform-footer__column l-column l-column--smaller">
      <ul class="c-platform-footer-brand c-platform-footer-brand--platform">
        <li class="c-platform-footer-brand__item">
          <h2 class="c-platform-footer-brand__title js-footer-open-sub-menu">
            Platform

            <span class="c-platform-footer-brand__arrow">
              <svg width="10px" height="17px" viewBox="0 0 10 17" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">   <path transform="translate(-8.000000, -5.000000)" d="M15.3610114,5.87946602 L8.86459388,12.5876406 C8.62203758,12.8388577 8.50002884,13.1692873 8.50002884,13.499717 C8.49783707,13.8331643 8.6205764,14.1628395 8.86459388,14.4140566 L15.3610114,21.1229856 C15.8468546,21.6246653 16.6424685,21.6269285 17.1312341,21.1222312 C17.6236526,20.6130074 17.6214608,19.7982494 17.1334258,19.2943064 L11.5232155,13.5012258 L17.1334258,7.7088996 C17.6185384,7.20721987 17.6214608,6.38567218 17.1312341,5.88022042 C16.8857554,5.62674014 16.5657564,5.5 16.246488,5.5 C15.9257585,5.5 15.6057595,5.62749455 15.3610114,5.87946602 Z" id="path-1"></path> </svg>
            </span>
          </h2>

          <ul class="c-platform-footer-list c-platform-footer-list--platform">
                          <li class="c-platform-footer-list__item">
                <a href="/pledge" class="c-platform-footer-link ">Pledge Store</a>
              </li>

            <li class="c-platform-footer-list__item">
              <a href="/download" class="c-platform-footer-link ">Download</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/spectrum/community/SC" class="c-platform-footer-link">Spectrum</a>
            </li>

                      </ul>
        </li>
      </ul>
    </div>

    <div class="c-platform-footer__column l-column l-column--smaller">
      <ul class="c-platform-footer-brand c-platform-footer-brand--utility">
        <li class="c-platform-footer-brand__item">
          <h2 class="c-platform-footer-brand__title js-footer-open-sub-menu">
            Utilities

            <span class="c-platform-footer-brand__arrow">
              <svg width="10px" height="17px" viewBox="0 0 10 17" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">   <path transform="translate(-8.000000, -5.000000)" d="M15.3610114,5.87946602 L8.86459388,12.5876406 C8.62203758,12.8388577 8.50002884,13.1692873 8.50002884,13.499717 C8.49783707,13.8331643 8.6205764,14.1628395 8.86459388,14.4140566 L15.3610114,21.1229856 C15.8468546,21.6246653 16.6424685,21.6269285 17.1312341,21.1222312 C17.6236526,20.6130074 17.6214608,19.7982494 17.1334258,19.2943064 L11.5232155,13.5012258 L17.1334258,7.7088996 C17.6185384,7.20721987 17.6214608,6.38567218 17.1312341,5.88022042 C16.8857554,5.62674014 16.5657564,5.5 16.246488,5.5 C15.9257585,5.5 15.6057595,5.62749455 15.3610114,5.87946602 Z" id="path-1"></path> </svg>
            </span>
          </h2>

          <ul class="c-platform-footer-list c-platform-footer-list--utility">
            <li class="c-platform-footer-list__item">
              <a href="//support.robertsspaceindustries.com" class="c-platform-footer-link">Help</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/press" class="c-platform-footer-link">Press</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="https://cloudimperiumgames.com/join-us" class="c-platform-footer-link">Careers</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/tos" class="c-platform-footer-link">Terms of Services</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/privacy" class="c-platform-footer-link">Privacy Policy</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/eula" class="c-platform-footer-link">EULA</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/dmca" class="c-platform-footer-link">DMCA</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/legal" class="c-platform-footer-link">Legal</a>
            </li>

            <li class="c-platform-footer-list__item">
              <a href="/acknowledgements" class="c-platform-footer-link">Acknowledgements</a>
            </li>
          </ul>
        </li>
      </ul>
    </div>

  </div>


</footer>

<div class="c-platform-copyright c-platform-copyright--rsi">
  <div class="l-platform-copyright-container">
    <a href="https://cloudimperiumgames.com" class="c-platform-copyright__logo h-svg__logo-cig js-svg-inliner"></a>
    <p class="c-platform-copyright__body">© 2012-2020 Cloud Imperium Rights LLC and Cloud Imperium Rights Ltd.</p>
  </div>
</div>


<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KHNFZPT"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->


<script type="text/javascript">
  window.RSI.Footer = new RSI.Footer();
</script>

    </div>


      <script type="text/javascript" src='/rsi/static/packages/platformbar/rsi.platformbar.build.be48f.js'></script>

  <script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","licenseKey":"58013cabd7","applicationID":"375102748","transactionName":"Y1JaYktUWxZUV0QKV1oYe0NKQVoIGmZjKmtdQ111VltBF1pYXAZKDg1ZQlZYcwxbUA==","queueTime":0,"applicationTime":250,"atts":"TxVNFANOSEkXVRJZQ0lK","errorBeacon":"bam.nr-data.net","agent":""}</script></body>
</html>
"""
