
connection_type = "TCP"
connection_type = "UDP"
connection_type = "chat"

match connection_type:
    case "TCP":
        import zuni.tcp.tcp_client

    case "UDP":
        import zuni.udp.udp_client
    case "chat":
        import zuni.chat.chat_client
