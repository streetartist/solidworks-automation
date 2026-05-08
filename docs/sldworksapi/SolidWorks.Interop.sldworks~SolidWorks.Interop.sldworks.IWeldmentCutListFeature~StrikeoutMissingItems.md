# StrikeoutMissingItems Property (IWeldmentCutListFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~StrikeoutMissingItems`

Gets or sets whether to strike out missing items in the weldment cut list table.
Gets or sets whether to strike out missing items in the weldment cut list table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property StrikeoutMissingItems As System.Boolean
```

```

Dim instance As IWeldmentCutListFeature
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

True to strike out missing items in the weldment cut list table, false to not

Remarks

Use [IWeldmentCutListFeature::KeepMissingItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepMissingItems.md) to determine if missing cut list items are to be shown in the weldment cut list table.

Example

See the [IWeldmentCutListFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.md)  
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.md)  
[IWeldmentCutListFeature::KeepCurrentItemNumbers Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepCurrentItemNumbers.md)  
[IWeldmentCutListFeature::SequenceStartNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~SequenceStartNumber.md)
