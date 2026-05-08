# GetFeatureMgrViewHWndx64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWndx64`

Gets the window handle for the specified FeatureManager design tree view in 64-bit applications.
Gets the window handle for the specified FeatureManager design tree view in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatureMgrViewHWndx64( _
   ByVal FeatMgrViewPane As System.Integer _
) As System.Long
```

```

Dim instance As IModelViewManager
Dim FeatMgrViewPane As System.Integer
Dim value As System.Long
 
value = instance.GetFeatureMgrViewHWndx64(FeatMgrViewPane)
```

```

System.long GetFeatureMgrViewHWndx64( 
   System.int FeatMgrViewPane
)
```

```

System.int64 GetFeatureMgrViewHWndx64( 
   System.int FeatMgrViewPane
) 
```

#### Parameters

*FeatMgrViewPane*
:   FeatureManager design tree view as defined by [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

#### Return Value

Window handle for the specified FeatMgrViewPane

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.md)  
[IModelViewManager::GetFeatureMgrViewHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWnd.md)
