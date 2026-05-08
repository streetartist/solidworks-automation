# IsTemporaryBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsTemporaryBody`

Gets whether the body is a temporary body.
Gets whether the body is a temporary body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsTemporaryBody() As System.Boolean
```

```

Dim instance As IBody2
Dim value As System.Boolean
 
value = instance.IsTemporaryBody()
```

```

System.bool IsTemporaryBody()
```

```

System.bool IsTemporaryBody(); 
```

#### Return Value

True the body is a temporary body, false if not

Remarks

You can select an entity from a temporary body. You can also assign colors to faces on temporary bodies and to entire temporary bodies. See [IBody2::Display3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.md) and [IFace2::MaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialPropertyValues.md) or [IFace2::IMaterialPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IMaterialPropertyValues.md) and [IBody2::MaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.md) or [IBody2::IMaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IMaterialPropertyValues2.md).

Example

[Delete Faces (VBA)](Delete_Faces_Example_VB.htm)  
[Create Loft Body (C#)](Create_Loft_Body_Example_CSharp.htm)  
[Create Loft Body (VB.NET)](Create_Loft_Body_Example_VBNET.htm)  
[Create Loft Body (VBA)](Create_Loft_Body_Example_VB.htm)  
[Delete Blended Faces (C#)](Delete_Blended_Faces_Example_CSharp.htm)  
[Delete Blended Faces (VB.NET)](Delete_Blended_Faces_Example_VBNET.htm)  
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
