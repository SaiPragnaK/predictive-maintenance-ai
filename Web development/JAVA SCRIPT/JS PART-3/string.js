let msg="  hello  "
msg;
msg.trim();

let pwd=prompt("set your password");
let newpwd=pwd.trim()
console.log(newpwd);


let name="Apna College";
 res1=name.toLowerCase();
 console.log(res1);
 console.log(name.toUpperCase());


 let str="ILoveCoding";
 console.log(str);
 console.log(str.indexOf("Love"));
console.log(str.indexOf("J"));
console.log(str.indexOf("o"));



//method chaining
// let str1="  hello  "
// let nstr=str1.trim();
// console.log("after trim",nstr);
// nstr=nstr.toUpperCase();
// console.log("after trim and uppercase",nstr);

//so simply we can write
let str1="  hello  "
let nstr=str1.trim().toUpperCase();
console.log(nstr);

//slice method
let s2="hello";
console.log(s2.slice(0,4));
console.log(s2.slice(4,s2.length));
console.log(s2.slice(-1));

//replace
let s3="IloveCoding";
console.log(s3.replace("love","do"));
let fruit="Mango";
console.log(fruit.repeat(5));
