# StartEntity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~StartEntity`

Gets or sets the starting entity for the helix of this thread feature.
Gets or sets the starting entity for the helix of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property StartEntity As System.Object
```

```

Dim instance As IThreadFeatureData
Dim value As System.Object
 
instance.StartEntity = value
 
value = instance.StartEntity
```

```

System.object StartEntity {get; set;}
```

```

property System.Object^ StartEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), or planar [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) (see **Remarks**)

Remarks

Use [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) with Mark = 2 to select the start entity.

This property is optional, but required if [IThreadFeatureData::Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Edge.md) is not a planar circular [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
