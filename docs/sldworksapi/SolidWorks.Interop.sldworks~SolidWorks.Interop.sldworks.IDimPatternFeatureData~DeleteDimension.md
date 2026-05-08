# DeleteDimension Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~DeleteDimension`

Deletes the specified column of dimensions in the pattern table in this variable pattern feature.
Deletes the specified column of dimensions in the pattern table in this variable pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteDimension( _
   ByVal DimensionColumnName As System.String _
) As System.Boolean
```

```

Dim instance As IDimPatternFeatureData
Dim DimensionColumnName As System.String
Dim value As System.Boolean
 
value = instance.DeleteDimension(DimensionColumnName)
```

```

System.bool DeleteDimension( 
   System.string DimensionColumnName
)
```

```

System.bool DeleteDimension( 
   System.String^ DimensionColumnName
) 
```

#### Parameters

*DimensionColumnName*
:   Name of the column of dimensions to delete (see **Remarks**)

#### Return Value

True if the column of dimensions is deleted, false if not

Remarks

The name of a column corresponds to the dimension name and feature name, separated by an @ symbol; e.g., **D3@Fillet1**.

There are various ways of getting the name of the column of dimensions to delete from a pattern table. For example, you can traverse the features, get the dimensions, and get the names of the dimensions. You can also select a dimension and get its name. See the examples for details.

**NOTE:** You cannot delete a column containing the dimensions of a parent sketch or feature.

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
[IDimPatternFeatureData::AddDimension Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~AddDimension.md)
