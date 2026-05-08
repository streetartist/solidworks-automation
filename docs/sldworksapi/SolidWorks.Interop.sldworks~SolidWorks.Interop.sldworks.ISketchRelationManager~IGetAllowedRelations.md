# IGetAllowedRelations Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetAllowedRelations`

Gets the types of sketch relations valid for the specified entities.
Gets the types of sketch relations valid for the specified entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetAllowedRelations( _
   ByVal NumEntities As System.Integer, _
   ByRef EntityArray As System.Object, _
   ByVal NumAllowedRelations As System.Integer _
) As System.Integer
```

```

Dim instance As ISketchRelationManager
Dim NumEntities As System.Integer
Dim EntityArray As System.Object
Dim NumAllowedRelations As System.Integer
Dim value As System.Integer
 
value = instance.IGetAllowedRelations(NumEntities, EntityArray, NumAllowedRelations)
```

```

System.int IGetAllowedRelations( 
   System.int NumEntities,
   ref System.object EntityArray,
   System.int NumAllowedRelations
)
```

```

System.int IGetAllowedRelations( 
   System.int NumEntities,
   System.Object^% EntityArray,
   System.int NumAllowedRelations
) 
```

#### Parameters

*NumEntities*
:   Number of entities

*EntityArray*
:   Array of entities

*NumAllowedRelations*
:   Number of relations valid for the specified entities

#### Return Value

- in-process, unmanaged C++: Pointer to an array of sketch relation types valid for the specified entities as defined in [swConstraintType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [ISketchRelationManager::IGetAllowedRelationsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~IGetAllowedRelationsCount.md) before calling this method to get the value for NumEntities.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.md)  
[ISketchRelationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.md)  
[ISketchRelationManager::GetAllowedRelations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager~GetAllowedRelations.md)
