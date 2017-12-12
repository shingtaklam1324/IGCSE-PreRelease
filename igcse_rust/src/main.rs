use std::collections::HashMap;
use std::io;

const NUM_OF_COWS: u8 = 8;

fn main() {
    let mut cows: HashMap<u16, Vec<f64>> = HashMap::new();

    let mut buf = String::new();

    for day in 1..8 {
        println!("Day: {}", day);
        for m in 0..2 {
            println!(
                "{}",
                match m {
                    0 => "morning",
                    _ => "afternoon",
                }
            );
            for _ in 0..NUM_OF_COWS {
                buf.clear();
                println!("Input Cow ID:");
                io::stdin()
                    .read_line(&mut buf)
                    .expect("Error reading input");
                let id = buf.trim().parse::<u16>().expect("Error parsing input");

                let cow = cows.entry(id).or_insert(Vec::new());

                buf.clear();
                println!("Input volume of milk:");
                io::stdin()
                    .read_line(&mut buf)
                    .expect("Error reading input");
                let val = buf.trim().parse::<f64>().expect("Error parsing input");

                (*cow).push(val);
            }
        }
    }

    let total_vol = cows.values()
        .fold(0.0, |acc, cow| {
            acc + cow.into_iter().fold(0.0, |acc, x| x + acc)
        })
        .round();

    println!("Total Vol: {}", total_vol);
    println!("Average: {}", total_vol / 10.0);

    let mut vols = cows.iter()
        .map(|(id, vols)| (id, vols.into_iter().sum::<f64>()))
        .collect::<Vec<(&u16, f64)>>();

    vols.sort_by(|&(_, avol), &(_, bvol)| avol.partial_cmp(&bvol).unwrap());
    println!(
        "Highest Volume: {}: {}",
        vols.last().unwrap().0,
        vols.last().unwrap().1
    );


    cows.iter().for_each(|(id, vols)| {
        let volumes = (0..7)
            .into_iter()
            .map(|x| vols[2 * x] + vols[2 * x + 1])
            .collect::<Vec<f64>>();
        if volumes
            .into_iter()
            .fold(0, |acc, x| if x < 12.0 { acc + 1 } else { acc }) >= 4
        {
            println!("id: {}", id);
        }
    });
}
