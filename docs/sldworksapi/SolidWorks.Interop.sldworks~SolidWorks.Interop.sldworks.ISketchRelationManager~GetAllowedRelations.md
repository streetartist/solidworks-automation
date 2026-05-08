# GetAllowedRelations Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetAllowedRelations`

Gets the types of sketch relations valid for the specified entities.
Gets the types of sketch relations valid for the specified entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAllowedRelations( _
   ByVal Entities As System.Object _
) As System.Object
```

```

Dim instance As ISketchRelationManager
Dim Entities As System.Object
Dim value As System.Object
 
value = instance.GetAllowedRelations(Entities)
```

```

System.object GetAllowedRelations( 
   System.object Entities
)
```

```

System.Object^ GetAllowedRelations( 
   System.Object^ Entities
) 
```

#### Parameters

*Entities*
:   Array of entities

#### Return Value

Array of sketch relation types valid for the specified entities as defined in [swConstraintType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.md)  
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.md)  
[ISketchManagerRelation::IGetAllowedRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetAllowedRelations.md)  
[ISketchManagerRelation::IGetAllowedRelationsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetAllowedRelationsCount.md)
