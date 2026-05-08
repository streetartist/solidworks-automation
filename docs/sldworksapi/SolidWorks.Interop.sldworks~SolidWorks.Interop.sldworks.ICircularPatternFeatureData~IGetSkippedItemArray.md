# IGetSkippedItemArray Method (ICircularPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetSkippedItemArray`

Gets an array of integers that represent the skipped items in this circular feature.
Gets an array of integers that represent the skipped items in this circular feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetSkippedItemArray() As System.Integer
```

```

Dim instance As ICircularPatternFeatureData
Dim value As System.Integer
 
value = instance.IGetSkippedItemArray()
```

```

System.int IGetSkippedItemArray()
```

```

System.int IGetSkippedItemArray(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of integers that represent the skipped items in the pattern

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

This is a 0-based array, so if you skip the third and fifth items in the pattern, then:

- Array[0] = 3
- Array[1] = 5

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)  
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.md)  
[ICircularPatternFeatureData::GetSkippedItemCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetSkippedItemCount.md)  
[ICircularPatternFeatureData::ISetSkippedItemArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetSkippedItemArray.md)  
[ICircularPatternFeatureData::SkippedItemArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~SkippedItemArray.md)
