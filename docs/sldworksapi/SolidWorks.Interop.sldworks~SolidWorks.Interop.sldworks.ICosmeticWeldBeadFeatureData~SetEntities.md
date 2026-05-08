# SetEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntities`

Obsolete. Superseded by ICosmeticWeldBeadFeatureData::SetEntitiesWeldFrom and ICosmeticWeldBeadFeatureData::SetEntitiesWeldTo.
Obsolete. Superseded by [ICosmeticWeldBeadFeatureData::SetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldFrom.md) and [ICosmeticWeldBeadFeatureData::SetEntitiesWeldTo.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldTo.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetEntities( _
   ByVal Entities As System.Object _
) 
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim Entities As System.Object
 
instance.SetEntities(Entities)
```

```

void SetEntities( 
   System.object Entities
)
```

```

void SetEntities( 
   System.Object^ Entities
) 
```

#### Parameters

*Entities*
:   Array of [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s and [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)s

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)  
[ICosmeticWeldBeadFeatureData::GetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntities.md)
