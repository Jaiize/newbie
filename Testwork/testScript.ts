// node testscript.js
// tsc testscript.ts

let num = 1255.575485;
// arg = 0: is th same as empty parenthesis 
var result = num.toFixed(0);
var rounded = Math.round(num); // Both the same
// console.log(num, result, rounded);

var bigNo = 25545236888;
var fin = bigNo.toLocaleString();
// Alternative
var final = bigNo.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
// console.log(final)

const data = {
price: 2545825.25,
  discount: 2545825 / 2,
  items: 74253654,
  name: "Emmanuel",
};

// Object.keys(data).forEach((key) => {
//   data[key] = data[key].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
// });
// console.log(data)

let them = [4000, 4542695, 3000000, 12412452];
const no = them.map((pick) =>
  pick.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
  // pick.toLocaleString()
);
// console.log(no)


// let regex = /([a-z])\1.*(.)\d/ // prior index are accted (except the xter in-betweeb) for idx of the last two digits
// let regex = /([a-z])\1.*(\d)/ // prior index are accted for idx of the last digit(zero-based) and last digit len-based
// let regex = /([a-z])\1+(.)+(.)\d/ // prior index are accnted for but last 2 \d must be two for perfect indexing

// let regex = /([a-z])\1+([a-z])+(.)\d/ // (2, 3) means zero index 2 and len index 3 of the starting seen conditon 
// NB: This is how it all works. (This is the most accurate)

// let regex = /([a-z])\1+([a-z])+(\d)/ // identical xter + one xter + identical digit 


// let regex = /(\d)\1\1/; // For three identical digit!
// let regex  = /(s)+(.)+(s)\1"/ // For s(anything)ss
// let regex = /(s)+([a-z])+(s)\1"/ // For s(any lower. alphabet)ss
// let regex = /(\d)\1/; // For duplicate digit next to each other!
// let regex = /(.)\1/; // Works for both digits and letters
// let regex = /([a-z])\1\1/; // for three identical letters (lowercase)
// let regex = /(\d)/;  // Locate the first digit
// let regex = /(b)+(.*)+(b)/; // To check a xter (e.g b) that appeared more than once NB It also works on identical xter positioned side by side
// let regex = /([a-z][a-z])/; // Location of any two xters following each other
// let regex = /(?=.*[a-z])(?=.*[@$!%*?&])(?=.*\d)/g;
// let regex = /(?=.*\d)(?<=.*\d)/; // At least two digits anywhere (either together or separately) or /(?=.*\d.*\d)/g
// let regex = /(?=.*\d{2})/g; // At least any two digits following each other
// let regex = /^(?!.*\d{2}).*$/; // There's no two or more consecutive digits
// let regex = /(?=.*[a-z]{2})/g; // At least any two xters following each other

// let regex = /([a-z])\1.*(.)\d/;  // For a duplicate digit and letter
// let regex = /([a-z]{3})/;
// let pass = "P@sssw2rd";
// let pass = "P@w7d8df";
// let pass = "4555267";
// let pass = "P@ssw75df";
let regex = /(bab)/;
let pass = "rabab";

if (regex.test(pass)) {
  let receiver = regex.exec(pass);
  console.log("Yes!", receiver, `Len = ${receiver![0].length}`, `Index = ${receiver?.index}`);
  // let output = '';
  // for(let i = 0; i < pass.length; i++){
  // console.log(pass[i])
  // process.stdout.write // npm i --save-dev @types/node
  // output += pass[i]
  // }
  // console.log('\n')

  // for(let i = 0; i < pass.length; i++){
  //   // if(i >= receiver![0].length - 1){
  //   if(i >= receiver?.index!){
  //     console.log(pass[i])
  //   }
  // }
} else {
  console.log("No!");
}




let newData = { ...data, price: undefined };
let catched = JSON.stringify(newData);
let opp = JSON.parse(catched);
// console.log(catched, '\n', opp);

const myDate = new Date();
let to_join = ["Tos", "in", "Jo", "seph",]
let resu = to_join.join("")
// console.log(to_join, resu)

// const time_Test = myDate.toLocaleTimeString('en-US', {hour: 'numeric', minute: 'numeric', month: "long"}) // Don't know month shows up
// const time_Test = myDate.toLocaleTimeString('en-US', {hour: 'numeric', minute: 'numeric'}) // 10:50 PM


// const goodDate = myDate.toDateString(); // Fri Jul 11 2025
// const dateTest = myDate.toUTCString() // Fri, 11 Jul 2025 15:55:04 GMT NB: Hour is an Hour late

/**
 * Monday, August 4, 2025 at 10:55 PM
 */
// const dateTest = myDate.toLocaleString('en-US', {month: 'long', weekday: 'long', day: 'numeric', year: 'numeric', hour: 'numeric', minute: 'numeric'})


/**
 * Monday, August 4 10:51 PM NB: you can also get month separately by filling in the month property only
 * */
const dateString = myDate.toLocaleDateString('en-US', {weekday: 'long', month: 'long', day: 'numeric', hour: 'numeric', minute: '2-digit'}) 


// const year = myDate.getFullYear()
// const month = myDate.getMonth() + 1
// const date = myDate.getDate()
// const day = myDate.getDay() // Day of the week in number (e.g monday = 1)

// const frmted = `${month} ${day} ${date}, ${year}`

// console.log(frmted)

const key = crypto.randomUUID();
// console.log(key.replace(/(-)/g, '0'));
// console.log(key);

interface Article {
  Author: string,
  tagg: string[]
  // tagg: string
  published: boolean
}

const for_tags: Article[] = [
  {Author: "Tosin", tagg: ["Coding", "Testing"], published: true},
  {Author: "Jaize", tagg: ["Coding"], published: true},
  {Author: "Joseph", tagg: ["Testing"], published: true},
  {Author: "Emmanuel", tagg: ["testing", "coding"], published: true}
] 

// const for_tags: Article[] = [
//   {Author: "Tosin", tagg: "Coding,Testing", published: true},
//   {Author: "Jaize", tagg: "Coding", published: true},
//   {Author: "Joseph", tagg: "Testing,Coding", published: true}
// ]

let tag_test = ["Coding", "Testing"]

// const for_d = for_tags.filter((pick) => {
//   return pick.tagg.includes("Coding")
// })

const for_multi = for_tags.filter((pick) => 
  tag_test.every(t => pick.tagg.includes(t))
)

// console.log(for_d)
// console.log(for_multi)

interface Person {
  name: string,
  age: number,
  address: string | string[], 
  isOnline: boolean
}

interface other extends Person {
  image: string,
  kin: string | string[],
  maidenName: string,
}

const instead: Person = {
  name: "Jaize",
  age: 12,
  address: 'LA',
  isOnline: false
}


// instead.isOnline = instead.isOnline ?? false
instead.isOnline = !!instead.name


// console.log('\n', instead)

let a1 = [7, 8, 9]
let a2 = [4, 5, 6]

let a3 = a1.concat(a2)
// console.log(a3, typeof a3)

const man = (name: string, age: number) => name
interface Bodies {
  boy: (name: string, age: number) => any
  girl: (name: string, age: number, hairLen: string) => any
}

interface Parent {
  father: (name: string, age: number) => any
  mother: (name: string, age: number, hairLen: number) => any
}

type Family<T> = T extends Bodies ? T['boy'] : T extends Parent ? T['mother'] : never; 

// type seen = Parameters<typeof man>
// type seen = Parameters<Family<Bodies>>
type seen = Parameters<Family<Bodies | Parent>>
const ss = (s: seen[2]) => s
// console.log(ss(45))

// const cryp = Math.round(Math.random() * 1e3)
// console.log(cryp)

let fresh_now = new Date();
let Now = Date.now()
let stamptwist = new Date(Now)
let specific =  60 * 60 * 1000; // 1Hr
let spec = new Date(Now + specific)

console.log(`\nFresh: ${fresh_now} \nNow: ${Now} \nStampfiltered: ${stamptwist} \nSpecific: ${spec} \n`)
let arrayStr = ["['Tosin', 'Joseph', 'Emmanuel']"]

// let jsonStr = JSON.stringify(arrayStr[0]?.replace(/'/g, "\""))
let jsonStr = JSON.stringify(arrayStr[0])
let jsonPar = JSON.parse(jsonStr)

let check = (arrayStr[0] as string).split(',')

/*
for(let i in check){
  // check[i] = check[i]!.replace(/"/g, '')
  check[i] = check[i]!.replace(/'/g, '')
  check[i] = check[i].replace(/\s+/g, '')
  check[i] = check[i].replace("[", '')
  check[i] = check[i].replace("]", '')
}
*/

// console.log(arrayStr, '\n', jsonStr, '\n', jsonPar, check, typeof check)

// let ttt = "-T!osin Emmanuel Jos@eph-"
// console.log(ttt.replace(/[^a-z0-9\s]/ig, ''))




let base: string[] = ["Coding", "Testing"]
// let base: string[] = []
let concat = ['Tosin', "Emmanuel"]
// base.forEach(t => {
//   concat.push(t)
// })
// console.log("base:", base, "\nconcat:", concat)

// let ayo = concat.map(t => t)
let ayo = [...base, ...concat]

console.log(ayo)































/**
 * 
function sender(c: (new () => void) | (() => void)){
  return c;
}

const fPrinter = sender(() => {})

fPrinter

const cPrinter = sender(new (() => console.log('Class type'))
);

cPrinter;
*/

/*
if(regex.exec(pass)){
    let idx = regex.exec(pass)?.index
    let main = parseInt(pass[idx!]) * 3;
    // console.log("Yes =", regex.exec(pass));

    if(main.toString().length > 1){
        pass = pass.replace(pass[idx!], main.toString());
        pass = pass.replace(pass[idx! + 2], "");
        pass = pass.replace(pass[idx! + 2], "");
    }else if(main.toString().length == 1){
        pass = pass.replace(pass[idx!], main.toString());
        pass = pass.replace(pass[idx! + 1], "");
        pass = pass.replace(pass[idx! + 1], "");
    }
    
}else{
    console.log("No!")
}
console.log(pass);
*/


/*
async function generateAesKey() {
  try {
    const s3Key = await crypto.subtle.generateKey({
      name: 'AES-GCM',
      length: 256,
    }, true, ["encrypt", "decrypt"]);
    
    const key = await crypto.subtle.exportKey('jwk', s3Key)
    
    console.log(key, '\n');
  } catch(error) {
    console.log(error)
  }
}
generateAesKey()
*/

/*
async function generateRsaKey() {
  try {
    const s3Key = await crypto.subtle.generateKey({
      name: 'RSASSA-PKCS1-v1_5',
      modulusLength: 2048,
      publicExponent: new Uint8Array([1, 0, 1]),
      hash: 'SHA-256'
    }, true, ["sign", "verify"]);
    
    const publickey = await crypto.subtle.exportKey('jwk', s3Key.publicKey)
    const privateKey = await crypto.subtle.exportKey('jwk', s3Key.privateKey)
    
    console.log('Public K:', publickey, '\n');
    console.log('Private K:', privateKey);
  } catch (error) {
    console.log(error)
  }
}
generateRsaKey()
*/


// Available in Angular or install Node core and types
// import * as fs from 'fs/promises'
// async function readFile() {
//   try{
//     const data = await fs.readFile('example.txt', 'utf8')
//     console.log(data)
//   }catch (err) {
//     console.log(err)
//   }
// }

// async function writeFile(file: string){
//   try{
//     const Okay = await fs.writeFile('example.txt', file)
//     console.log('File saved!')
//   }catch (err){
//     console.log(err)
//   }
// }


// For javascript syntax
/*
import * as fs from 'fs'
fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err){
    console.log(err)
  }else{
    console.log(data)
  }
})

fs.writeFile('example.txt', 'Hello world!', (err) => {
  if (err){
    console.log(err)
  }else{
    console.log('File saved')
  }
})
*/
