# ZeroQuantityDisplay Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~ZeroQuantityDisplay`

Gets or sets the character or value to display when a value is 0 in this BOM table.
Gets or sets the character or value to display when a value is 0 in this BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ZeroQuantityDisplay As System.Integer
```

```

Dim instance As IBomFeature
Dim value As System.Integer
 
instance.ZeroQuantityDisplay = value
 
value = instance.ZeroQuantityDisplay
```

```

System.int ZeroQuantityDisplay {get; set;}
```

```

property System.int ZeroQuantityDisplay {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Character or value to display when value is 0 as defined by [swZeroQuantityDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swZeroQuantityDisplay_e.html)

Example

See [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)
