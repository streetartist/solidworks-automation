# Collate Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~Collate`

Gets or sets whether to collate the pages in multiple copies of this document.
Gets or sets whether to collate the pages in multiple copies of this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Collate As System.Boolean
```

```

Dim instance As IPrintSpecification
Dim value As System.Boolean
 
instance.Collate = value
 
value = instance.Collate
```

```

System.bool Collate {get; set;}
```

```

property System.bool Collate {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to collate pages in multiple copies, false to not

Example

See the [IPrintSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md)  
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.md)
