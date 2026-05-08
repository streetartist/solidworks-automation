# GetFeatMgrViewWnd Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWnd`

Gets the FeatureManager design tree view window handle as a CWnd object.
Gets the FeatureManager design tree view window handle as a CWnd object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatMgrViewWnd() As System.Integer
```

```

Dim instance As IFeatMgrView
Dim value As System.Integer
 
value = instance.GetFeatMgrViewWnd()
```

```

System.int GetFeatMgrViewWnd()
```

```

System.int GetFeatMgrViewWnd(); 
```

#### Return Value

CWnd handle of the FeatureManager design tree view

Remarks

If your application must be x64 compatible, then use [IFeatMgrView::GetFeatMgrViewWndx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWndx64.md).

You can use this CWnd in combination with standard MFC calls to draw into this view.

Call this method when the FeatureManager design tree is created with  [IModelViewManager::CreateFeatureMgrView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.md). You do not need to call this method with [IModelDoc2::AddFeatureMgrView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.md), because you created the view and already have its handle.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.md)  
[IFeatMgrView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.md)  
[IModelViewManager::GetFeatureMgrViewHWnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWnd.md)
