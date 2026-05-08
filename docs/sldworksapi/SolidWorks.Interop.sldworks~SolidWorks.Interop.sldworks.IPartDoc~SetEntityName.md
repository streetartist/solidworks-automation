# SetEntityName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetEntityName`

Sets the name of the entity if the entity does not have a name and the name is unique to the part.
Sets the name of the entity if the entity does not have a name and the name is unique to the part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetEntityName( _
   ByVal Entity As System.Object, _
   ByVal StringValue As System.String _
) As System.Boolean
```

```

Dim instance As IPartDoc
Dim Entity As System.Object
Dim StringValue As System.String
Dim value As System.Boolean
 
value = instance.SetEntityName(Entity, StringValue)
```

```

System.bool SetEntityName( 
   System.object Entity,
   System.string StringValue
)
```

```

System.bool SetEntityName( 
   System.Object^ Entity,
   System.String^ StringValue
) 
```

#### Parameters

*Entity*
:   [Entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)

*StringValue*
:   Name of the entity

#### Return Value

True if name is set successfully, false if not

Remarks

If the entity already has a name or the specified name is not unique to the part, then this method does not change the name and returns false.

This behavior is intended to prevent a program from accidentally renaming an entity that is referenced in some other location. For example, if an assembly contains a mate to a face on a part, then a name is automatically assigned to that face. If you were to change that name, then there is no guarantee that the mate is still valid. Therefore, when using entity names, you should first check to see if the entity is already named, and, if so, use the existing name. If no name exists for the entity, then you can name the entity.

You can explicitly delete an entity name using the [IPartDoc::DeleteEntityName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~DeleteEntityName.md) or [IPartDoc::IDeleteEntityName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IDeleteEntityName.md) method. You then have the option of renaming the item or using that name elsewhere. The method was provided because the action is already available in the core SOLIDWORKS product. However, you should recognize the possibility of reference failures as described.

Example

[Select and Rename Object (VBA)](Create_and_Rename_Objects_Example_VB.htm)  
[Get Entity By Name (VBA)](Get_Entity_By_Name_Example.htm)  
[Get Cross Break Feature Data in Sheet Metal Part (C#)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_CSharp.htm)  
[Get Cross Break Feature Data in Sheet Metal Part (VB.NET)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VBNET.htm)  
[Get Cross Break Feature Data in Sheet Metal Part (VBA)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::GetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.md)  
[IPartDoc::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityName.md)  
[IPartDoc::IGetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.md)  
[IPartDoc::IGetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityName.md)  
[IPartDoc::IGetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetNamedEntities.md)  
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.md)  
[IPartDoc::GetNamedEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntitiesCount.md)  
[IPartDoc::ISetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ISetEntityName.md)  
[IPartDoc::IDeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IDeleteEntityName.md)  
[IPartDoc::DeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~DeleteEntityName.md)
