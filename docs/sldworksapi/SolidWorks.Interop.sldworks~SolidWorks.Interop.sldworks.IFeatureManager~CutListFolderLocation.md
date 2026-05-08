# CutListFolderLocation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CutListFolderLocation`

Gets the parent folder of the specified solid body / cut list item / body folder.
Gets the parent folder of the specified solid body / cut list item / body folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CutListFolderLocation( _
   ByVal QueryObj As System.Object _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim QueryObj As System.Object
Dim value As System.Object
 
value = instance.CutListFolderLocation(QueryObj)
```

```

System.object CutListFolderLocation( 
   System.object QueryObj
)
```

```

System.Object^ CutListFolderLocation( 
   System.Object^ QueryObj
) 
```

#### Parameters

*QueryObj*
:   Solid Body / cut list item / body folder / sub-weldment folder [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

#### Return Value

Parent folder feature of QueryObj; null if QueryObj is not a Solid Body / cut list / body folder / sub-weldment folder

Remarks

This method only works for:

- Solid Bodies / cut list items
- Feature / body folders
- Sub-weldment folders

Use [IFeatureManager::FeatureFolderLocation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFolderLocation.md) to locate other FeatureManager design tree objects.

Example

See the [IModelDocExtension::ReorderFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IModelDocExtension::ReorderFeature2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature2.md)
