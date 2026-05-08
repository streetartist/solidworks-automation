# CreateFillet Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateFillet`

Creates a sketch fillet using the selected sketch entities.
Creates a sketch fillet using the selected sketch entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFillet( _
   ByVal Radius As System.Double, _
   ByVal ConstrainedCorners As System.Integer _
) As SketchSegment
```

```

Dim instance As ISketchManager
Dim Radius As System.Double
Dim ConstrainedCorners As System.Integer
Dim value As SketchSegment
 
value = instance.CreateFillet(Radius, ConstrainedCorners)
```

```

SketchSegment CreateFillet( 
   System.double Radius,
   System.int ConstrainedCorners
)
```

```

SketchSegment^ CreateFillet( 
   System.double Radius,
   System.int ConstrainedCorners
) 
```

#### Parameters

*Radius*
:   Radius of the fillet in meters

*ConstrainedCorners*
:   Action to take as defined in [swConstrainedCornerAction\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstrainedCornerAction_e.html) (see **Remarks**)

#### Return Value

[Sketch segment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) for the fillet

Remarks

The ConstrainedCorners parameter indicates what action to take if the corner to fillet is constrained or dimensioned. If the corner is not constrained or dimensioned, then this parameter is ignored.

Example

[Edit Radial Dimension (C#)](Edit_Radial_Dimension_Example_CSharp.htm)  
[Edit Radial Dimension (VB.NET)](Edit_Radial_Dimension_Example_VBNET.htm)  
[Edit Radial Dimension (VBA)](Edit_Radial_Dimension_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
