# Python Deep Dive Part 2 Project 2

### This project contains 4 main classes:

- Poly(n, r)

- Polygons(m, r)

- PolyFactory(icount, clones, cloneamount, siderange, radrange, sig)

- NrsGlobalCache() 

### Poly(n, r):

- n = sides

- r = radius 

**_Polygon Calculated Properties_:**

*Calculated Properties are lazily evaluated, stored locally, and cached globally via NrsGlobalCache:*

- interior angle

- side length

- apothem 

- area

- perimeter


### Polygons(m, r, sig):

- Iterable class that returns an iterator

- next() returns a sequence of Polygon() objects starting with (m) sides with fixed radius (r) 

- Calculates max_efficency Polygon 


### NrsGlobalCache():
- Calculated Properties are stored in a Singleton FIFO Cache: *NrsGlobalCache()*

- NrsGlobalCache --> [(n, r)] [calculated_property] [value]

- NrsGlobalCache.cache_limit controls the cache size

- Reading or Writing to Cache causes the cached item to become the last item in the cache

### PolyFactory(icount, clones, cloneamount, siderange, radrange, sig):
    
- Creational factory class generates randomized instances of Poly(n,r) within specified parameters

- Randomized instances Poly() objects are named starting from 'poly101' and registered in the global namespace

- Newly generated object names can be retrieved via PolyFactory.polynames

- Any calculated property can be triggered for newly created Poly instances

- See help(PolyFactory) for more information

**_check_parameters():_**

- Helper function for PolyFactory()

- Verifies instance parameters are viable for desired randomized instances of Poly(n, r)

- If desired random instances are not possible, check_parameters returns the minimum viable parameters to satisfy 

![image](https://user-images.githubusercontent.com/6591429/60698385-e1ffb400-9ea3-11e9-8ab9-3b4b40d5909e.png)

