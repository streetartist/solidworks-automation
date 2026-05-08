# Register Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~Register`

Registers an AttributeDef object as the final part of its creation.
Registers an [AttributeDef](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md) object as the final part of its creation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Register() As System.Boolean
```

```

Dim instance As IAttributeDef
Dim value As System.Boolean
 
value = instance.Register()
```

```

System.bool Register()
```

```

System.bool Register(); 
```

#### Return Value

True if the AttributeDef object is registered successfully, false if not

Remarks

Call this method after the AttributeDef object is created using [ISldWorks::DefineAttribute](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineAttribute.md) and after all parameters are added to the attribute definition using [IAttributeDef::AddParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~Register.md).

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

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md)  
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.md)
