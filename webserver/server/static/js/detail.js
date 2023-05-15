
var name = decodeURIComponent(window.location.search.split("?")[1])
    console.log(name)
function showpic(data) {
    console.log(data)
    // div获取得到div内容列表
    var div = document.getElementsByClassName('paper')
    // 数组的map函数：map(参数：箭头函数)：返回一个数组，把data1返回为return的格式
    data1 = data.map((item) =>
    {
            return (
                '<div><img style="height: 200px;width: 200px"  id="round" src=" ' +item.Avtar+ '"></div>'+
                '<div>'+item.Name+'</div>'
            )
    })
    //console.log(data1)
    // innerHTML：获取对象的内容 或 向对象插入内容
    div[0].innerHTML = data1
}

function showdata(data) {
    // div获取得到div内容列表
    var div = document.getElementsByClassName('infolist')
    // 数组的map函数：map(参数：箭头函数)：返回一个数组，把data1返回为return的格式
    data1 = data.map((item) =>
    {
        
            return (
                '<div class="title"><strong>研究方向:</strong></div>'+
                    '<div class="title">&emsp;&emsp;'+item.Direction+'</div>'+
                '<div class="title"><strong>项目经历:</strong></div>'+
                    // map循环输出项目
                    '<div class="title">&emsp;&emsp;'+item.Projects.map(i => {
                        return i.ProjectName
                })+'</div>'+
                '<div class="title"><strong>科研成果:</strong></div>'+
                    '<div class="title">&emsp;&emsp;'+item.paperlist.map(i => {
                        return i.PaperName
                }
                )+'</div>'+
                '<div class="title"><strong>获奖情况:</strong></div>'+
                    '<div class="title">&emsp;&emsp;'+item.Awards+'</div>'
            )
    })
    //console.log(data1)
    // innerHTML：获取对象的内容 或 向对象插入内容
    div[0].innerHTML = data1
}

//1.获取数据
//2.异常处理
//3.页面跳转
function get(id) {
    tid = id
    // fetch('url').then(参数=>{函数操作}).then(参数=>{函数操作}).catch(参数=>{异常函数操作})
    //fetch get的参数传递:直接在url后添加?id
    fetch('/userinfo?name='+id).then(data => {
            return data.json()
        }
    ).then(data => {
        console.log(data)
        showdata(data)
        showpic(data)
    })
        .catch((err) => {
            console.log(err)
        })
}
get(name)

