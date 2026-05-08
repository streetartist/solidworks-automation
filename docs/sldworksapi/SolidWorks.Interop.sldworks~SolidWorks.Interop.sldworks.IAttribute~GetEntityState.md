# GetEntityState Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState`

Returns the state of the associated entity.
Returns the state of the associated entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntityState( _
   ByVal WhichState As System.Integer _
) As System.Boolean
```

```

Dim instance As IAttribute
Dim WhichState As System.Integer
Dim value As System.Boolean
 
value = instance.GetEntityState(WhichState)
```

```

System.bool GetEntityState( 
   System.int WhichState
)
```

```

System.bool GetEntityState( 
   System.int WhichState
) 
```

#### Parameters

*WhichState*
:   Entity state are defined in [swAssociatedEntityStates\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssociatedEntityStates_e.html)

#### Return Value

True if the query state matches WhichState, false if not

Remarks

If the attribute is not associated to any entity (that is, it is associated to the document), all queries return false.

The WhichState argument can take any of the values in the swAssociatedEntityStates\_e, where:

- swIsEntityInvalid is a general query. It returns true when the associated entity is not valid due to a suppression or modeling operation.
- swIsEntitySuppressed is a more specific query. It returns true only if the associated entity is not valid due to a suppression.

[IAttribute::GetEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntity.md)and [IAttribute::IGetEntity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetEntity2.md) return Nothing or null when the attribute is associated with:

- document
- invalid entity
- suppressed entity

For example, if an attribute is applied to a face on a boss feature and then that boss feature is suppressed, your application might make the following calls:

- IAttribute::GetEntity - Returns Nothing or null
- IAttribute::GetEntityState(*swIsEntityInvalid*) - Returns true to indicate possibly a suppressed or deleted entity
- IAttribute::GetEntityState(*swIsEntitySuppressed*) - Returns true to indicate that the entity is currently suppressed

Example

[Find Attribute (C#)](Find_Attribute_Example_CSharp.htm)  
[Find Attribute (VB.NET)](Find_Attribute_Example_VBNET.htm)  
[Find Attribute (VBA)](Find_Attribute_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md)  
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.md)  
[IAnnotation::GetAttachedEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetAttachedEntities2.md)  
[IAnnotation::IGetAttachedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetAttachedEntities.md)  
[IAttribute::GetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetDefinition.md)  
[IAttribute::IGetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetDefinition.md)  
[IAttribute::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetName.md)  
[IAttribute::GetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetParameter.md)  
[IAttribute::IGetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetParameter.md)  
[IAttributeDef::CreateInstance5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md)  
[IComponent2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FindAttribute.md)  
[IComponent2::IFindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IFindAttribute.md)  
[IEntity::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~FindAttribute.md)  
[IEntity::IFindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IFindAttribute.md)  
[IEntity::GetSafeEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetSafeEntity.md)  
[IEntity::GetType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~GetType.md)  
[IFaultEntity::Entity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity.md)  
[IFeature::GetSpecificFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md)  
[IModelDocExtension::GetCorrespondingEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity.md)  
[IPartDoc::GetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetEntityByName.md)  
[IPartDoc::IGetEntityByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetEntityByName.md)  
[IPartDoc::GetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetNamedEntities.md)  
[IPartDoc::IGetNamedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetNamedEntities.md)  
[IView::GetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetVisibleEntities.md)  
[IView::IGetVisibleEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetVisibleEntities.md)
