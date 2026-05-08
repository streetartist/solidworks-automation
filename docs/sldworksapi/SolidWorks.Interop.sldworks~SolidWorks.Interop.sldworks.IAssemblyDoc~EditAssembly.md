# EditAssembly Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditAssembly`

Switches back to the assembly document for editing.
Switches back to the assembly document for editing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditAssembly() 
```

```

Dim instance As IAssemblyDoc
 
instance.EditAssembly()
```

```

void EditAssembly()
```

```

void EditAssembly(); 
```

Remarks

This method is used with [IAssemblyDoc::EditPart2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditPart2.md), which allows you to edit a part within the context of an assembly.

Example

[Create Plane thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)  
[Suppress Component Feature (C#)](Suppress_Component_Feature_Example_CSharp.htm)  
[Suppress Component Feature (VB.NET)](Suppress_Component_Feature_Example_VBNET.htm)  
[Suppress Component Feature (VBA)](Suppress_Component_Feature_Example_VB.htm)  
[Insert Cavity (C#)](Insert_Cavity_Example_CSharp.htm)  
[Insert Cavity (VB.NET)](Insert_Cavity_Example_VBNET.htm)  
[Insert Cavity (VBA)](Insert_Cavity_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
