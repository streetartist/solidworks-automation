# FilletXpertMakeCorner Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertMakeCorner`

Creates or changes a fillet corner feature.
Creates or changes a fillet corner feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FilletXpertMakeCorner( _
   ByVal CornerType As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim CornerType As System.Integer
Dim value As Feature
 
value = instance.FilletXpertMakeCorner(CornerType)
```

```

Feature FilletXpertMakeCorner( 
   System.int CornerType
)
```

```

Feature^ FilletXpertMakeCorner( 
   System.int CornerType
) 
```

#### Parameters

*CornerType*
:   See **Remarks**

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

For the fillet corner, everything is dependent on the convexity of the three filleted edges adjacent.

 

If all three edges have the same convexity, then no corner substitution is possible. Otherwise, there will be two edges of one convexity, and one of the other. It does not matter if the two same edges are both convex or both concave, as long as the edges are the same.

 

The valid values for the CornerType argument are:

- 1 = if the two edges with the same convexity have the same radius, make a triangular corner patch.
- 2 = if the two edges with the same convexity have the same radius, make a quadrilateral corner patch.
- 3 = if the two edges with the same convexity have different radii, make a triangular corner patch.
- 4 = if the two edges with the same convexity have different radii, make two triangular corner patches (which together look like a split quadrilateral patch).
- 5 = if the two edges with the same convexity have different radii, make a quadrilateral corner patch.

NOTE: Types 1 and 3 relate to one another, as do types 2 and 5. This means that if the corner type is not consistent with the convexity/radius requirements, then the appropriate type will be mapped and substituted. Thus, specifying type 1 on a corner with two edges of the same convexity, but different radii, results in a type 3, automatically.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::FeatureFillet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet.md)  
[IFeatureManager::IFeatureFillet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IFeatureFillet.md)  
[IFeatureManager::FilletXpertChange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.md)  
[IFeatureManager::FilletXpertRemove Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.md)
