# SetEntitiesWeldPath Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldPath`

Sets the entities for this cosmetic weld bead, which was created using a weld path.
Sets the entities for this cosmetic weld bead, which was created using a weld path.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEntitiesWeldPath( _
   ByVal Entities As System.Object _
) 
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim Entities As System.Object
 
instance.SetEntitiesWeldPath(Entities)
```

```

void SetEntitiesWeldPath( 
   System.object Entities
)
```

```

void SetEntitiesWeldPath( 
   System.Object^ Entities
) 
```

#### Parameters

*Entities*
:   Array of entities of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [sketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md), or a combination of edges and sketches (see **Remarks**)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)  
[ICosmeticWeldBeadFeatureData::GetEntitiesWeldPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldPath.md)
