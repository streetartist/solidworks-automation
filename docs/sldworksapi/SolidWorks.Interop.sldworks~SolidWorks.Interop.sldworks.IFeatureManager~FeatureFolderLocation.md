# FeatureFolderLocation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFolderLocation`

Gets the folder feature for the specified feature.
Gets the folder feature for the specified feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureFolderLocation( _
   ByVal Feature As Feature _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Feature As Feature
Dim value As Feature
 
value = instance.FeatureFolderLocation(Feature)
```

```

Feature FeatureFolderLocation( 
   Feature Feature
)
```

```

Feature^ FeatureFolderLocation( 
   Feature^ Feature
) 
```

#### Parameters

*Feature*
:   [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) whose folder to get

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) folder

Example

[Move Assembly Components to New Folder (VBA)](Move_Assembly_Components_to_New_Folder_Example_VB.htm)  
[Move Assembly Components to New Folder (VB.NET)](Move_Assembly_Components_to_New_Folder_Example_VBNET.htm)  
[Move Assembly Components to New Folder (C#)](Move_Assembly_Components_to_New_Folder_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::CutListFolderLocation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CutListFolderLocation.md)
