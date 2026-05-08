# IDimPatternFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData`

Allows access to a variable pattern feature, which uses a table to store the dimensions and values of the pattern instances.
Allows access to a variable pattern feature, which uses a table to store the dimensions and values of the pattern instances.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IDimPatternFeatureData 
```

```

Dim instance As IDimPatternFeatureData
```

```

public interface IDimPatternFeatureData 
```

```

public interface class IDimPatternFeatureData 
```

Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

The variable pattern feature uses a table to store the dimensions and values of pattern instances.

You can [import tables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ImportFromExcel.md) and [export tables](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~ExportToExcel.md) using this interface.

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to create the variable pattern feature. Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the reference geometry to drive the seed feature and the feature to pattern in any order using Marks:

- reference geometry  = 1048576
- feature to pattern = 4

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) after initializing this feature data object in order to successfully create the derived pattern feature.

Example

[Insert Variable Pattern Feature (C#)](Insert_Advanced_Variable_Pattern_Feature_Example_CSharp.htm)  
[Insert Variable Pattern Feature (VB.NET)](Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm)  
[Insert Variable Pattern Feature (VBA)](Insert_Advanced_Variable_Pattern_Feature_Example_VB.htm)  
[Delete Instances and Dimensions in Variable Pattern Feature (C#)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_CSharp.htm)  
[Delete Instances and Dimensions in Variable Pattern Feature (VB.NET)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VBNET.htm)  
[Delete Instances and Dimensions in Variable Pattern Feature (VBA)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VB.htm)  
[Delete and Insert Instances in Variable Pattern Feature (C#)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_CSharp.htm)  
[Delete and Insert Instances in Variable Pattern Feature (VB.NET)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VBNET.htm)  
[Delete and Insert Instances in Variable Pattern Feature (VBA)](Delete_and_Insert_Instances_in_Variable_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::FeatureAdvancedTableDrivenPattern Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureAdvancedTableDrivenPattern.md)
