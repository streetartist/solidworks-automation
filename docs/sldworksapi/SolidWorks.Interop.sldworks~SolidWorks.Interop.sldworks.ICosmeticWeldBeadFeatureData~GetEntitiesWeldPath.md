# GetEntitiesWeldPath Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldPath`

Gets the entities for this cosmetic weld bead, which was created using a weld path.
Gets the entities for this cosmetic weld bead, which was created using a weld path.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntitiesWeldPath() As System.Object
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim value As System.Object
 
value = instance.GetEntitiesWeldPath()
```

```

System.object GetEntitiesWeldPath()
```

```

System.Object^ GetEntitiesWeldPath(); 
```

#### Return Value

Array of entities of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) or [sketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) or a combination of edges and sketches

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)  
[ICosmeticWeldBeadFeatureData::SetEntitiesWeldPath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldPath.md)
