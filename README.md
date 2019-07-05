# Python Deep Dive Part 2 Project 2

### This project contains 4 main classes:

- Poly(n, r, sig)

- Polygons(m, r, sig)

- PolyFactory(icount, clones, cloneamount, siderange, radrange, sig)

- NrsGlobalCache() 

## Poly(n, r, sig):

- n = sides
- r = radius 
- sig = significant digit precision for calculated properties

**Poly Calculated Properties:**

*Calculated Properties are lazily evaluated, stored locally, and cached globally via NrsGlobalCache:*

- interior angle

- side length

- apothem 

- area

- perimeter


## Polygons(m, r, sig):

- Iterable class that returns an iterator

- next() returns a sequence of Polygon() objects starting with (m) sides with fixed radius (r) 

- Calculates max_efficency Polygon 


## NrsGlobalCache():
- Calculated Properties are stored in a Singleton FIFO Cache: *NrsGlobalCache()*

- NrsGlobalCache --> [(n,r,s)] [calculated_property] [value]

- NrsGlobalCache.cache_limit controls the cache size

- Reading or Writing to Cache causes the cached item to become the last item in the cache
