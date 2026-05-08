# PreIntersect Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreIntersect`

Obsolete. Superseded by IFeatureManager::PreIntersect2.
Obsolete. Superseded by [IFeatureManager::PreIntersect2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreIntersect2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PreIntersect( _
   ByVal CapPlanar As System.Boolean _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim CapPlanar As System.Boolean
Dim value As System.Object
 
value = instance.PreIntersect(CapPlanar)
```

```

System.object PreIntersect( 
   System.bool CapPlanar
)
```

```

System.Object^ PreIntersect( 
   System.bool CapPlanar
) 
```

#### Parameters

*CapPlanar*
:   True to cap the flat openings of surfaces to define closed volumes, false to not

#### Return Value

Array of intersect [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

Before calling this method, you must select the intersecting [surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md), [solids](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md), or [planes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) that make up the intersect feature.

After calling this method, call [IFeatureManager::PostIntersect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostIntersect.md) to create the intersect feature.

Example

[Get Intersect Feature Data (VBA)](Get_Intersect_Feature_Data_Example_VB.htm)  
[Get Intersect Feature Data (VB.NET)](Get_Intersect_Feature_Data_Example_VBNET.htm)  
[Get Intersect Feature Data (C#)](Get_Intersect_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md)
