use std::io;

fn main(){
    let mut s = String::new();
    io::stdin().read_line(&mut s).unwrap();
    let li = s.split_whitespace();
    let mut x:i32 = 0;
    for i in li{
        x += i.parse::<i32>().unwrap();
    }
    println!("{}",x);
}