(function(e){function t(t){for(var r,a,i=t[0],s=t[1],u=t[2],f=0,l=[];f<i.length;f++)a=i[f],Object.prototype.hasOwnProperty.call(o,a)&&o[a]&&l.push(o[a][0]),o[a]=0;for(r in s)Object.prototype.hasOwnProperty.call(s,r)&&(e[r]=s[r]);p&&p(t);while(l.length)l.shift()();return c.push.apply(c,u||[]),n()}function n(){for(var e,t=0;t<c.length;t++){for(var n=c[t],r=!0,a=1;a<n.length;a++){var i=n[a];0!==o[i]&&(r=!1)}r&&(c.splice(t--,1),e=s(s.s=n[0]))}return e}var r={},a={app:0},o={app:0},c=[];function i(e){return s.p+"js/"+({about:"about"}[e]||e)+"."+{about:"c79c3188"}[e]+".js"}function s(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,s),n.l=!0,n.exports}s.e=function(e){var t=[],n={about:1};a[e]?t.push(a[e]):0!==a[e]&&n[e]&&t.push(a[e]=new Promise((function(t,n){for(var r="css/"+({about:"about"}[e]||e)+"."+{about:"1c7f9e6d"}[e]+".css",o=s.p+r,c=document.getElementsByTagName("link"),i=0;i<c.length;i++){var u=c[i],f=u.getAttribute("data-href")||u.getAttribute("href");if("stylesheet"===u.rel&&(f===r||f===o))return t()}var l=document.getElementsByTagName("style");for(i=0;i<l.length;i++){u=l[i],f=u.getAttribute("data-href");if(f===r||f===o)return t()}var p=document.createElement("link");p.rel="stylesheet",p.type="text/css",p.onload=t,p.onerror=function(t){var r=t&&t.target&&t.target.src||o,c=new Error("Loading CSS chunk "+e+" failed.\n("+r+")");c.code="CSS_CHUNK_LOAD_FAILED",c.request=r,delete a[e],p.parentNode.removeChild(p),n(c)},p.href=o;var d=document.getElementsByTagName("head")[0];d.appendChild(p)})).then((function(){a[e]=0})));var r=o[e];if(0!==r)if(r)t.push(r[2]);else{var c=new Promise((function(t,n){r=o[e]=[t,n]}));t.push(r[2]=c);var u,f=document.createElement("script");f.charset="utf-8",f.timeout=120,s.nc&&f.setAttribute("nonce",s.nc),f.src=i(e);var l=new Error;u=function(t){f.onerror=f.onload=null,clearTimeout(p);var n=o[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src;l.message="Loading chunk "+e+" failed.\n("+r+": "+a+")",l.name="ChunkLoadError",l.type=r,l.request=a,n[1](l)}o[e]=void 0}};var p=setTimeout((function(){u({type:"timeout",target:f})}),12e4);f.onerror=f.onload=u,document.head.appendChild(f)}return Promise.all(t)},s.m=e,s.c=r,s.d=function(e,t,n){s.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},s.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},s.t=function(e,t){if(1&t&&(e=s(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(s.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)s.d(n,r,function(t){return e[t]}.bind(null,r));return n},s.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return s.d(t,"a",t),t},s.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},s.p="/",s.oe=function(e){throw console.error(e),e};var u=window["webpackJsonp"]=window["webpackJsonp"]||[],f=u.push.bind(u);u.push=t,u=u.slice();for(var l=0;l<u.length;l++)t(u[l]);var p=f;c.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";n("bd03")},"23b0":function(e){e.exports=JSON.parse('{"baseURLProd":"http://95.161.199.126:8081/api/v1/","baseURLProd1":"http://172.27.22.251:8081/api/v1/","baseURL":"http://api.lcg.loc:8081/api/v1/"}')},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d"),n("3c6c"),n("b9fd"),n("a157"),n("c9d4");var r=n("5ae0"),a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-app",{attrs:{id:"inspire"}},[n("v-navigation-drawer",{attrs:{app:""},model:{value:e.drawer,callback:function(t){e.drawer=t},expression:"drawer"}},[n("v-list",{attrs:{dense:""}},[n("router-link",{attrs:{to:"/"}},[n("v-list-item",{attrs:{link:""}},[n("v-list-item-action",[n("v-icon",[e._v("mdi-home")])],1),n("v-list-item-content",[n("v-list-item-title",[e._v("Главная")])],1)],1)],1),n("router-link",{attrs:{to:"/agreement"}},[n("v-list-item",{attrs:{link:""}},[n("v-list-item-action",[n("v-icon",[e._v("mdi-clipboard-outline")])],1),n("v-list-item-content",[n("v-list-item-title",[e._v("Список дел")])],1)],1)],1),n("router-link",{attrs:{to:"/load-manager"}},[n("v-list-item",{attrs:{link:""}},[n("v-list-item-action",[n("v-icon",[e._v("mdi-plus")])],1),n("v-list-item-content",[n("v-list-item-title",[e._v("Загрузки")])],1)],1)],1)],1)],1),n("v-app-bar",{attrs:{app:"",color:"indigo",dark:"",dense:""}},[n("v-app-bar-nav-icon",{on:{click:function(t){t.stopPropagation(),e.drawer=!e.drawer}}}),n("v-toolbar-title",[e._v("LCG")])],1),n("v-content",[n("v-container",{attrs:{fluid:"",align:"start",justify:"start"}},[n("v-row",{attrs:{align:"start",justify:"start"}},[n("router-view")],1)],1)],1)],1)},o=[],c={props:{source:String},data:function(){return{drawer:null}}},i=c,s=(n("034f"),n("3404")),u=Object(s["a"])(i,a,o,!1,null,null,null),f=u.exports,l=n("ce5b"),p=n.n(l);n("bf40"),n("5363");r["default"].use(p.a);var d=new p.a({icons:{iconfont:"mdi"},theme:{themes:{light:{primary:"#ee44aa",secondary:"#424242",accent:"#82B1FF",error:"#FF5252",info:"#2196F3",success:"#4CAF50",warning:"#FFC107"}}}}),m=(n("0ae4"),n("8c4f"));r["default"].use(m["a"]);var g=new m["a"]({mode:"history",base:"",routes:[{path:"/",name:"home",component:function(){return n.e("about").then(n.bind(null,"0c7c"))}},{path:"/agreement",name:"agreement",component:function(){return n.e("about").then(n.bind(null,"5014"))}},{path:"/agreement/:id",name:"agreement-card",component:function(){return n.e("about").then(n.bind(null,"ae8d"))}},{path:"/load-manager",name:"load-manager",component:function(){return n.e("about").then(n.bind(null,"fc5d"))}}]}),_=n("2f62"),h=(n("f287"),n("1da1")),b=n("bc3a"),v=n("23b0"),y=b.create({baseURL:v.baseURL,timeout:1e5}),w={ref:{phone_type:[],contact_type:[],contact_result:[],process_type:[],csi:[]}},x={ref_customer_phone_type:function(e){return e.ref.phone_type},ref_process_type:function(e){return e.ref.process_type},ref_contact_type:function(e){return e.ref.contact_type},ref_contact_result:function(e){return e.ref.contact_result},ref_csi:function(e){return e.ref.csi}},R={setCustomerPhoneTypes:function(e,t){e.ref.phone_type=t},setProcessTypes:function(e,t){e.ref.process_type=t},setContactTypes:function(e,t){e.ref.contact_type=t},setContactsResults:function(e,t){e.ref.contact_result=t},setRefCsi:function(e,t){e.ref.csi=t}},k={loadCustomerPhoneTypes:function(e){return Object(h["a"])(regeneratorRuntime.mark((function t(){var n,r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.commit,t.next=3,y.get("/get_ref?type=phone_types").catch((function(e){console.log(e)}));case 3:if(r=t.sent,r.err){t.next=7;break}return n("setCustomerPhoneTypes",r.data.payload),t.abrupt("return",!0);case 7:case"end":return t.stop()}}),t)})))()},loadProcessTypes:function(e){return Object(h["a"])(regeneratorRuntime.mark((function t(){var n,r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.commit,t.next=3,y.get("/get_ref?type=processTypes").catch((function(e){console.log(e)}));case 3:if(r=t.sent,r.err){t.next=7;break}return n("setProcessTypes",r.data.payload),t.abrupt("return",!0);case 7:case"end":return t.stop()}}),t)})))()},loadContactTypes:function(e){return Object(h["a"])(regeneratorRuntime.mark((function t(){var n,r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.commit,t.next=3,y.get("/get_ref?type=contactTypes").catch((function(e){console.log(e)}));case 3:if(r=t.sent,r.err){t.next=7;break}return n("setContactTypes",r.data.payload),t.abrupt("return",!0);case 7:case"end":return t.stop()}}),t)})))()},loadContactResults:function(e){return Object(h["a"])(regeneratorRuntime.mark((function t(){var n,r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.commit,t.next=3,y.get("/get_ref?type=contactResults").catch((function(e){console.log(e)}));case 3:if(r=t.sent,r.err){t.next=7;break}return n("setContactsResults",r.data.payload),t.abrupt("return",!0);case 7:case"end":return t.stop()}}),t)})))()},loadRefCsi:function(e){return Object(h["a"])(regeneratorRuntime.mark((function t(){var n,r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.commit,t.next=3,y.get("/get_ref?type=csi").catch((function(e){console.log(e)}));case 3:if(r=t.sent,r.err){t.next=7;break}return n("setRefCsi",r.data.payload),t.abrupt("return",!0);case 7:case"end":return t.stop()}}),t)})))()}},C={state:w,getters:x,actions:k,mutations:R},A=n("bc3a"),j=n("23b0"),O=A.create({baseURL:j.baseURL,timeout:1e5}),L={items:[]},P={customer_phones:function(e){return e.items}},T={setCustomerPhones:function(e,t){e.items=t}},D={loadCustomerPhonesByAgreement:function(e,t){return Object(h["a"])(regeneratorRuntime.mark((function n(){var r,a;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return r=e.commit,n.next=3,O.get("/phone?agreement_id=".concat(t)).catch((function(e){console.log(e)}));case 3:if(a=n.sent,a.err){n.next=7;break}return r("setCustomerPhones",a.data.payload),n.abrupt("return",!0);case 7:case"end":return n.stop()}}),n)})))()}},I={state:L,getters:P,actions:D,mutations:T},N=(n("f243"),n("b956"),n("a43f"),n("6e6b"),n("791e"),n("bc3a")),S=n("23b0"),U=N.create({baseURL:S.baseURL,timeout:1e5}),E={items:[],contacts:[],contactData:{result:!1,type:!1,comment:"",agreement_id:null,phone_id:null,new_phone:null,new_phone_type:null,installment_amt:"",installment_dt_to:""},csi_action_data:{agreement_id:null,csi:{},arrest_of_salary:"N",arrest_of_property:"N",arrest_of_accounts:"N",arrest_of_deparure:"N",comment:""},payments:[],csi_actions:[],csi:{},loading:!0},F={agreement_list:function(e){return function(t){return 0==t.length?e.items:e.items.filter((function(e){return e.agreement_no==t||e.customer.inn==t||e.id==t||e.customer.f==t}))}},agreement_loading:function(e){return e.loading},all_customer_agreements:function(e){return function(t){var n=e.items.find((function(e){return e.id==t}));return n?e.items.filter((function(e){return e.customer.id==n.customer.id})):[]}},agreement_Card:function(e){return function(t){return e.items.find((function(e){return e.id==t}))}},contactData:function(e){return e.contactData},csiActionData:function(e){return e.csi_action_data},contacts:function(e){return e.contacts},csi_actions:function(e){return e.csi_actions},agreement_payments:function(e){return e.payments},sum_agreement_payments:function(e){return e.payments.reduce((function(e,t){return e+t.amount}),0)}},B={loading:function(e,t){e.loading=t},setList:function(e,t){e.items=t,this.commit("loading",!1)},addAgreement:function(e,t){var n=t[0],r=e.items.findIndex((function(e){return e.id===n.id}));r>-1&&e.items.splice(r,1),e.items.push(n)},addManyAgreement:function(e,t){var n=function(n){var r=e.items.findIndex((function(e){return e.id===n.id}));-1==r&&e.items.push(t[n])};for(var r in t)n(r)},setContactAgreement:function(e,t){e.contactData.agreement_id=t},setCsiActionAgreement:function(e,t){var n=e.items.findIndex((function(e){return e.id==t}));if(-1===n)return!1;e.csi_action_data.agreement_id=t,e.csi_action_data.csi=e.items[n]["csi"]},setContacts:function(e,t){e.contacts=t},setCsiActions:function(e,t){e.csi_actions=t},appendNewContact:function(e,t){e.contacts.push(t),e.contactData.result=!1,e.contactData.type=!1,e.contactData.comment="",e.contactData.installment_amt="",e.contactData.installment_dt_to=""},appendNewCsiAction:function(e,t){e.csi_actions.unshift(t),e.csi_action_data.csi={},e.csi_action_data.arrest_of_salary="N",e.csi_action_data.arrest_of_property="N",e.csi_action_data.arrest_of_accounts="N",e.csi_action_data.arrest_of_deparure="N",e.csi_action_data.give_csi_dt="",e.csi_action_data.recall_csi_dt="",e.csi_action_data.stop_actions_csi_dt="",e.csi_action_data.return_ispol_doc_dt="",e.csi_action_data.comment=""},editCsiAction:function(e,t){var n=e.csi_actions.findIndex((function(e,n){return n.id==t.id}));e.csi_actions[n]=t},deleteCsiAction:function(e,t){var n=e.csi_actions.findIndex((function(e,n){return n.id==t}));e.csi_actions.splice(n,1)},setAgreementPayments:function(e,t){e.payments=t}},M={loadAgreementItems:function(e){return Object(h["a"])(regeneratorRuntime.mark((function t(){var n,r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.commit,t.next=3,U.get("/agreement").catch((function(e){console.log(e)}));case 3:if(r=t.sent,r.err){t.next=7;break}return n("setList",r.data.payload),t.abrupt("return",!0);case 7:case"end":return t.stop()}}),t)})))()},searchAgreementByString:function(e,t){return Object(h["a"])(regeneratorRuntime.mark((function n(){var r,a;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return r=e.commit,n.next=3,U.get("/agreement?search_by_string=".concat(t)).catch((function(e){console.log(e)}));case 3:a=n.sent,r("addManyAgreement",a.data.payload);case 5:case"end":return n.stop()}}),n)})))()},getAgreementByID:function(e,t){return Object(h["a"])(regeneratorRuntime.mark((function n(){var r,a;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return r=e.commit,n.next=3,U.get("/agreement/".concat(t)).catch((function(e){console.log(e)}));case 3:if(a=n.sent,a.err){n.next=9;break}return r("addAgreement",a.data.payload),r("setContacts",a.data.contacts),r("setCsiActions",a.data.csi_actions),n.abrupt("return",!0);case 9:case"end":return n.stop()}}),n)})))()},getAgreementPaymentsByAgreementID:function(e,t){return Object(h["a"])(regeneratorRuntime.mark((function n(){var r,a;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return r=e.commit,n.next=3,U.get("/payment?agreement_id=".concat(t)).catch((function(e){console.log(e)}));case 3:if(a=n.sent,a.err){n.next=7;break}return r("setAgreementPayments",a.data.payload),n.abrupt("return",!0);case 7:case"end":return n.stop()}}),n)})))()},saveContactData:function(e){return Object(h["a"])(regeneratorRuntime.mark((function t(){var n,r,a;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.state,r=e.commit,t.next=3,U.post("/contact",n.contactData).catch((function(e){console.log(e)}));case 3:if(a=t.sent,a.err){t.next=7;break}return r("appendNewContact",a.data.payload),t.abrupt("return",!0);case 7:case"end":return t.stop()}}),t)})))()},saveCsiAction:function(e,t){return Object(h["a"])(regeneratorRuntime.mark((function t(){var n,r,a;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.state,r=e.commit,t.next=3,U.post("/csi_actions",n.csi_action_data).catch((function(e){console.log(e)}));case 3:if(a=t.sent,a.err){t.next=7;break}return r("appendNewCsiAction",a.data.payload),t.abrupt("return",!0);case 7:case"end":return t.stop()}}),t)})))()},editCsiAction:function(e,t){return Object(h["a"])(regeneratorRuntime.mark((function n(){var r,a;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return r=e.commit,n.next=3,U.put("/csi_actions",t).catch((function(e){console.log(e)}));case 3:if(a=n.sent,a.err){n.next=7;break}return r("editCsiAction",a.data.payload),n.abrupt("return",!0);case 7:case"end":return n.stop()}}),n)})))()},deleteCsiAction:function(e,t){return Object(h["a"])(regeneratorRuntime.mark((function n(){var r,a;return regeneratorRuntime.wrap((function(n){while(1)switch(n.prev=n.next){case 0:return r=e.commit,n.next=3,U.delete("/csi_actions/".concat(t)).catch((function(e){console.log(e)}));case 3:if(a=n.sent,a.err){n.next=7;break}return r("deleteCsiAction",t),n.abrupt("return",!0);case 7:case"end":return n.stop()}}),n)})))()},changeAgreement:function(e,t){var n=this;return Object(h["a"])(regeneratorRuntime.mark((function r(){var a,o;return regeneratorRuntime.wrap((function(r){while(1)switch(r.prev=r.next){case 0:return e.state,e.commit,a=n.getters.agreement_Card(t),r.next=4,U.put("/agreement/".concat(a.id),{agreement:a}).catch((function(e){console.log(e)}));case 4:if(o=r.sent,o.err){r.next=7;break}return r.abrupt("return",!0);case 7:return r.abrupt("return",!0);case 8:case"end":return r.stop()}}),r)})))()}},J={state:E,getters:F,actions:M,mutations:B},q=(n("c64a"),n("fbac"),n("8e0c"),n("e00f"),n("e9a4"),n("f681"),n("ceab"),n("390c"),n("0ea5"),n("5f18"),n("e137"),n("2139"),n("261b"),n("e5e7"),n("abfa"),n("482d"),n("c702"),n("1092"),n("92b6"),n("10cd"),n("e836"),n("cac0"),n("8319"),n("15bf"),n("c7a0"),n("a687"),n("ade3"),n("bc3a")),$=n("23b0");var G=q.create({baseURL:$.baseURL,timeout:3e5}),H={items:[],defaultItem:{select:0,types:[],file:void 0},loading:!0},K={load_list:function(e){return e.items},load_loading:function(e){return e.loading},loaderDefaultItem:function(e){return e.defaultItem}},z={setList:function(e,t){e.items=t},setLoaderDefaultItemType:function(e,t){e.defaultItem.types=t},closeLoaderModal:function(e){e.defaultItem.select=0,e.defaultItem.file=void 0}},Q={saveLoadData:function(e){return Object(h["a"])(regeneratorRuntime.mark((function t(){var n,r,a;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return e.commit,n=e.state,r=new FormData,r.append("file",n.defaultItem.file),r.append("type",n.defaultItem.select),t.next=6,G.post("/loader",r,{headers:{"Content-Type":"multipart/form-data"}}).catch((function(e){console.log(e)}));case 6:if(a=t.sent,!a.data["payload"]["content_type"]){t.next=10;break}return window.open($.baseURL+"get-report?content_type=".concat(a.data["payload"]["content_type"],"&filename=").concat(a.data["payload"]["filename"])),t.abrupt("return",!0);case 10:case"end":return t.stop()}}),t)})))()},loadLoaderItems:function(e){return Object(h["a"])(regeneratorRuntime.mark((function t(){var n,r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.commit,t.next=3,G.get("/loader").catch((function(e){console.log(e)}));case 3:if(r=t.sent,r.err){t.next=7;break}return n("setList",r.data.payload),t.abrupt("return",!0);case 7:case"end":return t.stop()}}),t)})))()},loaderLoadRefs:function(e){return Object(h["a"])(regeneratorRuntime.mark((function t(){var n,r;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return n=e.commit,t.next=3,G.get("/get_ref?type=loaderTypes").catch((function(e){console.log(e)}));case 3:if(r=t.sent,r.err){t.next=7;break}return n("setLoaderDefaultItemType",r.data.payload),t.abrupt("return",!0);case 7:case"end":return t.stop()}}),t)})))()}},V={state:H,getters:K,actions:Q,mutations:z};r["default"].use(_["a"]);var W=new _["a"].Store({modules:{ref:C,phone:I,agreement:J,loadManager:V}});n("d5e8");r["default"].config.productionTip=!1,new r["default"]({router:g,vuetify:d,store:W,render:function(e){return e(f)}}).$mount("#app")},bd03:function(e,t,n){}});
//# sourceMappingURL=app.7c586dd2.js.map