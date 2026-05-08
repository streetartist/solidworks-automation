# SeedPosition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData~SeedPosition`

Gets or sets which pattern instance to use as the seed feature for this derived pattern feature.
Gets or sets which pattern instance to use as the seed feature for this derived pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SeedPosition As System.Integer
```

```

Dim instance As IDerivedPatternFeatureData
Dim value As System.Integer
 
instance.SeedPosition = value
 
value = instance.SeedPosition
```

```

System.int SeedPosition {get; set;}
```

```

property System.int SeedPosition {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Pattern instance to use as the seed feature (see **Remarks**)

Remarks

The seed position is the index of a pattern instance, feature, or component that is part of an existing pattern and is used to drive the derived pattern feature.

The total number of seed positions = total number of pattern instances in the pattern used to create the derived pattern feature.

If the pattern used to create the derived pattern has pattern instances in Direction 1 and Direction 2, then the total number of seed positions = ((Number pattern instances in Direction 1) \* (Number pattern instances in Direction 2) - 1).

Setting the seed position outside of the range of pattern instances is silently rejected, and the seed position remains unchanged.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Example

[Create Derived Pattern Feature (C#)](Create_Derived_Pattern_Feature_Example_CSharp.htm)  
[Create Derived Pattern Feature (VB.NET)](Create_Derived_Pattern_Feature_Example_VBNET.htm)  
[Create Derived Pattern Feature (VBA)](Create_Derived_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.md)  
[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.md)
