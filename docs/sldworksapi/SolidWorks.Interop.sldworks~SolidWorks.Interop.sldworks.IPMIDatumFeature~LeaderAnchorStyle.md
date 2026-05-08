# LeaderAnchorStyle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature~LeaderAnchorStyle`

Gets the PMI datum leader anchor style.
Gets the PMI datum leader anchor style.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LeaderAnchorStyle As System.Integer
```

```

Dim instance As IPMIDatumFeature
Dim value As System.Integer
 
instance.LeaderAnchorStyle = value
 
value = instance.LeaderAnchorStyle
```

```

System.int LeaderAnchorStyle {get; set;}
```

```

property System.int LeaderAnchorStyle {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

PMI datum leader anchor style as defined in [swPMIDatumAnchorStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumAnchorStyle_e.html)

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDatumFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature.md)  
[IPMIDatumFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature_members.md)
