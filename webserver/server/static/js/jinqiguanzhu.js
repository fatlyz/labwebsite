function showdata(data) {
    // div获取得到div内容列表
    var div = document.getElementsByClassName('infolist')
    //每次点击前清屏掉div[0]的内容
    div[0].innerHTML = ''
    // 数组的map函数：map(参数：箭头函数)：返回一个数组，把data1返回为return的格式
    data1 = data.map((item) =>
    {
        return (
            '<div><strong>-&ensp;' + item.MeetName + '</strong></div>' +
            '<div>&emsp;&emsp;&emsp;' + item.Meetdate +  ' | ' +
            item.MeetPlace + '</div>'

        )
    })
    // innerHTML：获取对象的内容 或 向对象插入内容
    //div[0].innerHTML = data1
    //console.log(data)
    for(let i=0;i<data1.length;i++){
        var new_div=document.createElement('div')
        var br=document.createElement('br')
        new_div.innerHTML=data1[i]
        // new_div.style.marginLeft="50px"
        new_div.classList.add('paper_box')
        div[0].appendChild(new_div)
        div[0].appendChild(br)
    }
}
function showdata1(data) {
    // div获取得到div内容列表
    var div = document.getElementsByClassName('infolist')
    //每次点击前清屏掉div[0]的内容
    div[0].innerHTML = ''
    // 数组的map函数：map(参数：箭头函数)：返回一个数组，把data1返回为return的格式
    data1 = data.map((item) =>
    {
        return (
            '<div><strong>-&ensp;' + item.PeriodicalName + '</strong></div>' 
        )
    })
    // innerHTML：获取对象的内容 或 向对象插入内容
    //div[0].innerHTML = data1
    //console.log(data)
    for(let i=0;i<data1.length;i++){
        var new_div=document.createElement('div')
        var br=document.createElement('br')
        new_div.innerHTML=data1[i]
        // new_div.style.marginLeft="50px"
        new_div.classList.add('paper_box')
        div[0].appendChild(new_div)
        div[0].appendChild(br)
    }
}
//1.获取数据
//2.异常处理
function get() {
    //fetch get的参数传递:直接在url后添加?id
    //fetch post 的复杂
    //注意json文件里面外面必须加[],不然不行
    fetch('/meetinglist').then(data => {
            return data.json()
        }
    ).then(data => {
        showdata(data)
    })
        .catch((err) => {
            //console.log(err)
        })
}
function getpaper() {
    fetch('/periodicallist').then(data => {
            return data.json()
        }
    ).then(data => {
        console.log(data)
        showdata1(data)
    })
        .catch((err) => {
            //console.log(err)
        })
}
//该页面默认显示会议
get()