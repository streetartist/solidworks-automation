# ICircularPatternFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData`

Allows access to a circular pattern feature.
Allows access to a circular pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICircularPatternFeatureData 
```

```

Dim instance As ICircularPatternFeatureData
```

```

public interface ICircularPatternFeatureData 
```

```

public interface class ICircularPatternFeatureData 
```

Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to create the circular pattern feature.

| If... | Use... |
| --- | --- |
| Using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select entities | - 1 to mark the direction axis - 4 to mark the features to pattern - 256 to mark the bodies to pattern - 134217728 to mark the structure systems to pattern |

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) after initializing this feature data object in order to successfully create the circular pattern feature.

After creating the circular pattern feature, you can:

- [vary the spacing of pattern instances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~InstancesToVary.md) and dimensions by implementing [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.md).

- [change the structure system to pattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~StructureSystemToPatternArray.md).

Example

[Get Transform for Each Circular Pattern Instance (C#)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_CSharp.htm)  
[Get Transform for Each Circular Pattern Instance (VB.NET)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_VBNET.htm)  
[Get Transform for Each Circular Pattern Instance (VBA)](Get_Transform_for_Each_Circular_Pattern_Instance_Example_VB.htm)  
[Create Bidirectional Circular Pattern Feature (C#)](Create_Bidirectional_Circular_Pattern_Feature_Example_CSharp.htm)  
[Create Bidirectional Circular Pattern Feature (VB.NET)](Create_Bidirectional_Circular_Pattern_Feature_Example_VBNET.htm)  
[Create Bidirectional Circular Pattern Feature (VBA)](Create_Bidirectional_Circular_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ILocalCircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData.md)
