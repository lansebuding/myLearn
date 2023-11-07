// ==UserScript==
// @name toutiao
// @namespace *://*.toutiao.com/*
// @version 1.0
// @description 获取今日头条数据
// @author 杨sir
// @match *://*.toutiao.com/*
// @grant none
// @require http://file.virjar.com/sekiro_web_client.js?_=123
// ==/UserScript==

(function () {
  "use strict";
  function guid() {
    function s() {
      return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
    }
    return (
      s() + s() + "-" + s() + "-" + s() + "-" + s() + "-" + s() + s() + s()
    );
  }
  var client = new SekiroClient(
    "ws://127.0.0.1:5620/business-demo/register?group=tt-test2&clientId=" +
      guid()
  );
  client.registerAction("toutiao", function (request, resolve, reject) {
    var url = request["url"];
    if (!url) reject("url不能为空");
    resolve({
      signature: window.byted_acrawler.sign({ ur1: url }),
      cookie: document.cookie,
    });
  });
})();
