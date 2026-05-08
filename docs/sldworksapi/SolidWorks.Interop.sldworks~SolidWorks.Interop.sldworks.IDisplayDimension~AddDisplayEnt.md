# AddDisplayEnt Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~AddDisplayEnt`

Overrides the display graphics of objects.
Overrides the display graphics of objects.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddDisplayEnt( _
   ByVal Type As System.Integer, _
   ByVal Data As System.Object _
) As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim Type As System.Integer
Dim Data As System.Object
Dim value As System.Boolean
 
value = instance.AddDisplayEnt(Type, Data)
```

```

System.bool AddDisplayEnt( 
   System.int Type,
   System.object Data
)
```

```

System.bool AddDisplayEnt( 
   System.int Type,
   System.Object^ Data
) 
```

#### Parameters

*Type*
:   Type of graphical entity (see **Remarks**)

*Data*
:   Geometric data describing the entity (see **Remarks**)

#### Return Value

True if successful, false if not

Remarks

The new graphics displayed by this method are temporary. When the user changes the dimension, this display dimension reverts back to the SOLIDWORKS standard.

The type controls which geometry is added and what information is placed in the data array. All colors and line styles are taken from DisplayDimension.

|  |  |  |
| --- | --- | --- |
| type | Description | data |
| 1 | Line | 6 doubles; (x, y, z) start point and (x, y, z) end point |
| 2 | Filled triangle | 9 doubles; 3 (x, y, z) points of the triangle to fill |
| 3 | Filled 4 sided polygon | 12 doubles; 4 (x, y, z) points of the polygon to fill |
| 4 | Arc | 12 doubles; (x, y, z) center point, (x, y, z) normal vector, (x, y, z) start point and (x, y, z) end point |
| 5 | Circle | 7 doubles; (x, y, z) center point, (x, y, z) normal vector and radius |
| 6 | Filled dot | 4 doubles; (x, y, z) center point and radius |

Example

[Replace Dimension with Text (VBA)](Replace_Dimension_with_Text_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::IAddDisplayText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IAddDisplayText.md)
