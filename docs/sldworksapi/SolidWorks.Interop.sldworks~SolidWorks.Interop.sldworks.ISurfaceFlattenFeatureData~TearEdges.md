# TearEdges Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~TearEdges`

Gets or sets the tear edges for the relief cuts for this surface-flatten feature.
Gets or sets the tear edges for the relief cuts for this surface-flatten feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TearEdges As System.Object
```

```

Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Object
 
instance.TearEdges = value
 
value = instance.TearEdges
```

```

System.object TearEdges {get; set;}
```

```

property System.Object^ TearEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of entities that lie on the selected faces or surfaces to flatten (see **Remarks**)

Remarks

Tear edges:

- indicate where to make relief cuts before flattening the surface. During flattening, regions of the flattened surface are stretched while other regions are compressed. Adding tear edges through regions of high stress can reduce these deformations, which increases the accuracy of the flattened surface.
- allow users to flatten closed surfaces, such as spheres or entire solid bodies, that would otherwise not be flattened. See the **Example** section.
- can be any of these types of selected entities:
  - edges,
  - reference curves, and
  - 2D/3D splines.
- must each intersect the face or surface being flattened while touching one boundary edge, which is an edge adjacent to exactly one face or surface.
- are only applied when [ISurfaceFlattenFeatureData::ShouldMakeTears](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~ShouldMakeTears.md) is true.

The SOLIDWORKS API returns [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) for the entities selected for the tear edges in a surface-flatten feature.

Example

[Get Data for Surface-flatten Feature (C#)](Get_Data_for_Surface_Flatten_Feature_Example_CSharp.htm)  
[Get Data for Surface-flatten Feature (VB.NET)](Get_Data_for_Surface_Flatten_Feature_Example_VBNET.htm)  
[Get Data for Surface-flatten Feature (VBA)](Get_Data_for_Surface_Flatten_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.md)  
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.md)  
[ISurfaceFlattenFeatureData::MapEdges Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~MapEdges.md)
