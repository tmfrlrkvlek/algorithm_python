import Foundation

func solution(_ p:String) -> String {
    return solve(Array(p))
}

func solve(_ p: [Character]) -> String {
    guard !p.isEmpty else { return "" }
    var u: [Character], v: [Character] 
    (u, v) = split(p)
    switch isRight(u) {
    case true : return u.reduce("") {"\($0)\($1)"} + solve(v)
    case false : 
        u.removeFirst(); u.removeLast()
        return "(\(solve(v)))" + u.map() { $0 == "(" ? ")" : "(" }.reduce("") { "\($0)\($1)" }
    }
}

func split(_ p: [Character]) -> ([Character], [Character]) {
    var leftCount = 0
    var u: [Character] = []
    var v = p
    while !p.isEmpty {
        let char = v.removeFirst()
        switch char {
        case "(" : leftCount += 1
        default : leftCount -= 1
        }
        u.append(char)
        if leftCount == 0 { break }
    }
    return (u, v)
}

func isRight(_ p: [Character]) -> Bool {
    var leftCount = 0
    for char in p {
        switch char {
        case "(" : leftCount += 1
        default : leftCount -= 1
        }
        if leftCount < 0 { return false }
    }
    return true
}