# SaveVirtualComponent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SaveVirtualComponent`

Saves a virtual component to an external file.
Saves a virtual component to an external file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveVirtualComponent( _
   ByVal CompPathName As System.String _
) As System.Boolean
```

```

Dim instance As IComponent2
Dim CompPathName As System.String
Dim value As System.Boolean
 
value = instance.SaveVirtualComponent(CompPathName)
```

```

System.bool SaveVirtualComponent( 
   System.string CompPathName
)
```

```

System.bool SaveVirtualComponent( 
   System.String^ CompPathName
) 
```

#### Parameters

*CompPathName*
:   String containing full pathname of file to save component to

#### Return Value

True if successful, false if not

Example

[Insert New Virtual Component (C#)](Insert_New_Virtual_Component_Example_CSharp.htm)  
[Insert New Virtual Component (VB.NET)](Insert_New_Virtual_Component_Example_VBNET.htm)  
[Insert New Virtual Component (VBA)](Insert_New_Virtual_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.md)  
[IModelDocExtension::IsVirtualComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.md)  
[IAssemblyDoc::InsertNewVirtualPart Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualPart.md)  
[IAssemblyDoc::InsertNewAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewAssembly.md)  
[IAssemblyDoc::InsertNewVirtualAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.md)  
[IComponent2::MakeVirtual Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.md)
