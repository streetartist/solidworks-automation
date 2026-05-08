# PropagateVisualProperty Property (ICurveDrivenPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PropagateVisualProperty`

Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all curve-driven pattern instances.
Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all curve-driven pattern instances.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PropagateVisualProperty As System.Boolean
```

```

Dim instance As ICurveDrivenPatternFeatureData
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

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md)  
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.md)
