# PrintBackground Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintBackground`

Gets or sets whether to print the background.
Gets or sets whether to print the background.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PrintBackground As System.Boolean
```

```

Dim instance As IPrintSpecification
Dim value As System.Boolean
 
instance.PrintBackground = value
 
value = instance.PrintBackground
```

```

System.bool PrintBackground {get; set;}
```

```

property System.bool PrintBackground {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to print the background, false to not

Example

See the [IPrintSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md)  
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.md)
