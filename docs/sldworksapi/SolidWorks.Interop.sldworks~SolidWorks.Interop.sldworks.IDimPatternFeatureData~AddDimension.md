# AddDimension Method (IDimPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~AddDimension`

Adds the selected dimension as a column to the pattern table for this variable pattern feature.
Adds the selected dimension as a column to the pattern table for this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddDimension() As System.Boolean
```

```

Dim instance As IDimPatternFeatureData
Dim value As System.Boolean
 
value = instance.AddDimension()
```

```

System.bool AddDimension()
```

```

System.bool AddDimension(); 
```

#### Return Value

True adds the selected dimension as a column to the pattern table, false does not

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
[IDimPatternFeatureData::DeleteDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~DeleteDimension.md)
