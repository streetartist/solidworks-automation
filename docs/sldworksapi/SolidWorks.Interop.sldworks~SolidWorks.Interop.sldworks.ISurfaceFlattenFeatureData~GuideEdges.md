# GuideEdges Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~GuideEdges`

Gets or sets the edges to guide the shape and length of the flattened surface.
Gets or sets the edges to guide the shape and length of the flattened surface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GuideEdges As System.Object
```

```

Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Object
 
instance.GuideEdges = value
 
value = instance.GuideEdges
```

```

System.object GuideEdges {get; set;}
```

```

property System.Object^ GuideEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of the [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) to control the shape and length of the flattened surface

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.md)  
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.md)
