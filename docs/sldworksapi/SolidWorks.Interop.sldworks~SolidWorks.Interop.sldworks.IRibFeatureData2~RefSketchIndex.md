# RefSketchIndex Property (IRibFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~RefSketchIndex`

Gets or sets which sketch segment defines the draft direction of the rib feature.
Gets or sets which sketch segment defines the draft direction of the rib feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RefSketchIndex As System.Integer
```

```

Dim instance As IRibFeatureData2
Dim value As System.Integer
 
instance.RefSketchIndex = value
 
value = instance.RefSketchIndex
```

```

System.int RefSketchIndex {get; set;}
```

```

property System.int RefSketchIndex {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Index of the sketch segment that defines the draft direction

Remarks

This property is valid only when [IRibFeatureData2::EnableDraft](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~EnableDraft.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md)  
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.md)  
[IRibFeatureData2::DraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftAngle.md)  
[IRibFeatureData2::DraftOutward Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~DraftOutward.md)
