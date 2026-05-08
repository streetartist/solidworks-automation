# Delete Method (IAttribute)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~Delete`

Deletes an attribute and lets you indicate whether or not to update the FeatureManager design tree if the deleted attribute appears in it.
Deletes an attribute and lets you indicate whether or not to update the FeatureManager design tree if the deleted attribute appears in it.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Delete( _
   ByVal BuildTree As System.Boolean _
) As System.Boolean
```

```

Dim instance As IAttribute
Dim BuildTree As System.Boolean
Dim value As System.Boolean
 
value = instance.Delete(BuildTree)
```

```

System.bool Delete( 
   System.bool BuildTree
)
```

```

System.bool Delete( 
   System.bool BuildTree
) 
```

#### Parameters

*BuildTree*
:   True to update the FeatureManager design tree, false to not

#### Return Value

True if the attribute is deleted, false if not

Example

[Delete Faces (VBA)](Delete_Faces_Example_VB.htm)  
[Delete Attribute (C#)](Delete_Attribute_Example_CSharp.htm)  
[Delete Attribute (VB.NET)](Delete_Attribute_Example_VBNET.htm)  
[Delete Attribute (VBA)](Delete_Attribute_Example_VB.htm)  
[Delete Blended Faces (C#)](Delete_Blended_Faces_Example_CSharp.htm)  
[Delete Blended Faces (VB.NET)](Delete_Blended_Faces_Example_VBNET.htm)  
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md)  
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.md)
