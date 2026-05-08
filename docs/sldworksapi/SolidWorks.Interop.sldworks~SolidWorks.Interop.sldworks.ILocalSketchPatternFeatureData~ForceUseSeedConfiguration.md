# ForceUseSeedConfiguration Property (ILocalSketchPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData~ForceUseSeedConfiguration`

Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local sketch pattern feature.
Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local sketch pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ForceUseSeedConfiguration As System.Boolean
```

```

Dim instance As ILocalSketchPatternFeatureData
Dim value As System.Boolean
 
instance.ForceUseSeedConfiguration = value
 
value = instance.ForceUseSeedConfiguration
```

```

System.bool ForceUseSeedConfiguration {get; set;}
```

```

property System.bool ForceUseSeedConfiguration {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the seed component configuration for all pattern components, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalSketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData.md)  
[ILocalSketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.md)
