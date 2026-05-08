# PrintFile Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintFile`

Gets or sets the path and file name to which to print the document.
Gets or sets the path and file name to which to print the document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PrintFile As System.String
```

```

Dim instance As IPrintSpecification
Dim value As System.String
 
instance.PrintFile = value
 
value = instance.PrintFile
```

```

System.string PrintFile {get; set;}
```

```

property System.String^ PrintFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

File name; default file name is **output.prn**

Remarks

This property is valid only if [IPrintSpecification::PrintToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintToFile.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md)  
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.md)
