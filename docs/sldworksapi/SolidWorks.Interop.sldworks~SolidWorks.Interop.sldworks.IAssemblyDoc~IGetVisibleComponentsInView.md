# IGetVisibleComponentsInView Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetVisibleComponentsInView`

Gets a list of visible components in this assembly to save as solid bodies.
Gets a list of visible components in this assembly to save as solid bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetVisibleComponentsInView( _
   ByVal Count As System.Integer _
) As Component2
```

```

Dim instance As IAssemblyDoc
Dim Count As System.Integer
Dim value As Component2
 
value = instance.IGetVisibleComponentsInView(Count)
```

```

Component2 IGetVisibleComponentsInView( 
   System.int Count
)
```

```

Component2^ IGetVisibleComponentsInView( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of visible components in this assembly

#### Return Value

- in-process, unmanaged C++: Pointer to an array of visible [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) in this assembly of size count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

One way to save an assembly as a multibody part document is to save the visible components in the assembly document as solid bodies. This method corresponds to the Exterior Components option in the File, Save As dialog box. For more information about saving assemblies as multibody documents, see SOLIDWORKS Help.

Call [IAssemblyDoc::GetVisibleComponentsInViewCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetVisibleComponentsInViewCount.md) before calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::GetVisibleComponentsInView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetVisibleComponentsInView.md)
