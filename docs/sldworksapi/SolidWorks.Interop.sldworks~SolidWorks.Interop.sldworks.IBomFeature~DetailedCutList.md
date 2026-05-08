# DetailedCutList Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DetailedCutList`

Gets or sets whether to show the detailed cut list in this BOM table.
Gets or sets whether to show the detailed cut list in this BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DetailedCutList As System.Boolean
```

```

Dim instance As IBomFeature
Dim value As System.Boolean
 
instance.DetailedCutList = value
 
value = instance.DetailedCutList
```

```

System.bool DetailedCutList {get; set;}
```

```

property System.bool DetailedCutList {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to show the detailed cut list in the BOM table, false to not

Remarks

This property applies to all types of BOM tables.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomFeature::DissolvePartLevelRows Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~DissolvePartLevelRows.md)
