# CreateFeatureMgrWindowFromHandlex64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandlex64`

On 64-bit machines, creates a new view in the FeatureManager design tree using the specified .NET tab control.
On 64-bit machines, creates a new view in the FeatureManager design tree using the specified .NET tab control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateFeatureMgrWindowFromHandlex64( _
   ByVal BitMapFile As System.String, _
   ByVal WindowHandle As System.Long, _
   ByVal ToolTip As System.String, _
   ByVal WhichPane As System.Integer _
) As FeatMgrView
```

```

Dim instance As IModelViewManager
Dim BitMapFile As System.String
Dim WindowHandle As System.Long
Dim ToolTip As System.String
Dim WhichPane As System.Integer
Dim value As FeatMgrView
 
value = instance.CreateFeatureMgrWindowFromHandlex64(BitMapFile, WindowHandle, ToolTip, WhichPane)
```

```

FeatMgrView CreateFeatureMgrWindowFromHandlex64( 
   System.string BitMapFile,
   System.long WindowHandle,
   System.string ToolTip,
   System.int WhichPane
)
```

```

FeatMgrView^ CreateFeatureMgrWindowFromHandlex64( 
   System.String^ BitMapFile,
   System.int64 WindowHandle,
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

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

Example

[Add .NET Controls to SOLIDWORKS using an Add-in (C#)](Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.htm)  
[Add .NET Controls to SOLIDWORKS using an Add-in (VB.NET)](Add_.NET_Controls_to_SolidWorks_Using_an_Add-in_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IModelViewManager::DisplayWindowFromHandlex64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DisplayWindowFromHandlex64.md)  
[IModelViewManager::CreateFeatureMgrWindowFromHandle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrWindowFromHandle.md)
