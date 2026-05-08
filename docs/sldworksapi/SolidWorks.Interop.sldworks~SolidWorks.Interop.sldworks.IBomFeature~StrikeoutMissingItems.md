# StrikeoutMissingItems Property (IBomFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~StrikeoutMissingItems`

Inserts a horizontal line through }}-->missing items in this BOM table (also called strike outs).
Inserts a horizontal line through missing items in this BOM table (also called strike outs).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property StrikeoutMissingItems As System.Boolean
```

```

Dim instance As IBomFeature
Dim value As System.Boolean
 
instance.StrikeoutMissingItems = value
 
value = instance.StrikeoutMissingItems
```

```

System.bool StrikeoutMissingItems {get; set;}
```

```

property System.bool StrikeoutMissingItems {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to strike out suppressed components, false to not

Remarks

Missing items are suppressed components.

This property is valid only if [IBomFeature::KeepMissingItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepMissingItems.md) is set to true.

Example

See [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomFeature::KeepReplacedCompOption Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepReplacedCompOption.md)
