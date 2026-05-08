# SetEntitiesWeldTo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldTo`

Sets the weld-to entities for this cosmetic weld bead, which was created using weld geometry.
Sets the weld-to entities for this cosmetic weld bead, which was created using weld geometry.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEntitiesWeldTo( _
   ByVal Entities As System.Object _
) 
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim Entities As System.Object
 
instance.SetEntitiesWeldTo(Entities)
```

```

void SetEntitiesWeldTo( 
   System.object Entities
)
```

```

void SetEntitiesWeldTo( 
   System.Object^ Entities
) 
```

#### Parameters

*Entities*
:   Array of weld-to entities of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) (see **Remarks**)

Remarks

The weld-to entities must be the same type of entities; e.g., all faces or all edges.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)  
[ICosmeticWeldBeadFeatureData::GetEntitiesWeldTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldTo.md)  
[ICosmeticWeldBeadFeatureData::GetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldFrom.md)  
[ICosmeticWeldBeadFeatureData::SetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldFrom.md)
