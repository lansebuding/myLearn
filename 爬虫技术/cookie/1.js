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
var headerCode = function () {
  var org = window.XMLHttpRequest.prototype.setRequestHeader;

  window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
    if (key == "x-path") debugger;
    return org.apply(this, arguments);
  };
};

// 请求参数hook
var urlCode = function () {
  var org = window.XMLHttpRequest.prototype.open;
  window.XMLHttpRequest.prototype.open = function (method, url, async) {
    console.log(method, url, async);
    return org.open(this, arguments);
  };
};
