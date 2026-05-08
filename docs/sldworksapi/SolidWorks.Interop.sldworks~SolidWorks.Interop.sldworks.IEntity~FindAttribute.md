# FindAttribute Method (IEntity)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~FindAttribute`

Finds an attribute on an entity.
Finds an attribute on an entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FindAttribute( _
   ByVal AttributeDef As System.Object, _
   ByVal WhichOne As System.Integer _
) As System.Object
```

```

Dim instance As IEntity
Dim AttributeDef As System.Object
Dim WhichOne As System.Integer
Dim value As System.Object
 
value = instance.FindAttribute(AttributeDef, WhichOne)
```

```

System.object FindAttribute( 
   System.object AttributeDef,
   System.int WhichOne
)
```

```

System.Object^ FindAttribute( 
   System.Object^ AttributeDef,
   System.int WhichOne
) 
```

#### Parameters

*AttributeDef*
:   Attribute definition you want to find

*WhichOne*
:   Instance of this type on this entity (0,1,2,3, and so on)

#### Return Value

[Attribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) instance

Remarks

After you add an attribute instance to a face, edge, vertex, loop, feature, or document, you can retrieve the attribute for query or modification in several ways:

- Because an attribute instance is a feature:

  - You can use any of the standard feature traversal functions ([IPartDoc::FeatureByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureByName.md), [IModelDoc2::FirstFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.md), and [IFeature::GetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.md)) to get the feature representation of the attribute. You can then use the Feature object that represents the attribute instance with [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to get the underlying Attribute object.
  - It can be suppressed. Check its state by using [IAttribute::GetEntityState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.md) (swIsEntitySuppressed).
- If the user selected the attribute in the FeatureManager design tree, you can use standard selection control to get the Feature object for the attribute instance ([ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md)) and call Feature::GetSpecificFeature2 to get the underlying attribute object.
- If you traverse body topology, you can locate any Attribute object with a call to Entity::FindAttribute from the Entity object (for example, the face or edge). If the attribute instance was placed on the document, then you must use Feature::GetSpecificFeature2 to get back to it.
- Always call [IAttribute::GetEntityState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.md) to check if the attribute instance is valid and unambiguous.

Example

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)  
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)  
[Delete Faces (VBA)](Delete_Faces_Example_VB.htm)  
[Find Attribute (C#)](Find_Attribute_Example_CSharp.htm)  
[Find Attribute (VB.NET)](Find_Attribute_Example_VBNET.htm)  
[Find Attribute (VBA)](Find_Attribute_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)  
[IEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.md)  
[IEntity::IFindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IFindAttribute.md)  
[IAttribute::GetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetDefinition.md)  
[IAttributeDef::CreateInstance5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md)  
[IBody2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~FindAttribute.md)  
[IComponent2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FindAttribute.md)  
[ISldWorks::DefineAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineAttribute.md)
