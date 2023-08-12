
connection_type = "TCP"
connection_type = "UDP"

match connection_type:
    case "TCP":
        import zuni.tcp.tcp_server

    case "UDP":
        import zuni.udp.udp_server

