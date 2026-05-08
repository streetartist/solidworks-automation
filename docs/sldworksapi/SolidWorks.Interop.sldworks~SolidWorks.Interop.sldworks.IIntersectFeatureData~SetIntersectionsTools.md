# SetIntersectionsTools Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~SetIntersectionsTools`

Specifies the intersecting solids, surfaces, and planes for this intersect feature.
Specifies the intersecting solids, surfaces, and planes for this intersect feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetIntersectionsTools( _
   ByVal Tools As System.Object _
) 
```

```

Dim instance As IIntersectFeatureData
Dim Tools As System.Object
 
instance.SetIntersectionsTools(Tools)
```

```

void SetIntersectionsTools( 
   System.object Tools
)
```

```

void SetIntersectionsTools( 
   System.Object^ Tools
) 
```

#### Parameters

*Tools*
:   Array of intersecting [solids](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md), [surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md), and [planes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) for this intersect feature

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md)  
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.md)  
[IIntersectFeatureData::GetIntersectionsTools Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsTools.md)
