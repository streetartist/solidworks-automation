# ILinearPatternFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData`

Allows access to a linear pattern feature.
Allows access to a linear pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ILinearPatternFeatureData 
```

```

Dim instance As ILinearPatternFeatureData
```

```

public interface ILinearPatternFeatureData 
```

```

public interface class ILinearPatternFeatureData 
```

Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md), you must pre-select the entities needed to create the linear pattern feature.

| If... | To select an entity, use... |
| --- | --- |
| Using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select entities to pattern | - 1 to mark Direction 1 - 2 to mark Direction 2 - 4 to mark the faces or features to pattern - 256 to mark the solid bodies to pattern - 134217728 to mark the structure systems to pattern - 2097152 to mark up-to references - 8388608 to mark seed geometry references if not using centroids to measure offsets |
| Directly selecting an entity | [IEntity::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.md) with [ISelectData::Mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Mark.md)=   - 1 to mark Direction 1 - 2 to mark Direction 2   [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md) with Mark=   - 4 to mark the faces or features to pattern - 256 to mark the bodies to pattern - 134217728 to mark the structure systems to pattern  - 2097152 to mark up-to references - 8388608 to mark seed geometry references if not using centroids to measure offsets |

After calling IFeatureManager::CreateDefinition, you can initialize the feature data object using:

- [ILinearPatternFeatureData::D1Axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Axis.md) to specify Direction 1.
- [ILinearPatternFeatureData::BodyPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~BodyPattern.md) to specify the type of seed entities to pattern:
  - [ILinearPatternFeatureData::PatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternBodyArray.md), [PatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternFaceArray.md), or [PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PatternFeatureArray.md)
- [ILinearPatternFeatureData::D1EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndCondition.md) to specify either spacing and instances or offsetting from an up-to reference:

**If explicitly setting spacing and instances, use:**

- [ILinearPatternFeatureData::D1Spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1Spacing.md) to specify spacing between pattern instances

- [ILinearPatternFeatureData::D1TotalInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1TotalInstances.md) to specify the number of pattern instances.
- [ILinearPatternFeatureData::D1ReverseDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1ReverseDirection.md) to reverse Direction 1.

**If offsetting from an up-to reference, use:**

- - [ILinearPatternFeatureData::D1EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndReference.md) to specify the up-to reference.
  - [ILinearPatternFeatureData::D1EndRefOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndRefOffset.md) to specify the distance between the last pattern instance and the up-to reference.
  - [ILinearPatternFeatureData::D1EndRefReverseOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndRefReverseOffset.md) to reverse the offset.
  - [ILinearPatternFeatureData::D1EndUseSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndUseSeedReference.md) to specify either to measure the offset from seed geometry or a centroid. If true:
    - Use [ILinearPatternFeatureData::D1EndSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndSeedReference.md).
  - [ILinearPatternFeatureData::D1EndUseSpacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~D1EndUseSpacing.md) to specify either spacing or number of instances with the up-to reference:
    - Use ILinearPatternFeatureData::D1Spacing, if D1EndUseSpacing is true.
    - Use ILinearPatternFeatureData::D1TotalInstances, if D1EndUseSpacing is false.
- All of the ILinearPatternFeatureData::D2\* properties to specify Direction 2 for a bidirectional linear pattern.
- Other properties such as [feature scope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SetFeatureScope.md), [instances to skip](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~SkippedItemArray.md), [propagate visual properties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~PropagateVisualProperty.md), [geometry pattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~GeometryPattern.md), and [vary sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~VarySketch.md).

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) after initializing this feature data object in order to successfully create the linear pattern feature.

After creating the linear pattern feature, you can:

- [vary the spacing of pattern instances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~InstancesToVary.md) and dimensions by implementing [IInstanceToVaryOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.md).

- [change the structure system to pattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData~StructureSystemToPatternArray.md).

For more information, see the **Linear Patterns and the Linear Pattern PropertyManager** topic in the SOLIDWORKS user-interface help.

Example

'VBA

'----------------------------------------------------  
' Preconditions: Verify that the part exists.  
'  
' Postconditions:  
' 1. Opens the part.  
' 2. Selects the feature to pattern.  
' 3. Selects the edges for Direction 1 and  
'     Direction 2 for the bidirectional linear  
'     pattern.  
' 4. Creates a **LPattern1**.  
' 5. Examine the FeatureManager design tree and  
'     graphics area.  
'  
' NOTE: Because the part is used elsewhere, do not save  
' changes.  
'------------------------------------------------------  
Option Explicit  
Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swModelDocExt As SldWorks.ModelDocExtension  
Dim swFeatureManager As SldWorks.FeatureManager  
Dim swFeature As SldWorks.Feature  
Dim swLinearPatternFeatureData As SldWorks.LinearPatternFeatureData  
Dim status As Boolean  
Dim errors As Long  
Dim warnings As Long  
Dim fileName As String  
Sub main()

> Set swApp = Application.SldWorks  
> fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\box.sldprt"  
> Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes\_e.swDocPART, swOpenDocOptions\_e.swOpenDocOptions\_Silent, "", errors, warnings)  
> Set swModelDocExt = swModel.Extension  
> Set swFeatureManager = swModel.FeatureManager  
> 'Select feature to pattern  
> status = swModelDocExt.SelectByID2("CBORE for #6 Binding Head Machine Screw1", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, 0)

> 'Select edges for Direction 1 and Direction 2  
> status = swModelDocExt.SelectByID2("", "EDGE", -3.41223962029176E-02, 3.00321434688158E-02, 4.60303188361877E-02, True, 1, Nothing, 0)  
> status = swModelDocExt.SelectByID2("", "EDGE", 4.36465176948104E-02, 3.01916139486593E-02, 1.14344277122314E-02, True, 2, Nothing, 0)  
>   
> 'Create linear pattern  
> Set swLinearPatternFeatureData = swFeatureManager.**CreateDefinition**(swFmLPattern)  
> swLinearPatternFeatureData.**D1EndCondition** = 0  
> swLinearPatternFeatureData.**D1ReverseDirection** = False  
> swLinearPatternFeatureData.**D1Spacing** = 0.01  
> swLinearPatternFeatureData.**D1TotalInstances** = 4  
> swLinearPatternFeatureData.**D2EndCondition** = 0  
> swLinearPatternFeatureData.**D2PatternSeedOnly** = False  
> swLinearPatternFeatureData.**D2ReverseDirection** = False  
> swLinearPatternFeatureData.**D2Spacing** = 0.01  
> swLinearPatternFeatureData.**D2TotalInstances** = 4  
> swLinearPatternFeatureData.**GeometryPattern** = False  
> swLinearPatternFeatureData.**VarySketch** = False  
> Set swFeature = swFeatureManager.**CreateFeature**(swLinearPatternFeatureData)

End Sub

Example

[Get Linear Pattern Feature Data (C#)](Get_Linear_Pattern_Feature_Data_Example_CSharp.htm)  
[Get Linear Pattern Feature Data (VB.NET)](Get_Linear_Pattern_Feature_Data_Example_VBNET.htm)  
[Get Linear Pattern Feature Data (VBA)](Get_Linear_Pattern_Feature_Data_Example_VB.htm)  
[Create Bidirectional Linear Pattern (C#)](Create_Bidir_Linear_Pattern_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)
