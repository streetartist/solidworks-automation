# ConvertToHighQuality Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ConvertToHighQuality`

Gets or sets whether to convert draft quality drawing views to high quality.
Gets or sets whether to convert draft quality drawing views to high quality.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ConvertToHighQuality As System.Boolean
```

```

Dim instance As IPrintSpecification
Dim value As System.Boolean
 
instance.ConvertToHighQuality = value
 
value = instance.ConvertToHighQuality
```

```

System.bool ConvertToHighQuality {get; set;}
```

```

property System.bool ConvertToHighQuality {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to convert to high quality, false to not

Example

See the [IPrintSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md)  
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.md)
