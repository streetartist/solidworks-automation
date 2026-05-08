# PropagateVisualProperty Property (ILinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PropagateVisualProperty`

Gets or sets whether pattern instances inherit the visual properties (e.g., colors, textures, etc.) of the original seed feature in this linear pattern feature.
Gets or sets whether pattern instances inherit the visual properties (e.g., colors, textures, etc.) of the original seed feature in this linear pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PropagateVisualProperty As System.Boolean
```

```

Dim instance As ILinearPatternFeatureData
Dim value As System.Boolean
 
instance.PropagateVisualProperty = value
 
value = instance.PropagateVisualProperty
```

```

System.bool PropagateVisualProperty {get; set;}
```

```

property System.bool PropagateVisualProperty {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to propagate all visual properties, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)
