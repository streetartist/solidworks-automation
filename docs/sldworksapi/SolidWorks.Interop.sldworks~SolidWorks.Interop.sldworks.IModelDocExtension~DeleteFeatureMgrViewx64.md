# DeleteFeatureMgrViewx64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteFeatureMgrViewx64`

Removes the specified tab in the FeatureManager design tree in 64-bit applications.
Removes the specified tab in the FeatureManager design tree in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub DeleteFeatureMgrViewx64( _
   ByRef AppView As System.Long _
) 
```

```

Dim instance As IModelDocExtension
Dim AppView As System.Long
 
instance.DeleteFeatureMgrViewx64(AppView)
```

```

void DeleteFeatureMgrViewx64( 
   ref System.long AppView
)
```

```

void DeleteFeatureMgrViewx64( 
   System.int64% AppView
) 
```

#### Parameters

*AppView*
:   View handle of the FeatureManager design tree view to delete

Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

On the appropriate notification, you can call this method to clean up and delete your FeatureManager design tree view.

Use this method with [IModelViewManager::CreateFeatureMgrView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.md) or [IModelDoc2::AddFeatureMgrView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.md).

|  |  |
| --- | --- |
| **If you created the FeatureManager design tree view using...** | **Then...** |
| IModelViewManager::CreateFeatureMgrView2 | Calling IModelDocExtension::DeleteFeatureMgrViewx64 destroys the CView object used for the FeatureManager design tree view. |
| IModelDoc2::AddFeatureMgrView3 | Your application allocated the CView object and calling IModelDocExtension::DeleteFeatureMgrViewx64 does not destroy the CView object. In this case, you must destroy the CView object using the appropriate destructor. Never use the delete operator directly on the CView object. Always use one of the appropriate MFC view destructors. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IFeatMgrView::GetFeatMgrViewWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView~GetFeatMgrViewWndx64.md)  
[IModelViewManager::GetFeatureMgrViewHWndx64 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetFeatureMgrViewHWndx64.md)  
[IModelDoc2::DeleteFeatureMgrView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteFeatureMgrView.md)
