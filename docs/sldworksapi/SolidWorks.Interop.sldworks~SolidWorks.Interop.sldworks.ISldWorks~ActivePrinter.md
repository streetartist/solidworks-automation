# ActivePrinter Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivePrinter`

Obsolete. Superseded by IModelDoc2::Printer.
Obsolete. Superseded by [IModelDoc2::Printer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Printer.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ActivePrinter As System.String
```

```

Dim instance As ISldWorks
Dim value As System.String
 
instance.ActivePrinter = value
 
value = instance.ActivePrinter
```

```

System.string ActivePrinter {get; set;}
```

```

property System.String^ ActivePrinter {
   System.String^ get();
   void set (    System.String^ value);
}
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
