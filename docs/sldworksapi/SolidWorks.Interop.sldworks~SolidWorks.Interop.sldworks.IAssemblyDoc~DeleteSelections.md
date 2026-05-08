# DeleteSelections Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~DeleteSelections`

Delete either the selected components of a subassembly or the subassembly of the selected component.
Delete either the selected components of a subassembly or the subassembly of the selected component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteSelections( _
   ByVal DeleteOptions As System.Integer _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim DeleteOptions As System.Integer
Dim value As System.Boolean
 
value = instance.DeleteSelections(DeleteOptions)
```

```

System.bool DeleteSelections( 
   System.int DeleteOptions
)
```

```

System.bool DeleteSelections( 
   System.int DeleteOptions
) 
```

#### Parameters

*DeleteOptions*
:   Type of selection to delete as defined in [swAssemblyDeleteOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAssemblyDeleteOptions_e.html)

#### Return Value

True if either the selected components of a subassembly are deleted or the subassembly of the selected component is deleted, false if not

Example

[Delete Subassemblies (C#)](Delete_Subassemblies_Example_CSharp.htm)  
[Delete Subassemblies (VB.NET)](Delete_Subassemblies_Example_VBNET.htm)  
[Delete Subassemblies (VBA)](Delete_Subassemblies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IModelDoc2::EditDelete Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditDelete.md)  
[IModelDocExtension::DeleteSelection2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.md)
