use std::io;

fn main(){
    let mut s = String::new();
    io::stdin().read_line(&mut s).unwrap();
    let x:i64 = s.trim().parse::<i64>().unwrap();
    println!("{}",i64::pow(x,2));
    println!("{}",2);
}