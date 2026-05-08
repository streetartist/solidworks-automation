# ReverseThicknessDir Property (IRibFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~ReverseThicknessDir`

Gets or sets whether the extrusion is on the reverse side of this single-sided rib.
Gets or sets whether the extrusion is on the reverse side of this single-sided rib.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseThicknessDir As System.Boolean
```

```

Dim instance As IRibFeatureData2
Dim value As System.Boolean
 
instance.ReverseThicknessDir = value
 
value = instance.ReverseThicknessDir
```

```

System.bool ReverseThicknessDir {get; set;}
```

```

property System.bool ReverseThicknessDir {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if this single-sided rib is extruded on the reverse side, false if not

Remarks

This property is valid only when [IRibFeatureData2::IsTwoSided](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2~IsTwoSided.md) is set to false.

Example

See the [IRibFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRibFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2.md)  
[IRibFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.md)
