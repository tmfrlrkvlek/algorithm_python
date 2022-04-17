import Foundation

func solution(_ orders:[String], _ course:[Int]) -> [String] {
    let combinations = courses(orders, course)
    var result: [Int: (Int, [String])] = [:]
    for (combi, count) in combinations {
        let curCount = (result[combi.count] ?? (2, [])).0
        switch count {
        case curCount+1...Int.max : result.updateValue((count, [combi]), forKey: combi.count)
        case curCount : result.updateValue((count, (result[combi.count] ?? (0, [])).1 + [combi]) , forKey: combi.count)
        default : break
        }
    }
    var results: [[String]] = []
    result.forEach { _, combi in
        results.append(combi.1)
    }
    return results.flatMap() {$0}.sorted()
}

func courses(_ orders:[String], _ course: [Int]) -> [String: Int] {
    var combinations: [String: Int] = [:]
    func findCombination(_ order:[Character], _ combination:[Character], _ isContinue: Bool) {
        var order = order
        if !isContinue && course.contains(combination.count) {
            let key = combination.reduce("") {"\($0)\($1)"}
            combinations.updateValue((combinations[key] ?? 0) + 1, forKey: key)
        }
        if !order.isEmpty { 
            let char = order.removeFirst()
            findCombination(order, combination, true)
            findCombination(order, (combination + [char]).sorted(), false)
        }
    }
    orders.forEach() { findCombination(Array($0), [], false) }
    return combinations
}