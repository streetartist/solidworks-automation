# IGetAllowedRelationsCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetAllowedRelationsCount`

Gets the number of sketch relations valid for the specified entities.
Gets the number of sketch relations valid for the specified entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAllowedRelationsCount( _
   ByVal NumEntities As System.Integer, _
   ByRef EntityArray As System.Object _
) As System.Integer
```

```

Dim instance As ISketchRelationManager
Dim NumEntities As System.Integer
Dim EntityArray As System.Object
Dim value As System.Integer
 
value = instance.IGetAllowedRelationsCount(NumEntities, EntityArray)
```

```

System.int IGetAllowedRelationsCount( 
   System.int NumEntities,
   ref System.object EntityArray
)
```

```

System.int IGetAllowedRelationsCount( 
   System.int NumEntities,
   System.Object^% EntityArray
) 
```

#### Parameters

*NumEntities*
:   Number of entities

*EntityArray*
:   Array of entities

#### Return Value

Number of sketch relations valid for the specified entities

Remarks

Call this method before calling [ISketchRelationManager::IGetAllowedRelations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetAllowedRelations.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.md)  
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.md)  
[ISketchRelationManager::GetAllowedRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetAllowedRelations.md)
