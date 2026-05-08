# Options Property (IChainPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Options`

Gets or sets whether to calculate the mates between each pattern instance or copy each pattern instance without creating mates in this chain pattern feature.
Gets or sets whether to calculate the mates between each pattern instance or copy each pattern instance without creating mates in this chain pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Options As System.Integer
```

```

Dim instance As IChainPatternFeatureData
Dim value As System.Integer
 
instance.Options = value
 
value = instance.Options
```

```

System.int Options {get; set;}
```

```

property System.int Options {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Option as defined in [swChainPatternOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChainPatternOptions_e.html)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md)  
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.md)
