let color="green";
//Traffic Light System
if(color=="red"){
    console.log("Stop! light color is red");
}
else if(color=="yellow"){
    console.log("slow down light color is yellow");

}
else if(color=="green"){
    console.log("go light color is green");

}

//pq2
let size="XL"
if(size==="XL"){
    console.log("price is Rs.250");
}
else if(size==="L"){
    console.log("price is Rs.200")
}
else if(size==="M"){
    console.log("price is Rs.100");
}

else{
    console.log("price is Rs.50");
}

//nested if -else
    let marks=99;
if(marks>=33){
    console.log("Pass");
    if(marks>=80){
        console.log("Grade : O")
    }
    else{
        console.log("Grade:A");
    }
}
else{
    console.log("Better luck next time!");
}






//pq3 good string
let str="apple"
if((str[0]==='a')&&(str.length>3)){
    console.log("Good String");
}
else{
    console.log("not a good string");
}

//pq-3 predict the output
let num=12;
if((num%3===0)&&((num+1===15)||(num-1===11))){
    console.log("safe");
}
else{
    console.log("unsafe");
}


if(true){
    console.log("it has true value");
}
else{
    console.log("it has false value");
}



let string=" ";
if(string){
    console.log("String is not empty");
}
else{
    console.log("string is empty");
}


//switch statement
let color1="red";
switch (color1){
    case "red":
        console.log("stop");
        break;
    case "yellow":
        console.log("slow down");
        break;
    case "green":
        console.log("go");
        break;
    default:
        console.log("light is broken");
   
}
console.log("after switch statement st");



//pq-4 calendar days
let day=1;
switch(day){
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("Tuesday");
        break;
    case 3:
        console.log("Wednesday");
        break;
    case 4:
        console.log("Thursday");
        break;
    case 5:
        console.log("Friday");
        break;
    case 6:
        console.log("Saturday");
        break;
    case 7:
        console.log("Sunday,fun day");
        break;
    default:
        console.log("wrong day!"); 
}


//alert
alert("something is wrong!");
//error
console.error("this is an error msg");
console.warn("this is an warning  msg");

//prompt
fn=prompt("enter your first name");
ln=prompt("enter your last name");
console.log("Welcome",fn," ",ln,"!");
//or
let msg="Welcome"+fn+" "+ln+"!";
alert(msg);

//string methods
let msg1="  hello  "
msg1.trim();

