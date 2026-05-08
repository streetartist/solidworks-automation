# Group1PatternComponent Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PatternComponent`

Gets or sets the component to pattern for Chain Group 1 in this chain pattern feature.
Gets or sets the component to pattern for **Chain Group 1** in this chain pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Group1PatternComponent As System.Object
```

```

Dim instance As IChainPatternFeatureData
Dim value As System.Object
 
instance.Group1PatternComponent = value
 
value = instance.Group1PatternComponent
```

```

System.object Group1PatternComponent {get; set;}
```

```

property System.Object^ Group1PatternComponent {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to pattern

Remarks

This property is available to all types of chain patterns.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md)  
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.md)  
[IChainPatternFeatureData::Group1FlipPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1FlipPlane.md)  
[IChainPatternFeatureData::Group1PathLink1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink1.md)  
[IChainPatternFeatureData::Group1PathLink2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathLink2.md)  
[IChainPatternFeatureData::Group1PathPlane Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Group1PathPlane.md)
