# GetVisibleComponentsInView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetVisibleComponentsInView`

Gets a list of visible components in this assembly to save as solid bodies.
Gets a list of visible components in this assembly to save as solid bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetVisibleComponentsInView() As System.Object
```

```

Dim instance As IAssemblyDoc
Dim value As System.Object
 
value = instance.GetVisibleComponentsInView()
```

```

System.object GetVisibleComponentsInView()
```

```

System.Object^ GetVisibleComponentsInView(); 
```

#### Return Value

Array of visible [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in this assembly

Remarks

One way to save an assembly as a multibody part document is to save the visible components in the assembly document as solid bodies. This method corresponds to the Exterior Components option in the File, Save As dialog box. For more information about saving assemblies as multibody documents, see SOLIDWORKS Help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::IGetVisibleComponentsInView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetVisibleComponentsInView.md)
