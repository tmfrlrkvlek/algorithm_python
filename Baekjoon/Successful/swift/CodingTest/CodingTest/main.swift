//
//  main.swift
//  CodingTest
//
//  Created by 이지수 on 2021/09/04.
//

import Foundation

let n: Int = Int(readLine() ?? "0") ?? 0
var combinations = [[Int?]](repeating:Array(repeating: nil, count: 31), count: 31)
func combination(n:Int, r:Int) -> Int{
    if r == 0 || n == r { combinations[n][r] = 1 }
    guard let result = combinations[n][r] else {
        combinations[n][r] = combination(n: n-1, r: r-1) + combination(n: n-1, r: r)
        return combinations[n][r] ?? 1
    }
    return result
}
for _ in 0..<n {
    let sides: [String] = (readLine() ?? "0 0").components(separatedBy: " ")
    print(combination(n: Int(sides[1]) ?? 0, r: Int(sides[0]) ?? 0))
}

//func multiple(from: Double, to: Double) -> Double {
//    if to == from { return to }
//    else { return from * multiple(from: from - 1, to: to) }
//}
//
//for _ in 0..<n {
//    let sides: [String] = (readLine() ?? "0 0").components(separatedBy: " ")
//    let left = Double(sides[0]) ?? 0
//    let right = Double(sides[1]) ?? 0
//    let count = left > right ? 0 : multiple(from: right, to: right - left + 1) / multiple(from: left, to: 1)
//    print(Int(count))
//}

