# IGetEntityByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName`

Gets an entity (face, edge, vertex) by name.
Gets an entity (face, edge, vertex) by name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEntityByName( _
   ByVal Name As System.String, _
   ByVal EntityType As System.Integer _
) As Entity
```

```

Dim instance As IPartDoc
Dim Name As System.String
Dim EntityType As System.Integer
Dim value As Entity
 
value = instance.IGetEntityByName(Name, EntityType)
```

```

Entity IGetEntityByName( 
   System.string Name,
   System.int EntityType
)
```

```

Entity^ IGetEntityByName( 
   System.String^ Name,
   System.int EntityType
) 
```

#### Parameters

*Name*
:   Name of entity

*EntityType*
:   Entity type as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) (see **Remarks**)

#### Return Value

[Entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)

Remarks

Valid entityType types:

- swSelFACES
- swSelEDGES
- swSeleVERTICES

Another way to obtain an [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object based on its name is to traverse the body topology (for example, use [IBody2::GetFirstFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstFace.md) or [IBody2::IGetFirstFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstFace.md) and so on) and use [IModelDoc2::GetEntityName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetEntityName.md) or [IModelDoc2::IGetEntityName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetEntityName.md) to determine when you have located the desired entity.

Because the names of entities are stored with the part document, this method resides on the [IPartDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md) object.

Example

[Get Edge Data By Name (C++)](Get_Edge_Data_By_Name_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::GetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.md)  
[IPartDoc::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityName.md)  
[IPartDoc::DeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~DeleteEntityName.md)  
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.md)  
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.md)  
[IPartDoc::IDeleteEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IDeleteEntityName.md)  
[IPartDoc::IGetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.md)  
[IPartDoc::IGetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityName.md)  
[IPartDoc::IGetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetNamedEntities.md)  
[IPartDoc::SetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetEntityName.md)
