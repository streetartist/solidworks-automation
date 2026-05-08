# CreateFeatureMgrWindowFromHandle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandle`

Creates a new view in the FeatureManager design tree using the specified .NET tab control.
Creates a new view in the FeatureManager design tree using the specified .NET tab control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFeatureMgrWindowFromHandle( _
   ByVal BitMapFile As System.String, _
   ByVal WindowHandle As System.Integer, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

```

Dim instance As IModelViewManager
Dim BitMapFile As System.String
Dim WindowHandle As System.Integer
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView
 
value = instance.CreateFeatureMgrWindowFromHandle(BitMapFile, WindowHandle, ToolTip, WhichPane)
```

```

FeatMgrView CreateFeatureMgrWindowFromHandle( 
   System.string BitMapFile,
   System.int WindowHandle,
   System.string ToolTip,
   System.int WhichPane
)
```

```

FeatMgrView^ CreateFeatureMgrWindowFromHandle( 
   System.String^ BitMapFile,
   System.int WindowHandle,
   System.String^ ToolTip,
   System.int WhichPane
) 
```

#### Parameters

*BitMapFile*
:   Fully qualified path to the bitmap file that you want to use for the control

*WindowHandle*
:   Handle of the .NET tab control

*ToolTip*
:   Text for the ToolTip

*WhichPane*
:   Pane to use as defined in [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

#### Return Value

[IFeatMgrView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.md)

Remarks

If your application must be x64 compatible, then use [IModelViewManager::CreateFeatureMgrWindowFromHandlex64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandlex64.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::DisplayWindowFromHandle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandle.md)
