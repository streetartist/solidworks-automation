# CreateFormTool2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFormTool2`

Creates a forming tool feature with the specified point of insertion in a sheet metal part.
Creates a forming tool feature with the specified point of insertion in a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFormTool2( _
   ByVal OriginX As System.Double, _
   ByVal OriginY As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim OriginX As System.Double
Dim OriginY As System.Double
Dim value As Feature
 
value = instance.CreateFormTool2(OriginX, OriginY)
```

```

Feature CreateFormTool2( 
   System.double OriginX,
   System.double OriginY
)
```

```

Feature^ CreateFormTool2( 
   System.double OriginX,
   System.double OriginY
) 
```

#### Parameters

*OriginX*
:   x coordinate of insertion point

*OriginY*
:   y coordinate of insertion point

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md):

1. with Append = True and Mark = 1 to select the stopping face.
2. (optional) one or more times with Append = True and Mark = 2 to select the faces to remove.

To insert a forming tool from the Design Library, call [IFeatureManager::InsertFormToolFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFormToolFeature.md).

Example

[Create Forming Tool (VBA)](Create_Forming_Tool_Example_VB.htm)  
[Create Forming Tool (VB.NET)](Create_Forming_Tool_Example_VBNET.htm)  
[Create Forming Tool (C#)](Create_Forming_Tool_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
