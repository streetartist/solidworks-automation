# GetSafeEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetSafeEntity`

Gets a safe entity.
Gets a safe entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSafeEntity() As Entity
```

```

Dim instance As IEntity
Dim value As Entity
 
value = instance.GetSafeEntity()
```

```

Entity GetSafeEntity()
```

```

Entity^ GetSafeEntity(); 
```

#### Return Value

Pointer to the [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object

Remarks

A safe entity is an entity that continues to be valid after rebuilds until the pointer becomes invalid if the entity object to which it points is deleted.

To determine if an entity is safe, use the [IEntity::IsSafe](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IsSafe.md) property. This property is read-only and does not persist from session to session.

Example

[Get Faces Affected By Scale Feature (VBA)](Get_Faces_Affected_by_Scale_Feature_Example_VB.htm)  
[Use Safe Entity (VBA)](Use_Safe_Entity_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)  
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.md)  
[IBody2::GetSafeBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSafeBody.md)  
[IBody2::IsSafe Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsSafe.md)
