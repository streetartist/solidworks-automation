# GetFeatMgrViewWndx64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWndx64`

Gets the FeatureManager design tree view window handle as a CWnd object in 64-bit applications.
Gets the FeatureManager design tree view window handle as a CWnd object in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatMgrViewWndx64() As System.Long
```

```

Dim instance As IFeatMgrView
Dim value As System.Long
 
value = instance.GetFeatMgrViewWndx64()
```

```

System.long GetFeatMgrViewWndx64()
```

```

System.int64 GetFeatMgrViewWndx64(); 
```

#### Return Value

Window handle for this FeatureManager design tree view

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.md)  
[IFeatMgrView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.md)  
[IFeatMgrView::GetFeatMgrViewWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWnd.md)  
[IModelViewManager::GetFeatureMgrViewHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWndx64.md)
