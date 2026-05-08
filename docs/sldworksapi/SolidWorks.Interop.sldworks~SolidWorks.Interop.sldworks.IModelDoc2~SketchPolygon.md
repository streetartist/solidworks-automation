# SketchPolygon Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchPolygon`

Obsolete. Superseded by ISketchManager::CreatePolygon.
Obsolete. Superseded by [ISketchManager::CreatePolygon](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreatePolygon.md).

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

Dim instance As IModelDoc2
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
:   X component of the polygon's center

*YCenter*
:   Y component of the polygon's center

*XEdge*
:   X component of the first vertex on the polygon

*YEdge*
:   Y component of the first vertex on the polygon

*NSides*
:   Number of sides for the polygon

*BInscribed*
:   True to show an inscribed construction circle, false to show a circumscribed construction circle

#### Return Value

True if polygon created, false if not

Remarks

After using this method, the PropertyManager page is in edit mode for the polygon. To exit this PropertyManager page and complete the operation, use [IModelDoc2::SetPickMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetPickMode.md), [IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.md), or exit the sketch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
