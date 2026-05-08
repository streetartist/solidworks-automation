# Inspection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Inspection`

Gets or sets whether a display dimension above the dimension line is displayed as an inspection dimension.
Gets or sets whether a display dimension above the dimension line is displayed as an inspection dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Inspection As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
instance.Inspection = value
 
value = instance.Inspection
```

```

System.bool Inspection {get; set;}
```

```

property System.bool Inspection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the display dimension above the dimension line is displayed as an inspection dimension, false if not

Remarks

An inspection dimension is contained within an oval.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.md)  
[IDisplayDimension::SetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.md)  
[IDisplayDimension::LowerInspection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~LowerInspection.md)
