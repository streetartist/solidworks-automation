# PitchMethod Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~PitchMethod`

Gets or sets the pitch method for this chain pattern feature.
Gets or sets the pitch method for this chain pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PitchMethod As System.Integer
```

```

Dim instance As IChainPatternFeatureData
Dim value As System.Integer
 
instance.PitchMethod = value
 
value = instance.PitchMethod
```

```

System.int PitchMethod {get; set;}
```

```

property System.int PitchMethod {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Pitch method as defined in [swChainPatternPitchMethod\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChainPatternPitchMethod_e.html)

Remarks

This property gets or sets the type of chain feature pattern.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md)  
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.md)
