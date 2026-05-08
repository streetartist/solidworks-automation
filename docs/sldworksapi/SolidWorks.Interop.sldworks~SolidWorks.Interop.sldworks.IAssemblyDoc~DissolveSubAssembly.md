# DissolveSubAssembly Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~DissolveSubAssembly`

Dissolves the selected subassembly in this assembly.
Dissolves the selected subassembly in this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DissolveSubAssembly() As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim value As System.Boolean
 
value = instance.DissolveSubAssembly()
```

```

System.bool DissolveSubAssembly()
```

```

System.bool DissolveSubAssembly(); 
```

#### Return Value

True if the subassembly was successfully dissolved, false if not

Remarks

You must preselect the subassembly to dissolve when you run this method.

This method automatically deletes any features that need to be deleted as a result of the dissolve operation, without input from the user.

This method closes any component files when called in an assembly. If the components were modified, then those modifications are not automatically saved. You must save any modifications before the files are closed.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
