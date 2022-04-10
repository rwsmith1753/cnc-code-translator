
M0	=	'Stop Program'
M1	=	'Optional Stop Program'
M2	=	'Program End'
M3	=	'Spindle On Fwd'
M4	=	'Spindle On Rev'
M5	=	'Spindle Stop'
M8 	=	'Coolant On'
M9	=	'Coolant Off'
M10 =	'Chuck Clamp'
M11	=	'Chuck Unclamp'
M12 =	'Auto Jet Air Blast On'
M13	=	'Auto Jet Air Blast Off' 
M14 = 'Main Spindle Brake On'
M15	=	'Main Spindle Brake Off'
M17	=	'Turret Rotation Fwd'
M18	=	'Turret Rotation Rev'
M19	=	'Orient Spindle (Optional)'
M21	=	'Tailstock Advance (Optional)'
M22	=	'Tailstock Retract (Optional)'
M23	=	'Chamfer Out of Thread On'
M24	=	'Chamfer Out of Thread Off'
M30	=	'End of Program and Reset'
M31	=	'Chip Auger Forward (Optional)'
M33	=	'Chip Auger Stop (Optional)'
M35	=	'Parts Catcher Part-Off Position'
M36	=	'Parts Catcher On (Optional)'
M37	=	'Parts Catcher Off (Optional)'
M38 =	'Spindle Speed Variation On'
M39	=	'Spindle Speed Variation Off'
M41 =	'Low Gear'
M42	=	'High Gear'
M43	=	'Turret Unlock (Service Use Only)'
M44	=	'Turret Lock (Service Use Only)'
M51	=	'Turn On Built-In M-Code Relay'
M52	=	'Turn On Built-In M-Code Relay'
M53	=	'Turn On Built-In M-Code Relay'
M54	=	'Turn On Built-In M-Code Relay'
M55	=	'Turn On Built-In M-Code Relay'
M56	=	'Turn On Built-In M-Code Relay'
M59	=	'Turn On Output Relay'
M61	=	'Turn Off Built-In M-Code Relay'
M62	=	'Turn Off Built-In M-Code Relay'
M63	=	'Turn Off Built-In M-Code Relay'
M64	=	'Turn Off Built-In M-Code Relay'
M65	=	'Turn Off Built-In M-Code Relay'
M66	=	'Turn Off Built-In M-Code Relay'
M69	=	'Turn Off Output Relay'
M78	=	'Alarm if Skip Signal Found'
M79	=	'Alarm if Skip Signal Not Found'
M85 =	'Automatic Door Open'
M86	=	'Automatic Door Close'
M88 =	'High Pressure Coolant On'
M89	=	'High Pressure Coolant Off'
M90 =	'Fixture Clamp Input On'
M91	=	'Fixture Clamp Input On'
M95	=	'Sleep Mode'
M96	=	'Jump If No Signal'
M97	=	'Local Subprogram Call'
M98	=	'Subprogram Call'
M99	=	'Subprogram Return Or Loop'
M104 =	'Probe Arm Extend '
M105	=	'Probe Arm Retract'
M109	=	'Interactive User Input'
M110	=	'Secondary Spindle Chuck Clamp (Optional)'
M111	=	'Secondary Spindle Chuck Unclamp (Optional)'
M112 =	'Secondary Spindle Air Blast On'
M113	=	'Secondary Spindle Air Blast Off'
M114 =	'Secondary Spindle Brake On'
M115	=	'Secondary Spindle Brake Off'
M119	=	'Secondary Spindle Orient (Optional)'
M121 =	'Built-In M-Codes Relays with M-Fin'
M122 =	'Built-In M-Codes Relays with M-Fin'
M123 =	'Built-In M-Codes Relays with M-Fin'
M124 =	'Built-In M-Codes Relays with M-Fin'
M125 =	'Built-In M-Codes Relays with M-Fin'
M126 =	'Built-In M-Codes Relays with M-Fin'
M129 =	'Turn On M-Code Relay with M-Fin'
M130 = 'Display Media'
M131	=	'Cancel Display Media'
M133	=	'Live Tool Fwd (Optional)'
M134	=	'Live Tool Rev (Optional)'
M135	=	'Live Tool Stop (Optional)'
M138	=	'Spindle Speed Variation On'
M139	=	'Spindle Speed Variation Off'
M143	=	'Secondary Spindle Forward (Optional)'
M144	=	'Secondary Spindle Reverse (Optional)'
M145	=	'Secondary Spindle Stop (Optional)'
M146 =	'Steady Rest Clamp'
M147	=	'Steady Rest Unclamp (Optional)'
M158 = 'Mist Condenser On'
M159	=	'Mist Condenser Off'
M170 = 'Engage 4th Axis Brake'
M171	=	'Release 4th Axis Brake'
M214 = 'Live Tool Brake On'
M215	=	'Live Tool Brake Off'
M219	=	'Live Tool Orient (Optional)'
M299	=	'APL / Part Load / or Program End'
M300	=	'M300 - APL/Robot Custom Sequence'
M334 = 'P-Cool Increment'
M335 =	'P-Cool Decrement'
M373 =	'Tool Air Blash (TAB) On'
M374 =	'Tool Air Blash (TAB) OFF'
M388 =	'Through-Spindle Coolant On'
M389 =	'Through-Spindle Coolant Off'


def make_list():
    mlist = []
    for i in range(0,389):
        try:

            mlist.append('M' + str(i) + f": {eval('M' + str(i))}")

        except:
            pass
    return mlist

mcode_list = make_list()


if __name__ == '__main__':
  get_mcode(m)