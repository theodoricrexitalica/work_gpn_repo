import pandas as pd

def preproc_mer(mer_init):
    oilfieldSplit = pd.Series(mer_init.WELL).str.split('@')
    oilfieldSplit_inter = pd.DataFrame(oilfieldSplit.to_list(), columns = ['oilfield', 'col1', 'col2', 'well'])
    oilfieldSplit_inter = oilfieldSplit_inter[['oilfield','well']]
    mer_oilfield = mer_init.join(oilfieldSplit_inter)
    mer_oilfield.rename(columns = 
                {'Date':'date',
                'kPlast':'zone',
                'kCharWork':'type_work',
                'kState':'state',
                'kMethod':'method',
                'WorkTime':'work',
                'CollTime':'coll',
                'StayTime':'stay',
                'kStayReason':'stay_reason',
                'Oil':'oil',
                'Wat':'wat',
                'Gas':'gas',
                'NaturalGas':'natur_gas',
                'GasCondensate':'gas_condens',
                'CapGas':'cap_gas',
                'kAgentProd':'agent_prod',
                'kAgentInj':'ageny_inj',
                'OilV':'oil_v',
                'WatV':'wat_v',
                'OtherFluidV':'fluid_v',
                'Injection':'inj',
                'WaterLoss':'wat_loss',
                'TechInj':'tech_inj',}, inplace=True)
    mer = mer_oilfield[[ 'oilfield','well','date','zone','type_work','state','method','work','coll','stay','stay_reason','oil','wat','gas','oil_v',
               'wat_v','fluid_v','inj','wat_loss','tech_inj']]
    mer['date'] = pd.to_datetime(mer['date'], dayfirst=True)
    convert_dict = {'oilfield': 'string',
                    'well': 'string',
                    'zone': 'string',
                    'type_work': 'string',
                    'state': 'string',
                    'method': 'string',
                    'work': 'float64',
                    'coll': 'float64',
                    'stay': 'float64',
                    'stay_reason': 'string',
                   } 
    mer = mer.astype(convert_dict)
    mer['oil_tpd'] = (mer.oil/mer.work)*24
    mer['wat_tpd'] = (mer.wat/mer.work)*24
    mer['gas_upd'] = (mer.gas/mer.work)*24
    mer['wc'] = mer.wat_tpd/(mer.oil_tpd + mer.wat_tpd)
    
    return mer

def preproc_rigis(rigis_init):
    rigis_init.rename(columns = 
                {'Oilfield':'oilfield',
                'Well/Wellbore':'well',
                'plast':'zone',
                'plastzone':'zone_z',
                'H':'md',
                'L':'h_md',
                'Habs':'tvdss',
                'Labs':'h_tvdss', 
                'Lit':'lit',
                'Collector':'collector',
                'Sat':'satur',
                'Ro':'rt',
                'APS':'aps',
                'aGK':'agk',
                'Kpr':'kpr',
                'Kpor':'kp',
                'Kn':'kng',
                'Kgl':'kgl'}, inplace=True)
    rigis = rigis_init[['oilfield','well','zone','md','h_md','tvdss','h_tvdss','lit','collector','aps','agk','rt','kgl','kp','kpr','kng','satur']]
    convert_dict = {'oilfield': 'string',
                    'well': 'string',
                    'zone': 'string',
                    'lit': 'string',
                    'agk': 'float64',
                    'satur': 'string'} 
    rigis = rigis.astype(convert_dict)
    return rigis
 
def preproc_coord(coord_init):
    coord_init.rename(columns = 
                {'Oilfield':'oilfield',
                'Pl':'zone',
                'Well/Wellbore':'well',
                'X':'x',
                'Y':'y',
                'X0':'x0',
                'Y0':'y0',}, inplace=True)
    coord = coord_init[[ 'oilfield','well','zone','x','y','x0','y0']]
    convert_dict = {'oilfield': 'string',
                    'well': 'string',
                    'zone': 'string',
                    'x': 'float64',
                    'y': 'float64',
                    'x0': 'float64',
                    'y0': 'float64'} 
    coord = coord.astype(convert_dict)
    # делаем целыми и текстовыми координаты устья скважин
    int_dict = {'x0': 'int',
                'y0': 'int',
               }
    coord = coord.astype(int_dict)
    str_dict = {'x0': 'string',
                'y0': 'string',
               }
    coord = coord.astype(str_dict)
    return coord
  
def preproc_coord_join(coord):
    coord['x0y0'] = coord[['x0','y0']].agg(' '.join, axis=1)
    coord_wh = coord[['well','x0y0']]
    coord_wh = pd.DataFrame(coord.groupby('well')['x0y0'].max())
    coord_wh.reset_index(inplace=True)
    coord_wells = pd.DataFrame(coord_wh.groupby('x0y0')['well'].apply(lambda x: np.array(x)))
    coord_wells.reset_index(inplace=True)
    return coord_wells
    
def check_well_wellhead(coord_wells, wellName='555'):
    for wells in coord_wells.well:
        for item in wells:
            if wellName in item:
                print(wellName, wells)
                break

def display_well_mer(mer, well_name, zone_name):
     return mer[(mer.well.str.contains(well_name)) & (mer.zone.str.contains(zone_name))]
    
def check_well_mer(mer, well_name):
     mer_well_zone = mer[(mer.well.str.contains(well_name))]
     print(well_name)
     print('well names:',  list(mer_well_zone.well.unique()))
     print('zones names:', list(mer_well_zone.zone.unique()))
     print('zones names:', list(mer_well_zone.type_work.unique()))

def mer_oil_graph_wellzone (mer, well_name, zone_name):
     import matplotlib.pyplot as plt
     from matplotlib.ticker import MultipleLocator, ScalarFormatter
     
     f, ax = plt.subplots(figsize=(15,7))
     mer_well_zone = mer[(mer.well.str.contains(well_name)) & (mer.zone.str.contains(zone_name)) & (mer.type_work == 'НЕФ')]
     ax.step(mer_well_zone.date, mer_well_zone.oil_tpd, color = 'brown', where='pre')
     ax.step(mer_well_zone.date, mer_well_zone.wat_tpd, color = 'blue', where='pre')
     ax.set_title(mer_well_zone.well.iloc[0] + ' - ' + mer_well_zone.zone.iloc[0], fontsize=16)
     ax_wc = ax.twinx()
     ax_wc.step(mer_well_zone.date, mer_well_zone.wc, color = 'green',where='pre', ls = '--')
     plt.gca().xaxis.set_major_locator(plt.MultipleLocator(365))
     ax.tick_params(axis='x', labelrotation=45)
     ax.grid()