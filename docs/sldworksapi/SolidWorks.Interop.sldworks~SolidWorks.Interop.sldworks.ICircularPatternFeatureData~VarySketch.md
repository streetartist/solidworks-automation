# VarySketch Property (ICircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~VarySketch`

Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to the base part in this circular pattern.
Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to the base part in this circular pattern.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property VarySketch As System.Boolean
```

```

Dim instance As ICircularPatternFeatureData
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

True to allow the pattern instances of a seed sketch to vary in relation to enclosing geometry, false to not

Remarks

This property is valid only when creating a pattern from a seed sketch.

The seed sketch has:

- An enclosing boundary of base geometry.
- Fully defined relations.
- Dimensions only for measurements that will not vary in the pattern instances.
- A driving dimension that is used to specify the direction of the circular pattern.

If this property is true:

- Specify [ICircularPatternFeatureData::Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~Axis.md) with a driving dimension of the seed sketch.
- Pattern instances vary with and are constrained by the enclosing geometry.

See the **SOLIDWORKS Help > Parts and Features > Features > Patterns and Mirroring > Control and Modify Patterns >** **Vary Sketch** topic.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)  
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.md)
