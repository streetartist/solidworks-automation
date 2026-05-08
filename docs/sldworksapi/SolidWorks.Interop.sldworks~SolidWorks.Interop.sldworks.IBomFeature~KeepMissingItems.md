# KeepMissingItems Property (IBomFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepMissingItems`

Gets and sets the Keep Missing Items option for this BOM feature.
Gets and sets the Keep Missing Items option for this BOM feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepMissingItems As System.Boolean
```

```

Dim instance As IBomFeature
Dim value As System.Boolean
 
instance.KeepMissingItems = value
 
value = instance.KeepMissingItems
```

```

System.bool KeepMissingItems {get; set;}
```

```

property System.bool KeepMissingItems {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to keep suppressed components, false to not

Remarks

Missing items are suppressed components.

Example

See [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomFeature::StrikeoutMissingItems Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~StrikeoutMissingItems.md)  
[IBomFeature::KeepReplacedCompOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepReplacedCompOption.md)
