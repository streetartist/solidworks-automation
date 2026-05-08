# GetComponentByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByName`

Gets the specified top-level assembly component.
Gets the specified top-level assembly component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetComponentByName( _
   ByVal CompName As System.String _
) As Component2
```

```

Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim value As Component2
 
value = instance.GetComponentByName(CompName)
```

```

Component2 GetComponentByName( 
   System.string CompName
)
```

```

Component2^ GetComponentByName( 
   System.String^ CompName
) 
```

#### Parameters

*CompName*
:   Name of the top-level assembly component to get

#### Return Value

[Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Example

[Get Component by Name (C#)](Get_Component_by_Name_Example_CSharp.htm)  
[Get Component by Name (VB.NET)](Get_Component_by_Name_Example_VBNET.htm)  
[Get Component by Name (VBA)](Get_Component_by_Name_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.md)  
[IAssemblyDoc::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetComponents.md)  
[IAssemblyDoc::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames.md)  
[IComponent2::GetSelectByIDString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSelectByIDString.md)  
[IComponent2::Name2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Name2.md)  
[IAssemblyDoc::GetComponentByID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByID.md)
