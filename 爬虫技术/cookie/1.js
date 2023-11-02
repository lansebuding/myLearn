(function () {
  let temp = "";
  Object.defineProperty(document, "cookie", {
    set: function (val) {
      if (val.indexOf("__dfp") > -1) {
        debugger;
      }
      console.log("成功捕获，val===>" + val);
      temp = val;
      return val;
    },
    get: function () {
      return temp;
    },
  });
})();

// 请求头hook
(function () {
  var org = window.XMLHttpRequest.prototype.setRequestHeader;

  window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
    console.log(key,value);
    if (key == "portal-sign") {
      debugger;
    }
    return org.apply(this, arguments);
  };
})();

// 请求参数hook
(function () {
  var open = window.XMLHttpRequest.prototype.open;
  window.XMLHttpRequest.prototype.open = function (method, url, async) {
    console.log(url);
      if (url.indexOf("heart-beat") != -1) {
          debugger;
      }
      return open.apply(this, arguments);
  };
})();

// eval/Function
window.__cr_eval = window.eval
​
// 捕捉到debugger位置
var myeval = function (src) {
    console.log("============ eval begin: length=" + src.length + ",caller=" + (myeval.caller && myeval.caller.name) + " ===============")
    console.log(">>>>>>>>>>>> eval injected: " + document.location + " <<<<<<<<<<<<<<<<")
    console.log(src);
    console.log("============ eval end =============")
    return window.__cr_eval(src)
}
​
// 会有一些反爬会识别是不是本机代码,这个地方是小花招本招,防止被识别
var _myeval = myeval.bind(null)
_myeval.toString = window.__cr_eval.toString
Object.defineProperty(window, 'eval', { value: myeval })

// hook 函数构造器

Function.prototype._back = Function.prototype.constructor
Function.prototype.constructor = function(){
  if(arguments&&typeof arguments[0]=='string'){
    if(arguments[0]=='debugger')return ''
  }
  return Function.prototype._back.apply(this,arguments)
}