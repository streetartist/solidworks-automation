# IGetEditTarget2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetEditTarget2`

Gets the model document that is currently being edited.
Gets the model document that is currently being edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEditTarget2() As ModelDoc2
```

```

Dim instance As IAssemblyDoc
Dim value As ModelDoc2
 
value = instance.IGetEditTarget2()
```

```

ModelDoc2 IGetEditTarget2()
```

```

ModelDoc2^ IGetEditTarget2(); 
```

#### Return Value

[IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md) being edited

Remarks

This method is useful when the user is performing an in-context edit of a part component because the currently active document returned from [ISldWorks::ActiveDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActiveDoc.md) might not be the document that the user is editing. For example, the user can use in-context editing to modify an assembly component. The active document is the assembly, but this method returns the IModelDoc2 for the component being edited.

The IModelDoc2 object returned by this method might be that of the assembly if no part is being in-place edited. In other words, this method returns a valid pointer (non-NULL) even when user is not editing a part in-context.

You can use the IModelDoc2 object returned by this method to determine which assembly component is being edited in-context. In general, you should not use this IModelDoc2 object for feature creation within the component part. Feature creation typically requires the IModelDoc2 of the active document. During feature creation, SOLIDWORKS automatically determines whether the feature should be created and owned by the active assembly, or if it is an in-context edit in which the feature should be created and owned by the component part.

COM applications need to release the IModelDoc2 object returned because this method increments the reference count on the IModelDoc2 object even if the edit target is the active document.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IModelDoc2::IsEditingSelf Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsEditingSelf.md)  
[IAssemblyDoc::GetEditTarget Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetEditTarget.md)  
[IAssemblyDoc::GetEditTargetComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetEditTargetComponent.md)  
[ISelectionMgr::IsInEditTarget2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~IsInEditTarget2.md)  
[ISldWorks::IActiveDoc2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IActiveDoc2.md)
