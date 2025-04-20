import struct
import binascii

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!HH', self.src_port, self.dst_port)
        packed += struct.pack('!HH', self.length, self.checksum)
        return packed

    def unpack_Udphdr(buffer):
        unpacked = struct.unpack('!HHHH', buffer[:8])
        return unpacked

    def getSrcPort(unpacked_udpheader):
        return unpacked_udpheader[0]
    
    def getDstPort(unpacked_udpheader):
        return unpacked_udpheader[1]
    
    def getLength(unpacked_udpheader):
        return unpacked_udpheader[2]
    
    def getChecksum(unpacked_udpheader):
        return unpacked_udpheader[3]

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = Udphdr.unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'.format(
    Udphdr.getSrcPort(unpacked_udphdr), 
    Udphdr.getDstPort(unpacked_udphdr), 
    Udphdr.getLength(unpacked_udphdr), 
    Udphdr.getChecksum(unpacked_udphdr)))
