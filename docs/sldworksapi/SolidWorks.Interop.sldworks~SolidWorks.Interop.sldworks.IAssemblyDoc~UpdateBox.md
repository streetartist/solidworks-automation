# UpdateBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateBox`

Updates the bounding box for this assembly.
Updates the bounding box for this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub UpdateBox() 
```

```

Dim instance As IAssemblyDoc
 
instance.UpdateBox()
```

```

void UpdateBox()
```

```

void UpdateBox(); 
```

Remarks

Use this method to help avoid clipping in shaded display mode if the assembly bounds change; for example, if you modify a component location using [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md).

Example

[Recalculate Bounding Box (C#)](Recalculate_Bounding_Box_Example_CSharp.htm)  
[Recalculate Bounding Box (VB.NET)](Recalculate_Bounding_Box_Example_VBNET.htm)  
[Recalculate Bounding Box (VBA)](Recalculate_Bounding_Box_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::GetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetBox.md)  
[IAssemblyDoc::IGetBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetBox.md)  
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.md)  
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.md)  
[IModelDocExtension::GetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.md)
