# SkippedItemArray Property (ILocalCircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~SkippedItemArray`

Gets or sets the skipped components in this circular component pattern feature.
Gets or sets the skipped components in this circular component pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SkippedItemArray As System.Object
```

```

Dim instance As ILocalCircularPatternFeatureData
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

Array of integers representing the skipped components

Remarks

This array is 0-based. If you skip the third and fifth components, then the array looks like ArrayOut[0]=3 and ArrayOut[1]=5.

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

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)  
[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.md)  
[ILocalCircularPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~GetSkippedItemCount.md)  
[ILocalCircularPatternFeatureData::IGetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~IGetSkippedItemArray.md)  
[ILocalCircularPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData~ISetSkippedItemArray.md)
