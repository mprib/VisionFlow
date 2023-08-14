
connection_type = "TCP"
connection_type = "UDP"
connection_type = "chat"
connection_type = "thread"

match connection_type:
    case "TCP":
        import zuni.tcp.tcp_client

    case "UDP":
        import zuni.udp.udp_client
    case "chat":
        import zuni.chat.chat_client
    case "thread":
        import zuni.threading.thread_client
