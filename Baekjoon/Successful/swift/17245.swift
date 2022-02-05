// 17245
import Foundation

func count(_ mid: Int, _ coms: [[Int]]) -> Double {
    var count = 0
    for com in coms {
        for c in com {
            count += min(c, mid)
        }
    }
    return Double(count)
}

let n = Int(readLine()!)!
var coms = Array<[Int]>()
var l = 0
var r = 0
var target: Double = 0
for _ in 0..<n {
    let com = readLine()!.split(separator: " ").map(){Int($0)!}
    coms.append(com)
    r = max(r, com.max()!)
    target += Double(com.reduce(0, +))
}
target /= 2
var result = 0
while l <= r {
    let mid = (l+r)/2
    if count(mid, coms) >= target {
        result = mid
        r = mid-1
    } else {
        l = mid+1
    }
}
print(result)

