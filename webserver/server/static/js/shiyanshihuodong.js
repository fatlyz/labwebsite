function showdata(data) {
    // div获取得到div内容列表
    var div = document.getElementsByClassName('img-activity')
    div[0].innerHTML=''
    console.log(data)
    // 数组的map函数：map(参数：箭头函数)：返回一个数组，把data1返回为return的格式
    data1 = data.map((item) => {
        if (item.Tag == 1) {
            return (
                '<div><img style="height: 80%;width:70% " id="round" src=" ' + item.MeetingPhotoUrl+ '"</div>' +
                '<div><strong> '+item.Time +'</strong></div>'+
                '<div><strong>'+item.Content +'</strong></div>'
            )
        } else {
            return (
                '<div><img style="height: 80%;width:70% " id="round" src=" ' + item.ActivityPhotoUrl + '"</div>' +
                '<div><strong> '+item.Time+'</strong></div>'+
                '<div><strong> '+item.Title+'</strong></div>'
            )
        }

    })
    for (let i = 0; i < data1.length; i++) {
        var new_div = document.createElement('div')
        new_div.innerHTML = data1[i]
        new_div.classList.add('paper_box')
        div[0].appendChild(new_div)
    }
    // innerHTML：获取对象的内容 或 向对象插入内容
    // div[0].innerHTML = data1
}

//1.获取数据
//2.异常处理
function get(id) {
    // console.log(id)
    /*data：函数参数
    箭头指向函数操作
    需要至少两次then
    fetch('url').then(参数=>{函数操作}).then(参数=>{函数操作}).catch(参数=>{异常函数操作})*/

    // fetch get的参数传递:直接在url后添加?id
    // fetch post 的复杂
    fetch('/activelist?number='+id).then(data => {
            return data.json()
        }
    ).then(data => {
        //json数据对象:
        //{"name":"值","age":20},{"name":"值","age":20}
        showdata(data)
    })
        .catch((err) => {
            console.log(err)
        })
}


//该页面默认显示2022年论文,页面初次加载时执行一次，默认显示2022的界面
get(1)
