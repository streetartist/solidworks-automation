# DeleteFeatureMgrView Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteFeatureMgrView`

Removes the specified tab in the FeatureManager design tree.
Removes the specified tab in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub DeleteFeatureMgrView( _
   ByRef AppView As System.Integer _
) 
```

```

Dim instance As IModelDoc2
Dim AppView As System.Integer
 
instance.DeleteFeatureMgrView(AppView)
```

```

void DeleteFeatureMgrView( 
   ref System.int AppView
)
```

```

void DeleteFeatureMgrView( 
   System.int% AppView
) 
```

#### Parameters

*AppView*
:   View handle of the FeatureManager design tree view to delete

Remarks

If your application must be x64 compatible, then use [IModelDocExtension::DeleteFeatureMgrViewx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteFeatureMgrViewx64.md).

On the appropriate notification, you can call this method to clean up and delete your FeatureManager design tree view.

Use this method with [IModelViewManager::CreateFeatureMgrView2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateFeatureMgrView2.md) or [IModelDoc2::AddFeatureMgrView3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddFeatureMgrView3.md).

|  |  |
| --- | --- |
| **If you created the FeatureManager design tree view using...** | **Then...** |
| IModelViewManager::CreateFeatureMgrView2 | Calling IModelDoc2::DeleteFeatureMgrView destroys the CView object used for the FeatureManager design tree view. |
| IModelDoc2::AddFeatureMgrView3 | Your application allocated the CView object and calling IModelDoc2::DeleteFeatureMgrView does not destroy the CView object. In this case, you must destroy the CVew object using the appropriate destructor. Never use the delete operator directly on the CView object. Always use one of the appropriate MFC view destructors. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
