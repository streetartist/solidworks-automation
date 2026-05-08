# IDerivedPatternFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData`

Allows access to a derived pattern feature.
Allows access to a derived pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IDerivedPatternFeatureData 
```

```

Dim instance As IDerivedPatternFeatureData
```

```

public interface IDerivedPatternFeatureData 
```

```

public interface class IDerivedPatternFeatureData 
```

Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to create the derived pattern feature. Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the seed components and pattern feature in any order using Marks:

- seed component  = 1
- pattern feature = 2

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) after initializing this feature data object in order to successfully create the derived pattern feature.

**NOTE**: A derived pattern feature is also called a pattern driven pattern feature.

For more information, see the **SOLIDWORKS user-interface help > Assemblies > Basic Component Operations > Component Patterns > Pattern Driven Component Pattern PropertyManager** topic.

Example

[Get and Set Seed Components (C#)](Get_and_Set_Seed_Components_Example_CSharp.htm)  
[Get and Set Seed Components (VB.NET)](Get_and_Set_Seed_Components_Example_VBNET.htm)  
[Get and Set Seed Components (VBA)](Get_and_Set_Seed_Components_Example_VB.htm)  
[Get Number of Instances Skipped in Driving Feature (C#)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_CSharp.htm)  
[Get Number of Instances Skipped in Driving Feature (VB.NET)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VBNET.htm)  
[Get Number of Instances Skipped in Driving Feature (VBA)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VB.htm)  
[Create Derived Pattern Feature (C#)](Create_Derived_Pattern_Feature_Example_CSharp.htm)  
[Create Derived Pattern Feature (VB.NET)](Create_Derived_Pattern_Feature_Example_VBNET.htm)  
[Create Derived Pattern Feature (VBA)](Create_Derived_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDerivedPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
