# IFindAttribute Method (IEntity)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IFindAttribute`

Finds an attribute on an entity.
Finds an attribute on an entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFindAttribute( _
   ByVal AttributeDef As AttributeDef, _
   ByVal WhichOne As System.Integer _
) As Attribute
```

```

Dim instance As IEntity
Dim AttributeDef As AttributeDef
Dim WhichOne As System.Integer
Dim value As Attribute
 
value = instance.IFindAttribute(AttributeDef, WhichOne)
```

```

Attribute IFindAttribute( 
   AttributeDef AttributeDef,
   System.int WhichOne
)
```

```

Attribute^ IFindAttribute( 
   AttributeDef^ AttributeDef,
   System.int WhichOne
) 
```

#### Parameters

*AttributeDef*
:   Pointer to the [attribute definition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md) you want to find

*WhichOne*
:   Instance of this type on this entity (0,1,2,3, and so on)

#### Return Value

Pointer to the [attribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) instance

Remarks

After you add an attribute instance to a face, edge, vertex, loop, feature, or document, you can retrieve the attribute for query or modification in several ways:

- Because an attribute instance is a feature:

  - You can use any of the standard feature traversal functions ([IPartDoc::IFeatureByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFeatureByName.md), [IModelDoc2::IFirstFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFirstFeature.md), and [IFeature::IGetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextFeature.md)) to get the feature representation of the attribute. You can then use the Feature object that represents the attribute instance with [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to get the underlying Attribute object.
  - It can be suppressed. Check its state by using [IAttribute::GetEntityState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.md) (swIsEntitySuppressed).
- If the user selected the attribute in the FeatureManager design tree, you can use standard selection control to get the Feature object for the attribute instance ([ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md)) and call Feature::GetSpecificFeature2 to get the underlying attribute object.
- If you traverse body topology, you can locate any Attribute object with a call to Entity::FindAttribute from the Entity object (for example, the face or edge). If the attribute instance was placed on the document, then you must use Feature::GetSpecificFeature2 to get back to it.
- Always call [IAttribute::GetEntityState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.md) to check if the attribute instance is valid and unambiguous.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)  
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.md)  
[IEntity::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~FindAttribute.md)  
[IAttrbute::IGetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetDefinition.md)  
[IAttributeDef::CreateInstance5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md)  
[IBody2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~FindAttribute.md)  
[IComponent2::IFindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IFindAttribute.md)  
[ISldWorks::DefineAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineAttribute.md)
