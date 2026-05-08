# CreateRuledSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateRuledSurface`

Creates a ruled surface from the specified curves and apex point.
Creates a ruled surface from the specified curves and apex point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateRuledSurface( _
   ByVal Curve1 As System.Object, _
   ByVal Curve2 As System.Object, _
   ByVal ApexPoint As System.Object _
) As System.Object
```

```

Dim instance As IBody2
Dim Curve1 As System.Object
Dim Curve2 As System.Object
Dim ApexPoint As System.Object
Dim value As System.Object
 
value = instance.CreateRuledSurface(Curve1, Curve2, ApexPoint)
```

```

System.object CreateRuledSurface( 
   System.object Curve1,
   System.object Curve2,
   System.object ApexPoint
)
```

```

System.Object^ CreateRuledSurface( 
   System.Object^ Curve1,
   System.Object^ Curve2,
   System.Object^ ApexPoint
) 
```

#### Parameters

*Curve1*
:   First curve

*Curve2*
:   Second curve

*ApexPoint*
:   Array of 3 doubles (x, y, z), the apex point

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
