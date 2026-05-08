# GetIntersectionsTools Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsTools`

Gets the intersecting solids, surfaces, and planes in this intersect feature.
Gets the intersecting solids, surfaces, and planes in this intersect feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIntersectionsTools() As System.Object
```

```

Dim instance As IIntersectFeatureData
Dim value As System.Object
 
value = instance.GetIntersectionsTools()
```

```

System.object GetIntersectionsTools()
```

```

System.Object^ GetIntersectionsTools(); 
```

#### Return Value

Array of intersecting [solids](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md), [surfaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md), and [planes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) in this intersect feature

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md)  
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.md)  
[IIntersectFeatureData::GetIntersectionsToolsCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsToolsCount.md)  
[IIntersectFeatureData::SetIntersectionsTools Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~SetIntersectionsTools.md)
