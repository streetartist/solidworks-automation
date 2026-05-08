# GetFeatureMgrViewHWnd Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWnd`

Gets the window handle for the specified FeatureManager design tree view.
Gets the window handle for the specified FeatureManager design tree view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatureMgrViewHWnd( _
   ByVal FeatMgrViewPane As System.Integer _
) As System.Integer
```

```

Dim instance As IModelViewManager
Dim FeatMgrViewPane As System.Integer
Dim value As System.Integer
 
value = instance.GetFeatureMgrViewHWnd(FeatMgrViewPane)
```

```

System.int GetFeatureMgrViewHWnd( 
   System.int FeatMgrViewPane
)
```

```

System.int GetFeatureMgrViewHWnd( 
   System.int FeatMgrViewPane
) 
```

#### Parameters

*FeatMgrViewPane*
:   FeatureManager design tree view as defined by [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

#### Return Value

Window handle for the specified FeatMgrViewPane

Remarks

If your application must be x64 compatible, then use [IModelViewManager::GetFeatureMgrViewHWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWndx64.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.md)  
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.md)  
[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.md)
