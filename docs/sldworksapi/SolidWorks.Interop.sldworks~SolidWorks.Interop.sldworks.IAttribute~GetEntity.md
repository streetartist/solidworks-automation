# GetEntity Method (IAttribute)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntity`

Gets the entity to which this attribute was originally associated.
Gets the entity to which this attribute was originally associated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntity() As System.Object
```

```

Dim instance As IAttribute
Dim value As System.Object
 
value = instance.GetEntity()
```

```

System.object GetEntity()
```

```

System.Object^ GetEntity(); 
```

#### Return Value

Object for the entity or NULL (see **Remarks**)

Remarks

This method returns NULL when the attribute is associated with:

- the document
- an invalid entity
- a suppressed entity

When this method returns NULL, use [IAttribute::GetEntityState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.md) to determine which of these situations you have encountered.

When the [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) object is suppressed, this method returns NULL.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md)  
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.md)  
[IAttribute::IGetEntity2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetEntity2.md)  
[IAttribute::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetName.md)  
[IAttribute::GetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetParameter.md)  
[IAttributeDef::CreateInstance5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md)  
[IBody2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~FindAttribute.md)  
[IEntity::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~FindAttribute.md)  
[IEntity::IFindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IFindAttribute.md)  
[IFeature::GetSpecificFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md)  
[ISldWorks::DefineAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineAttribute.md)
