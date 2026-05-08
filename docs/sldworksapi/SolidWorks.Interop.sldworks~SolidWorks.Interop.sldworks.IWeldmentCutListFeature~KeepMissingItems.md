# KeepMissingItems Property (IWeldmentCutListFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepMissingItems`

Gets or sets whether to continue to show cut list items that were deleted from the weldment in the weldment cut list table.
Gets or sets whether to continue to show cut list items that were deleted from the weldment in the weldment cut list table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepMissingItems As System.Boolean
```

```

Dim instance As IWeldmentCutListFeature
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

True to keep missing cut list items, false to not

Remarks

Use [IWeldmentCutListFeature::StrikeoutMissingItems](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~StrikeoutMissingItems.md) to determine if deleted items are to be shown with strikeout formatting in the weldment cut list table.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldmentCutListFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.md)  
[IWeldmentCutListFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.md)  
[IWeldmentCutListFeature::KeepCurrentItemNumbers Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~KeepCurrentItemNumbers.md)  
[IWeldmentCutListFeature::SequenceStartNumber Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature~SequenceStartNumber.md)
