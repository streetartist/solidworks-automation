# SketchPolygon Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchPolygon`

Obsolete. Superseded by IModelDoc2::SketchPolygon.
Obsolete. Superseded by [IModelDoc2::SketchPolygon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchPolygon.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchPolygon( _
   ByVal XCenter As System.Double, _
   ByVal YCenter As System.Double, _
   ByVal XEdge As System.Double, _
   ByVal YEdge As System.Double, _
   ByVal NSides As System.Integer, _
   ByVal BInscribed As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc
Dim XCenter As System.Double
Dim YCenter As System.Double
Dim XEdge As System.Double
Dim YEdge As System.Double
Dim NSides As System.Integer
Dim BInscribed As System.Boolean
Dim value As System.Boolean
 
value = instance.SketchPolygon(XCenter, YCenter, XEdge, YEdge, NSides, BInscribed)
```

```

System.bool SketchPolygon( 
   System.double XCenter,
   System.double YCenter,
   System.double XEdge,
   System.double YEdge,
   System.int NSides,
   System.bool BInscribed
)
```

```

System.bool SketchPolygon( 
   System.double XCenter,
   System.double YCenter,
   System.double XEdge,
   System.double YEdge,
   System.int NSides,
   System.bool BInscribed
) 
```

#### Parameters

*XCenter*

*YCenter*

*XEdge*

*YEdge*

*NSides*

*BInscribed*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
