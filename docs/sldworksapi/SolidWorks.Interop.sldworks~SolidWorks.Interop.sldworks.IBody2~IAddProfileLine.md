# IAddProfileLine Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileLine`

Creates a line profile curve and returns a pointer to that curve.
Creates a line profile curve and returns a pointer to that curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddProfileLine( _
   ByVal RootPoint As System.Object, _
   ByVal Direction As System.Object _
) As Curve
```

```

Dim instance As IBody2
Dim RootPoint As System.Object
Dim Direction As System.Object
Dim value As Curve
 
value = instance.IAddProfileLine(RootPoint, Direction)
```

```

Curve IAddProfileLine( 
   System.object RootPoint,
   System.object Direction
)
```

```

Curve^ IAddProfileLine( 
   System.Object^ RootPoint,
   System.Object^ Direction
) 
```

#### Parameters

*RootPoint*
:   Array of 3 doubles (x,y,z)

*Direction*
:   Array of 3 doubles (x,y,z)

#### Return Value

Line profile, [ICurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Remarks

You can use this method with [IBody2::ICreateRevolutionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRevolutionSurface.md) to generate a cylindrical surface of revolution or with [IBody2::ICreateExtrusionSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateExtrusionSurface.md) to generate a tabulated cylinder.

Example

[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::AddProfileLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddProfileLine.md)
