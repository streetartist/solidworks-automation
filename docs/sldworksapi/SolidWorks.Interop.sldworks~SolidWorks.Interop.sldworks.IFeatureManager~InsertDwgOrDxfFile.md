# InsertDwgOrDxfFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile`

Obsolete. Superseded by IFeatureManager::InsertDwgOrDxfFile2.
Obsolete. Superseded by [IFeatureManager::InsertDwgOrDxfFile2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDwgOrDxfFile2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertDwgOrDxfFile( _
   ByVal FileName As System.String _
) As Feature
```

```

Dim instance As IFeatureManager
Dim FileName As System.String
Dim value As Feature
 
value = instance.InsertDwgOrDxfFile(FileName)
```

```

Feature InsertDwgOrDxfFile( 
   System.string FileName
)
```

```

Feature^ InsertDwgOrDxfFile( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Name of the DXF or DWG image file

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

This method returns:

- Nothing or null if the file contains solid bodies data.
- is not supported for use in assembly documents.

You must also select a plane or planar surface before calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
