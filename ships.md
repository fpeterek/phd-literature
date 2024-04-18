MMSI - identifikátor používaný např. při komunikaci

IMO - permanentní globální identifikátor

Displacement - váha lodi, počítána pomocí Archimédova zákona

Metacenter - bod, kde se protnou přímky procházející těžištěm (a kolmá k podlaze) a bodem vztlaku (center of buoyancy) (přímka kolmá k zemi)

Metacentric height - Vzdálenost mezi metacentrem a těžištěm (lze považovat za fixní, pokud se loď nenaklání příliš)

Yaw/Pitch/Roll - to samé, co v letadle (yaw - rotace okolo osy Z, pitch - náklon přídi nahoru/dolů, roll - náklon lodi doleva/doprava)

Significant wave height - průměr 33 % největších vln 

Starboard - pravá strana lodi

Portside - levá strana lodi (stejně jako v letadle, podle toho, kde se vystupuje)

XTD - [cross-track distance](https://www.researchgate.net/figure/Cross-track-distance-XTD-is-set-to-a-number-of-meters-on-the-port-and-starboard-side_fig2_349713709)

Starboard XTD - jak daleko doprava od plánované cesty může loď bezpečně plout

Portside XTD - jak daleko doleva od plánované cesty může loď bezpečně plout

XTL - cross-track limit

```
The Cross Track Limit (XTL) could be described as the minimum safety corridor
along the navigational route which is defined by end user. Meanwhile, the Cross
Track Distance (XTD) usually represents the XTL value or individual max cross
track distance for each route leg. Furthermore, Cross Track Error (XTE) alarm
will be triggered when the vessel deviation from the route plan is larger than
the set XTL value
```

https://www.researchgate.net/publication/343240424_Zone_of_Confidence_Impact_on_Cross_Track_Limit_Determination_in_ECDIS_Passage_Planning

[Depth contour](https://www.linkedin.com/pulse/ecdis-depth-contours-explained-emiliano-caroletti-) - rozděluje vodu podle hloubky dna, standardní hodnoty jsou 5, 10, 15, 20, 50, 100 metrů

Safety contour - safety depth taková, aby loď mohla ve vodě bezpečně plout

Draft/draught - ponor lodi

Draft aft - ponor vzadu

Draft forward - ponor na přídi

UKC - under keel clearance

## Papers

### Ship route optimization using hybrid physics-guided machine learning

https://iopscience.iop.org/article/10.1088/1742-6596/2311/1/012037/pdf

* Optimalizace lodí plujících po norském pobřeží
* Nasbírali data z lodi a natrénovali model, který predikoval spotřebu lodi
* Algoritmus dostane cestu nadefinovanou pomocí waypointů a XTD (maximální povolenou odchylku od definované cesty)
* Algoritmus může loď přesměrovat v rámci těchto limitů
* Součást RTZ formátu, paper se na něj odkazuje
* Relevantní zdroje:
    * https://www.researchgate.net/publication/362593755_Energy_Efficient_and_Safe_Ship_Routing_using_Machine_Learning_Techniques_on_Operational_and_Weather_Data
    * https://www.mdpi.com/2077-1312/7/5/127

### Energy Efficient and Safe Ship Routing using Machine Learning Techniques on Operational and Weather Data

https://www.researchgate.net/publication/362593755_Energy_Efficient_and_Safe_Ship_Routing_using_Machine_Learning_Techniques_on_Operational_and_Weather_Data

* Neřeší zrychlování při výjezdu z přístavu, ani zpomalování před dojezdem
    * Malá část plavby, pravděpodobně dost omezené možnosti optimalizace
* Interpolací vygenerovali další pozice mezi jednotlivými waypointy, tuto cestu pak optimalizovali
* Výsledkem je případně pozměněná cesta s předdefinovanými rychlostmi

### A route generation algorithm for an optimal fuel routing problem between two single ports

https://onlinelibrary.wiley.com/doi/10.1111/itor.12410

* Popisuje algoritmus optimalizace cesty
* Řeší minimalizaci ceny paliva na cestě mezi dvěma přístavy
* Nemaximalizuje zisk, nebere v potaz posádku
* Fixed fleet
* Mixed-integer nonlinear optimization problem

> To avoid potential damage to the ship’s engine at slow speeds, the shipping speed must remain
above a certain threshold.

> Normally, a ship's engine operates at 70-85% of its maximum continous rating.

### Advanced optimized weather routing for an ocean-going vessel

https://ieeexplore.ieee.org/document/7352247
