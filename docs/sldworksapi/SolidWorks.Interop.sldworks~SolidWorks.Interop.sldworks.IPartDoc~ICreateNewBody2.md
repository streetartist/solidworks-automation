# ICreateNewBody2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateNewBody2`

Creates a new body to use for import sewing operations and returns it to the caller.
Creates a new body to use for import sewing operations and returns it to the caller.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateNewBody2() As Body2
```

```

Dim instance As IPartDoc
Dim value As Body2
 
value = instance.ICreateNewBody2()
```

```

Body2 ICreateNewBody2()
```

```

Body2^ ICreateNewBody2(); 
```

#### Return Value

[Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

The intention is that with a handle on such a (initially empty) body, appropriate construction methods (for example, [IBody2::CreateTrimmedSurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateTrimmedSurface.md)) can be called that eventually amount to a non-trivial object.

Example

[Create Imported Surface Body from Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IPartDoc::CreateNewBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateNewBody.md)
