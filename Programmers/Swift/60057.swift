import Foundation

func solution(_ s:String) -> Int {
    return Array(1...max(1, Int(s.count/2))).reduce(s.count) { b, c in min(b, checkCount(s, c)) }
}

func checkCount(_ s: String, _ c: Int) -> Int {
    let string = Array(s)
    var length = s.count
    var start = 0
    var accumulateCount = 1
    while start+2*c <= s.count {
        var valid = true
        for i in start..<start+c where string[i] != string[i+c] { 
            valid = false
            break
        }
        switch valid {
        case true : accumulateCount += 1
        case false : 
            length -= (accumulateCount > 1 ? c*(accumulateCount-1) - (String(accumulateCount).count) : 0)
            accumulateCount = 1
        }
        start += c
    }
    length -= (accumulateCount > 1 ? c*(accumulateCount-1)-String(accumulateCount).count : 0)
    return length
}