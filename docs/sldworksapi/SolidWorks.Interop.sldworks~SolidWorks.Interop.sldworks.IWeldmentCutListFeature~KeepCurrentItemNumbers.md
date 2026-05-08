# KeepCurrentItemNumbers Property (IWeldmentCutListFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepCurrentItemNumbers`

Gets or sets whether item numbers are kept with their rows when columns are sorted or reordered in this weldment cut list table.
Gets or sets whether item numbers are kept with their rows when columns are sorted or reordered in this weldment cut list table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepCurrentItemNumbers As System.Boolean
```

```

Dim instance As IWeldmentCutListFeature
Dim value As System.Boolean
 
instance.KeepCurrentItemNumbers = value
 
value = instance.KeepCurrentItemNumbers
```

```

System.bool KeepCurrentItemNumbers {get; set;}
```

```

property System.bool KeepCurrentItemNumbers {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to keep item numbers with their rows when columns are sorted or reordered, false to not

Example

See the [IWeldmentCutListFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.md)  
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.md)  
[IWeldmentCutListFeature::KeepMissingItems Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepMissingItems.md)  
[IWeldmentCutListFeature::SequenceStartNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~SequenceStartNumber.md)  
[IWeldmentCutListFeature::StrikeoutMissingItems Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~StrikeoutMissingItems.md)
