# PrintToFile Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintToFile`

Gets or sets whether to print to a file.
Gets or sets whether to print to a file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PrintToFile As System.Boolean
```

```

Dim instance As IPrintSpecification
Dim value As System.Boolean
 
instance.PrintToFile = value
 
value = instance.PrintToFile
```

```

System.bool PrintToFile {get; set;}
```

```

property System.bool PrintToFile {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to print to a file, false to print to a [printer queue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrinterQueue.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md)  
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.md)
