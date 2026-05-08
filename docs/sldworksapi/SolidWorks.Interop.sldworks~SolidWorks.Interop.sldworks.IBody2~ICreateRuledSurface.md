# ICreateRuledSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRuledSurface`

Creates a ruled surface from the specified curves and apex point.
Creates a ruled surface from the specified curves and apex point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateRuledSurface( _
   ByVal Curve1 As Curve, _
   ByVal Curve2 As Curve, _
   ByRef ApexPoint As System.Double _
) As Surface
```

```

Dim instance As IBody2
Dim Curve1 As Curve
Dim Curve2 As Curve
Dim ApexPoint As System.Double
Dim value As Surface
 
value = instance.ICreateRuledSurface(Curve1, Curve2, ApexPoint)
```

```

Surface ICreateRuledSurface( 
   Curve Curve1,
   Curve Curve2,
   ref System.double ApexPoint
)
```

```

Surface^ ICreateRuledSurface( 
   Curve^ Curve1,
   Curve^ Curve2,
   System.double% ApexPoint
) 
```

#### Parameters

*Curve1*
:   Pointer to first [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*Curve2*
:   Pointer to second [curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*ApexPoint*
:   Array of 3 doubles (x, y, z) being the apex point

#### Return Value

Pointer to ruled [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

Remarks

Any existing object created by this method is destroyed if you call this method again.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateRuledSurface.md)
