# GetDimension2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetDimension2`

Gets the model dimension used to create this display dimension.
Gets the model dimension used to create this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDimension2( _
   ByVal Index As System.Integer _
) As Dimension
```

```

Dim instance As IDisplayDimension
Dim Index As System.Integer
Dim value As Dimension
 
value = instance.GetDimension2(Index)
```

```

Dimension GetDimension2( 
   System.int Index
)
```

```

Dimension^ GetDimension2( 
   System.int Index
) 
```

#### Parameters

*Index*
:   - 0 to get the first chamfer display dimension
    - 1 to get the second chamfer display dimension

#### Return Value

[Dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)

Remarks

The Index argument is valid for chamfer display dimensions only. If the display dimension is not a chamfer display dimension, then Index is ignored. To get both chamfer display dimensions, you must call this property twice; specify 0 for Index in the first call and 1 for Index in the second call.

SOLIDWORKS can display a dimension more than once. For example, a base-extrude dimension can be brought into three different views on a drawing. These three dimensions are referred to as display dimensions and are represented by the DisplayDimension object in the SOLIDWORKS API. The original base-extrude dimension is represented by the Dimension object in the SOLIDWORKS API.

Example

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)  
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)  
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)
