({4870:function(){var t,e=this&&this.__extends||(t=function(e,n){return t=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var n in e)Object.prototype.hasOwnProperty.call(e,n)&&(t[n]=e[n])},t(e,n)},function(e,n){if("function"!=typeof n&&null!==n)throw new TypeError("Class extends value "+String(n)+" is not a constructor or null");function r(){this.constructor=e}t(e,n),e.prototype=null===n?Object.create(n):(r.prototype=n.prototype,new r)}),n=this&&this.__assign||function(){return n=Object.assign||function(t){for(var e,n=1,r=arguments.length;n<r;n++)for(var i in e=arguments[n])Object.prototype.hasOwnProperty.call(e,i)&&(t[i]=e[i]);return t},n.apply(this,arguments)},r=this&&this.__read||function(t,e){var n="function"==typeof Symbol&&t[Symbol.iterator];if(!n)return t;var r,i,o=n.call(t),a=[];try{for(;(void 0===e||e-- >0)&&!(r=o.next()).done;)a.push(r.value)}catch(t){i={error:t}}finally{try{r&&!r.done&&(n=o.return)&&n.call(o)}finally{if(i)throw i.error}}return a},i=this&&this.__spreadArray||function(t,e,n){if(n||2===arguments.length)for(var r,i=0,o=e.length;i<o;i++)!r&&i in e||(r||(r=Array.prototype.slice.call(e,0,i)),r[i]=e[i]);return t.concat(r||Array.prototype.slice.call(e))},o=this&&this.__values||function(t){var e="function"==typeof Symbol&&Symbol.iterator,n=e&&t[e],r=0;if(n)return n.call(t);if(t&&"number"==typeof t.length)return{next:function(){return t&&r>=t.length&&(t=void 0),{value:t&&t[r++],done:!t}}};throw new TypeError(e?"Object is not iterable.":"Symbol.iterator is not defined.")},a=function(){function t(t,e,n,r,i){var o=':input[name="'+e+'"]';this.input=t.find(o).addBack(o),this.idForLabel=n,this.setState(r),this.parentCapabilities=i||new Map}return t.prototype.getValue=function(){return this.input.val()},t.prototype.getState=function(){return this.input.val()},t.prototype.setState=function(t){this.input.val(t)},t.prototype.getTextLabel=function(t){var e=this.getValue();if("string"!=typeof e)return null;var n=t&&t.maxLength;return n&&e.length>n?e.substring(0,n-1)+"…":e},t.prototype.focus=function(){this.input.focus()},t.prototype.setCapabilityOptions=function(t,e){Object.assign(this.parentCapabilities.get(t),e)},t}(),u=function(){function t(t,e){this.boundWidgetClass=a,this.html=t,this.idPattern=e}return t.prototype.render=function(t,e,n,r,i){var o=this.html.replace(/__NAME__/g,e).replace(/__ID__/g,n),a=this.idPattern.replace(/__ID__/g,n),u=$(o);return $(t).replaceWith(u),new this.boundWidgetClass(u,e,a,r,i)},t}();window.telepath.register("wagtail.widgets.Widget",u);var s=function(t){function n(){return null!==t&&t.apply(this,arguments)||this}return e(n,t),n.prototype.getValue=function(){return this.input.is(":checked")},n.prototype.getState=function(){return this.input.is(":checked")},n.prototype.setState=function(t){this.input.attr("checked",t||null)},n}(a),l=function(t){function n(){var e=null!==t&&t.apply(this,arguments)||this;return e.boundWidgetClass=s,e}return e(n,t),n}(u);window.telepath.register("wagtail.widgets.CheckboxInput",l);var c=function(){function t(t,e,n,r){this.element=t,this.name=e,this.idForLabel=n,this.selector='input[name="'+e+'"]:checked',this.setState(r)}return t.prototype.getValue=function(){return this.element.find(this.selector).val()},t.prototype.getState=function(){return this.element.find(this.selector).val()},t.prototype.setState=function(t){this.element.find('input[name="'+this.name+'"]').val([t])},t.prototype.focus=function(){this.element.find('input[name="'+this.name+'"]').focus()},t}(),p=function(t){function n(){var e=null!==t&&t.apply(this,arguments)||this;return e.boundWidgetClass=c,e}return e(n,t),n}(u);window.telepath.register("wagtail.widgets.RadioSelect",p);var h=function(t){function n(){return null!==t&&t.apply(this,arguments)||this}return e(n,t),n.prototype.getTextLabel=function(){return this.input.find(":selected").text()},n}(a),f=function(t){function n(){var e=null!==t&&t.apply(this,arguments)||this;return e.boundWidgetClass=h,e}return e(n,t),n}(u);window.telepath.register("wagtail.widgets.Select",f);var d=function(){function t(t,e,n){this.html=t,this.idPattern=e,this.config=n}return t.prototype.render=function(t,e,n,r){var i=this.html.replace(/__NAME__/g,e).replace(/__ID__/g,n),o=$(i);$(t).replaceWith(o);var a=createPageChooser(n,null,this.config);return a.setState(r),a},t}();window.telepath.register("wagtail.widgets.PageChooser",d);var g=function(t){function n(){return null!==t&&t.apply(this,arguments)||this}return e(n,t),n.prototype.render=function(e,n,r,i,o){var a=t.prototype.render.call(this,e,n,r,i,o);return window.autosize($("#"+r)),a},n}(u);window.telepath.register("wagtail.widgets.AdminAutoHeightTextInput",g);var y=function(){function t(t){this.options=t}return t.prototype.render=function(t,e,a,u,s){var l=this.options,c=n({},l),p=s||new Map,h=p.get("split");h&&(c.controls=c.controls?i([],r(c.controls),!1):[],c.controls.push(draftail.getSplitControl(h.fn,!!h.enabled)));var f=document.createElement("input");f.type="hidden",f.id=a,f.name=e;var d=!!u.getCurrentContent;f.value=d?"null":u,t.appendChild(f);var g=r(draftail.initEditor("#"+a,c,document.currentScript),2),y=g[0],w=g[1],v={getValue:function(){return f.value},getState:function(){return f.draftailEditor.getEditorState()},setState:function(t){f.draftailEditor.onChange(t)},getTextLabel:function(t){var e,n,r=t&&t.maxLength;if(!f.value)return"";var i=JSON.parse(f.value);if(!i||!i.blocks)return"";var a="";try{for(var u=o(i.blocks),s=u.next();!s.done;s=u.next()){var l=s.value;if(l.text&&(a+=a?" "+l.text:l.text,r&&a.length>r))return a.substring(0,r-1)+"…"}}catch(t){e={error:t}}finally{try{s&&!s.done&&(n=u.return)&&n.call(u)}finally{if(e)throw e.error}}return a},focus:function(){setTimeout((function(){f.draftailEditor.focus()}),50)},setCapabilityOptions:function(t,e){var o=Object.assign(p.get(t),e);"split"===t&&w(n(n({},y),{controls:i(i([],r(l||[]),!1),[draftail.getSplitControl(o.fn,!!o.enabled)],!1)}))}};return d&&v.setState(u),v},t}();window.telepath.register("wagtail.widgets.DraftailRichTextArea",y);var w=function(t){function n(t){return this.options=t,this}return e(n,t),n.prototype.render=function(t,e,n,r){var i=document.createElement("input");i.type="text",i.name=e,i.id=n,t.replaceWith(i),this.initChooserFn(n,this.options);var o={getValue:function(){return i.value},getState:function(){return i.value},setState:function(t){i.value=t},focus:function(t){t&&t.soft||i.focus()},idForLabel:n};return o.setState(r),o},n}(u),v=function(t){function n(){var e=null!==t&&t.apply(this,arguments)||this;return e.initChooserFn=window.initDateChooser,e}return e(n,t),n}(w);window.telepath.register("wagtail.widgets.AdminDateInput",v);var m=function(t){function n(){var e=null!==t&&t.apply(this,arguments)||this;return e.initChooserFn=window.initTimeChooser,e}return e(n,t),n}(w);window.telepath.register("wagtail.widgets.AdminTimeInput",m);var _=function(t){function n(){var e=null!==t&&t.apply(this,arguments)||this;return e.initChooserFn=window.initDateTimeChooser,e}return e(n,t),n}(w);window.telepath.register("wagtail.widgets.AdminDateTimeInput",_);window.telepath.register("wagtail.errors.ValidationError",(function(t){this.messages=t}))}})[4870]();