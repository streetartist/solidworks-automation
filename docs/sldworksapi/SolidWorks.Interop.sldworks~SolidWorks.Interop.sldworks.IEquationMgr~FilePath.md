# FilePath Property (IEquationMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~FilePath`

Gets or sets the path for an exported equation text (.txt) file.
Gets or sets the path for an exported equation text (**.txt**) file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FilePath As System.String
```

```

Dim instance As IEquationMgr
Dim value As System.String
 
instance.FilePath = value
 
value = instance.FilePath
```

```

System.string FilePath {get; set;}
```

```

property System.String^ FilePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path for the exported equation text (**.txt**) file

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
[IEquationMgr::LinkToFile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~LinkToFile.md)  
[IEquationMgr::UpdateValuesFromExternalEquationFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~UpdateValuesFromExternalEquationFile.md)
