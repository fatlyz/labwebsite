function showdata(data) {
    // div获取得到div内容列表
    var div = document.getElementsByClassName('infolist')
    // 每次点击前清屏掉div[0]的内容
    div[0].innerHTML = ''
    // 数组的map函数：map(参数：箭头函数)：返回一个数组，把data1返回为return的格式
    data1 = data.map((item) =>
    {
        if(item.Tag==0){
            return (
                /*tag==0表示期刊*/
                '<div><strong> -&ensp;'+item.PaperName+'</strong></div>'+
                '<div>&emsp;&emsp;&emsp;'+item.Authors+'</div>'+
                '<div>&emsp;&emsp;&emsp;'+item.periodical.Category+'</div>'+
                '<div>&emsp;&emsp;&emsp;Year:&ensp;'+item.PublicTime+'&ensp;|&ensp;Volume:&ensp;'+item.periodical.VolumeNumber+'&ensp;,&ensp;Issue:&ensp;'+item.periodical.IssueNumber+'&ensp;|&ensp;'
                +item.periodical.PeriodicalName+'&ensp;|&ensp;Publisher:&ensp;'+item.periodical.Institution +'</div>'+
                '<div onclick = \'showabstract(this)\' class = "click"><strong>&emsp;&emsp;&emsp;Abstract▼</strong>'+
                '<div class = "Abstract" style = "display:none;">'+item.Abstract+'</div></div>'
            )
        }
        else{
            return (
                /*tag==1表示会议*/
                '<div><strong> -&ensp;'+item.PaperName+'</strong></div>'+
                '<div>&emsp;&emsp;&emsp;'+item.Authors+'</div>'+
                '<div>&emsp;&emsp;&emsp;'+item.meeting.MeetName+'</div>'+
                '<div>&emsp;&emsp;&emsp;Year:&ensp;'+item.PublicTime+'&ensp;|&ensp;Time:&ensp;'+item.meeting.Meetdate+'&ensp;|&ensp;Place:&ensp;'+item.meeting.MeetPlace+'&ensp;|&ensp;Term:&ensp;'
                +item.meeting.MeetTerm+'&ensp;|&ensp;Publisher:&ensp;'+item.meeting.Institution
                +'</div>'+
                '<div onclick = \'showabstract(this)\' class = "click"><strong>&emsp;&emsp;&emsp;Abstract▼</strong>'+
                '<div class = "Abstract" style = "display:none;">'+item.Abstract+'</div></div>'
            )
        }


    })
    console.log(data1)


    for(let i=0;i<data1.length;i++){
        var new_div=document.createElement('div')
        var br=document.createElement('br')
        new_div.innerHTML=data1[i]
        // new_div.style.marginLeft="50px"
        new_div.classList.add('paper_box')
        div[0].appendChild(new_div)
        div[0].appendChild(br)
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

    //fetch get的参数传递:直接在url后添加?id
    //fetch post 的复杂
    fetch('/issuelist?year='+id).then(data => {
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
var Abstract = document.getElementsByClassName('Abstract')
//该页面默认显示2022年论文,页面初次加载时执行一次，默认显示2022的界面
get(2022)
function showabstract(id){
    console.log(id.childNodes[0])
    if(id.childNodes[1].style.display == 'none')
        id.childNodes[1].style.display = 'block'
    else id.childNodes[1].style.display = 'none'
    if(id.childNodes[1].style.display == 'none')
        id.childNodes[0].innerHTML='&emsp;&emsp;&emsp;Abstract▼'
    else id.childNodes[0].innerHTML='&emsp;&emsp;&emsp;Abstract▲'
    return 0
}