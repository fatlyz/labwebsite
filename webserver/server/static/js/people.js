function GetUrlParam(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null)
        return unescape(r[2]);
    return null;
}

//调用获取参数方法
var name = GetUrlParam("name");
console.log(name);

function getText() {
        var res = $('p').find('p').text();
        alert(res);
}
