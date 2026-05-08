# InsertRuledSurfaceFromEdge Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRuledSurfaceFromEdge`

Obsolete. Superseded by IFeatureManager::InsertRuledSurfaceFromEdge2.
Obsolete. Superseded by [IFeatureManager::InsertRuledSurfaceFromEdge2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertRuledSurfaceFromEdge2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertRuledSurfaceFromEdge( _
   ByVal Type As System.Integer, _
   ByVal Length As System.Double, _
   ByVal FlipPullDir As System.Boolean, _
   ByVal FlipDir As System.Boolean, _
   ByVal TrimAndSew As System.Boolean, _
   ByVal Angle As System.Double, _
   ByVal CoordInput As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
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
Dim value As Feature
 
value = instance.InsertRuledSurfaceFromEdge(Type, Length, FlipPullDir, FlipDir, TrimAndSew, Angle, CoordInput, X, Y, Z)
```

```

Feature InsertRuledSurfaceFromEdge( 
   System.int Type,
   System.double Length,
   System.bool FlipPullDir,
   System.bool FlipDir,
   System.bool TrimAndSew,
   System.double Angle,
   System.bool CoordInput,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

Feature^ InsertRuledSurfaceFromEdge( 
   System.int Type,
   System.double Length,
   System.bool FlipPullDir,
   System.bool FlipDir,
   System.bool TrimAndSew,
   System.double Angle,
   System.bool CoordInput,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*Type*

*Length*

*FlipPullDir*

*FlipDir*

*TrimAndSew*

*Angle*

*CoordInput*

*X*

*Y*

*Z*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
