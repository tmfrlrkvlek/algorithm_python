import Foundation

struct KakaoDate: Comparable {
    let year: Int
    let month: Int
    let day: Int
    let hour: Int
    let minute: Int
    let second: Double
    
    static func < (lhs: KakaoDate, rhs: KakaoDate) -> Bool {
        let lhsInfo = [lhs.year, lhs.month, lhs.day, lhs.hour, lhs.minute]
        let rhsInfo = [rhs.year, rhs.month, rhs.day, rhs.hour, rhs.minute]
        for (l, r) in zip(lhsInfo, rhsInfo) where l != r {
            return l < r
        }
        return lhs.second < rhs.second
    }
    
    init(_ year: Int, _ month: Int, _ day: Int, _ hour: Int, _ minute: Int, _ second: Double) {
        (self.year, self.month, self.day) = (year, month, day)
        (self.hour, self.minute, self.second) = (hour, minute, second)
    }
    
    init(date: [Int], time: [Double]) {
        (self.year, self.month, self.day) = (date[0], date[1], date[2])
        self.hour = Int(time[0])
        self.minute = Int(time[1])
        self.second = time[2]
    }
    
    init(_ date: KakaoDate, _ gap: Double, _ plus: Bool = false) {
        (self.year, self.month, self.day) = (date.year, date.month, date.day)
        (self.hour, self.minute, self.second) = (date.hour, date.minute, plus ? date.second+gap : date.second-gap)
    }
    
    func startDate(_ duration: Double) -> KakaoDate {
        guard self.second < duration else { return KakaoDate(self, duration) }
        switch (self.hour, self.minute) {
        case (0, 0) : return KakaoDate(self.year, self.month, self.day-1, 59, 59, self.second+60-duration)
        case (_, 0) : return KakaoDate(self.year, self.month, self.day, self.hour-1, 59, self.second+60-duration) 
        case (_, _) : return KakaoDate(self.year, self.month, self.day, self.hour, self.minute-1, self.second+60-duration) 
        }
    }
    
    func validEndDate() -> KakaoDate {
        guard self.second > 59 else { return KakaoDate(self, 0.999, true) }
        switch (self.hour, self.minute) {
        case (59, 59) : return KakaoDate(self.year, self.month, self.day+1, 0, 0, self.second+0.999-60)
        case (_, 59) : return KakaoDate(self.year, self.month, self.day, self.hour+1, 0, self.second+0.999-60) 
        case (_, _) : return KakaoDate(self.year, self.month, self.day, self.hour, self.minute+1, self.second+0.999-60) 
        }
    }
}

struct KakaoDateNode: Comparable {
    let date: KakaoDate
    let isStartDate: Bool
    
    static func < (lhs: KakaoDateNode, rhs: KakaoDateNode) -> Bool {
        if lhs.date == rhs.date {
            switch (lhs.isStartDate, rhs.isStartDate) {
            case (false, true) : return true
            default : return false
            }
        } else {
            return lhs.date < rhs.date
        }
    }
    
    static func == (lhs: KakaoDateNode, rhs: KakaoDateNode) -> Bool {
        return lhs.date == rhs.date && lhs.isStartDate == rhs.isStartDate
    }
}


func solution(_ lines:[String]) -> Int {
    var queue: [KakaoDateNode] = []
    for line in lines {
        let input = line.components(separatedBy: " ")
        let date = input.first!.components(separatedBy: "-").map() { Int($0)! }
        let time = input[1].components(separatedBy: ":").map() { Double($0)! }
        let duration = Double(input[2].components(separatedBy: "s")[0])!
        var endDate = KakaoDate(date: date, time: time)
        let startDate = endDate.startDate(duration)
        endDate = endDate.validEndDate()
        queue.append(KakaoDateNode(date: startDate, isStartDate: true))
        queue.append(KakaoDateNode(date: endDate, isStartDate: false))
    }
    queue.sort()
    var result = 0
    var current = 0
    while !queue.isEmpty {
        switch queue.removeFirst().isStartDate {
        case true : 
            current += 1
            result = result < current ? current : result
        case false :
            current -= 1
        }
    }
    return result
    
}