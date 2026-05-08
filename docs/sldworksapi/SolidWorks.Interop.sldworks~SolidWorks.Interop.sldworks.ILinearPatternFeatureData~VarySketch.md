# VarySketch Property (ILinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~VarySketch`

Gets or sets whether to allow the pattern instances of a seed sketch to vary in relation to enclosing geometry in this linear pattern feature.
Gets or sets whether to allow the pattern instances of a seed sketch to vary in relation to enclosing geometry in this linear pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property VarySketch As System.Boolean
```

```

Dim instance As ILinearPatternFeatureData
Dim value As System.Boolean
 
instance.VarySketch = value
 
value = instance.VarySketch
```

```

System.bool VarySketch {get; set;}
```

```

property System.bool VarySketch {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to allow the pattern instances of a seed sketch to vary in relation to enclosing geomtry, false to not

Remarks

This property is valid only when creating a pattern from a seed sketch.

The seed sketch has:

- An enclosing boundary of base geometry.
- Fully defined relations.
- Dimensions only for measurements that will not vary in the pattern instances.
- A driving dimension that is used to specify the direction of the linear pattern.

If this property is true:

- Specify [ILinearPatternFeatureData::D1Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Axis.md) with a driving dimension of the seed sketch.
- Pattern instances vary with and are constrained by the enclosing geometry.

See the **SOLIDWORKS Help > Parts and Features > Features > Patterns and Mirroring > Control and Modify Patterns >** **Vary Sketch** topic.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

See the [ILinearPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)
