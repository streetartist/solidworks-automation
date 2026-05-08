# SplitEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~SplitEntity`

Splits the selected sketch entity at the specified point.
Splits the selected sketch entity at the specified point.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SplitEntity( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal ClosedX As System.Double, _
   ByVal ClosedY As System.Double, _
   ByVal ClosedZ As System.Double _
) 
```

```

Dim instance As ISketchSegment
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim ClosedX As System.Double
Dim ClosedY As System.Double
Dim ClosedZ As System.Double
 
instance.SplitEntity(X, Y, Z, ClosedX, ClosedY, ClosedZ)
```

```

void SplitEntity( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double ClosedX,
   System.double ClosedY,
   System.double ClosedZ
)
```

```

void SplitEntity( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double ClosedX,
   System.double ClosedY,
   System.double ClosedZ
) 
```

#### Parameters

*X*
:   x coordinate where to split the selected entity

*Y*
:   y coordinate where to split the selected entity

*Z*
:   z coordinate where to split the selected entity

*ClosedX*
:   x coordinate where to close the split entity

*ClosedY*
:   y coordinate where to close the split entity

*ClosedZ*
:   z coordinate where to close the split entity

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.md)
