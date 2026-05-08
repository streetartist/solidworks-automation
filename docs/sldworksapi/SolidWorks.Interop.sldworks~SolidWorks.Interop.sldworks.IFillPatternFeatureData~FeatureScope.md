# FeatureScope Property (IFillPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeatureScope`

Gets or sets whether to use scope for this fill pattern feature in a multibody part.
Gets or sets whether to use scope for this fill pattern feature in a multibody part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FeatureScope As System.Boolean
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Boolean
 
instance.FeatureScope = value
 
value = instance.FeatureScope
```

```

System.bool FeatureScope {get; set;}
```

```

property System.bool FeatureScope {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if only specified bodies in a multibody part are affected by the fill pattern feature; false if all the bodies are affected

Remarks

This property is valid only if [IFillPatternFeatureData::GeometryPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~GeometryPattern.md) is true.

If this property is true, you can use [IFillPatternFeatureData::AutoSelect](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~AutoSelect.md) and [IFillPatternFeatureData::FeatureScopeBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~FeatureScopeBodies.md) to specify affected bodies.

For more information, see the **Fill** **Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)  
[IFillPatternFeatureData::AutoSelect Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~AutoSelect.md)
