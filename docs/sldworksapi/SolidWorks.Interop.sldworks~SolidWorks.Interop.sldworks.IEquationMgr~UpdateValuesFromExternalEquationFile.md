# UpdateValuesFromExternalEquationFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~UpdateValuesFromExternalEquationFile`

Updates equations dependent on a linked equation file and ensures that the linked equation file exists and updates its current path, if necessary.
Updates equations dependent on a linked equation file and ensures that the linked equation file exists and updates its current path, if necessary.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function UpdateValuesFromExternalEquationFile() As System.Boolean
```

```

Dim instance As IEquationMgr
Dim value As System.Boolean
 
value = instance.UpdateValuesFromExternalEquationFile()
```

```

System.bool UpdateValuesFromExternalEquationFile()
```

```

System.bool UpdateValuesFromExternalEquationFile(); 
```

#### Return Value

True if the equations are updated, false if not

Example

[Pack and Go Part and Linked Equation (C#)](Pack_and_Go_Part_and_Linked_Equation_Example_CSharp.htm)  
[Pack and Go Part and Linked Equation (VB.NET)](Pack_and_Go_Part_and_Linked_Equation_Example_vbnet.htm)  
[Pack and Go Part and Linked Equation (VBA)](Pack_and_Go_Part_and_Linked_Equation_Example_vb.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.md)  
[IEquationMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.md)  
[IEquationMgr::LinkToFile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~LinkToFile.md)  
[IEquationMgr::FilePath Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~FilePath.md)
