# CreateNewBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateNewBody`

Creates a new body to use for import sewing operations and returns it to the caller.
Creates a new body to use for import sewing operations and returns it to the caller.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateNewBody() As System.Object
```

```

Dim instance As IPartDoc
Dim value As System.Object
 
value = instance.CreateNewBody()
```

```

System.object CreateNewBody()
```

```

System.Object^ CreateNewBody(); 
```

#### Return Value

New [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

The intention is that with a handle on such a (initially empty) body, appropriate construction methods (for example, [IBody2::CreateTrimmedSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTrimmedSurface.md)) can be called that eventually amount to a non-trivial object.

Example

[Create Body Using Trimmed Surfaces (VBA)](Create_Body_using_Trimmed_Surfaces_Example_VB.htm)  
[Create Reference Curve (C#)](Create_Reference_Curve_Example_CSharp.htm)  
[Create Reference Curve (VB.NET)](Create_Reference_Curve_Example_VBNET.htm)  
[Create Reference Curve (VBA)](Create_Reference_Curve_Example_VB.htm)  
[Create Imported Solid Body (C#)](Create_Imported_Solid_Body_Example_CSharp.htm)  
[Create Imported Solid Body (VB.NET)](Create_Imported_Solid_Body_Example_VBNET.htm)  
[Create Imported Solid Body (VBA)](Create_Imported_Solid_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::ICreateNewBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateNewBody2.md)
