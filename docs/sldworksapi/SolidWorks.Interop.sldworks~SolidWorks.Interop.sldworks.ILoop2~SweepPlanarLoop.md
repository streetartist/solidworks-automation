# SweepPlanarLoop Method (ILoop2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~SweepPlanarLoop`

Creates a temporary body by sweeping a planar loop along a vector.
Creates a temporary body by sweeping a planar loop along a vector.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SweepPlanarLoop( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal DraftAngle As System.Double _
) As System.Object
```

```

Dim instance As ILoop2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim DraftAngle As System.Double
Dim value As System.Object
 
value = instance.SweepPlanarLoop(X, Y, Z, DraftAngle)
```

```

System.object SweepPlanarLoop( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle
)
```

```

System.Object^ SweepPlanarLoop( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle
) 
```

#### Parameters

*X*
:   X component of the sweep vector

*Y*
:   Y component of the sweep vector

*Z*
:   Z component of the sweep vector

*DraftAngle*
:   Draft angle for the faces on the side of this swept body

#### Return Value

Array containing new swept [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) (element 1) and two stop [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) (elements 2 and 3)

Remarks

This method requires simplification of the imported body.

Example

[Sweep Planar Loop Along Vector (VBA)](Sweep_Planar_Loop_Along_Vector_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.md)  
[ILoop2::ISweepPlanarLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~ISweepPlanarLoop.md)
