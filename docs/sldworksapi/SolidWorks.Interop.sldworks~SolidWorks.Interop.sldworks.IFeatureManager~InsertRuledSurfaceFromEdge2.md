# InsertRuledSurfaceFromEdge2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRuledSurfaceFromEdge2`

Inserts a ruled surface from the selected edge on this feature.
Inserts a ruled surface from the selected edge on this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertRuledSurfaceFromEdge2( _
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
   ByVal BConnectSurface As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
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
Dim value As Feature
 
value = instance.InsertRuledSurfaceFromEdge2(Type, Length, FlipPullDir, FlipDir, TrimAndSew, Angle, CoordInput, X, Y, Z, BConnectSurface)
```

```

Feature InsertRuledSurfaceFromEdge2( 
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
   System.bool BConnectSurface
)
```

```

Feature^ InsertRuledSurfaceFromEdge2( 
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
   System.bool BConnectSurface
) 
```

#### Parameters

*Type*
:   - 0 = Tangent to Surface
    - 1 = Normal to Surface
    - 2 = Tapered to Vector
    - 3 = Perpendicular to Vector
    - 4 = Sweep

*Length*
:   Distance at which to create the surface; valid for Tangent to Surface, Tapered to Vector, Perpendicular to Vector, and Sweep types only

*FlipPullDir*
:   True to flip the pull direction, false to not; valid for Normal to Surface and Tapered to Vector types only

*FlipDir*
:   True to flip the direction, false to not; valid for Perpendicular to Vector type only

*TrimAndSew*
:   True to trim and knit the surface, false to not

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

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

If you [select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) an edge with a selection mark of 4, the default face is used.  If you select an edge with a selection mark of 6, the alternate face is used.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.md)  
[IModeler::CreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurface.md)  
[IModeler::CreateRuledSurfaceFromEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateRuledSurfaceFromEdge.md)  
[IModeler::ICreateRuledSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurface.md)  
[IModeler::ICreateRuledSurfaceFromEdge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateRuledSurfaceFromEdge.md)
