import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    var idCounts: [String: Int] = [:]
    for re in Set(report) {
        let p = re.split(separator: " ").map{String($0)}[1]
        idCounts.updateValue((idCounts[p] ?? 0)+1, forKey: p)
    }
    var mainCounts: [String: Int] = [:]
    for re in Set(report) {
        let p = re.split(separator: " ").map{String($0)}
        if idCounts[p[1]]! >= k {
            mainCounts.updateValue((mainCounts[p[0]] ?? 0)+1, forKey: p[0])
        }
    }
    return id_list.map { mainCounts[$0] ?? 0 }
}