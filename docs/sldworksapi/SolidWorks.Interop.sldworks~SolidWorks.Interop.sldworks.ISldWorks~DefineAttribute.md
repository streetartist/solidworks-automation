# DefineAttribute Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineAttribute`

Creates an attribute definition, which is the first step in generating attributes.
Creates an attribute definition, which is the first step in generating attributes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DefineAttribute( _
   ByVal Name As System.String _
) As System.Object
```

```

Dim instance As ISldWorks
Dim Name As System.String
Dim value As System.Object
 
value = instance.DefineAttribute(Name)
```

```

System.object DefineAttribute( 
   System.string Name
)
```

```

System.Object^ DefineAttribute( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Name to give to the attribute definition; the name must be unique and qualified among the attributes defined in the current session (see Remarks)

#### Return Value

[Attribute definition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md)

Remarks

An attribute definition is a container that can hold a group of parameters. For example, you can use this container to hold machining information or BOM data. Instances of this container may then be created as [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) objects on the document object, or on faces, edges, vertices, and features within the document. Once created, you can get any of the IAttribute objects and query or change its parameter values.

The Name argument used for this attribute definition must be unique and qualified among the attributes defined in the current session. To ensure this, the first three letters of the name must be an officially recognized third-party identifier. Contact SOLIDWORKS Corporation if you need one. You can also use the prefix: "pub" ( for "public" ) if you are just testing.

**General sequence of steps in attribute creation**

1. Create an attribute definition (ISldWorks::DefineAttribute or [ISldWorks::IDefineAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IDefineAttribute.md))
2. Add parameters to the attribute definition ([IAttributeDef::AddParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~AddParameter.md))
3. Register the attribute definition ([IAttributeDef::Register](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~Register.md))
4. Create instances of the attribute definition on objects throughout the model ([IAttributeDef::CreateInstance5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.md))

Perform steps 1 through 3 only once for each working session. In other words, perform steps 1 through 3 when your DLL or EXE is initially loaded or run. Until the DLL is unloaded, or the EXE is closed, you can create as many instances of the attribute definition as you want as shown in step 4.

Calling this method attaches to an existing attribute definition with the specified Name or creates new attribute definition if a match is not found. The attribute definition exists throughout the current SOLIDWORKS session and persistent across SOLIDWORKS sessions if an attribute instance with that definition exists in the document. If an attribute definition exists, you cannot add or remove its parameters.

After an attribute instance is added to a face, edge, vertex, loop, feature, or document, there are several ways to get back to the attribute for query or modification.

1. Because an attribute instance is a feature, you can use any of the standard feature traversal routines (the FeatureByName methods, [IModelDoc2::FirstFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.md) or [IModelDoc2::IFirstFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFirstFeature.md), and [IFeature::GetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.md) or [IModelDoc2::IGetNextFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextFeature.md)) to grab the feature representation of the attribute. After you have the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object that represents the attribute instance, you can call [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to get the underlying [IAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md) object.
2. If the end-user selected the attribute in the FeatureManager design tree, you can use standard selection control to get the IFeature object representing the attribute instance ([ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md)) and then call IFeature::GetSpecificFeature2 to get the underlying IAttribute object.
3. If you are traversing body topology, then you can locate any IAttribute objects with a call to [IEntity::FindAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~FindAttribute.md) or [IEntity::IFindAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IFindAttribute.md) from the particular [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object (that is, face, edge, and so on). If the attribute instance was placed on the document, then you would need to use option 1 to get back to it.

After you have the IAttribute object that you want to query or modify, use the [IAttribute::GetParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetParameter.md) or [IAttribute::IGetParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetParameter.md) method to return the desired attribute parameter object. The [IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md) object provides a set of functions to query or modify specific attribute values.

Example

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)  
[Delete Faces (VBA)](Delete_Faces_Example_VB.htm)  
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)  
[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)  
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)  
[Delete Blended Faces (C#)](Delete_Blended_Faces_Example_CSharp.htm)  
[Delete Blended Faces (VB.NET)](Delete_Blended_Faces_Example_VBNET.htm)  
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::IDefineAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IDefineAttribute.md)
