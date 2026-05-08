# GetSelectByIDString Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSelectByIDString`

Gets the name of the component for possible use with IModelDocExtension::SelectByID2, for selectively opening a document using ISldWorks::OpenDoc7 and IDocumentSpecification, etc.
Gets the name of the component for possible use with [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md), for selectively opening a document using [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md) and [IDocumentSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md), etc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectByIDString() As System.String
```

```

Dim instance As IComponent2
Dim value As System.String
 
value = instance.GetSelectByIDString()
```

```

System.string GetSelectByIDString()
```

```

System.String^ GetSelectByIDString(); 
```

#### Return Value

Name of component

Example

[Get Component Name from Selected Entity (VB.NET)](Get_Component_Name_From_Selected_Entity_Example_VBNET.htm)  
[Get Component Name From Selected Entity (VBA)](Get_Component_Name_From_Selected_Entity_Example_VB.htm)  
[Get Component Name from Selected Entity (C#)](Get_Component_Name_From_Selected_Entity_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IAssemblyDoc::GetComponentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByName.md)  
[IComponent2::Name2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Name2.md)  
[IAssemblyDoc::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames.md)
