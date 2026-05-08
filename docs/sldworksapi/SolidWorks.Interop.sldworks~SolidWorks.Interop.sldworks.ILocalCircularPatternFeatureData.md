# ILocalCircularPatternFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData`

Allows access to a circular component pattern feature in an assembly.
Allows access to a circular component pattern feature in an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ILocalCircularPatternFeatureData 
```

```

Dim instance As ILocalCircularPatternFeatureData
```

```

public interface ILocalCircularPatternFeatureData 
```

```

public interface class ILocalCircularPatternFeatureData 
```

Remarks

Read [Pattern Features and their Feature Data Objects](sldworksapiprogguide.chm::/OVERVIEW/Pattern_Features_and_their_Feature_Data_Objects.htm).

Before calling IFeatureManager::CreateDefinition, you must pre-select the entities needed to create the local circular pattern feature.

| If... | To select a component, use... |
| --- | --- |
| Using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select components, ordered selection of the components is required | - 1 to mark the components to pattern - 2 to mark the axis |
| Directly selecting a component or axis | [ISelectData::Mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Mark.md) and [Component2::Select3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select3.md)   - 1 to mark the components to pattern - 2 to mark the axis |

You must call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) after initializing this feature data object in order to successfully create the local circular pattern feature.

Example

'VBA

'-------------------------------------------------------  
' Preconditions: Verify that the assembly exists.  
'  
' Postconditions:  
' 1. Opens the assembly.  
' 2. Selects an edge for the direction axis.  
' 3. Selects a subassembly to pattern.  
' 4. Creates **LocalCirPattern1**.  
' 5. Examine the FeatureManager design tree and  
' graphics area.  
'  
' NOTE: Because the assembly is used elsewhere, do not  
' save changes.  
'--------------------------------------------------------  
Option Explicit  
Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swModelDocExt As SldWorks.ModelDocExtension  
Dim swFeatureManager As SldWorks.FeatureManager  
Dim swFeature As SldWorks.Feature  
Dim swLocalCirPattFD As SldWorks.LocalCircularPatternFeatureData  
Dim status As Boolean  
Dim errors As Long  
Dim warnings As Long  
Dim fileName As String  
Sub main()

> Set swApp = Application.SldWorks  
> fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\distance linkage.sldasm"  
> Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes\_e.swDocASSEMBLY, swOpenDocOptions\_e.swOpenDocOptions\_Silent, "", errors, warnings)  
> Set swModelDocExt = swModel.Extension  
> Set swFeatureManager = swModel.FeatureManager  
> status = swModelDocExt.SelectByID2("", "EDGE", 0.22639417933982, -0.194822643434378, 0.102086175644843, False, 2, Nothing, 0)  
> status = swModelDocExt.SelectByID2("mount base-1@distance linkage", "COMPONENT", 0, 0, 0, True, 1, Nothing, 0)  
> Set swLocalCirPattFD = swFeatureManager.**CreateDefinition**(swFmLocalCirPattern)  
> swLocalCirPattFD.**TotalInstances** = 3  
> swLocalCirPattFD.**EqualSpacing** = True  
> Set swFeature = swFeatureManager.**CreateFeature**(swLocalCirPattFD)  
> swModel.ClearSelection2 True

End Sub

Example

[Get and Set Seed Components (C#)](Get_and_Set_Seed_Components_Example_CSharp.htm)  
[Get and Set Seed Components (VB.NET)](Get_and_Set_Seed_Components_Example_VBNET.htm)  
[Get and Set Seed Components (VBA)](Get_and_Set_Seed_Components_Example_VB.htm)  
[Create Local Circular Pattern (C#)](Create_Local_Circular_Pattern_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILocalCircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)
