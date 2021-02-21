var control_btn = document.getElementById("control_btn");
var scan_btn = document.getElementById("scan_btn");
var main_btn = document.getElementById("main_btn");
var up_btn = document.getElementById("up_btn");
var left_btn = document.getElementById("left_btn");
var right_btn = document.getElementById("right_btn");
var down_btn = document.getElementById("down_btn");
var target_red = document.getElementById("target_red");
var target_green = document.getElementById("target_green");
var target_blue = document.getElementById("target_blue"); 
var target_yellow = document.getElementById("target_yellow");
var select = document.getElementById("select");
var scan = document.getElementById("scan");
var go = document.getElementById("go");
var scan_timer;
var json_data = {
    "command": ""
};
main_btn.addEventListener('click',function(){
    reset_targets();
    control_btn.style.display = "block";
    scan_btn.style.display = "block";
    up_btn.style.display = "none";
    left_btn.style.display = "none";
    right_btn.style.display = "none";
    down_btn.style.display = "none";
    main_btn.style.display = "none";
    scan.style.display = "none";
    select.style.display = "none";
    select.style.color = "black";
    target_red.style.display = "none";
    target_green.style.display = "none";
    target_blue.style.display = "none";
    target_yellow.style.display = "none";
    go.style.display = "none";
})
control_btn.addEventListener("click",function() {
    control_btn.style.display = "none";
    scan_btn.style.display = "none";
    up_btn.style.display = "block";
    left_btn.style.display = "block";
    right_btn.style.display = "block";
    down_btn.style.display = "block";
    main_btn.style.display = "block";
})
scan_btn.addEventListener("click",function() {
    reset_targets();
    control_btn.style.display = "none";
    scan_btn.style.display = "none";
    scan.style.color = "red"; 
    scan.innerHTML = "Scanning...";
    scan.style.display = "block";
    main_btn.style.display = "block";
    window.scan_timer = setInterval(read_json,250);
    json_data["command"] = "5";
    send_json(JSON.stringify(json_data));
    console.log("bastı1"); 
})
up_btn.addEventListener("mousedown", function() {
    json_data["command"] = "1";
    send_json(JSON.stringify(json_data));
    console.log("bastı1"); 
})
up_btn.addEventListener("mouseup",function(){
    json_data["command"] = "0";
    send_json(JSON.stringify(json_data));
    console.log("bıraktı"); 
})
left_btn.addEventListener("mousedown", function() {
    json_data["command"] = "2";
    send_json(JSON.stringify(json_data));
    console.log("bastı2"); 
})
left_btn.addEventListener("mouseup",function(){
    json_data["command"] = "0";
    send_json(JSON.stringify(json_data));
    console.log("bıraktı"); 

})
right_btn.addEventListener("mousedown", function() {
    json_data["command"] = "3";
    send_json(JSON.stringify(json_data));
    console.log("bastı3"); 
})
right_btn.addEventListener("mouseup",function(){
    json_data["command"] = "0";
    send_json(JSON.stringify(json_data));
    console.log("bıraktı"); 

})
down_btn.addEventListener("mousedown", function() {
    json_data["command"] = "4";
    send_json(JSON.stringify(json_data));
    console.log("bastı4"); 
})
down_btn.addEventListener("mouseup",function(){
    json_data["command"] = "0";
    send_json(JSON.stringify(json_data));
    console.log("bıraktı"); 
})
target_red.addEventListener("click",function (){
    select.innerHTML = "Red Target Selected";
    select.style.color = "red";
    go.style.display = "block";
})
target_green.addEventListener("click",function (){
    select.innerHTML = "Green Target Selected";
    select.style.color = "green";
    go.style.display = "block";
})
target_blue.addEventListener("click",function (){
    select.innerHTML = "Blue Target Selected";
    select.style.color = "blue";
    go.style.display = "block";
})
target_yellow.addEventListener("click",function (){
    select.innerHTML = "Yellow Target Selected";
    select.style.color = "yellow";
    go.style.display = "block";
})
go.addEventListener("click",function () {
    json_data["command"] = "6";
    send_json(JSON.stringify(json_data));
    console.log("GO");
})


function send_json(data) {
    var request = new XMLHttpRequest();
    request.open("POST","request.php");
    request.send(data);
}
function reset_targets(){
    window.target_red.style.display = "none";
    window.target_green.style.display = "none";
    window.target_blue.style.display = "none";
    window.target_yellow.style.display = "none";
    window.select.style.display = "none";
}
function read_json() {
    var request = new XMLHttpRequest();
    request.open("GET","json/info.json")
    request.onload = function name(params) {
        var data = JSON.parse(request.responseText);
        console.log("scanning");
        if (data['scaned'][0] == '1'){
            scan.style.color = "green";
            scan.innerHTML = "Scan is finished.";
            
            if (data['target'][0] == '1'){
                target_red.style.display = "block";
                select.innerHTML = "Select A Target";
                select.style.display = "block";
                console.log("red");
            }  
            if (data['target'][1] == '1'){
                target_green.style.display = "block";
                select.innerHTML = "Select A Target";
                select.style.display = "block";
                console.log("green");
            }  
            if (data['target'][2] == '1'){
                target_blue.style.display = "block";
                select.innerHTML = "Select A Target";
                select.style.display = "block";
                console.log("blue");
            }  
            if (data['target'][3] == '1'){
                target_yellow.style.display = "block";
                select.innerHTML = "Select A Target";
                select.style.display = "block";
                console.log("yellow");
            }
            delete window.data; 
            clearInterval(window.scan_timer);
        }
           
    }
    request.send()
}