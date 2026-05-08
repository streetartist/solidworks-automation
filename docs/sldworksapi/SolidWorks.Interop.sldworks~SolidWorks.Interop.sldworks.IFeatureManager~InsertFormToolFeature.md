# InsertFormToolFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFormToolFeature`

Obsolete. Superseded by IFeatureManager::CreateDefinition and IFeatureManager::CreateFeature.
Obsolete. Superseded by [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md) and [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertFormToolFeature( _
   ByVal Path As System.String, _
   ByVal Flip As System.Boolean, _
   ByVal RotAngle As System.Double, _
   ByVal Config As System.String, _
   ByVal OverrideDoc As System.Boolean, _
   ByVal ShowPunch As System.Boolean, _
   ByVal ShowProfile As System.Boolean, _
   ByVal ShowCenter As System.Boolean, _
   ByVal LinkToPart As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Path As System.String
Dim Flip As System.Boolean
Dim RotAngle As System.Double
Dim Config As System.String
Dim OverrideDoc As System.Boolean
Dim ShowPunch As System.Boolean
Dim ShowProfile As System.Boolean
Dim ShowCenter As System.Boolean
Dim LinkToPart As System.Boolean
Dim value As Feature
 
value = instance.InsertFormToolFeature(Path, Flip, RotAngle, Config, OverrideDoc, ShowPunch, ShowProfile, ShowCenter, LinkToPart)
```

```

Feature InsertFormToolFeature( 
   System.string Path,
   System.bool Flip,
   System.double RotAngle,
   System.string Config,
   System.bool OverrideDoc,
   System.bool ShowPunch,
   System.bool ShowProfile,
   System.bool ShowCenter,
   System.bool LinkToPart
)
```

```

Feature^ InsertFormToolFeature( 
   System.String^ Path,
   System.bool Flip,
   System.double RotAngle,
   System.String^ Config,
   System.bool OverrideDoc,
   System.bool ShowPunch,
   System.bool ShowProfile,
   System.bool ShowCenter,
   System.bool LinkToPart
) 
```

#### Parameters

*Path*
:   Pathname of the forming tool part file in the Design Library

*Flip*
:   Whether to reverse the direction of the cut of the forming tool when inserted

*RotAngle*
:   Angle of the forming tool

*Config*
:   Name of the configuration of the forming tool to insert

*OverrideDoc*
:   True to override the document settings in **Tools > Options > Document Properties > Sheet Metal,** false to not

*ShowPunch*
:   True to display the cut of the forming tool when the part is flattened, false to not; valid only if OverrideDoc = true

*ShowProfile*
:   True to display the placement sketch of the forming tool when the part is flattened, false to not; valid only if OverrideDoc = true

*ShowCenter*
:   True to display the center mark where the forming tool is located in the flat pattern, false to not; valid only if OverrideDoc = true

*LinkToPart*
:   True to link the forming tool feature to its part in the Design Library, false to not

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, select either a face or a 2D sketch containing points. If you select:

- face, a single instance of the Design Library forming tool is placed on it.
- sketch containing points, an instance of the Design Library forming tool is placed at each point in the sketch.

To create your own forming tool, call [IFeatureManager::CreateFormTool](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFormTool.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IView::InsertPunchTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertPunchTable.md)
