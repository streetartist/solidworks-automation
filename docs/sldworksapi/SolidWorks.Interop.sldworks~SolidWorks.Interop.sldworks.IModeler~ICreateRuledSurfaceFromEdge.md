# ICreateRuledSurfaceFromEdge Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurfaceFromEdge`

Creates a ruled surface using the specified edges and returns a surface body.
Creates a ruled surface using the specified edges and returns a surface body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateRuledSurfaceFromEdge( _
   ByVal ModDoc As ModelDoc2, _
   ByVal NumOfEdges As System.Integer, _
   ByRef Edges As Edge, _
   ByVal Type As System.Integer, _
   ByVal Length As System.Double, _
   ByVal FlipPullDir As System.Boolean, _
   ByVal FlipDir As System.Boolean, _
   ByVal TrimAndSew As System.Boolean, _
   ByVal Angle As System.Double, _
   ByVal CoordInput As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal BConnectSurface As System.Boolean, _
   ByRef RuledSurface As Body2 _
) As System.Integer
```

```

Dim instance As IModeler
Dim ModDoc As ModelDoc2
Dim NumOfEdges As System.Integer
Dim Edges As Edge
Dim Type As System.Integer
Dim Length As System.Double
Dim FlipPullDir As System.Boolean
Dim FlipDir As System.Boolean
Dim TrimAndSew As System.Boolean
Dim Angle As System.Double
Dim CoordInput As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim BConnectSurface As System.Boolean
Dim RuledSurface As Body2
Dim value As System.Integer
 
value = instance.ICreateRuledSurfaceFromEdge(ModDoc, NumOfEdges, Edges, Type, Length, FlipPullDir, FlipDir, TrimAndSew, Angle, CoordInput, X, Y, Z, BConnectSurface, RuledSurface)
```

```

System.int ICreateRuledSurfaceFromEdge( 
   ModelDoc2 ModDoc,
   System.int NumOfEdges,
   ref Edge Edges,
   System.int Type,
   System.double Length,
   System.bool FlipPullDir,
   System.bool FlipDir,
   System.bool TrimAndSew,
   System.double Angle,
   System.bool CoordInput,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool BConnectSurface,
   out Body2 RuledSurface
)
```

```

System.int ICreateRuledSurfaceFromEdge( 
   ModelDoc2^ ModDoc,
   System.int NumOfEdges,
   Edge^% Edges,
   System.int Type,
   System.double Length,
   System.bool FlipPullDir,
   System.bool FlipDir,
   System.bool TrimAndSew,
   System.double Angle,
   System.bool CoordInput,
   System.double X,
   System.double Y,
   System.double Z,
   System.bool BConnectSurface,
   [Out] Body2^ RuledSurface
) 
```

#### Parameters

*ModDoc*
:   [Model document](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) in which to create surface body

*NumOfEdges*
:   Number of edges on which to create ruled surface

*Edges*
:   Array of edges on which to create ruled surface

    **NOTE:** Currently only a single edge is supported.

*Type*
:   0 = Tangent to Surface

    1 = Normal to Surface

    2 = Tapered to Vector

    3 = Perpendicular to Vector

    4 = Sweep

*Length*
:   Distance at which to create the surface; valid for Tangent to Surface, Tapered to Vector, Perpendicular to Vector, and Sweep types only

*FlipPullDir*
:   True to flip the pull direction, false to not; valid for Normal to Surface and Tapered to Vector types only

*FlipDir*
:   True to flip the direction, false to not; valid for Perpendicular to Vector type only

*TrimAndSew*
:   True to trim and knit the surface, false to not

*Angle*
:   Angle for Tapered to Vector type only

*CoordInput*
:   True to enable coordinate input, false if not; for Sweep type only

*X*
:   x coordinate

*Y*
:   y coordinate

*Z*
:   z coordinate

*BConnectSurface*
:   True to remove any connecting surfaces, false to not

*RuledSurface*
:   Ruled surface [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

#### Return Value

0 if ruled surface body created, -1 if not

Remarks

This method returns a surface body, unlike [IFeatureManager::InsertRuledSurfaceFromEdge2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRuledSurfaceFromEdge2.md), which returns a feature.

If you [select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) an edge with a selection mark of 4, the default face is used.  If you select an edge with a selection mark of 6, the alternate face is used.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.md)  
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.md)  
[IModeler::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurface.md)  
[IModeler::CreateRuledSurfaceFromEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurfaceFromEdge.md)  
[IModeler::CreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.md)
