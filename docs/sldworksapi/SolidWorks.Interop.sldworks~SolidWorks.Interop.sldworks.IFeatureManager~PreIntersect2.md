# PreIntersect2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreIntersect2`

Prepares an intersect feature.
Prepares an intersect feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PreIntersect2( _
   ByVal CapPlanar As System.Boolean, _
   ByVal RegionType As System.Integer _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim CapPlanar As System.Boolean
Dim RegionType As System.Integer
Dim value As System.Object
 
value = instance.PreIntersect2(CapPlanar, RegionType)
```

```

System.object PreIntersect2( 
   System.bool CapPlanar,
   System.int RegionType
)
```

```

System.Object^ PreIntersect2( 
   System.bool CapPlanar,
   System.int RegionType
) 
```

#### Parameters

*CapPlanar*
:   True to cap the flat openings of surfaces to define closed volumes, false to not

*RegionType*
:   Type of regions to create:

    - 0 = Intersecting regions
    - 1 = Internal regions
    - 2 = Intersecting and internal regions

#### Return Value

Array of intersecting [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

Before calling this method, you must select the intersecting [surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md), [solids](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md), or [planes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) that make up the intersect feature.

After calling this method, call [IFeatureManager::PostIntersect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostIntersect.md) to create the intersect feature.

Example

[Create Intersect Feature (C#)](Create_Intersect_Feature_Example_CSharp.htm)  
[Create Intersect Feature (VB.NET)](Create_Intersect_Feature_Example_VBNET.htm)  
[Create Intersect Feature (VBA)](Create_Intersect_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md)
