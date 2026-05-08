# ICreatePoint2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreatePoint2`

Obsolete. Superseded by IModelDoc2::ICreatePoint2.
Obsolete. Superseded by [IModelDoc2::ICreatePoint2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePoint2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreatePoint2( _
   ByVal PointX As System.Double, _
   ByVal PointY As System.Double, _
   ByVal PointZ As System.Double _
) As SketchPoint
```

```

Dim instance As IModelDoc
Dim PointX As System.Double
Dim PointY As System.Double
Dim PointZ As System.Double
Dim value As SketchPoint
 
value = instance.ICreatePoint2(PointX, PointY, PointZ)
```

```

SketchPoint ICreatePoint2( 
   System.double PointX,
   System.double PointY,
   System.double PointZ
)
```

```

SketchPoint^ ICreatePoint2( 
   System.double PointX,
   System.double PointY,
   System.double PointZ
) 
```

#### Parameters

*PointX*

*PointY*

*PointZ*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
