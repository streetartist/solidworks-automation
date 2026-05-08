# SweepPlanarLoop Method (ILoop)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop~SweepPlanarLoop`

Obsolete. Superseded by ILoop2::SweepPlanarLoop.
Obsolete. Superseded by [ILoop2::SweepPlanarLoop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~SweepPlanarLoop.md).

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

Dim instance As ILoop
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

*Y*

*Z*

*DraftAngle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop.md)  
[ILoop Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop_members.md)
