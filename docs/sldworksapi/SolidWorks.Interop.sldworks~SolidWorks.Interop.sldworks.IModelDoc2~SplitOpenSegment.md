# SplitOpenSegment Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SplitOpenSegment`

Obsolete. Superseded by ISketchManager::SplitOpenSegment.
Obsolete. Superseded by [ISketchManager::SplitOpenSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~SplitOpenSegment.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SplitOpenSegment( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
 
instance.SplitOpenSegment(X, Y, Z)
```

```

void SplitOpenSegment( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

void SplitOpenSegment( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X value of the point that splits the sketch segment in two

*Y*
:   Y value of the point that splits the sketch segment in two

*Z*
:   Z value of the point that splits the sketch segment in two

Remarks

The selected sketch segment must be an open entity; for example, the start and end points cannot be the same.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)  
[IModelDoc2::SplitClosedSegment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SplitClosedSegment.md)
