from pymol import cmd

proteins = ['DPP4','DPP8', 'DPP9']
probes = ['IPOH','IPAM','ACET','ACEM','BNZ','ISB']
color_scheme = {'IPOH':'yellow','IPAM':'blue','ACET':'red','ACEM':'orange','ISB':'silver','BNZ':'darksalmon'} # Color scheme per probe type
isomesh_cutoff_range = [0.005,0.01,0.02,0.03,0.04,0.05,0.07]

#First load the data
for protein in proteins:
    cmd.do(f'load {protein}.pdb')



# Load the ligands
cmd.do(f'load Vildagliptin.pdb')
cmd.do(f'util.cbap Vildagliptin')
cmd.do(f'load 1G244.pdb')
cmd.do(f'util.cbap 1G244')
cmd.do('load nlrp1.pdb')
cmd.do('util.cbao nlrp1')
cmd.do(f'load 4_oxo_b_lactam_inhibitor_12.pdb')
cmd.do('util.cbao 4_oxo_b_lactam_inhibitor_12')


# Load the probes

for protein in proteins:
    for probe in probes:
        cmd.do(f'load {protein}_density_data/{probe}_density.dx')
        cmd.do(f'set_name {probe}_density, {protein}.{probe}.density')
        print(f'Loaded the following data: {protein}  -  {probe}')

        for cutoff in isomesh_cutoff_range:
            cmd.do(f'isosurface {protein}.{probe}.{cutoff},{protein}.{probe}.density,{cutoff} ')
            this_color = color_scheme[probe]
            cmd.do(f'color {this_color}, {protein}.{probe}.{cutoff}')
            cmd.do(f'disable {protein}.{probe}.{cutoff}')






