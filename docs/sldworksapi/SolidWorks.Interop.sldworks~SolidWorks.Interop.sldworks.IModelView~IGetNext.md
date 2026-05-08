# IGetNext Method (IModelView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetNext`

Gets the next model view after this model view.
Gets the next model view after this model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetNext() As ModelView
```

```

Dim instance As IModelView
Dim value As ModelView
 
value = instance.IGetNext()
```

```

ModelView IGetNext()
```

```

ModelView^ IGetNext(); 
```

#### Return Value

Next [model view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md) or NULLif no more model views exist

Remarks

You can traverse through the model views in a document by using this method to get the initial view and each of the following views. When this method returns Nothing, you have reached the end of the list.

See [IModelDoc2::EnumModelViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EnumModelViews.md) for a method for traversing the model views on a document.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetNext.md)  
[IModelDoc2::GetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFirstModelView.md)  
[IModelDoc2::IGetFirstModelView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetFirstModelView.md)  
[IModelDoc2::ActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ActiveView.md)  
[IModelDoc2::IActiveView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IActiveView.md)  
[IEnumModelViews::Next Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews~Next.md)
