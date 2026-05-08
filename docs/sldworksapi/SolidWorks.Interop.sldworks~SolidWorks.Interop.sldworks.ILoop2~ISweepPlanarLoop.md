# ISweepPlanarLoop Method (ILoop2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~ISweepPlanarLoop`

Creates a temporary body by sweeping a planar loop along a vector.
Creates a temporary body by sweeping a planar loop along a vector.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISweepPlanarLoop( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal DraftAngle As System.Double, _
   ByRef StopFacesOut As Face2 _
) As Body2
```

```

Dim instance As ILoop2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim DraftAngle As System.Double
Dim StopFacesOut As Face2
Dim value As Body2
 
value = instance.ISweepPlanarLoop(X, Y, Z, DraftAngle, StopFacesOut)
```

```

Body2 ISweepPlanarLoop( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle,
   ref Face2 StopFacesOut
)
```

```

Body2^ ISweepPlanarLoop( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle,
   Face2^% StopFacesOut
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

*StopFacesOut*
:   Array of two stop [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

#### Return Value

New swept [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

This method requires simplification of the imported body.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.md)  
[ILoop2::SweepPlanarLoop Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~SweepPlanarLoop.md)
