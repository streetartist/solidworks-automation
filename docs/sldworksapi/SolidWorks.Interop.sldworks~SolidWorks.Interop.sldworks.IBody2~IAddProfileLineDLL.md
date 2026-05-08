# IAddProfileLineDLL Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IAddProfileLineDLL`

Adds a profile line.
Adds a profile line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddProfileLineDLL( _
   ByRef RootPoint As System.Double, _
   ByRef Direction As System.Double _
) As Curve
```

```

Dim instance As IBody2
Dim RootPoint As System.Double
Dim Direction As System.Double
Dim value As Curve
 
value = instance.IAddProfileLineDLL(RootPoint, Direction)
```

```

Curve IAddProfileLineDLL( 
   ref System.double RootPoint,
   ref System.double Direction
)
```

```

Curve^ IAddProfileLineDLL( 
   System.double% RootPoint,
   System.double% Direction
) 
```

#### Parameters

*RootPoint*
:   Pointer to an array of 3 doubles (x,y,z)

*Direction*
:   Pointer to an array of 3 doubles (x,y,z)

#### Return Value

Pointer to the profile line [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
