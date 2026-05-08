# DeleteInstanceAt Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~DeleteInstanceAt`

Deletes the specified pattern instance in this variable pattern feature.
Deletes the specified pattern instance in this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteInstanceAt( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As IDimPatternFeatureData
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.DeleteInstanceAt(Index)
```

```

System.bool DeleteInstanceAt( 
   System.int Index
)
```

```

System.bool DeleteInstanceAt( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0-based index indicating where to delete this pattern instance in the pattern table and pattern; -1 indicates to delete this pattern instance at the end of the pattern table and pattern (see **Remarks**)

#### Return Value

True if the pattern instance is deleted, false if not

Remarks

Use [IDimPatternFeatureData::GetInstanceCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~GetInstanceCount.md) to get the number of pattern instances.

Example

[Delete Instances and Dimensions in Variable Pattern Feature (C#)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_CSharp.htm)  
[Delete Instances and Dimensions in Variable Pattern Feature (VB.NET)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VBNET.htm)  
[Delete Instances and Dimensions in Variable Pattern Feature (VBA)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)  
[IDimPatternFeatureData::AddInstanceAt Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~AddInstanceAt.md)
