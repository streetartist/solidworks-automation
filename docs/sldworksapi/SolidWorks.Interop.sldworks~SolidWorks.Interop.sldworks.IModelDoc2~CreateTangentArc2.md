# CreateTangentArc2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateTangentArc2`

Obsolete. Superseded by ISketchManager::CreateTangentArc.
Obsolete. Superseded by [ISketchManager::CreateTangentArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateTangentArc.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateTangentArc2( _
   ByVal P1x As System.Double, _
   ByVal P1y As System.Double, _
   ByVal P1z As System.Double, _
   ByVal P2x As System.Double, _
   ByVal P2y As System.Double, _
   ByVal P2z As System.Double, _
   ByVal ArcTypeIn As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim P1x As System.Double
Dim P1y As System.Double
Dim P1z As System.Double
Dim P2x As System.Double
Dim P2y As System.Double
Dim P2z As System.Double
Dim ArcTypeIn As System.Integer
Dim value As System.Boolean
 
value = instance.CreateTangentArc2(P1x, P1y, P1z, P2x, P2y, P2z, ArcTypeIn)
```

```

System.bool CreateTangentArc2( 
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.int ArcTypeIn
)
```

```

System.bool CreateTangentArc2( 
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z,
   System.int ArcTypeIn
) 
```

#### Parameters

*P1x*
:   x coordinate of start point in meters

*P1y*
:   y coordinate of start point in meters

*P1z*
:   Always 0

*P2x*
:   x coordinate of end point in meters

*P2y*
:   y coordinate of end point in meters

*P2z*
:   Always 0

*ArcTypeIn*
:   Type of tangent arc as defined in [swTangentArcTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangentArcTypes_e.html)

#### Return Value

1 = success, 0 = failure

Remarks

This method can only create 2D tangent arcs. Use [ISketchManager::CreateTangentArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateTangentArc.md) to create 3D tangent arcs.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::Create3PointArc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Create3PointArc.md)  
[IModelDoc2::CreateArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArc2.md)  
[IModelDoc2::CreateArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArcByCenter.md)  
[IModelDoc2::ICreateArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateArc2.md)
