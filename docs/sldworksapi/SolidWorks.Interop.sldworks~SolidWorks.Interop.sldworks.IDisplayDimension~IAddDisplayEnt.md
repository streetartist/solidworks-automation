# IAddDisplayEnt Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IAddDisplayEnt`

Overrides the display graphics of objects for this display dimension.
Overrides the display graphics of objects for this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddDisplayEnt( _
   ByVal Type As System.Integer, _
   ByRef Data As System.Double _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim Type As System.Integer
Dim Data As System.Double
Dim value As System.Boolean
 
value = instance.IAddDisplayEnt(Type, Data)
```

```

System.bool IAddDisplayEnt( 
   System.int Type,
   ref System.double Data
)
```

```

System.bool IAddDisplayEnt( 
   System.int Type,
   System.double% Data
) 
```

#### Parameters

*Type*
:   Type of graphical entity (see **Remarks**)

*Data*
:   - in-process, unmanaged C++: Pointer to an array of geometric data describing the entity (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if successful, false if not

Remarks

The new graphics displayed by this method are temporary. When the user changes the dimension, this display dimension reverts back to the SOLIDWORKS standard.

The type controls which geometry is added and what information is placed in the data array. All colors and line styles are taken from IDisplayDimension.

|  |  |  |
| --- | --- | --- |
| type | Description | data |
| 1 | Line | 6 doubles; (x, y, z) start point and (x, y, z) end point |
| 2 | Filled triangle | 9 doubles; 3 (x, y, z) points of the triangle to fill |
| 3 | Filled 4 sided polygon | 12 doubles; 4 (x, y, z) points of the polygon to fill |
| 4 | Arc | 12 doubles; (x, y, z) center point, (x, y, z) normal vector, (x, y, z) start point and (x, y, z) end point |
| 5 | Circle | 7 doubles; (x, y, z) center point, (x, y, z) normal vector and radius |
| 6 | Filled dot | 4 doubles; (x, y, z) center point and radius |

The size of the array is the size of the expected returned array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::AddDisplayEnt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AddDisplayEnt.md)
