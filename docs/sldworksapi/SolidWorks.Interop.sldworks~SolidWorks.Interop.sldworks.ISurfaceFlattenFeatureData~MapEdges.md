# MapEdges Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~MapEdges`

Gets or sets the map edges for this surface-flatten feature.
Gets or sets the map edges for this surface-flatten feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MapEdges As System.Object
```

```

Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Object
 
instance.MapEdges = value
 
value = instance.MapEdges
```

```

System.object MapEdges {get; set;}
```

```

property System.Object^ MapEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of entities that lie on the selected faces or surfaces to flatten (see **Remarks**)

Remarks

Map edges:

- are entities to map to the flattened surface. By default, any entity that lies on top of a face or surface to flatten is ignored unless the user selects the entity as a map edge.
- are useful when users want to see where a selected entity on the original body would lie on a flattened surface. For example, users might select edges as map lines to serve as bend lines in the flattened surface.
- can be any of these types of selected entities:
  - edges,
  - reference curves,
  - 2D/3D splines,
  - sketches, and
  - sketch text.

The SOLIDWORKS API returns [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) for the entities selected for the map edges in a surface-flatten feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.md)  
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.md)  
[ISurfaceFlattenFeatureData::TearEdges Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~TearEdges.md)
