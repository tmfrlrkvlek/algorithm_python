// 1895
import Foundation

var map = Array<[Int]>()
var count: Int = 0
let input = readLine()!.split(separator: " ").map(){Int(String($0))!}
for _ in 0..<input[0] {
    map.append(readLine()!.split(separator: " ").map(){Int(String($0))!})
}
var t = Int(readLine()!)!
for i in 0..<input[0]-2 {
    for j in 0..<input[1]-2 {
        if (map[i..<i+3].map(){return Array($0[j..<j+3])}.flatMap{$0}.sorted(by: <)[4]) >= t {
            count += 1
        }
    }
}
print(count)