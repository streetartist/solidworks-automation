# KeepReplacedCompOption Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepReplacedCompOption`

Gets or sets how to replace components when keeping missing items.
Gets or sets how to replace components when keeping missing items.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepReplacedCompOption As System.Integer
```

```

Dim instance As IBomFeature
Dim value As System.Integer
 
instance.KeepReplacedCompOption = value
 
value = instance.KeepReplacedCompOption
```

```

System.int KeepReplacedCompOption {get; set;}
```

```

property System.int KeepReplacedCompOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Option for replacing components as defined in [swKeepReplacedCompOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swKeepReplacedCompOption_e.html)

Remarks

This property is valid only if [IBomFeature::KeepMissingItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepMissingItems.md) is set to true.

Example

See the [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomFeature::StrikeoutMissingItems Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~StrikeoutMissingItems.md)
