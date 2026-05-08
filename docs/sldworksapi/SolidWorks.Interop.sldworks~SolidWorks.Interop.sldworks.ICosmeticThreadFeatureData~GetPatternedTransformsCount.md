# GetPatternedTransformsCount Method (ICosmeticThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~GetPatternedTransformsCount`

Gets the number of instances of this cosmetic thread that are patterns of this feature.
Gets the number of instances of this cosmetic thread that are patterns of this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPatternedTransformsCount() As System.Integer
```

```

Dim instance As ICosmeticThreadFeatureData
Dim value As System.Integer
 
value = instance.GetPatternedTransformsCount()
```

```

System.int GetPatternedTransformsCount()
```

```

System.int GetPatternedTransformsCount(); 
```

#### Return Value

Number of instances of this cosmetic thread that are patterns of this feature

Remarks

The value returned by this method does not include this cosmetic thread, which is the seed feature and not an instance of the pattern. Therefore, if this cosmetic thread is not used in any pattern feature, then this method returns 0.

Use this method before using [ICosmeticThreadFeatureData::IGetPatternedTransforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~IGetPatternedTransforms.md) to determine the size of the array to pass to that method.

Example

[Get Cosmetic Threads Features in a Part (VBA)](Get_Cosmetic_Threads_in_a_Part_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md)  
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.md)  
[ICosmeticThreadFeatureData::PatternedTransforms Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~PatternedTransforms.md)
