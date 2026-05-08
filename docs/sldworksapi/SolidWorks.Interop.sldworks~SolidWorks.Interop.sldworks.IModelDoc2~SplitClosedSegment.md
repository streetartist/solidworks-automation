# SplitClosedSegment Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SplitClosedSegment`

Obsolete. Superseded by ISketchManager::SplitClosedSegment.
Obsolete. Superseded by [ISketchManager::SplitClosedSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitClosedSegment.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SplitClosedSegment( _
   ByVal X0 As System.Double, _
   ByVal Y0 As System.Double, _
   ByVal Z0 As System.Double, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim X0 As System.Double
Dim Y0 As System.Double
Dim Z0 As System.Double
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
 
instance.SplitClosedSegment(X0, Y0, Z0, X1, Y1, Z1)
```

```

void SplitClosedSegment( 
   System.double X0,
   System.double Y0,
   System.double Z0,
   System.double X1,
   System.double Y1,
   System.double Z1
)
```

```

void SplitClosedSegment( 
   System.double X0,
   System.double Y0,
   System.double Z0,
   System.double X1,
   System.double Y1,
   System.double Z1
) 
```

#### Parameters

*X0*
:   X value of first point

*Y0*
:   Y value of first point

*Z0*
:   Z value of first point

*X1*
:   X value of second point

*Y1*
:   Y value of second point

*Z1*
:   Z value of second point

Remarks

The selected sketch segment must be a closed entity (for example, the start and end points must be the same). To split a closed sketch segment (for example, a complete circle) into two pieces, you must specify two points (x1, y1, z1) and (x2, y2, z2).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::SplitOpenSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SplitOpenSegment.md)  
[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)
