
connection_type = "TCP"
connection_type = "UDP"
connection_type = "chat"
connection_type = "thread"

match connection_type:
    case "TCP":
        import zuni.tcp.tcp_server

    case "UDP":
        import zuni.udp.udp_server

    case "chat":
        import zuni.chat.chat_server


    case "thread":
        import zuni.threading.thread_server