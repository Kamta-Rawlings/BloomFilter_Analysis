# hashing helper - turns an item into k bit positions
# uses the "double hashing" trick: h_i = h1 + i*h2  (mod m)
# so we only need 2 real hashes instead of k.
