# DeleteView Method (IFeatMgrView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeleteView`

Removes this view from the FeatureManager design tree.
Removes this view from the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteView() As System.Boolean
```

```

Dim instance As IFeatMgrView
Dim value As System.Boolean
 
value = instance.DeleteView()
```

```

System.bool DeleteView()
```

```

System.bool DeleteView(); 
```

#### Return Value

True if the tab is deleted, false if not

Remarks

Use this method to delete a tab created by [IModelViewManager::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddControl.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatMgrView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView.md)  
[IFeatMgrView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.md)  
[IFeatMgrView::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~ActivateView.md)  
[IFeatMgrView::DeActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~DeActivateView.md)
