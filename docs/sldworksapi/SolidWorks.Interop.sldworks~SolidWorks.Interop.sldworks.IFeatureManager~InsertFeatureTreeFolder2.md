# InsertFeatureTreeFolder2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureTreeFolder2`

Inserts a folder in the FeatureManager design tree for pre-selected features or components.
Inserts a folder in the FeatureManager design tree for pre-selected features or components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertFeatureTreeFolder2( _
   ByVal Type As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Type As System.Integer
Dim value As Feature
 
value = instance.InsertFeatureTreeFolder2(Type)
```

```

Feature InsertFeatureTreeFolder2( 
   System.int Type
)
```

```

Feature^ InsertFeatureTreeFolder2( 
   System.int Type
) 
```

#### Parameters

*Type*
:   Type of folder to insert as defined by [swFeatureTreeFolderType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureTreeFolderType_e.html)

#### Return Value

Newly created folder [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

This method operates on the features that are selected before this method executes.

|  |  |
| --- | --- |
| **If creating...** | **Then...** |
| A folder to contain preselected features | Certain types of features cannot be moved into that folder, such as the predefined planes that exist when a new part is created. These types of features are ignored by this method.  If multiple features are selected when this method runs, all of the features are moved into the new folder; however, these features must be consecutive. If they are not, only the first group of consecutive features are moved into the new folder. |
| An empty folder | The folder is created just before the first valid feature in the selections. The new folder cannot be placed before certain features, such as the predefined planes that exist when a new part is created. |
| Mold folders | When a surface feature is pre-selected, three sub-folders are created in the Surface Bodies folder: Cavity Surface Bodies, Core Surface Bodies, and Parting Surface Bodies |

Because a folder cannot be created inside another folder, any selected features already inside a folder are ignored.

This method works with components and features.

Example

[Move Assembly Components to New Folder (C#)](Move_Assembly_Components_to_New_Folder_Example_CSharp.htm)  
[Move Assembly Components to New Folder (VB.NET)](Move_Assembly_Components_to_New_Folder_Example_VBNET.htm)  
[Move Assembly Components to New Folder (VBA)](Move_Assembly_Components_to_New_Folder_Example_VB.htm)  
[Specify IGES Levels and Values, Then Import IGES File (C#)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_CSharp.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VB.NET)](Specify_IGES_Levels_and_Values_Then_Import_IGES_File_Example_VBNET.htm)  
[Specify IGES Levels and Values, Then Import IGES File (VBA)](Specify_IGES_Levels_and_Values,_Then_Import_IGES_File_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder.md)
