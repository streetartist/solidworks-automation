# ISweepPlanarLoop Method (ILoop)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop~ISweepPlanarLoop`

Obsolete. Superseded by ILoop2::ISweepPlanarLoop.
Obsolete. Superseded by [ILoop2::ISweepPlanarLoop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~ISweepPlanarLoop.md).

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
   ByRef StopFacesOut As Face _
) As Body
```

```

Dim instance As ILoop
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim DraftAngle As System.Double
Dim StopFacesOut As Face
Dim value As Body
 
value = instance.ISweepPlanarLoop(X, Y, Z, DraftAngle, StopFacesOut)
```

```

Body ISweepPlanarLoop( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle,
   ref Face StopFacesOut
)
```

```

Body^ ISweepPlanarLoop( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double DraftAngle,
   Face^% StopFacesOut
) 
```

#### Parameters

*X*

*Y*

*Z*

*DraftAngle*

*StopFacesOut*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop.md)  
[ILoop Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop_members.md)
