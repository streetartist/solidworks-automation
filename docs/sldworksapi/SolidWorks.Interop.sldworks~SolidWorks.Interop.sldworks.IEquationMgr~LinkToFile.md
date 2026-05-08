# LinkToFile Property (IEquationMgr)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~LinkToFile`

Gets or sets whether the equation is linked to an exported equation text (.txt) file.
Gets or sets whether the equation is linked to an exported equation text (**.txt**) file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkToFile As System.Boolean
```

```

Dim instance As IEquationMgr
Dim value As System.Boolean
 
instance.LinkToFile = value
 
value = instance.LinkToFile
```

```

System.bool LinkToFile {get; set;}
```

```

property System.bool LinkToFile {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the equation is linked to an exported equation text (**.txt**) file, false if not

Remarks

The setter of this property works only after you have set [IEquationMgr::FilePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~FilePath.md).

Example

Dim swApp As SldWorks.SldWorks  
Dim swmodel As SldWorks.ModelDoc2

Option Explicit  
  
Sub main()

     Set swApp = Application.SldWorks  
     Dim equationMgr As SldWorks.EquationMgr  
     Set swmodel = swApp.**ActiveDoc**  
     Set equationMgr = swmodel.**GetEquationMgr**  
     equationMgr.**FilePath** = 'E:\API\_SR\equations2.txt'  
     equationMgr.**LinkToFile** = True

End Sub

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
[IEquationMgr::UpdateValuesFromExternalEquationFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr~UpdateValuesFromExternalEquationFile.md)
