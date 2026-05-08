# SkippedItemArray Property (ILinearPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SkippedItemArray`

Gets or sets the items skipped in this linear pattern feature.
Gets or sets the items skipped in this linear pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SkippedItemArray As System.Object
```

```

Dim instance As ILinearPatternFeatureData
Dim value As System.Object
 
instance.SkippedItemArray = value
 
value = instance.SkippedItemArray
```

```

System.object SkippedItemArray {get; set;}
```

```

property System.Object^ SkippedItemArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of integers representing skipped items

Remarks

The array is 0-based. If you skip the third and fifth items, then the array looks like ArrayOut[0]=3 and ArrayOut[1]=5.

To calculate the pattern instance numbers to skip:

Calculate:

      For a bi-directional pattern:

*I* = *n2* \* (*i* - 1) + (*j* - 1)

      For a uni-directional pattern:

*I* = *i* - 1

      where:

- *I* = pattern instance number
- *n2* = number of instances in Direction 2
- *i* = index for Direction 1
- *j* = index for Direction 2

> In the pattern's PropertyManager, find *n2* in the **Direction 2** **> Spacing and Instances > Number of instances** field and find [*i,j*] in the **Modified Instances** section.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)  
[ILinearPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GetSkippedItemCount.md)  
[ILinearPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~IGetSkippedItemArray.md)  
[ILinearPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~ISetSkippedItemArray.md)
