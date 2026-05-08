# ICreateSpline Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreateSpline`

Obsolete. Superseded by IModelDoc2::ICreateSpline.
Obsolete. Superseded by [IModelDoc2::ICreateSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSpline.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSpline( _
   ByVal PointCount As System.Integer, _
   ByRef PointData As System.Double _
) As SketchSegment
```

```

Dim instance As IModelDoc
Dim PointCount As System.Integer
Dim PointData As System.Double
Dim value As SketchSegment
 
value = instance.ICreateSpline(PointCount, PointData)
```

```

SketchSegment ICreateSpline( 
   System.int PointCount,
   ref System.double PointData
)
```

```

SketchSegment^ ICreateSpline( 
   System.int PointCount,
   System.double% PointData
) 
```

#### Parameters

*PointCount*

*PointData*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
