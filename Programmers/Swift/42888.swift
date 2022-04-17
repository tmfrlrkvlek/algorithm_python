import Foundation

enum Instruction: String {
    case enter = "들어왔습니다.", leave = "나갔습니다.", change = ""
}

func solution(_ record:[String]) -> [String] {
    var idNicknames: [String: String] = [:]
    var orders: [(Instruction, String)] = []

    record.forEach() { re in
        let r = re.split(separator: " ").map{String($0)}
        switch r[0] {
        case "Enter" :  
            orders.append((Instruction.enter, r[1]))
            idNicknames.updateValue(r[2], forKey: r[1])
        case "Leave" :
            orders.append((Instruction.leave, r[1]))
        case "Change" :
            idNicknames.updateValue(r[2], forKey: r[1])
        default : break
        }
    }
    
    return orders.map() { message, id in
        return "\(idNicknames[id]!)님이 \(message.rawValue)"
    }
}