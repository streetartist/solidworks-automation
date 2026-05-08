# PatternedTransforms Property (ICosmeticThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~PatternedTransforms`

Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature.
Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property PatternedTransforms As System.Object
```

```

Dim instance As ICosmeticThreadFeatureData
Dim value As System.Object
 
value = instance.PatternedTransforms
```

```

System.object PatternedTransforms {get;}
```

```

property System.Object^ PatternedTransforms {
   System.Object^ get();
}
```

#### Property Value

Array of the transforms of the instances of this cosmetic thread

Remarks

The value returned by this property does not include this cosmetic thread, which is the seed feature and not a pattern instance. Therefore, if this cosmetic thread is not used in a pattern feature, then [ICosmeticThreadFeatureData::GetPatternedTransformsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~GetPatternedTransformsCount.md) returns 0 and this property returns an empty array.

Example

[Get Cosmetic Threads Features in a Part (VBA)](Get_Cosmetic_Threads_in_a_Part_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md)  
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.md)  
[ICosmeticThreadFeatureData::IGetPatternedTransforms Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~IGetPatternedTransforms.md)
