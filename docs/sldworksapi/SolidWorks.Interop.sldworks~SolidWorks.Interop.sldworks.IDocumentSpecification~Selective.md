# Selective Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Selective`

Gets or sets whether to open a document in Quick view (parts and drawings) or Quick view / Selective (assemblies) mode.
Gets or sets whether to open a document in Quick view (parts and drawings) or Quick view / Selective (assemblies) mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Selective As System.Boolean
```

```

Dim instance As IDocumentSpecification
Dim value As System.Boolean
 
instance.Selective = value
 
value = instance.Selective
```

```

System.bool Selective {get; set;}
```

```

property System.bool Selective {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to open the document in Quick view / Selective open mode, false to not

Remarks

Use [IDocumentSpecification::ComponentList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ComponentList.md) to specify the selected components to load when opening the assembly document.

Example

[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)  
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)  
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)  
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)  
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)  
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)  
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.md)  
[IAssemblyDoc::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames.md)  
[IAssemblyDoc::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~HasUnloadedComponents.md)  
[IComponent2::GetHiddenUnloadedChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetHiddenUnloadedChildrenCount.md)  
[IComponent2::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetUnloadedComponentNames.md)  
[IComponent2::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.md)  
[IDocumentSpecification::InteractiveComponentSelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveComponentSelection.md)
