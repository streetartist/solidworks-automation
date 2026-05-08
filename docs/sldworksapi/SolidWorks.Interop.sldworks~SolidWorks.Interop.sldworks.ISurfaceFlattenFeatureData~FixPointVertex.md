# FixPointVertex Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~FixPointVertex`

Gets or sets the anchor point for flattening the selected faces or surfaces.
Gets or sets the anchor point for flattening the selected faces or surfaces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FixPointVertex As System.Object
```

```

Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Object
 
instance.FixPointVertex = value
 
value = instance.FixPointVertex
```

```

System.object FixPointVertex {get; set;}
```

```

property System.Object^ FixPointVertex {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Anchor point ([vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) or a point on an [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)) for flattening

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.md)  
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.md)
