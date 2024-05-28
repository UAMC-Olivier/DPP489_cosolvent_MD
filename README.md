# Cosolvent MD data DPP4, DPP8 and DPP9

This repository contains the fragment density data resulting from our cosolvent MD simulations on DPP4, DPP8 and DPP9.

## Software requirements

Recommended: Pymol

Alternatively other visualization softwares may also work, but you will have to visualize the density maps yourself.

## Loading the data and visualizing the density maps

Get the data using:

```
git clone FILL
```

To visualize only the central carbon densities, type the following line in the command line:

```
pymol pymol_simple.py
```

(Loading the visualization may take some time. You can track the progress of loading the files in the terminal output of Pymol)

The legend for the created objects is as follows:

`protein name.probe name abbreviation.cutoff `

We use the following abbreviations:

+ `IPOH`: isopropanol
+ `IPAM`: isopropyl ammonium
+ `ACET`: acetate
+ `ACEM`: acetamide
+ `ISB`: isobutane
+ `BNZ`: benzene

In Pymol you can now click the cutoff you wish to visualize for each density in the Pymol sidebar. Cutoffs are given in Å**-3

To visualize the atom densities of the functonial groups as well:

```
pymol pymol_full.py
```

(Visualizing the atom densities of the functonial groups takes additional time and uses more memory)

The legend for the additional objects is as follows:

`protein name.probe name abbreviation.atom group.cutoff `


## Making your own visualizations

Feel free to visualize different cutoffs of density data (dx files) using the [isosurface](https://pymolwiki.org/index.php/Isosurface) or [isomesh](https://pymolwiki.org/index.php/Isomesh) commands of Pymol. If you used `pymol_simple.py` or `pymol_full.py` then the dx files data is stored in the following object:

`protein name.probe name abbreviation.density`

`protein name.probe name abbreviation.atom group.density`

## Publication

Currently in press

## References

The repository contains data from the following PDB files: 6B1E, 6EOP, 6EOR, 6X6A, 7A3J

These are from the following publications:

* Joel, P.B., et al. (2018) A comparative study of the binding properties, dipeptidyl peptidase- 4 (DPP- 4) inhibitory activity and glucose- lowering efficacy of the DPP- 4 inhibitors alogliptin, linagliptin, saxagliptin, sitagliptin and vildagliptin in mice. Endocrinol Diab Metab 1.

* Breyan, R., et al. (2018) Structures and mechanism of dipeptidyl peptidases 8 and 9, important players in cellular homeostasis and cancer. Proceedings of the National Academy of Sciences 115:E1437-E1445

* Hollingsworth, L.R., et al. (2021) DPP9 sequesters the C terminus of NLRP1 to repress inflammasome activation. Nature 592 (7856):778-783.

* Carvalho, L.A., et al. (2022) Chemoproteomics‐Enabled Identification of 4‐Oxo‐β‐Lactams as Inhibitors of Dipeptidyl Peptidases 8 and 9. Angewandte Chemie International Edition